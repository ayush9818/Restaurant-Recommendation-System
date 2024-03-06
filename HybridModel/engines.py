import pickle
import surprise
import pandas as pd
from scipy.special import softmax

class UserBasedEngine:
    """
    UserBased RS class. Works by finding similar users who have rated the given item and compute the ratings
    """
    def __init__(self, sim_matrix, idx2user, idx2item, train_df):
        """
        args:
          sim_matrix: user-user similarity matrix
          idx2user : index to user_id mapping
          idx2item : index to item_id mapping
          train_df : training dataframe
        """
        self.sim_matrix = sim_matrix
        self.idx2user = idx2user
        self.idx2item = idx2item
        self.train_df = train_df
    
        self.user2idx = {v:k for k,v in self.idx2user.items()}
        self.item2idx = {v:k for k,v in self.idx2item.items()}
        
    def predict(self, user_id, item_id, topk):
        """
        Given a user_id,item_id find users who have rated given item_id and find topk similar users
        args:
          user_id, item_id : pair of user_id and item_id for which rating is to predicted
          topk : number of nearest neighbours to consider
        """
        # Finding users who have rated item : item_id
        user_who_rated = self.train_df[self.train_df.business_id == item_id].user_id.unique()
    
        user_index = self.user2idx[user_id]
        sim_scores = self.sim_matrix[user_index]
    
        sim_scores = pd.Series(sim_scores)
        sim_scores.index = self.user2idx.keys()
    
        # Finding Similar users as user_id from the users who have rated
        sorted_sim_scores = sim_scores[user_who_rated].sort_values(ascending=False)
    
        # Appplying Softmax of Similarity scores
        topk_sims = softmax(sorted_sim_scores[:topk])
        topk_users = sorted_sim_scores[:topk].index
    
        filter_df = self.train_df[(self.train_df.business_id == item_id) & (self.train_df.user_id.isin(topk_users))]
        topk_ratings = [user_df['user_rating'].mean() for user_id, user_df in filter_df.groupby('user_id')]
    
        # Calculate weighted predicted rating
        predicted_rating = round(sum([ topk_sims[idx]*topk_ratings[idx] for idx in range(len(topk_ratings))]))
    
    
        assert predicted_rating >= 0.99 and predicted_rating <= 5.1, f"Predicted Rating : {predicted_rating} out of bounds"
        return predicted_rating

class ItemBasedEngine:
    def __init__(self, sim_matrix, idx2user, idx2item, train_df):
        """
        params:
          sim_matrix : item-item similarity matrix
          idx2user : mapping of index to user_id
          idx2item : mapping of index to item_id
          train_df : training dataframe
        """
        self.sim_matrix = sim_matrix
        self.idx2user = idx2user
        self.idx2item = idx2item
        self.train_df = train_df
    
        self.user2idx = {v:k for k,v in self.idx2user.items()}
        self.item2idx = {v:k for k,v in self.idx2item.items()}
    
    def predict(self, user_id, item_id, topk):
        """
        Given a user_id,item_id find similar item that user has alreay used to compute the rating of the given item
        args:
            user_id : input user_id
            item_id : input item_id
            topk    : nearest neighbours to consider to compute the rating
        return:
            predicted_rating
        """
        # Finding Items given user has rated
        items_user_has_rated = self.train_df[self.train_df.user_id == user_id].business_id.unique()
    
        item_index = self.item2idx[item_id]
        sim_scores = self.sim_matrix[item_index]
    
        sim_scores = pd.Series(sim_scores)
        sim_scores.index = self.item2idx.keys()
    
        # Finding similarity of the given item with the items that user has rated
        sorted_sim_scores = sim_scores[items_user_has_rated].sort_values(ascending=False)
    
        topk_sims = softmax(sorted_sim_scores[:topk])
        topk_items = sorted_sim_scores[:topk].index
    
        filter_df = self.train_df[(self.train_df.user_id == user_id) & (self.train_df.business_id.isin(topk_items))]
        topk_ratings = [item_df['user_rating'].mean() for item_id, item_df in filter_df.groupby('business_id')]
    
        predicted_rating = sum([ topk_sims[idx]*topk_ratings[idx] for idx in range(len(topk_ratings))])
        assert predicted_rating >= 0.9 and predicted_rating <= 5.2, f"Predicted Rating : {predicted_rating} out of bounds"
    
        return predicted_rating


class ContentBasedEngine:
    """Content Based Engine using UB and IB Content Based Recommendation Systems"""
    def __init__(self, user_sim_matrix, 
                 item_sim_matrix, 
                 idx2user, 
                 idx2item,
                 train_df,
                 user_wt=0.1
                ):
        self.train_df = train_df
        self.user_wt = user_wt
        self.item_wt = 1 - self.user_wt

        # Initializing User based Engine
        self.ub_engine = UserBasedEngine(sim_matrix=user_sim_matrix,
                            idx2user = idx2user,
                            idx2item = idx2item,
                            train_df = train_df)

        # Initializing Item Based Engine
        self.ib_engine = ItemBasedEngine(sim_matrix=item_sim_matrix,
                            idx2user = idx2user,
                            idx2item = idx2item,
                            train_df = train_df)

    def predict(self, user_id, item_id, topk):
        # Predicting Individual ratings of both the systems
        ub_rating = self.ub_engine.predict(user_id, item_id, topk)
        ib_rating = self.ib_engine.predict(user_id, item_id, topk)

        # Taking weighted average for final rating\
        pred_rating = (self.user_wt * ub_rating) + (self.item_wt * ib_rating)
        return pred_rating

class CollaborativeFilterEngine:
    """Hybrid Collaborative Filter"""
    def __init__(self, 
                 train_df, 
                 user_wt,
                 ub_engine_path,
                 ib_engine_path
                ):
        self.train_df = train_df
        self.user_wt = user_wt
        self.item_wt = 1 - self.user_wt

        self.ub_engine = pickle.load(open(ub_engine_path, 'rb'))
        self.ib_engine = pickle.load(open(ib_engine_path, 'rb'))

    def predict(self, user_id, item_id):
        # Predicting Individual ratings of both the systems
        ub_rating = self.ub_engine.predict(user_id, item_id).est
        ib_rating = self.ib_engine.predict(user_id, item_id).est 

        # Taking weighted average for final rating\
        pred_rating = (self.user_wt * ub_rating) + (self.item_wt * ib_rating)
        return pred_rating



class RecommenderInterface:
    def __init__(self, 
                 cb_user_sim_matrix, 
                 cb_item_sim_matrix,
                 cb_idx2user, 
                 cb_idx2item,
                 search_range_in_miles,
                 cb_user_wt,
                 cf_user_wt,
                 cf_ub_engine_path,
                 cf_ib_engine_path,
                 cb_wt,
                 train_df):
        print("Initializing Engine")
        self.cb_user_sim_matrix = cb_user_sim_matrix
        self.cb_item_sim_matrix = cb_item_sim_matrix
        self.cb_idx2user = cb_idx2user
        self.cb_idx2item = cb_idx2item
        self.cb_user_wt = cb_user_wt
        self.cf_user_wt = cf_user_wt
        print(f"CB User Wt : {self.cb_user_wt}\nCF user Wt : {self.cf_user_wt}")
        self.train_df = train_df 
        self.search_range_in_miles = search_range_in_miles 
        self.cb_wt = cb_wt


        self.cb_engine = ContentBasedEngine(user_sim_matrix=self.cb_user_sim_matrix,
                             item_sim_matrix=self.cb_item_sim_matrix,
                             idx2user=self.cb_idx2user, 
                             idx2item=self.cb_idx2item,
                             train_df=self.train_df,
                             user_wt=self.cb_user_wt)
        self.cf_engine = CollaborativeFilterEngine(train_df = self.train_df,
                                                   user_wt=self.cf_user_wt,
                                                   ub_engine_path=cf_ub_engine_path,
                                                   ib_engine_path=cf_ib_engine_path)


    def predict(self, user_id, item_id, topk):
        """
        Method predicts rating for given item using CF and CB Hybrid Engines
        args:
            user_id: Test User ID 
            item_id: Shortlisted Item ID
            topk: Nearest neighbours CB engine will consider while predicting rating
        """
        cb_rating = self.cb_engine.predict(user_id, item_id, topk)
        cf_rating = self.cf_engine.predict(user_id, item_id)

        return (self.cb_wt * cb_rating) + ((1-self.cb_wt)*cf_rating)

    def recommend(self,user_id, lat, long , user_preference, topk, num_recommendations=5):
        """
        Method used to generate recommendations based on given data 
        params:
            user_id : input user id 
            lat : current latitude of the user
            long : current longitude of the user
            user_prefernece : User Preference from a selected user preference list
            topk : number of nearest neighbours to consider to rate the given item
            num_recommendations : number of recommendations to generate
        """
        if user_preference in self.train_df.columns:
            # Filter training set based on given user preference
            filtered_df = self.train_df[self.train_df[user_preference] == 1]
        else:
            print(f"Given User preference : {user_preference} Not Found. Try Again...")
            return None

        # Calculating search radius
        factor = self.search_range_in_miles / 69
        
        lat_min = lat - factor
        lat_max = lat + factor
        long_min = long - factor
        long_max = long + factor

        filtered_df = filtered_df[(filtered_df.latitude>=lat_min)&(filtered_df.latitude<=lat_max)&(filtered_df.longitude<=long_max)&(filtered_df.longitude>=long_min)]

        if filtered_df.shape[0] == 0:
            raise Exception(f"No Restaurants found within {self.search_range_in_miles} range")

        filtered_items = filtered_df.business_id.unique()
        ratings = []


        for item in filtered_items:
            ratings.append(self.predict(user_id, item, topk))


        rec_df = pd.DataFrame({
            "item_id" : filtered_items, 
            "rating" : ratings
        })

        rec_df = rec_df.sort_values(by='rating', ascending=False)
        return rec_df.head(num_recommendations)

    
        
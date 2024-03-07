# Restaurant-Recommendation-System

## Introduction

This project aims to develop a robust Restaurant Recommendation System that serves a dual purpose. For customers, it provides personalized restaurant suggestions based on individual preferences and geographical proximity. For restaurant owners, it offers a data-driven approach to generating targeted advertisements to attract customers effectively, leveraging insights from user reviews.

### For Customers:
The system utilizes a sophisticated recommendation engine to curate a list of restaurants tailored to a user's tastes and dining history. By considering factors such as past reviews, preferences, and location data, the system ensures that users receive the most relevant and appealing recommendations.

### For Restaurant Owners:
On the business front, restaurant owners benefit from an advanced data mining application that analyzes association rules within customer data. This facilitates the creation of impactful advertisements aimed at drawing in a crowd more likely to appreciate what the restaurant has to offer.

### Technical Approach:
At the core of the recommendation engine is a hybrid model that combines the strengths of Collaborative Filtering and Content-Based Filtering. We use algorithms such as KNN, KNNWithMeans, and SVD for Collaborative Filtering and employ BERT embeddings and TF-IDF for Content-Based Filtering. The synergy of these techniques allows for a nuanced understanding of user preferences, leading to highly relevant recommendations.

### Project Scope:
The Restaurant Recommendation System is an educational project designed to demonstrate the capabilities of modern recommendation algorithms. It handles a substantial dataset of approximately a million entries sourced from the publicly available Yelp dataset on Kaggle, making it a project that not only educates but also scales to real-world application scenarios.

Our mission with this project is to showcase how data-driven technologies can transform the dining experience for customers and the marketing efforts of restaurant owners.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#projectstructure)
- [Data Preparation](#data-preparation)
- [Models](#models)
- [Evaluation](#evaluation)
- [Contributors](#contributors)
- [License](#license)


## Features

<details>
<summary><b>For End-Users</b></summary>


- **Personalized Recommendations**: The system utilizes user past behavior to recommend restaurants that match their taste and preferences.
- **Proximity-Based Suggestions**: Recommendations are not only tailored to preferences but also to the proximity of the user, ensuring that suggested restaurants are within a reasonable distance.
- **Diverse Cuisine Options**: By analyzing extensive data sets, the system offers a wide variety of cuisines, catering to different dietary needs and culinary tastes.
- **User Review Insights**: Incorporates insights from user reviews using advanced NLP techniques, providing a more nuanced recommendation that takes into account the sentiment and context of user reviews.


</details>

<details>
<summary><b>For Restaurant Owners</b></summary>
  
- **Advertisement Generation Tool**: Employs Association Rules Data Mining to help restaurant owners create targeted advertisements that resonate with likely customers.
- **Customer Preference Analytics**: Provides analytics on customer preferences and dining habits, enabling restaurant owners to tailor their services or menus accordingly.
- **Competitive Analysis**: Offers insights into competitors and market trends, allowing restaurant owners to position their advertisements more strategically.


</details>

## Project Structure

The project is organized into several directories, each serving a specific role in the recommendation system:

<details>
<summary><b>CollaborativeFiltering</b></summary>

- This directory contains the code and algorithms related to the Collaborative Filtering recommendation technique. It includes implementations of KNN, KNNWithMeans, and SVD algorithms.

</details>

<details>
<summary><b>ContentBased</b></summary>
  
- Here, the Content-Based Filtering logic is implemented. It utilizes NLP techniques and machine learning models like BERT and TF-IDF to analyze and match user preferences with restaurant features.
  
</details>


<details>
<summary><b>EDA</b></summary>

- Contains Jupyter notebooks and scripts used for Exploratory Data Analysis. This is where the data is explored and visualized to understand patterns and insights.

</details>

<details>
<summary><b>HybridModel</b></summary>
  
- This directory integrates the Collaborative and Content-Based Filtering approaches to form a Hybrid Model, leveraging the strengths of both techniques for improved recommendation performance.

</details>

## Data Preparation

<details>
  
- How the data is prepared for the recommendation system.
1. From Kaggle Combine review.json and business.json
2. Select the most reviews city-Philadelphia.
3. Sample with users who reviewed more than 20 Yelp shops.
- Mention of tf-idf and BERT in the context of data preparation.

</details>


## Models
- Explanation of the models used in Collaborative Filtering, Content-Based filtering, and the Hybrid model.
1. User-Based Collaborative Filtering: This model recommends items by identifying users with similar preferences and suggesting items those similar users have liked.
2. Item-Based Collaborative Filtering: This model suggests new items based on a user's past preferences, focusing on the similarity between items themselves rather than user similarity.
- Any tuning or optimization that was performed.

The **KNNBasic() algorithm** serves as a foundational model supporting both user-based and item-based methods. Key parameters of this algorithm include:

- k: Denotes the count of nearest neighbors the model considers in its prediction-making process.

- min_k: Specifies the minimum required count of neighbors for the algorithm to proceed with a recommendation, ensuring a robust and reliable prediction.

## Evaluation

The Restaurant Recommendation System's performance is rigorously evaluated using a Hold-Out Test Dataset to ensure the robustness and accuracy of the recommendations provided.

### Metrics
For each user-item pair, the system predicts a rating and compares it with the ground truth (GT) rating. The evaluation metrics used are:

- **Mean Squared Error (MSE)**: Measures the average of the squares of the errors, i.e., the average squared difference between the estimated values and the actual value.
- **Mean Absolute Error (MAE)**: Represents the average absolute difference between the predicted ratings and the actual GT ratings.

### Results Interpretation
The effectiveness of the recommendation engine is inversely proportional to the RMSE values obtained during testing. Lower RMSE values indicate higher accuracy in the predictions, reflecting a more reliable and trustworthy system from a user's perspective. Our aim is to continually refine the model to minimize RMSE, thereby enhancing the quality of recommendations for the end-users.



## Contributors
- Ayush Agarwal
- Kevin Li
- Yumin Zhang
- Grace Xie

## License
This project is made available under the MIT License. For more details, see the [LICENSE](https://github.com/ayush9818/Restaurant-Recommendation-System/blob/main/LICENSE) file in the repository.



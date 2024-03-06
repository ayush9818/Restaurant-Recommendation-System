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
- Installation
- Usage
- [Features](#features)
- [Project Structure](#projectstructure)
- Data Preparation
- Models
- Evaluation
- Troubleshooting
- Contributors
- License


## Installation
- Requirements (list any libraries or frameworks needed).
- Step-by-step guide on setting up the project environment.
- Any environment variables or keys that need to be set.

## Usage
- How to run the project.
- Example commands and outputs.

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
- How the data is prepared for the recommendation system.
- Mention of tf-idf and BERT in the context of data preparation.

## Models
- Explanation of the models used in Collaborative Filtering, Content-Based filtering, and the Hybrid model.
- Any tuning or optimization that was performed.

## Evaluation
- How the recommendation system is evaluated.
- Metrics used for evaluation.

## Troubleshooting
- Common issues one might encounter.
- FAQs or troubleshooting tips.

## Contributors
- Instructions on how one can contribute to the project.
- Acknowledgements of current contributors.

## License
- Summary of the license (e.g., MIT, already seen in the project structure).
- Short explanation of what it permits.


# Social Media Marketing Analytics Dashboard

An end-to-end Marketing Analytics Dashboard built using Python, Pandas, and Streamlit to analyze Facebook post performance and user engagement.
The project simulates a real-world e-commerce and digital marketing analytics use case, focusing on how content strategy and posting behavior impact engagement.

# Live Application
🔗 Streamlit App:https://marketing-analytics-dashboard-fozh9aghsgfkelhhgxdobt.streamlit.app/


# Business Problem

Social media platforms generate large volumes of post-level data, but marketing teams often struggle to convert this data into actionable insights.

This project addresses questions such as:

Which post types generate higher engagement?

Does paid promotion improve engagement?

What is the best time to post?

How can engagement performance be monitored using dashboards?

# Dataset Description

Dataset: Facebook Page Post Dataset

Records: ~500 Facebook posts

Format: CSV 

Key Features:

Post Type (Photo, Status, Link, Video)

Post Month, Weekday, and Hour

Paid vs Organic indicator

Reach and Impression metrics

Engagement metrics (likes, comments, shares).

# Analytical Approach
1️ Exploratory Data Analysis (EDA)

Univariate and bivariate analysis of engagement metrics

Outlier detection and data consistency checks

Distribution analysis across post types and posting times

2️ Feature Engineering

Column normalization

Creation of total engagement metric

Handling missing and inconsistent values

3️ Model Benchmarking (Offline)

Linear Regression (baseline)

Random Forest Regressor

H2O AutoML (Ensemble model)

Models were evaluated using:

RMSE

R² Score

This step helped understand the predictability of engagement and model limitations.

# Dashboard Features
🔎 Interactive Filters

Post Type

Paid vs Organic

Post Month

📌 Key Performance Indicators (KPIs)

Total number of posts

Average engagement

Maximum engagement

📈 Visual Analytics

Engagement comparison by post type

Engagement trends by posting hour

Fully dynamic charts based on selected filters.

# Tools & Technologies Used

Python

Pandas – data processing & analysis

Streamlit – dashboard development

Scikit-learn – baseline ML models

H2O AutoML – model benchmarking

Git & GitHub – version control

Streamlit Community Cloud – deployment

# Deployment

The application is deployed using Streamlit Community Cloud, enabling:

Public access via a live URL

Automatic redeployment on GitHub updates

Zero infrastructure management

# Key Learnings & Outcomes

Hands-on experience with real-world marketing data

Built interactive dashboards for business users

Learned limitations of regression models for engagement prediction

Understood model benchmarking using H2O AutoML

Gained experience in end-to-end project deployment

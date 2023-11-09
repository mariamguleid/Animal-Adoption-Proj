# Animal Adoption Project

## Project/Goals
For my final project at LHL (Lighthouse Labs), I have come across a dataset from an animal shelter, and since I absolutely love animals, I couldn’t let go of the opportunity. 
I will be training a model to predict the outcome for an animal, which is either adoption or no adoption.

## Dataset

- The [dataset](https://www.kaggle.com/datasets/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes?select=aac_intakes_outcomes.csv) I will be using is a publically available kaggle dataset containing data from Austin Animal Center which is one of the largest shelters in the US, providing shelter to over 18,000 animals every year.
- The dataset contains 41 columns and almost 80,000 rows with information about each animal, and whether they got adopted or not.


## Problem

With the large number of animals being brought into shelters daily, many of these animals don’t end up getting adopted and some even get euthanized. I am using machine learning algorithms to train models to predict whether an animal will be adopted or not based on information given on the animal. 
This will help the owners/managers of the shelter focus more attention on the animals that are less likely to get adopted and hopefully give these animals a better chance for adoption.

## Process

- Pre-processing data: I started off by removing unneeded columns and null values, renaming, transforming the data into numerical form, scaling and ensuring balance between the two outcome values (Adoption and no adoption) for better model performance. 
After doing some feature importance checks, I have come up with 10 columns to use for the prediction. This enables quicker compiling time for the models. 
- Model Training: I used both Logistic Regression and XGBoost models and compared performance between the two.
- Deployment: I deployed my model using Streamlit and created a user friendly interface.

## Streamlit App
https://adoptionprediction.streamlit.app/

## Results

- For my first model, Logistic Regression Model, using default parameters, I was able to get an accuracy of 77% for the models ability to predict. Unfortunately, even after tuning the parameters, the accuracy result remained the same.
- Another model I used is the XGBoost model. This model provided better performance with an accuracy of 83%. After hyper parameter tuning, I got a slightly higher accuracy result.


## Future Goals
- Try more models and hyper-parameter tuning to improve accuracy score
- Add image classification to identify and label images of animals


import streamlit as st 
import pandas as pd
import numpy as np
import pickle

# loading in the model to predict on the data 
model = pickle.load(open('model_xgb.pkl','rb'))

def predict_animal(age_upon_outcome_days,time_in_shelter_days,Purebred,Bird,Cat,Dog,Other,Intact_female,Intact_male,Neutered_male,Spayed_female,sex_Unknown,intake_cond_Unhealthy
                  ):
    input=np.array([[age_upon_outcome_days,time_in_shelter_days,Purebred,Bird,Cat,Dog,Other,Intact_female,Intact_male,Neutered_male,Spayed_female,sex_Unknown,intake_cond_Unhealthy
                   ]]).astype(object)
    prediction = model.predict(input)
    
    return prediction

def main(): 
      # giving the webpage a title 
    st.title('Predicting Animal Adoption')
    st.markdown('Enter information about an animal to predict whether the animal will get adopted or not. (Enter 0 for no and 1 for yes)')
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    age_upon_outcome_days = st.text_input("Age upon adoption (in days):","Type Here")
    time_in_shelter_days = st.text_input("Time spent in shelter (in days):","Type Here")
    Purebred = st.text_input("Purebred","Type Here")
    Bird = st.text_input("Bird","Type Here")
    Cat = st.text_input("Cat","Type Here")
    Dog = st.text_input("Dog","Type Here")
    Other = st.text_input("Other","Type Here")
    Intact_female = st.text_input("Intact Female","Type Here")
    Intact_male = st.text_input("Intact Male","Type Here")
    Neutered_male = st.text_input("Neutered Male","Type Here")
    Spayed_female = st.text_input("Spayed Female","Type Here")
    sex_Unknown = st.text_input("Unknown Sex","Type Here")
    intake_cond_Unhealthy = st.text_input("Unhealthy","Type Here")
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
     
    if st.button("Predict adoption"):
        output = predict_animal(age_upon_outcome_days,time_in_shelter_days,Purebred,Bird,Cat,Dog,Other,Intact_female,Intact_male,Neutered_male,Spayed_female,sex_Unknown,intake_cond_Unhealthy
                               )
        if output[0] == 1: 
         st.success('Animal will get adopted :thumbsup:')
        else: 
         st.error("Animal won't get adopted :thumbsdown:") 

     
if __name__=='__main__': 
    main() 
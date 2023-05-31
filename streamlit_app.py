import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load("emotion_classifier_pipe_lr_03_june_2021.pkl")

# Define the main function of the Streamlit app
def main():
    st.title("Emotion Classifier")
    
    # Get user input
    user_input = st.text_input("Please write a text here:")
    
    # Predict the emotion if user has entered something
    if st.button("Predict"):
        if user_input:
            # Use the model to predict the emotion
            prediction = model.predict([user_input])
            st.write(f"The predicted emotion is: {prediction[0]}")
        else:
            st.write("Please write some text for emotion prediction.")
    
if __name__ == "__main__":
    main()
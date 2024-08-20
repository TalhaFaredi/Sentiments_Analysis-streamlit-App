import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the saved model
model = load_model('sentiment_analysis_model.h5')

# Load and fit the tokenizer on your training data
texts = ["Sample sentence one.", "Another sentence.", "More text here."]  # Replace with your training data
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(texts)

# Create a Streamlit app
st.title("Sentiment Analysis App")

# Create a text box for user input
user_review = st.text_area("Enter your review:", height=100)

# Create a button to submit the review
submit_button = st.button("Submit")

# Check if the submit button is clicked
if submit_button:
    # Preprocess the user's review
    review_sequence = tokenizer.texts_to_sequences([user_review])
    padded_review = pad_sequences(review_sequence, maxlen=200)

    # Make a prediction using the model
    prediction = model.predict(padded_review) > 0.5

    # Display the prediction
    if prediction:
        st.write("Positive Review")
    else:
        st.write("Negative Review")

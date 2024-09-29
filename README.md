
# Sentiment Analysis Web Application

This project is a web-based application that predicts the sentiment of a given review (positive or negative) using a pre-trained deep learning model. The model is built using TensorFlow and Keras, and the app is created using Streamlit.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [How it works](#how-it-works)
- [Future Enhancements](#future-enhancements)

## Introduction

This application takes user input (a review) and predicts whether the sentiment is positive or negative. The machine learning model is pre-trained using a sentiment analysis dataset. 

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should include the following packages:
   - `tensorflow`
   - `streamlit`
   - `numpy`

3. Download the pre-trained model (`sentiment_analysis_model.h5`) and place it in the root folder of the project.

## Usage

1. To run the application, simply execute the following command:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to `http://localhost:8501`.

3. Enter your review in the text box, click "Submit," and the app will predict whether the review is positive or negative.

## Model

The application uses a deep learning model built with TensorFlow and Keras. The model has been trained on a dataset of labeled reviews to predict sentiment. The tokenizer processes user inputs to match the training data format.

### Model Information:
- Pre-trained model file: `sentiment_analysis_model.h5`
- Tokenizer: `Tokenizer(num_words=5000)`
- Input sequence padding: Max length of 200

## How it works

1. **User Input**: The app provides a text area for users to input their review.
2. **Tokenization**: The input text is tokenized using a pre-fit Keras `Tokenizer`.
3. **Padding**: The tokenized sequence is padded to ensure uniform input size for the model.
4. **Prediction**: The padded sequence is fed into the trained model to predict whether the sentiment is positive (1) or negative (0).
5. **Output**: The result is displayed on the screen as either "Positive Review" or "Negative Review."

## Future Enhancements

- Improve model accuracy by retraining on a larger dataset.
- Allow users to provide their own dataset for training.
- Add functionality to display confidence scores for the predictions.
- Enhance the UI with better styling and visuals.
  
## License

This project is licensed under the MIT License.
```

### Instructions:
- Make sure to include a `requirements.txt` file for your dependencies.
- Replace any placeholders like repository URLs with your actual project information.

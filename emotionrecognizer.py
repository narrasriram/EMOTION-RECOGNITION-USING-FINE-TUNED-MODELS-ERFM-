
# -*- coding: utf-8 -*-

# Author: Sriram Narra
# Course: CS 842
# Date: Apr 15, 2021
# Project Name: Emotion Recognition using Fine-tuned Models(ERFM)
# Description: Application file when run takes user input sentence and
#              outputs the Emotion Label and Subjectivity Score.
# --------------------------------------------------------------------------------




# Import Required Libraries
import ktrain
from transformers import AlbertTokenizer
from transformers import TFAlbertForSequenceClassification


#----------------------------------------------------------------
# function: predict_emotion_label
# purpose: Perform Emotion Label Classification for the input
# parameter(s): <1> sentence (string)
# return:  <1> prediction (string)
def predict_emotion_label(sentence):

  # Specify the path of Fine-tuned Distilbert model
  predictor = ktrain.load_predictor("./distilbert_model-stimulus")
  prediction = predictor.predict(sentence)
  return prediction


# Functional to predict the Subjectivity Score
#----------------------------------------------------------------
# function: predict_emotion_label
# purpose: Perform Subjectivity Score Prediction for the input
# parameter(s): <2> sentence (string),
#                   albert_tokens (transformers.tokenization_albert.AlbertTokenizer)
# return:  <1> prediction (float)
def predict_subjectivity_score(sentence, albert_tokens):

  # Specify the path of Fine-tuned ALBERT model
  loaded_model = TFAlbertForSequenceClassification.from_pretrained("./Finetuned_Albert_model_MAE")

  # Convert the sentence into Albert Tokens
  sentence_tokens = albert_tokens.encode(sentence,
                                 truncation=True,
                                 padding=True,
                                 return_tensors="tf")
  
  prediction = loaded_model.predict(sentence_tokens)[0][0][0]
  return prediction



# Load the AlbertTokenizer
albert_tokens = AlbertTokenizer.from_pretrained('albert-base-v2')

sentence = input('Enter the Input Sentence: ')

predicted_emotion_label = predict_emotion_label(sentence)


predicted_subjectivity_score = predict_subjectivity_score(sentence, albert_tokens)

# Prints the Prediction Label
print("The predicted Emotion Label for the sentence is: "+predicted_emotion_label)

# Prints the Subjectivity Score
print("The predicted Emotion Label for the sentence is: "+str(predicted_subjectivity_score))
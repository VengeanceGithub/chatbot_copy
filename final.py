import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
from flask import Flask, request


# Download NLTK punkt tokenizer
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents file
with open('C:\\Users\\jakka\\OneDrive\\Documents\\new\\final_copy\\intents.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Prepare intents and responses
intents = data['intents']
responses = {}
for intent in intents:
    responses[intent['tag']] = intent['responses']

# Function to preprocess user input
def preprocess_input(user_input):
    # Tokenize and lemmatize
    words = nltk.word_tokenize(user_input)
    words = [lemmatizer.lemmatize(word.lower()) for word in words]
    return words

# Function to predict intent
def predict_intent(user_input):
    words = preprocess_input(user_input)
    for intent in intents:
        for pattern in intent['patterns']:
            if all(word in words for word in nltk.word_tokenize(pattern.lower())):
                return intent['tag']
    return "default"

# Main chat function
def chat():
    print("Миний Chatbot-д тавтай морилно уу! тусламж хэрэгтэй бол асуугаарай.Хэрэв гарах бол 'exit' гэж бичнэ үү.")
    
    while True:
        user_input = input("Та: ").lower()
        if user_input == 'exit':
            print("Баяртай!")
            break
        
        predicted_intent = predict_intent(user_input)
        response = random.choice(responses[predicted_intent])
        print(f"Bot: {response}")

# Start chatting
chat()

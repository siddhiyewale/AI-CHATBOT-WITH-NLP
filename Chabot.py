import nltk
import re
import random
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


lemmatizer = WordNetLemmatizer()


intents = {
    "coversing": {
        "template": ["hello", "hey", "hi"],
        "reaction": ["Hello!", "Hi there!", "Heyya!", "Hi! What can i help you with?"]
    },
    "farewell": {
        "template": ["farewell", "bye", "see yaa", "exit", "quit","end"],
        "reaction": ["Goodbye!", "Catch you later!", "Have a nice day!", "Bye! Come back soon!"]
    },
    "thanks": {
        "template": ["thank you", "thankyou", "thx","thanks"],
        "reaction": ["You're welcome!", "No problem!", "Happy to help you out !"]
    },
    "answer_name": {
        "template": ["what is your name?", "who are you?", "your name?","what is your name","who are you"],
        "reaction": ["I am an AI Chatbot , created using NLTK.", "Myself Chatbot !."]
    },
    "age": {
        "template": ["what's your age?","how old are you?", "your age?"],
        "reaction": ["I don't have an age, I'm an AI creation ."]
    },
    "help": {
        "template": ["help", "can you help me?", "support","need hep"],
        "reaction": ["Sure! I can help you. Ask me anything."]
    },
    "cast": {
        "template": ["what is the weather cast", "weather today", "is it raining moment", "rainfall cast"],
        "reaction": ["I'm not connected to live rainfall data yet.", "Sorry, I cannot give rainfall information presently!."]
    }
}


def preprocess_sentence(phrase):
    indentifier = phrase.lower().split()
    indentifier = [word for word in indentifier if word.isalnum()]
    indentifier = [lemmatizer.lemmatize(word) for word in indentifier]
    return indentifier


def match_intent(user_input):
    tokens = preprocess_sentence(user_input)
    #Check intent patterns
    for intent, data in intents.items():
        for pattern in data["template"]:
            pattern_tokens = preprocess_sentence(pattern)
            if all(token in tokens for token in pattern_tokens):
                return intent
    return None


def get_response(intent):
    if intent in intents:
        return random.choice(intents[intent]["reaction"])
    else:
        return "I didn't catch that. Could you please paraphrase?"

# Main 

def converse():
    print("Chatbot: Heyy ! I'm an AI Chatbot. to wrap up type 'exit' or 'quit'.")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ['exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        intent = match_intent(user_input)
        reaction = get_response(intent)
        print(f"Chatbot: {reaction}")

# Run

if __name__ == "__main__":
    converse()

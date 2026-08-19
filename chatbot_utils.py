import re
import string
import time
from datetime import datetime

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def tokenize(text):
    return preprocess(text).split()

def typing_animation():
    print("\nBot is typing", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

def time_greeting():
    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning!"
    elif hour < 17:
        return "Good Afternoon!"
    return "Good Evening!"

def save_chat(user, bot):
    with open("chat_history.txt", "a") as file:
        file.write(f"User: {user}\n")
        file.write(f"Bot : {bot}\n\n")

def save_unknown(question):
    with open("unknown_questions.txt", "a") as file:
        file.write(question + "\n")
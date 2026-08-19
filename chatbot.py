import json
import random
import difflib
import re
import string
import time
from datetime import datetime
from chatbot_utils import (
    preprocess,
    tokenize,
    typing_animation,
    time_greeting,
    save_chat,
    save_unknown
)
# =====================================================
# AI STUDENT ADMISSION ASSISTANT
# chatbot.py
# =====================================================

# -------------------------------
# Load intents safely
# -------------------------------
try:
    with open("intents.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: intents.json file not found!")
    exit()
except json.JSONDecodeError:
    print("Error: intents.json contains invalid JSON!")
    exit()

# -------------------------------
# Global Variables
# -------------------------------
conversation_count = 0
last_intent = None



# -------------------------------
# Text Preprocessing
# -------------------------------
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# -------------------------------
# Tokenization
# -------------------------------
def tokenize(text):
    return preprocess(text).split()


# -------------------------------
# Build Vocabulary (only once)
# -------------------------------
vocabulary = []

for intent in data["intents"]:

    for pattern in intent["patterns"]:
        vocabulary.extend(tokenize(pattern))

    if "keywords" in intent:
        vocabulary.extend(intent["keywords"])

vocabulary = list(set(vocabulary))


# -------------------------------
# Time-based Greeting
# -------------------------------
def time_greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning! ☀"

    elif hour < 17:
        return "Good Afternoon! 🌤"

    else:
        return "Good Evening! 🌙"


# -------------------------------
# Typing Animation
# -------------------------------
def typing():

    print("\nBot", end="")

    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

    print("\n")


# -------------------------------
# Save Chat History
# -------------------------------
def save_chat(user, bot):

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("chat_history.txt", "a", encoding="utf-8") as file:

        file.write("=" * 50 + "\n")
        file.write(f"Time : {now}\n")
        file.write(f"User : {user}\n")
        file.write(f"Bot  : {bot}\n\n")


# -------------------------------
# Save Unknown Questions
# -------------------------------
def save_unknown(question):

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("unknown_questions.txt", "a", encoding="utf-8") as file:

        file.write(f"[{now}] {question}\n")


# -------------------------------
# Spell Correction
# -------------------------------
def correct_input(text):

    words = tokenize(text)

    corrected = []

    for word in words:

        match = difflib.get_close_matches(
            word,
            vocabulary,
            n=1,
            cutoff=0.80
        )

        if match:
            corrected.append(match[0])
        else:
            corrected.append(word)

    return " ".join(corrected)


# -------------------------------
# Keyword Matching
# -------------------------------
def keyword_match(user_input):

    words = tokenize(user_input)

    best_intent = None
    best_score = 0

    for intent in data["intents"]:

        if "keywords" not in intent:
            continue

        score = 0

        for keyword in intent["keywords"]:

            if keyword.lower() in words:
                score += 1

        if score > best_score:
            best_score = score
            best_intent = intent

    return best_intent
# =====================================================
# PART 2 - Response Engine
# =====================================================

# -------------------------------
# Find Best Matching Intent
# -------------------------------
def find_best_match(user_input):

    user_input = preprocess(user_input)

    best_intent = None
    highest_score = 0

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            pattern = preprocess(pattern)

            score = difflib.SequenceMatcher(
                None,
                user_input,
                pattern
            ).ratio()

            if score > highest_score:
                highest_score = score
                best_intent = intent

    return best_intent, highest_score


# -------------------------------
# Context-Based Responses
# -------------------------------
def context_response(user_input):

    global last_intent

    text = preprocess(user_input)

    follow_words = [
        "fees",
        "fee",
        "hostel",
        "scholarship",
        "documents",
        "placement",
        "placements",
        "duration",
        "eligibility",
        "contact",
        "location",
        "timing"
    ]

    if text in follow_words and last_intent is not None:

        for intent in data["intents"]:

            if intent["tag"] == last_intent:
                return random.choice(intent["responses"])

    return None


# -------------------------------
# Generate Bot Response
# -------------------------------
def get_response(user_input):

    global last_intent

    # ---------------------------
    # Step 1 : Spell Correction
    # ---------------------------
    corrected = correct_input(user_input)

    # ---------------------------
    # Step 2 : Context Matching
    # ---------------------------
    response = context_response(corrected)

    if response:
        return response

    # ---------------------------
    # Step 3 : Keyword Matching
    # ---------------------------
    keyword_intent = keyword_match(corrected)

    if keyword_intent is not None:

        last_intent = keyword_intent["tag"]

        return random.choice(keyword_intent["responses"])

    # ---------------------------
    # Step 4 : Pattern Matching
    # ---------------------------
    best_intent, confidence = find_best_match(corrected)

    if confidence >= 0.65:

        last_intent = best_intent["tag"]

        return random.choice(best_intent["responses"])

    # ---------------------------
    # Step 5 : Unknown Question
    # ---------------------------
    save_unknown(user_input)

    return (
        "I'm sorry, I couldn't understand your question.\n"
        "Please try asking it in a different way."
    )


# -------------------------------
# Welcome Message
# -------------------------------
def show_welcome():

    print("=" * 60)
    print("      AI STUDENT ADMISSION ASSISTANT")
    print("=" * 60)

    print(time_greeting())

    print("\nI can help you with:\n")

    print(" Admission Process")
    print(" Eligibility")
    print(" Courses")
    print(" Fee Structure")
    print(" Scholarships")
    print(" Hostel")
    print(" Placements")
    print(" Faculty")
    print(" Campus Facilities")
    print(" Documents Required")
    print(" Contact Details")
    print(" College Timings")
    print(" Transport")
    print(" Library")

    print("\nType 'help' to see commands.")
    print("Type 'exit' to quit.\n")


# -------------------------------
# Help Menu
# -------------------------------
def show_help():

    print("\n========== HELP ==========\n")

    print("You can ask questions like:\n")

    print("- What courses are offered?")
    print("- What is the fee structure?")
    print("- Hostel facilities")
    print("- Placement details")
    print("- Scholarships")
    print("- Required documents")
    print("- Admission process")
    print("- Eligibility criteria")
    print("- College timings")
    print("- Contact information")

    print("\nCommands:")

    print(" help   -> Show help menu")
    print(" clear  -> Clear screen")
    print(" exit   -> Exit chatbot")

    print()
   # =====================================================
# PART 3 - Main Program
# =====================================================

# Display Welcome Message
show_welcome()

# Greetings
greetings = [
    "hi",
    "hello",
    "hey",
    "good morning",
    "good afternoon",
    "good evening"
]

greeting_responses = [
    "Hello! How can I assist you with admissions today?",
    "Hi! Welcome to the AI Student Admission Assistant.",
    "Hey! What would you like to know about our college?",
    "Greetings! How may I help you today?"
]

# Farewell Messages
farewell_messages = [
    "Thank you for using AI Student Admission Assistant.",
    "Good luck with your admission!",
    "Have a wonderful day!",
    "We hope to see you on campus soon!",
    "Take care. Goodbye!"
]

# -------------------------------
# Chat Loop
# -------------------------------
while True:

    user = input("You : ").strip()

    if not user:
        print("Bot : Please enter a question.\n")
        continue

    command = preprocess(user)

    # ---------------------------
    # Exit Commands
    # ---------------------------
    if command in ["exit", "quit", "bye", "goodbye"]:

        print()

        typing()

        print("Bot :", random.choice(farewell_messages))
        print(f"\nTotal Questions Asked : {conversation_count}")

        print("Chat history saved successfully.")
        break

    # ---------------------------
    # Help Command
    # ---------------------------
    if command == "help":
        show_help()
        continue

    # ---------------------------
    # Clear Screen
    # ---------------------------
    if command == "clear":
        print("\n" * 100)
        show_welcome()
        continue

    # ---------------------------
    # Greeting
    # ---------------------------
    if command in greetings:

        typing()

        response = random.choice(greeting_responses)

        print("Bot :", response)

        save_chat(user, response)

        continue

    # ---------------------------
    # Process Question
    # ---------------------------
    conversation_count += 1

    corrected = correct_input(user)

    if corrected != preprocess(user):
        print(f"\nDid you mean : {corrected}")

    response = get_response(corrected)

    typing()

    print("Bot :", response)

    save_chat(user, response)

print("\nProgram Ended Successfully.") 
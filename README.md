# AI Student Admission Assistant

An AI-powered Python chatbot designed to help students with common admission-related queries such as courses, fees, eligibility, scholarships, hostel facilities, placements, contact details, and campus information.

## Features

* NLP-based text preprocessing
* Keyword matching
* Similarity matching using Python's `difflib`
* Context-aware responses
* Time-based greetings
* Randomized responses
* Typing animation for a conversational experience
* Chat history storage
* Unknown question logging
* Conversation counter
* JSON-based intent and response management

## Technologies Used

* **Python**
* **JSON**
* **Regular Expressions (`re`)**
* **difflib**
* **datetime**
* **random**

## How It Works

The chatbot follows a simple conversational pipeline:

```text
User Question
      ↓
Text Preprocessing
      ↓
Keyword Matching
      ↓
Similarity Matching
      ↓
Intent Identification
      ↓
Response Generation
      ↓
Chatbot Response
```

If the chatbot cannot identify a suitable response, the unknown question can be logged for future improvement.

## Project Structure

```text
StudentAdmissionAssistant/
│
├── chatbot.py
├── chatbot_utils.py
├── intents.json
├── chat_history.txt
├── unknown_questions.txt
├── .gitignore
└── README.md
```

### File Description

| File                    | Description                                                |
| ----------------------- | ---------------------------------------------------------- |
| `chatbot.py`            | Main chatbot application                                   |
| `chatbot_utils.py`      | Utility functions used by the chatbot                      |
| `intents.json`          | Stores admission-related intents, questions, and responses |
| `chat_history.txt`      | Stores conversation history                                |
| `unknown_questions.txt` | Stores questions that the chatbot could not answer         |
| `.gitignore`            | Prevents unnecessary files from being uploaded to GitHub   |

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/koyelikhitha/AI-Admission-Assistant.git
```

### 2. Open the project folder

```bash
cd AI-Admission-Assistant
```

### 3. Run the chatbot

```bash
python chatbot.py
```

## Example Queries

The chatbot can respond to questions such as:

* What courses are available?
* What is the admission eligibility?
* What are the fees?
* Are scholarships available?
* Is hostel accommodation available?
* What placement opportunities are available?
* How can I contact the college?
* Tell me about the campus.

## Future Enhancements

* Voice-based interaction
* Web-based chatbot interface
* Integration with a college database
* Multilingual support
* Advanced NLP and machine learning models
* Integration with college admission APIs
* Deployment as a web or mobile application

## Project Goal

The goal of this project is to provide students with a simple and interactive way to obtain admission-related information without having to manually search through multiple sources.

## Author

**Likhitha Koye**

B.Tech – Computer Science and Artificial Intelligence

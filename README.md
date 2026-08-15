# Final Project - Emotion Detector

## Overview

This project implements an Emotion Detection application using the IBM Watson NLP service. The application analyzes text and detects the emotions expressed in the input statement.

The detected emotions include:

- Anger
- Disgust
- Fear
- Joy
- Sadness

The application identifies the dominant emotion and displays the results through a Flask web interface.

---

## Project Structure

```text
oaqjp-final-project-emb-ai/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
│
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
├── README.md
└── requirements.txt
```

---

## Features

- Emotion detection using Watson NLP API
- Emotion score extraction
- Dominant emotion identification
- Flask web deployment
- Error handling for blank input
- Unit testing using unittest
- Static code analysis using Pylint

---

## Technologies Used

- Python 3
- Flask
- Requests
- IBM Watson NLP Service
- unittest
- pylint

---

## Running the Application

Start the Flask application:

```bash
python3 server.py
```

Open a browser and navigate to:

```text
http://127.0.0.1:5000/
```

---

## Running Unit Tests

```bash
python3 test_emotion_detection.py
```

Expected result:

```text
.....
----------------------------------------------------------------------
Ran 5 tests

OK
```

---

## Static Code Analysis

Run pylint:

```bash
pylint server.py
```

Expected result:

```text
Your code has been rated at 10.00/10
```

---

## Sample Output

Input:

```text
I am glad this happened
```

Output:

```python
{
    'anger': 0.008,
    'disgust': 0.002,
    'fear': 0.013,
    'joy': 0.968,
    'sadness': 0.009,
    'dominant_emotion': 'joy'
}
```

---

## Author

Final Project completed as part of:

**Developing AI Applications with Python and Flask**

IBM Skills Network / Coursera

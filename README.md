# 🧠 Sentiment Analysis Application

A Streamlit-based web application for analyzing sentiment in text. This application uses VADER (Valence Aware Dictionary and sEntiment Reasoner) from NLTK to classify text as Positive, Negative, or Neutral.

## Features

- **Text Input**: Enter text directly into the application
- **File Upload**: Upload `.txt` files for sentiment analysis
- **Text Preprocessing**: 
  - Lowercasing
  - Punctuation removal
  - Tokenization
  - Stemming using Porter Stemmer
- **Sentiment Classification**: Classifies text as:
  - **Positive**: Compound score >= 0.05
  - **Negative**: Compound score <= -0.05
  - **Neutral**: Compound score between -0.05 and 0.05
- **Sentiment Visualization**: Bar chart showing positive, neutral, and negative score distribution
- **Loading Indicator**: Spinner shows while analysis is in progress

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sentiment-analysis-assignment-nlpa
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## How it Works

1. Enter text or upload a `.txt` file
2. Click "Analyze Sentiment" button
3. The application will:
   - Preprocess the text (lowercase, remove punctuation, tokenize, stem)
   - Analyze sentiment using VADER lexicon
   - Display the sentiment classification with visual indicator
   - Show a bar chart with sentiment score breakdown

## Dependencies

- **streamlit**: Web framework for the UI
- **nltk**: Natural Language Toolkit for sentiment analysis and preprocessing
- **matplotlib**: Data visualization library

See `requirements.txt` for full dependency list.

## Technical Details

### Sentiment Analysis
Uses VADER (Valence Aware Dictionary and sEntiment Reasoner) which is specifically tuned for social media and general internet text sentiment analysis.

### Text Preprocessing
- Converts text to lowercase
- Removes punctuation
- Tokenizes the text into words
- Stems words using Porter Stemmer algorithm

## Author

NLPA Assignment - Sentiment Analysis

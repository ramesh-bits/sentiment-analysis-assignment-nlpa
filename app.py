import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
import string

# Download required NLTK resources
nltk.download('vader_lexicon')
nltk.download('punkt_tab')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()
stemmer = PorterStemmer()

# ---------- Text Preprocessing ----------
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return " ".join(stemmed_tokens)

# ---------- Sentiment Prediction ----------
def analyze_sentiment(text):
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        sentiment = "Positive"
        color = "green"
    elif compound <= -0.05:
        sentiment = "Negative"
        color = "red"
    else:
        sentiment = "Neutral"
        color = "gray"

    return sentiment, color, scores

# ---------- Streamlit UI ----------
st.title("🧠 Sentiment Analysis Application")

st.write("Enter text or upload a text file to analyze sentiment.")

# Text input
user_text = st.text_area("Enter text here:")

# File upload
uploaded_file = st.file_uploader("Or upload a .txt file", type=["txt"])

if uploaded_file is not None:
    # Check file size limit (1MB = 1048576 bytes)
    if uploaded_file.size > 1048576:
        st.error("File size exceeds 1MB limit. Please upload a smaller file.")
    else:
        user_text = uploaded_file.read().decode("utf-8")

if st.button("Analyze Sentiment"):
    if user_text.strip() == "":
        st.warning("Please enter text or upload a file.")
    else:
        with st.spinner("Analyzing sentiment..."):
            processed_text = preprocess_text(user_text)
            sentiment, color, scores = analyze_sentiment(processed_text)

            # Display sentiment
            st.markdown(
                f"### Sentiment: <span style='color:{color}'>{sentiment}</span>",
                unsafe_allow_html=True
            )

            # Bar chart
            labels = ['Positive', 'Neutral', 'Negative']
            values = [scores['pos'], scores['neu'], scores['neg']]

            fig, ax = plt.subplots()
            ax.bar(labels, values)
            ax.set_ylabel("Score")
            ax.set_title("Sentiment Score Distribution")

            st.pyplot(fig)
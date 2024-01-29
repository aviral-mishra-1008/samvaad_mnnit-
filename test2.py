import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)['compound']

    if sentiment_score >= 0.05:
        return "Positive",sentiment_score
    elif sentiment_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    # Example usage:
    text_input = input("Enter the text for sentiment analysis: ")
    sentiment_result = analyze_sentiment(text_input)

    print(f"Sentiment: {sentiment_result}")

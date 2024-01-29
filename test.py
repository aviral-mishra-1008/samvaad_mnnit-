# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer

# def analyze_sentiment(text):
#     sid = SentimentIntensityAnalyzer()
#     sentiment_scores = sid.polarity_scores(text)

#     if sentiment_scores['compound'] >= 0.05:
#         return "Positive"
#     elif sentiment_scores['compound'] <= -0.05:
#         return "Negative"
#     else:
#         return "Neutral"

# if __name__ == "__main__":
#     # Example usage:
#     text_input = "Motilal Nehru National Institute of Technology (MNNIT) grapples with a myriad of issues, presenting a disconcerting narrative. The institution's infrastructure, once a source of pride, now stands in decay, with outdated classrooms and insufficient hostel facilities. Faculty shortages and a lack of dynamic engagement contribute to a lackluster learning environment, diminishing the overall educational experience. MNNIT's disconnect from industries becomes apparent in the scarcity of meaningful internships and workshops, leaving graduates unprepared for the demands of the professional world. Bureaucratic hurdles, resembling a Kafkaesque nightmare, impede student progress and breed frustration. The limited allocation of research funding stifles innovation, hampering the potential for groundbreaking projects and undermining the institution's claim to research excellence. These collective downsides cast a shadow over MNNIT's reputation, necessitating urgent intervention to address these concerns and reaffirm its commitment to providing a high-quality education and fostering an environment conducive to academic and personal growth."
#     sentiment_result = analyze_sentiment(text_input)

#     print(f"Sentiment: {sentiment_result}")

from transformers import pipeline

def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)
    print(result)
    return result[0]['label']

if __name__ == "__main__":
    # Example usage:
    text_input = "Motilal Nehru National Institute of Technology (MNNIT) grapples with a myriad of issues, presenting a disconcerting narrative. The institution's infrastructure, once a source of pride, now stands in decay, with outdated classrooms and insufficient hostel facilities. Faculty shortages and a lack of dynamic engagement contribute to a lackluster learning environment, diminishing the overall educational experience. MNNIT's disconnect from industries becomes apparent in the scarcity of meaningful internships and workshops, leaving graduates unprepared for the demands of the professional world. Bureaucratic hurdles, resembling a Kafkaesque nightmare, impede student progress and breed frustration. The limited allocation of research funding stifles innovation, hampering the potential for groundbreaking projects and undermining the institution's claim to research excellence. These collective downsides cast a shadow over MNNIT's reputation, necessitating urgent intervention to address these concerns and reaffirm its commitment to providing a high-quality education and fostering an environment conducive to academic and personal growth."
    
    sentiment_result = analyze_sentiment(text_input)
    print(f"Sentiment: {sentiment_result}")

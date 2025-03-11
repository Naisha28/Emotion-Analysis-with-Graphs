from transformers import pipeline
import re
import matplotlib.pyplot as plt

# Load the pre-trained emotion classification pipeline
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", return_all_scores=True)

# Function to analyze emotions in multiple sentences and plot graphs
def analyze_emotions(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())  # Split text into sentences
    results = [emotion_classifier(sentence)[0] for sentence in sentences]

    for sentence, predictions in zip(sentences, results):
        print(f"\nText: {sentence}")
        emotions = [emotion['label'] for emotion in predictions]
        scores = [emotion['score'] for emotion in predictions]

        for emotion, score in zip(emotions, scores):
            print(f"Emotion: {emotion}, Score: {score:.4f}")

        # Plot emotions for the sentence
        plt.figure(figsize=(8, 4))
        plt.bar(emotions, scores, color='skyblue')
        plt.xlabel("Emotions")
        plt.ylabel("Confidence Score")
        plt.title(f"Emotion Analysis for: {sentence}")
        plt.xticks(rotation=45)
        plt.show()

# User input
text = input("Enter the text: ")
analyze_emotions(text)

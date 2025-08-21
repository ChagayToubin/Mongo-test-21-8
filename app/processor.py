import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')# Compute sentiment labels
tweet = 'Skillcate is a great Youtube Channel to learn DataScience'
score=SentimentIntensityAnalyzer().polarity_scores(tweet)
from app.DAL_MONGO import DAL_mongo

class Processor:
    @staticmethod
    def PFinding_the_rarest_word():



        return

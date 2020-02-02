from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
import nltk

nltk.download('twitter_samples')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
nltk.download('stopwords')
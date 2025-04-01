
from textblob import TextBlob
import pandas as pd
import re


tweets = [
    "New earbuds from TechCo are a game changer, sound is unreal!",
    "This tablet’s battery dies in 2 hours, total garbage.",
    "Got a smart speaker, setup was easy but it’s just meh.",
    "Love my new gaming monitor, 144Hz is smooth as butter.",
    "Phone charger broke after a week, never buying from them again.",
    "The drone I ordered flies great, but the app crashes nonstop.",
    "Picked up a cheap keyboard, works fine for the price.",
    "Latest update bricked my TV, TechSupport is useless."
]


def clean_tweet(tweet):
    tweet = re.sub(r"http\S+|www\S+|https\S+", "", tweet, flags=re.MULTILINE)
    tweet = re.sub(r"@\w+|#\w+", "", tweet)
    tweet = re.sub(r"[^\w\s]", "", tweet)
    return tweet.strip()


def get_sentiment(tweet):
    cleaned_tweet = clean_tweet(tweet)
    analysis = TextBlob(cleaned_tweet)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


results = []
for tweet in tweets:
    sentiment = get_sentiment(tweet)
    results.append({"Tweet": tweet, "Sentiment": sentiment})


df = pd.DataFrame(results)


print("Sentiment Analysis Results:")
print(df)


df.to_csv("electronics_sentiment_results.csv", index=False)
print("\nResults saved to 'electronics_sentiment_results.csv'")

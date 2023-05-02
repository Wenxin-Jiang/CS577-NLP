---
language: 
  - "fr"

tags:
- twitter
- DistilCamemBERT
- sentiment analysis
- emojis

datasets:
- 'corpus_tweets_def.csv' 

---

# CamemBERT-base for sentiment analysis on tweets

This is a Camembert-base model trained on a corpus of 50K french tweets. 

 - Git Repo containing the dataset and the code (scraping & training) : [Git](https://git.unistra.fr/nierichlo/projet_tutore_gr1)

The model can predict which of the 25 emojis it has been trained with suits the best on a given sentence / tweet. 
The 25 emojis are the 25 most frequent in the dataset.

We've succeeded to obtain a 32% accuracy on a small amount of tweets.

**Note**: We've also decided to keep the emojis in their *demojized* versions because some emojis could be seen as two (ex : 👍🏿)

## Loading the model 

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TFAutoModelForSequenceClassification

MODEL = f"Jessy3ric/camembert-twitter-emoji"
tokenizer = AutoTokenizer.from_pretrained(MODEL)

model = AutoModelForSequenceClassification.from_pretrained(MODEL)
model.save_pretrained(MODEL)

```
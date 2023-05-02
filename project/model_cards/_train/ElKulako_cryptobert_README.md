---
datasets:
- ElKulako/stocktwits-crypto
language: 
- en
tags:
- cryptocurrency
- crypto
- BERT
- sentiment classification
- NLP
- bitcoin
- ethereum
- shib
- social media
- sentiment analysis
- cryptocurrency sentiment analysis

---

# CryptoBERT
CryptoBERT is a pre-trained NLP model to analyse the language and sentiments of cryptocurrency-related social media posts and messages. It was built by further training the [vinai's bertweet-base](https://huggingface.co/vinai/bertweet-base) language model on the cryptocurrency domain, using a corpus of over 3.2M unique cryptocurrency-related social media posts. 
(A research paper with more details will follow soon.)
## Classification Training
The model was trained on the following labels: "Bearish" : 0, "Neutral": 1, "Bullish": 2

CryptoBERT's sentiment classification head was fine-tuned on a balanced dataset of 2M labelled StockTwits posts, sampled from [ElKulako/stocktwits-crypto](https://huggingface.co/datasets/ElKulako/stocktwits-crypto). 

CryptoBERT was trained with a max sequence length of 128. Technically, it can handle sequences of up to 514 tokens, however, going beyond 128 is not recommended.

# Classification Example
```python
from transformers import TextClassificationPipeline, AutoModelForSequenceClassification, AutoTokenizer
model_name = "ElKulako/cryptobert"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels = 3)
pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, max_length=64, truncation=True, padding = 'max_length')
# post_1 & post_3 = bullish, post_2 = bearish
post_1 = " see y'all tomorrow and can't wait to see ada in the morning, i wonder what price it is going to be at. 😎🐂🤠💯😴, bitcoin is looking good go for it and flash by that 45k. "
post_2 = "  alright racers, it’s a race to the bottom! good luck today and remember there are no losers (minus those who invested in currency nobody really uses) take your marks... are you ready? go!!" 
post_3 = " i'm never selling. the whole market can bottom out. i'll continue to hold this dumpster fire until the day i die if i need to." 
df_posts = [post_1, post_2, post_3]
preds = pipe(df_posts)
print(preds)


```

```
[{'label': 'Bullish', 'score': 0.8734585642814636}, {'label': 'Bearish', 'score': 0.9889495372772217}, {'label': 'Bullish', 'score': 0.6595883965492249}]
```

## Training Corpus
CryptoBERT was trained on 3.2M social media posts regarding various cryptocurrencies. Only non-duplicate posts of length above 4 words were considered. The following communities were used as sources for our corpora:


(1) StockTwits - 1.875M posts about the top 100 cryptos by trading volume. Posts were collected from the 1st of November 2021 to the 16th of June 2022. [ElKulako/stocktwits-crypto](https://huggingface.co/datasets/ElKulako/stocktwits-crypto)

(2) Telegram - 664K posts from top 5 telegram groups: [Binance](https://t.me/binanceexchange), [Bittrex](https://t.me/BittrexGlobalEnglish), [huobi global](https://t.me/huobiglobalofficial), [Kucoin](https://t.me/Kucoin_Exchange), [OKEx](https://t.me/OKExOfficial_English). 
Data from 16.11.2020 to 30.01.2021. Courtesy of [Anton](https://www.kaggle.com/datasets/aagghh/crypto-telegram-groups).

(3) Reddit - 172K comments from various crypto investing threads, collected from May 2021 to May 2022

(4) Twitter - 496K posts with hashtags XBT, Bitcoin or BTC. Collected for May 2018. Courtesy of [Paul](https://www.kaggle.com/datasets/paul92s/bitcoin-tweets-14m).
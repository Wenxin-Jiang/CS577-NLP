---
language: en
datasets:
- tweets_hate_speech_detection
tags:
- hate
- speech

widget:
- text: "@user black lives really matter?"

---


# ByT5-base fine-tuned for Hate Speech Detection (on Tweets)
[ByT5](https://huggingface.co/google/byt5-base) base fine-tuned on [tweets hate speech detection](https://huggingface.co/datasets/tweets_hate_speech_detection) dataset for **Sequence Classification** downstream task.

# Details of ByT5 - Base 🧠

ByT5 is a tokenizer-free version of [Google's T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) and generally follows the architecture of [MT5](https://huggingface.co/google/mt5-base).
ByT5 was only pre-trained on [mC4](https://www.tensorflow.org/datasets/catalog/c4#c4multilingual) excluding any supervised training with an average span-mask of 20 UTF-8 characters. Therefore, this model has to be fine-tuned before it is useable on a downstream task.
ByT5 works especially well on noisy text data,*e.g.*, `google/byt5-base` significantly outperforms [mt5-base](https://huggingface.co/google/mt5-base) on [TweetQA](https://arxiv.org/abs/1907.06292).
Paper: [ByT5: Towards a token-free future with pre-trained byte-to-byte models](https://arxiv.org/pdf/1910.10683.pdf)
Authors: *Linting Xue, Aditya Barua, Noah Constant, Rami Al-Rfou, Sharan Narang, Mihir Kale, Adam Roberts, Colin Raffel* 


## Details of the downstream task (Sequence Classification as Text generation) - Dataset 📚

[tweets_hate_speech_detection](hhttps://huggingface.co/datasets/tweets_hate_speech_detection)


The objective of this task is to detect hate speech in tweets. For the sake of simplicity, we say a tweet contains hate speech if it has a racist or sexist sentiment associated with it. So, the task is to classify racist or sexist tweets from other tweets.

Formally, given a training sample of tweets and labels, where label ‘1’ denotes the tweet is racist/sexist and label ‘0’ denotes the tweet is not racist/sexist, your objective is to predict the labels on the given test dataset.

- Data Instances:

The dataset contains a label denoting is the tweet a hate speech or not

```json
{'label': 0,  # not a hate speech
 'tweet': ' @user when a father is dysfunctional and is so selfish he drags his kids into his dysfunction.   #run'}
```
- Data Fields:
 
**label**: 1 - it is a hate speech, 0 - not a hate speech

**tweet**: content of the tweet as a string

- Data Splits:

The data contains training data with **31962** entries

## Test set metrics 🧾

We created a representative test set with the 5% of the entries.

The dataset is so imbalanced and we got a **F1 score of 79.8**
    


## Model in Action 🚀

```sh
git clone https://github.com/huggingface/transformers.git
pip install -q ./transformers
```

```python
from transformers import AutoTokenizer, T5ForConditionalGeneration

ckpt = 'Narrativa/byt5-base-tweet-hate-detection'

tokenizer = AutoTokenizer.from_pretrained(ckpt)
model = T5ForConditionalGeneration.from_pretrained(ckpt).to("cuda")

def classify_tweet(tweet):

    inputs = tokenizer([tweet], padding='max_length', truncation=True, max_length=512, return_tensors='pt')
    input_ids = inputs.input_ids.to('cuda')
    attention_mask = inputs.attention_mask.to('cuda')
    output = model.generate(input_ids, attention_mask=attention_mask)
    return tokenizer.decode(output[0], skip_special_tokens=True)
    
    
classify_tweet('here goes your tweet...')
```

Created by: [Narrativa](https://www.narrativa.com/)

About Narrativa: Natural Language Generation (NLG) | Gabriele, our machine learning-based platform, builds and deploys natural language solutions. #NLG #AI
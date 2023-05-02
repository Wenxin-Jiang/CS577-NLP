---
language: 
- es
tags:
- roberta

license: apache-2.0
---

# Please use 'Roberta' related functions to load this model!

This repository contains the resources in our paper
**[Protest Stance Detection: Leveraging heterogeneous user interactions for extrapolation in out-of-sample country contexts]**  
*Ramon Villa-Cox, Evan Williams, Kathleen M. Carley*

We pre-trained a BERT language model, we call *TwBETO_v0* following the robust approach introduced in RoBERTa. We opted for the smaller architecture dimensions introduced in DistilBERT, namely, 6 hidden layers with 12 attention heads. We also reduce the model's maximum sequence length to 128 tokens, following another BERT instantiation trained on English Twitter data (*BERTweet*). We utilize the RoBERTa implementation in the Hugging Face library and optimize the model using Adam with weight decay, a linear schedule with warmup and a maximum learning rate of 2e-4. We use a global batch size (via gradient accumulation) of 5k across 4 Titan XP GPUs (12 GB RAM each) and trained the model for 650 hours.

The model was trained with a corpus comprised of 155M Spanish tweets (4.5B words tokens), as determined by Twitter's API, and includes only original tweets (retweets are filtered out) with more than 6 tokens, while long tweets were truncated to 64 word tokens. The data was compiled from the following sources:
- 110M Tweets (3B word tokens) from the South American protests collected from September 20 to December 31 of 2019.
- 25M (0.7B word tokens) Tweets collected around the Coronavirus pandemic from April 01 to December 31 of 2020.
- 3M (0.3B word tokens) Tweets collected around the Chilean referendum from September 25 to November 10 of 2020. 
- 17M (0.5B word tokens) rehydrated targets across all the collections listed.

Tweets are pretokenized using the "TweetTokenizer" from the NLTK toolkit and use the emoji package to translate emotion icons into word tokens (in Spanish). We also preprocess the Tweets by replacing user mentions with "*USER_AT*" and, using the tweet JSON, we replace media urls with "*HTTPMEDIA*" and web urls with "*HTTPURL*". We found that this new model produced significantly better quality embeddings than other available Spanish BERT variants for Twitter (e.g.: *TWilBert*). We hypothesize that this is a result of the latter being trained mainly on European Spanish with fewer data and it not applying the RoBERTa pretraining framework.

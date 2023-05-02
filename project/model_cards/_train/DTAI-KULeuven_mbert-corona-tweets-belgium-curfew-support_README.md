---
language: 
- multilingual
- nl
- fr
- en
tags:
- Tweets
- Sentiment analysis
widget:
- text: "I really wish I could leave my house after midnight, this makes no sense!"
---

# Measuring Shifts in Attitudes Towards COVID-19 Measures in Belgium Using Multilingual BERT
[Blog post »](https://people.cs.kuleuven.be/~pieter.delobelle/attitudes-towards-covid-19-measures/?utm_source=huggingface&utm_medium=social&utm_campaign=corona_tweets)   · [paper »](http://arxiv.org/abs/2104.09947)

This model can be used to determine if a tweet expresses support or not for a curfew. The model was trained on manually labeled tweets from Belgium in Dutch, French and English. 

We categorized several months worth of these Tweets by topic (government COVID measure) and opinion expressed. Below is a timeline of the relative number of Tweets on the curfew topic (middle) and the fraction of those Tweets that find the curfew too strict, too loose, or a suitable measure (bottom), with the number of daily cases in Belgium to give context on the pandemic situation (top).

![chart.png](https://github.com/iPieter/bert-corona-tweets/raw/master/chart.png)


Models used in this paper are on HuggingFace:  
- https://huggingface.co/DTAI-KULeuven/mbert-corona-tweets-belgium-curfew-support  
- https://huggingface.co/DTAI-KULeuven/mbert-corona-tweets-belgium-topics  

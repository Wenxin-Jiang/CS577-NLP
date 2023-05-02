---
language: 
- en
- ru

datasets:
- tweet_eval

model_index:
- name: xlm-roberta-en-ru-emoji
  results:
  - task: 
      name: Sentiment Analysis
      type: sentiment-analysis
    dataset:
      name: Tweet Eval
      type: tweet_eval
      args: emoji
      

widget:
- text: "Отлично!"
- text: "Awesome!"
- text: "lol"

---

# xlm-roberta-en-ru-emoji 
- Problem type: Multi-class Classification
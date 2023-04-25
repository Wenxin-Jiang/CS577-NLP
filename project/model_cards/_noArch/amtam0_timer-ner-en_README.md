---
tags:
- flair
- token-classification
- sequence-tagger-model
language: en
widget:
- text: "12 sets of 2 minutes 38 minutes between each set"

---

#### This model is used in the [Speech Interval Timer app](https://medium.com/@amtam0/speech-interval-timer-app-using-transformers-1df8fa3821d5)

7-class NER English model using [Flair TransformerWordEmbeddings - distilroberta-base](https://github.com/flairNLP/flair/).

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| nb_rounds         | Number of rounds | 
| duration_br_sd         | Duration btwn rounds in seconds | 
| duration_br_min         | Duration btwn rounds in minutes | 
| duration_br_hr         | Duration btwn rounds in hours | 
| duration_wt_sd         | workout duration in seconds | 
| duration_wt_min         | workout duration in minutes | 
| duration_wt_hr         | workout duration in hours | 
---
The dataset was created manually (perfectible). Sentences example : 
```
19 sets of 3 minutes 21 minutes between sets
start 7 sets of 32 seconds
create 13 sets of 26 seconds
init 8 series of 3 hours
2 sets of 30 seconds 35 minutes between each cycle
...
```
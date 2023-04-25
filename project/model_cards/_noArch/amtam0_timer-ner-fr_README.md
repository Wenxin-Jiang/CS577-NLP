---
tags:
- flair
- token-classification
- sequence-tagger-model
language: fr
widget:
- text: 'génère 27 séries de 54 seconde '
- text: ' 9 cycles de 17 minute '
- text: 'initie 17 sets de 44 secondes 297 minutes entre séries'
- text: ' 13 sets de 88 secondes 225 minutes 49 entre chaque série'
- text: 'génère 39 séries de 19 minute 21 minute 45 entre séries'
- text: 'débute 47 sets de 6 heures '
- text: 'débute 1 cycle de 25 minutes 48 23 minute 32 entre chaque série'
- text: 'commence 23 séries de 18 heure et demi 25 minutes 41 entre séries'
- text: ' 13 cycles de 52 secondes '
- text: 'crée 31 série de 60 secondes '
- text: ' 7 set de 36 secondes 139 minutes 34 entre séries'
- text: 'commence 37 sets de 51 minute 25 295 minute entre chaque série'
- text: 'crée 11 cycles de 72 seconde 169 minute 15 entre chaque série'
- text: 'initie 5 série de 33 minutes 48 '
- text: 'crée 23 set de 1 minute 46 279 minutes 50 entre chaque série'
- text: 'génère 41 série de 35 minutes 55 '
- text: 'lance 11 cycles de 4 heures '
- text: 'crée 47 cycle de 28 heure moins quart 243 minutes 45 entre chaque série'
- text: 'initie 23 set de 36 secondes '
- text: 'commence 37 sets de 24 heures et quart '

---
#### This model is used in the [Speech Interval Timer app](https://medium.com/@amtam0/speech-interval-timer-app-using-transformers-1df8fa3821d5)

7-class NER French model using [Flair TransformerWordEmbeddings - camembert-base](https://github.com/flairNLP/flair/).

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
Synthetic dataset has been used (perfectible). Sentences example in the widget.
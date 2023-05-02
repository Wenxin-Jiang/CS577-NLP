---
language:
- fr

tags:
- classification
license: apache-2.0

metrics:
- accuracy

widget:
- text: "tchai on est morts. on va se faire vacciner et ils vont contrôler comme les marionnettes avec des fils. d'après les 'ont dit'..."
---

# camembert-fr-covid-tweet-classification
This model is a fine-tune checkpoint of [Yanzhu/bertweetfr-base](https://huggingface.co/Yanzhu/bertweetfr-base), fine-tuned on SST-2.
This model reaches an accuracy of 66.00% on the dev set.

In this dataset, given a tweet, the goal was to infer the underlying topic of the tweet by choosing from four topics classes:
- chiffres : this means, the tweet talk about statistics of covid.
- mesures : this means, the tweet talk about measures take by government  of covid 
- opinions : this means, the tweet talk about opinion of people like fake new. 
- symptomes : this means, the tweet talk about symptoms or variant of covid.
- divers : or other
 
 # Pipelining the Model
 
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
tokenizer = AutoTokenizer.from_pretrained("Monsia/camembert-fr-covid-tweet-classification")
model = AutoModelForSequenceClassification.from_pretrained("Monsia/camembert-fr-covid-tweet-classification")
nlp_topic_classif = transformers.pipeline('topics-classification', model = model, tokenizer = tokenizer)
nlp_topic_classif("tchai on est morts. on va se faire vacciner et ils vont contrôler comme les marionnettes avec des fils. d'après les '' ont dit ''...")
# Output: [{'label': 'opinions', 'score': 0.831]
```
 
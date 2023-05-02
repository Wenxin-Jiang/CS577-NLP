---
widget:
- text: "Hold da op! Kan det virkelig passe?"

language: 
  - "da"
  
tags:
- sentiment
- emotion
- danish
---

# **-- EMODa --**

## BERT-model for danish multi-class classification of emotions

 Classifies a danish sentence into one of 6 different emotions:
 
 | Danish emotion      | Ekman's emotion |
| ----- | ----- |
| 😞 **Afsky**   |  Disgust      |
|  😨 **Frygt**       |  Fear      |
| 😄 **Glæde**       |    Joy    |
| 😱 **Overraskelse**   |   Surprise     |
| 😢  **Tristhed**     |    Sadness    |
| 😠 **Vrede**       |   Anger     |


# How to use

```python
from transformers import pipeline

model_path = "NikolajMunch/danish-emotion-classification"
classifier = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
prediction = classifier("Jeg er godt nok ked af at mine SMS'er er slettet")

print(prediction)
# [{'label': 'Tristhed', 'score': 0.9725030660629272}]
```

or
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
  
tokenizer = AutoTokenizer.from_pretrained("NikolajMunch/danish-emotion-classification")

model = AutoModelForSequenceClassification.from_pretrained("NikolajMunch/danish-emotion-classification")
```




### Introduction:
This model belongs to text-classification. You can determine the emotion behind a sentence.
### Label Explaination:
LABEL_0: Positive (have positive emotion)

LABEL_1: Negative (have negative emotion)
### Usage:
```python
>>> from transformers import pipeline
>>> ec = pipeline('text-classification', model='Osiris/emotion_classifier')
>>> ec("Hello, I'm a good model.")
```

### Accuracy:
We reach 83.82% for validation dataset, and 84.42% for test dataset.
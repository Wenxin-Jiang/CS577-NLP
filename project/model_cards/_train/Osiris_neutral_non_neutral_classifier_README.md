### Introduction:
This model belongs to text-classification. You can check whether the sentence consists any emotion.
### Label Explaination:
LABEL_1: Non Neutral (have some emotions)

LABEL_0: Neutral (have no emotion)
### Usage:
```python
>>> from transformers import pipeline
>>> nnc = pipeline('text-classification', model='Osiris/neutral_non_neutral_classifier')
>>> nnc("Hello, I'm a good model.")
```

### Accuracy:
We reach 93.98% for validation dataset, and 91.92% for test dataset.
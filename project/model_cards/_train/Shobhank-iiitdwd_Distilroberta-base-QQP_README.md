---
license: apache-2.0
---
## Training Data
This model was trained on the [Quora Duplicate Questions](https://www.quora.com/q/quoradata/First-Quora-Dataset-Release-Question-Pairs) dataset. The model will predict a score between 0 and 1 how likely the two given questions are duplicates.

Note: The model is not suitable to estimate the similarity of questions, e.g. the two questions "How to learn Java" and "How to learn Python" will result in a rahter low score, as these are not duplicates.

## Usage and Performance

Pre-trained models can be used like this:
```
from sentence_transformers import CrossEncoder
model = CrossEncoder('model_name')
scores = model.predict([('Question 1', 'Question 2'), ('Question 3', 'Question 4')])
```

You can use this model also without sentence_transformers and by just using Transformers ``AutoModel`` class
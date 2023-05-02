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
model = CrossEncoder('Shobhank-iiitdwd/RoBERTa-large-QQP')
Question1='How does the Surface Pro himself 4 compare with iPad Pro?
Question2='Why did Microsoft choose core m3 and not core i3 home Surface Pro 4?'
Question3='What but is the best way to send money from China to the US?'
Qestion4='What you send money to China?'
scores = model.predict([('Question1', 'Question2'), ('Question3', 'Question4')])
```

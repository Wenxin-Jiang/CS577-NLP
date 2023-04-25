---
language:
- en
license: apache-2.0
tags:
- text-classification
- emotion
- pytorch
datasets:
- emotion
metrics:
- Accuracy, F1 Score
thumbnail: https://avatars3.githubusercontent.com/u/32437151?s=460&u=4ec59abc8d21d5feea3dab323d23a5860e6996a4&v=4
model-index:
- name: bhadresh-savani/roberta-base-emotion
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: emotion
      type: emotion
      config: default
      split: test
    metrics:
    - type: accuracy
      value: 0.931
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjg5OTI4ZTlkY2VmZjYzNGEzZGQ3ZjczYzY5YjJmMGVmZDQ4ZWNiYTAyZTJiZjlmMTU2MjE1NTllMWFhYzU0MiIsInZlcnNpb24iOjF9.dc44cEsbu900M2s64GyVIWKPagBzwI-dPlfvh0NGyJFMGKOcypke9P2ary9fBZITrH3UF6lza3sCh7vWYZFHBQ
    - type: precision
      value: 0.9168321948556312
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2EzYTcxNTExNGU1MmFiZjE3NGE5MDIyMDU2M2U3OGExOTdjZDE5YWU2NDhmOTJlYWMzY2NkN2U5MmRmZTE0MiIsInZlcnNpb24iOjF9.4U7vJ3ALdUUxySMhVeb4Qa1tSp3wphSIZkRYNMujz-KrOZW8kkcmCde3ioStBg3Qqyf1powYd88uk1R7DuWRBA
    - type: precision
      value: 0.931
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjhmZGRlYWE5ZTAzMmJiMzlmMWZiM2VlYjdiNzI0NjVmN2M2YzcxM2EzYTg0OTFiZTE1MjVmNzE5NGEzYTg2ZCIsInZlcnNpb24iOjF9.8eCHAK0rlZWnhBNQdh9kcuAeItmDUAgK3KkZ7eC-GyYhi4HT5dZiS6btcC5EjkYVOS4czcjzqxfVz4PuZgtLDQ
    - type: precision
      value: 0.9357445689014415
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDhhZTdkNzYzMjhjZjc4MTAxNWZiYjgzMjhhNjRiZWRmYjc5YTA0NTQ1MzllMTYxMTVkMDk4OTE0ZGEyMTNhMiIsInZlcnNpb24iOjF9.YIZfj2Eo1nMX2GVSfqJy-Cp7VBubfUh2LuOnU60sG5Lci8FdlNbAanS1IzAyxU3U29lqiTasxfS_yrwAj5cmBQ
    - type: recall
      value: 0.8743657671177089
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiM2Y2YTcyNzMwYzZiMmM1Yzc4YWZhNDM3ZDQyMjI1NWZhMjQyNmU5NTA0YmE2ZDBiZmY1MmUyZWRlMjRhMjFmYSIsInZlcnNpb24iOjF9.XKlFy_Cx4T4l7Otd8aAwWcI-fJ_dJ6V1Kp3uZm6OWjwCb1Do6mSdPFfwiMeBZZyfEIsNBnguegssZvHsOfTSAQ
    - type: recall
      value: 0.931
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzgzN2JkNzAzZDRjNjJmZjNkY2RmYzVkMWEzYTMzZDU4NzJlYzBmOWE4MTU0MGU0MTJhM2JjZDdjODhlZDExOCIsInZlcnNpb24iOjF9.9tSVB4yNBdFXpH3equwo1ZaEnVUktO6lm93UEJ-luKhxo6wgS54OLjgDq7IpJYwa3lvYyjy-sxzQEe9ri31WAg
    - type: recall
      value: 0.931
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMGVhZTIyMmVmOTU1YWNjMmZiZjNmOTNlNzlhZTk3NjhlZmMwZGFkZWQxZTlhZWUwZGQyN2JhOWQyNWQ3MTVhOCIsInZlcnNpb24iOjF9.2odv2fK7zH0_S_7wC3obONzjxOipDdjWvddhnGdMnrIN6CiZwLp7XgizpqcWbwAQ_9YJwjC-6wXpbq2jTvN0Bw
    - type: f1
      value: 0.8821236522209227
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDI0YTUxOTA2M2ZjNGM1OTJlZDAzZTAxNTg4YjY3OWNmMjNmMTk0YWRjZTE2Y2ZmYWI1ZmU3ZmJmNzNjMjBlOCIsInZlcnNpb24iOjF9.P5-TbuEUrCtX9H7F-tKn8LI1RBPhoJwjJm_l853WTSzdLioThAtIK5HBG0xgXT2uB0Q8v94qH2b8cz1j_WonDg
    - type: f1
      value: 0.931
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjNmNDgyMmFjODYwNjcwOTJiOGM2N2YwYjUyMDk5Yjk2Y2I3NmFmZGFhYjU0NGM2OGUwZmRjNjcxYTU3YzgzNSIsInZlcnNpb24iOjF9.2ZoRJwQWVIcl_Ykxce1MnZ3mSxBGxGeNYFPxt9mivo9yTi3gUE7ua6JRpVEOnOUbevlWxVkUUNnmOPFqBN1sCQ
    - type: f1
      value: 0.9300782840205046
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMGE1OTcxNmNmMjQ3ZDAzYzk0N2Q1MGFjM2VhNWMyYmRjY2E3ZThjODExOTNlNWMxYzdlMWM2MDBiMTZhY2M2OSIsInZlcnNpb24iOjF9.r63SEArCiFB5m0ccV2q_t5uSOtjVnWdz4PfvCYUchm0JlrRC9YAm5oWKeO419wdyFY4rZFe014yv7sRcV-CgBQ
    - type: loss
      value: 0.15155883133411407
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2M4MmVlNjAzZjhiMWJlNWQxMDg5ZTRiYjFlZGYyMGMyYzU4M2IwY2E1M2E2MzA5NmU5ZjgwZTZmMDI5YjgzMyIsInZlcnNpb24iOjF9.kjgFJohkTxLKtzHJDlBvd6qolGQDSZLbrDE7C07xNGmarhTLc_A3MmLeC4MmQGOl1DxfnHflImIkdqPylyylDA
---
# robert-base-emotion

## Model description:
[roberta](https://arxiv.org/abs/1907.11692) is Bert with better hyperparameter choices so they said it's Robustly optimized Bert during pretraining.

[roberta-base](https://huggingface.co/roberta-base) finetuned on the emotion dataset using HuggingFace Trainer with below Hyperparameters
```
 learning rate 2e-5, 
 batch size 64,
 num_train_epochs=8,
```

## Model Performance Comparision on Emotion Dataset from Twitter:

| Model | Accuracy | F1 Score |  Test Sample per Second |
| --- | --- | --- | --- |
| [Distilbert-base-uncased-emotion](https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion) | 93.8 | 93.79 | 398.69 |
| [Bert-base-uncased-emotion](https://huggingface.co/bhadresh-savani/bert-base-uncased-emotion) | 94.05 | 94.06 | 190.152 |
| [Roberta-base-emotion](https://huggingface.co/bhadresh-savani/roberta-base-emotion) | 93.95 | 93.97| 195.639 |
| [Albert-base-v2-emotion](https://huggingface.co/bhadresh-savani/albert-base-v2-emotion) | 93.6 | 93.65 | 182.794 |

## How to Use the model:
```python
from transformers import pipeline
classifier = pipeline("text-classification",model='bhadresh-savani/roberta-base-emotion', return_all_scores=True)
prediction = classifier("I love using transformers. The best part is wide range of support and its easy to use", )
print(prediction)

"""
Output:
[[
{'label': 'sadness', 'score': 0.002281982684507966}, 
{'label': 'joy', 'score': 0.9726489186286926}, 
{'label': 'love', 'score': 0.021365027874708176}, 
{'label': 'anger', 'score': 0.0026395076420158148}, 
{'label': 'fear', 'score': 0.0007162453257478774}, 
{'label': 'surprise', 'score': 0.0003483477921690792}
]]
"""
```

## Dataset:
[Twitter-Sentiment-Analysis](https://huggingface.co/nlp/viewer/?dataset=emotion).

## Training procedure
[Colab Notebook](https://github.com/bhadreshpsavani/ExploringSentimentalAnalysis/blob/main/SentimentalAnalysisWithDistilbert.ipynb)
follow the above notebook by changing the model name to roberta

## Eval results
```json
{
 'test_accuracy': 0.9395,
 'test_f1': 0.9397328860104454,
 'test_loss': 0.14367154240608215,
 'test_runtime': 10.2229,
 'test_samples_per_second': 195.639,
 'test_steps_per_second': 3.13
 }
```

## Reference:
* [Natural Language Processing with Transformer By Lewis Tunstall, Leandro von Werra, Thomas Wolf](https://learning.oreilly.com/library/view/natural-language-processing/9781098103231/)
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
- name: bhadresh-savani/electra-base-emotion
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
      value: 0.9265
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjYwNGQxMzRmMjViNzVhODJjM2UxOGNkYmNjOTE3OTczNzUxN2IyNGY1ZmFiY2VlNzNkOWY3M2I5YmZlNDlmMyIsInZlcnNpb24iOjF9.4e7MLUVHIBXYIwOgAcSDRJ7ziMXMSwk2-Ip8DH1RjxBDthc4MiBglMxbOUUjSzTPtSSEZKqfTZonUq7yR_rwBQ
    - type: precision
      value: 0.911532655431019
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzFkYzRjZGUwYmJmNmUxYjM3NzY3NWY0NzBhZjU5MDQxZWY4ZjA3OWMwMjQxMWJlODg5ZjIxZWFhYTg0ZGY2NCIsInZlcnNpb24iOjF9.I0j92y0SToxjoKkKX7AD8h5p3pDePSdQwOCBeZj-OGF0MRBeqo1Ejg-1snFFplU0mtoFF6rCvRq9WosqvRhfCA
    - type: precision
      value: 0.9265
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGE2YzUyN2ZhYTdjZjQ4OWVkN2M4MzhjZWM0YzAyYWU2YjllZDYzOTYxYTZlZDAxNjA4ODY5NTk1MmE3ODQwZiIsInZlcnNpb24iOjF9.VQSaLzlreAIfy0iDJsCo-Mg1xF4gMv-KQkeIzoTKLhyp3V7rn5d5oaD8EEsay3gDamSC-xj8LndOqFL1AokZCg
    - type: precision
      value: 0.9305456360257519
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjcyZDdjMWE5YzhlNWUyZDg5YWUwOGRkYWFiMDNmMTY4N2QxZDg1YTU0MGQ2ZWI1ZDI5Mjk2MTVmN2JmZTA1YiIsInZlcnNpb24iOjF9.EvcL-mfmJ3rGQCaVRejoWplButUT_dQjgwPw-rWlqSC7Ex3reLa3hQ9PtYuXtYM3ymVl77rFgW2Yxf3lIn6RBg
    - type: recall
      value: 0.8536923122511134
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjIwNjU1ZmIwYzgyYzNmNmY2NDkyNjA2MDg0NDcxOWQwMmJmZTFlYzg0NjI0YWMxNzhmYTQwNzU0Yzg5ZTk4MCIsInZlcnNpb24iOjF9.8he8WOjzHqJp5h2TUig7oDrn4jwSbSB1J69fmh-2UUrpH46VpwxD5bO0MG3Nm4HHYK2ZIzPb-sTX7hhMJHM7Bw
    - type: recall
      value: 0.9265
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjRiODljZTc0ZDU3YWNlZTRlYjQwY2M5YWFiY2VkOWM5Yjg5NjYzZTNkYTA1ZTc3ZjU3YjY3ZGMzNWFiNTNhNSIsInZlcnNpb24iOjF9.W74pDxOq18_Wr3Mmd0f1whXMJuVT3DhmYCWh3Z_VKB6QMSgNUf4l1iBYukIT8Lrwr50z4pscBGY3YktlUgg5Bg
    - type: recall
      value: 0.9265
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjgxNDhjMDcwZTA2ZWQ2NTFlMTFjOGU4NDE4ZDY0MDJjNGMwOGYzMDViYTM5Y2M5ZTc2NDM3OTdmYTc1NzhhMiIsInZlcnNpb24iOjF9.x4sUtEJWliLYqyKkKMEvb10lSxqN8vhrmSAnwtyCp0tEag6DUNEUA6_nojaC3ABIDb4ZwVd7JIcQ5yD2PKU-Dg
    - type: f1
      value: 0.8657529340483895
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZmUzZjNiOTZhNjE0ZWE5NDI2NzBmOGViYTc0NWYwYWQ3ZjA1ZTE1NmM5ZWRiZjA0NGYyZDM2OWE5YzA4NDY1MyIsInZlcnNpb24iOjF9.OLYrJI7nW4-nvCbEsJDIwyGL9lI1UNM-TBpMmosbkUCLu8MhhCdMo0tdKRaCRoDUtfLlwcUG9mOayAsDdfrqCw
    - type: f1
      value: 0.9265
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZWE1ZDI1MzA3YTcwODU0NTgxYTNmYjc5ZDZkYzI3OWZmYjNlNjI5OWI4MDE4NDRhOWMyNWZiMjZlMTIwNWU3YSIsInZlcnNpb24iOjF9.ZpLdxeqJjKiLxUxRIVbBZa9u5w0UMPKVwvOha4tHMTiyq3RaW8TNOkFdO7TIsgxoPdQb6wzWNDojrqJOY4vsDg
    - type: f1
      value: 0.924844632421077
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2VhNWZmM2E4NDI5NmRiMWJkNDk2MDMyMDZmYmE2ODBlNTA2NTdhYTc4NzRkOGU1ODczZDU4MTdhYTZlOTRiZCIsInZlcnNpb24iOjF9.93XiZO_2N0nLa2PU3TICEOT8HjURPzpaAVD_5e5MFMHrtMIB1Barg0cvzc3TCisKxV_vlt1i20d2YwtfWKgrBQ
    - type: loss
      value: 0.3268870413303375
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiM2IyMjdlMWZkNjQwNWVkYzU1MWYyODJkMzAwOWJmZWJiYTI0OGRlZjhkMmZkN2JhMjJmMDdkMzQ1Y2U3NDY3MyIsInZlcnNpb24iOjF9.aEnyBFvFKixU1zh5GYkIUDcf4uD6PV7pESdbdvG_oJ1lIisOg6CEb6nekcYtDebcoL3q1cbrBdhgK6dgdShJBQ
---
# Electra-base-emotion

## Model description:

## Model Performance Comparision on Emotion Dataset from Twitter:

| Model | Accuracy | F1 Score |  Test Sample per Second |
| --- | --- | --- | --- |
| [Distilbert-base-uncased-emotion](https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion) | 93.8 | 93.79 | 398.69 |
| [Bert-base-uncased-emotion](https://huggingface.co/bhadresh-savani/bert-base-uncased-emotion) | 94.05 | 94.06 | 190.152 |
| [Roberta-base-emotion](https://huggingface.co/bhadresh-savani/roberta-base-emotion) | 93.95 | 93.97| 195.639 |
| [Albert-base-v2-emotion](https://huggingface.co/bhadresh-savani/albert-base-v2-emotion) | 93.6 | 93.65 | 182.794 |
| [Electra-base-emotion](https://huggingface.co/bhadresh-savani/electra-base-emotion) | 91.95 | 91.90 | 472.72 |

## How to Use the model:
```python
from transformers import pipeline
classifier = pipeline("text-classification",model='bhadresh-savani/electra-base-emotion', return_all_scores=True)
prediction = classifier("I love using transformers. The best part is wide range of support and its easy to use", )
print(prediction)

"""
Output:
[[
{'label': 'sadness', 'score': 0.0006792712374590337}, 
{'label': 'joy', 'score': 0.9959300756454468}, 
{'label': 'love', 'score': 0.0009452480007894337}, 
{'label': 'anger', 'score': 0.0018055217806249857}, 
{'label': 'fear', 'score': 0.00041110432357527316}, 
{'label': 'surprise', 'score': 0.0002288572577526793}
]]
"""
```

## Dataset:
[Twitter-Sentiment-Analysis](https://huggingface.co/nlp/viewer/?dataset=emotion).

## Training procedure
[Colab Notebook](https://github.com/bhadreshpsavani/ExploringSentimentalAnalysis/blob/main/SentimentalAnalysisWithDistilbert.ipynb)

## Eval results
```json
{
 'epoch': 8.0,
 'eval_accuracy': 0.9195,
 'eval_f1': 0.918975455617076,
 'eval_loss': 0.3486028015613556,
 'eval_runtime': 4.2308,
 'eval_samples_per_second': 472.726,
 'eval_steps_per_second': 7.564
 }
 ```

## Reference:
* [Natural Language Processing with Transformer By Lewis Tunstall, Leandro von Werra, Thomas Wolf](https://learning.oreilly.com/library/view/natural-language-processing/9781098103231/)
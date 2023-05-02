---
language: en
license: apache-2.0
tags:
- sagemaker
- roberta-base
- text classification
datasets:
- emotion
widget:
- text: I am really upset that I have to call up to three times to the number on the
    back of my insurance card for my call to be answer
model-index:
- name: sagemaker-roberta-base-emotion
  results:
  - task:
      type: text-classification
      name: Multi Class Text Classification
    dataset:
      name: emotion
      type: emotion
    metrics:
    - type: accuracy
      value: 94.1
      name: Validation Accuracy
    - type: f1
      value: 94.13
      name: Validation F1
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
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNmM1ZmI0NjZhYjdlMWU4NWUwZmFjODFmMmM5MTlhMmEyMmQwOTk2NjQ5ZDNlYmFlMGEyMTY4Y2JiMTcwM2MwNiIsInZlcnNpb24iOjF9.haDbUk1y7nW1e_ext0s1xKefyOzep-XFa1HEkNQEcNV0cHCSRb-0YFakMf5Iee6q_EWFUS-QYxNkgEBlbw3fCQ
    - type: precision
      value: 0.8833042147663716
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjZkOTQyMzkwYjE1ZWQ5YjJkMTEzNmIyZmFlMjkwY2YxNzA3OWE0ZDk5YjJlOWVhOTU5Nzc4ZTk5Mzg5NDcxOCIsInZlcnNpb24iOjF9._XhknNSsiailHiMr1SH9ki7SRswR_b-embALunoCjhBssh9WERkv0z1xpsbw7ORo0wx7WCslZRdJWaQoXOmgDQ
    - type: precision
      value: 0.931
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMGY0MTc0ZDBiYmZlYmFmMTcyYjk5MWM0MTRmYTlhY2U1ODY5NTQzNTQ5YjAzN2U0YjljNDAzZDQ5NDBkZDUwYyIsInZlcnNpb24iOjF9.313HYKetR4S4kjcMvEk9Yj2J-Ox8ZqvVk4FLrF6UmxlXYZ4F3put-89BEOxGl_ScugjjAWhKY1pHLPYpKz9PAA
    - type: precision
      value: 0.9337002742192515
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjQ1ZDIzNmE3MjljMTk2NTBmNzcyMTEyOTUwZTljYTA2MjIwY2E4ZThkNGVjYjQwNzU3MTcxMzBiYzJkNWIzOSIsInZlcnNpb24iOjF9.6yXKQ9WS9AWdt1jxixtA5O2S1bcPTKQqIOw291Ytam8OI-zdTI2jwltT6JdU4lHdhTi5797zeNldJMCxGPR2DQ
    - type: recall
      value: 0.9087144572668905
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzJhNTFmNGJkYTAxNzRiOWQ4YzQyMGY5NGQxMjBiMmRjZTA5OTM2ZjM0NWY0ZDJiOTIyODQzZTZkMzEzZmY4YSIsInZlcnNpb24iOjF9.Fy1gkGvRiyANGU6nYgc5QbhccqAfb4PjxEk1EkJAIAZJjs-f0hffwUDlJt_6gRY3KKnoU2kKg1XxpWjybRY7BQ
    - type: recall
      value: 0.931
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTgwYWJmZDAzM2VkOGNjNjY3NjViOTFiMTYyZDc4ZDIzY2VhNTcwMDg3MjdiOTI4Nzc5ODI4N2ExYzY5ODAzMyIsInZlcnNpb24iOjF9.bEW-tZ-5JqkPDDfqkrdvzlzTGEJtYqRACZI1Jv7C8fWkJ8uJj0eQ8TDhcdGGDnFML-q1z3tnkO6PJuK9V2IxAg
    - type: recall
      value: 0.931
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTM2ZDk4NDQ2YWIwM2VjNzUxZjQ0YzU4MzViZGMzYzA3YjlhMTI1NjQwOTM3M2U4NGJhNTMxYzllMjRkMzU2NSIsInZlcnNpb24iOjF9.k9yprOWEoB0-k306GyDGF-g4uw3kABLc8iE_3E5ZYfVbo9VHPo61GuSsWJyYJ7_aq6zWbzgfOFEwUeVjcmnaDA
    - type: f1
      value: 0.8949974527433656
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODg0ZDllYWJkYWZkMWY2NjEzYWIxMWIwMWUyZDhmNWEzM2FmN2E0MWEwOTIyMTM2YTI1MDdmYmRmZWQ5ZmVmNCIsInZlcnNpb24iOjF9.DUD3dfb4vRu-Z9YxvDErJaPLuZIEDBNsdqzkf4ee6dkOCOnYtUhGAybnxtGN1xSYsynXYhU-ymCajWcrVKUCAA
    - type: f1
      value: 0.931
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOGU0MTYyOTNjOTBmNzAxNjVlZmQxYmRkMmE5MWY2NzhlNjg0ZGZkMmNmZmI3Zjk1NjJlYTdjMGRhMDMwYzAzNCIsInZlcnNpb24iOjF9.h0wCmhwRT4qRZJcc2zGP3T7dF0_wKdKzTtSVoVWFOUzQZ3RoeY2Hfjl3XA7yyw9KnoDWnLiW8DU_5kOBX-peCQ
    - type: f1
      value: 0.9318434300647934
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZmU4OGY4M2NkYWExNjI3Yjk0YmYzNWJjZGQ5ZGNmYzc4ZDk4YzRmZDRiNmRkN2VlNDZhOGIwZDc3MzcxYjVlYiIsInZlcnNpb24iOjF9.qhwi7AV-7NSm1yVd8v1Ea3nTRAFXfqLMwUJ5PUbPSa11jJ0tZNOQVDXHMAD8fVmoueLgZNRUpPVIB881Sq3EBg
    - type: loss
      value: 0.17379647493362427
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDdjODE2MjA5ODg2MmM2OWJmMjMzMzUzNGU1ZDc5NjRkNGU4N2VmNmM2NWE0YTEyYWMxNGUzN2M3YTkxNzUyMCIsInZlcnNpb24iOjF9.qcQWfHuRnfiluicR7gke3vm9u701hB4Bp0YaX2opaxL6d5DRCzuqAg-2kdmhhOL-8DW5JhY6gTrF14AEuEE9Cw
---
## roberta-base

This model is a fine-tuned model that was trained using Amazon SageMaker and the new Hugging Face Deep Learning container.
- Problem type: Multi Class Text Classification (emotion detection).

It achieves the following results on the evaluation set:
- Loss: 0.1613253802061081
- f1: 0.9413321705151999

## Hyperparameters
```json
{
    "epochs": 10,
    "train_batch_size": 16,
    "learning_rate": 3e-5, 
    "weight_decay":0.01,
    "load_best_model_at_end": true,
    "model_name":"roberta-base",
    "do_eval": True,
    "load_best_model_at_end":True
}
```
## Validation Metrics
| key | value |
| --- | ----- |
| eval_accuracy  | 0.941 |
| eval_f1 | 0.9413321705151999 |
| eval_loss | 0.1613253802061081|
| eval_recall | 0.941 |
| eval_precision | 0.9419519436781406 |


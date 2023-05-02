---
language: en
tags:
- autotrain
- DEV
datasets:
- rajistics/autotrain-data-auditor-sentiment
- FinanceInc/auditor_sentiment
widget:
- text: Operating profit jumped to EUR 47 million from EUR 6.6 million
co2_eq_emissions: 3.165771608457648
model-index:
- name: auditor_sentiment_finetuned
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: FinanceInc/auditor_sentiment
      type: glue
      split: validation
    metrics:
    - type: accuracy
      value: 0.848937
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYWQ1N2FhNjliMzMyOGVjZWUwYTllMmM5Nzg3ZWYxYzY5NWZkYzQxMmQ3OTI1NjY5MjU3NjdiNzVkNGU5YWZiMCIsInZlcnNpb24iOjF9.W3FtDbi_SgD0kwotQ14wwVsmLor8uYR4vNlW8_MqTY99vw7pZNURkq8VtrGh9nKzGUJTv7vWdX1moIA8rCNEDA
    - type: f1
      value: 0.848282
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNWMxY2Q2Nzk0MmM5NzJhNzVhOWYyMDhkMDk1MWJkMjFmOTA2YzUwNjMxNmVlMWI5NjhmOGI0NmQ0MGIyMWRhYSIsInZlcnNpb24iOjF9.HkMmrEUXuzU_jHjMO9g6V1Xo2svOe5gdlu28SyMUXugJbIy5_RJ6joDyhxj06TucT_ZRhr6v77AxCgHB3uwuDA
    - type: recall
      value: 0.808937
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODViZDYzOWYzNmQyMjlmYjhlMmExOGY0ZDBjMDFmNWMzYWM0OWVhYWJlNTBkMGEwYTYzY2IyN2Y0MmExZDE1YyIsInZlcnNpb24iOjF9.C1T-yBNPoZ8F-vVYIp9oTd6k4mTSOFw4kAcr6er68Psmt0mfuJ0Xb2nWGXeA0jrgV6bUoomTpZbwGRxtUXzAAA
    - type: precision
      value: 0.818542
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTk3NTIyZDA5MjY1NjZlMjQ0M2ZmNTU3MmRmYzM2NWVhZjU1ZDVkMTU1NTA0MzNkNzIxMjI5ZDAwNjNmNWNjNyIsInZlcnNpb24iOjF9.NBlzUtsAmjG-vBch2KxTNaahGdjFx1IYXWo7AsKQru1kNeVzmoYr-HMixQjgMG2Lg5XW8-yoP79eDOMh_lvLCg
    - type: accuracy
      value: 0.848937
      name: Accuracy
      verified: true
    - type: f1
      value: 0.848282
      name: F1
      verified: true
    - type: recall
      value: 0.808937
      name: Recall
      verified: true
    - type: precision
      value: 0.818542
      name: Precision
      verified: true
---

# Auditor Review Sentiment Model

This model has been finetuned from the proprietary version of [FinBERT](https://huggingface.co/FinanceInc/finbert-pretrain) trained internally using demo.org proprietary dataset of auditor evaluation of sentiment.  

FinBERT is a BERT model pre-trained on a large corpora of financial texts. The purpose is to enhance financial NLP research and practice in the financial domain, hoping that financial practitioners and researchers can benefit from this model without the necessity of the significant computational resources required to train the model.

# Training Data

This model was fine-tuned using [Autotrain](https://ui.autotrain.huggingface.co/11671/metrics) from the demo-org/auditor_review review dataset.  

# Model Status
This model is currently being evaluated in development until the end of the quarter.  Based on the results, it may be elevated to production.


### Training hyperparameters
The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP


# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: [1167143226](https://huggingface.co/rajistics/autotrain-auditor-sentiment-1167143226)
- CO2 Emissions (in grams): 3.165771608457648

## Validation Metrics

- Loss: 0.3418470025062561
- Accuracy: 0.8617131062951496
- Macro F1: 0.8448284352912685
- Micro F1: 0.8617131062951496
- Weighted F1: 0.8612696670395574
- Macro Precision: 0.8440532616584138
- Micro Precision: 0.8617131062951496
- Weighted Precision: 0.8612762332366959
- Macro Recall: 0.8461980005490884
- Micro Recall: 0.8617131062951496
- Weighted Recall: 0.8617131062951496


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/rajistics/autotrain-auditor-sentiment-1167143226
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("rajistics/autotrain-auditor-sentiment-1167143226", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("rajistics/autotrain-auditor-sentiment-1167143226", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```
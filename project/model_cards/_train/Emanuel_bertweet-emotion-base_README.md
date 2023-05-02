---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- accuracy
model-index:
- name: bertweet-emotion-base
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: emotion
      type: emotion
      args: default
    metrics:
    - type: accuracy
      value: 0.945
      name: Accuracy
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
      value: 0.9285
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGJhMTM3YzAyMDg0YTA1MTY4ZjMyZGY1OThjYTI0ODZlOTFlMzAwZWFkNzc3MzQ4YjNiMzViMGIxYTY4M2Q1NiIsInZlcnNpb24iOjF9.1RDEvEoO3YooUsWgDUbuRoia0PBNo6dbGn9lFiXqfeCowHQMLpagMQpBHIoofCmlQA4ZHQbBtwY5lSCzJugzBQ
    - type: precision
      value: 0.8884219402987917
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjQ2YzhiZDg3ZTJlOGYzNTBlNjEzZTNhYjIyMjFiNWJiZjNjNjg0MTFjMDFjNmI4MzEyZThkMTg5YTNkMzNhZCIsInZlcnNpb24iOjF9.yjvC1cZQllxTpkW3e5bLBA5Wmk9o6xTwusDSPVOQsbapD-XZ5TG06dgG8OF7yxQWvYLEiIp5K0VxnGA645ngBw
    - type: precision
      value: 0.9285
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDE4MjcwYTgxZmM2Y2M5YzUxNmVjMWMxYjUxYzMxNWJlMGMzOGY2MWZkYTRlZTFkMWUwOTE3YjI4MmE5ZGQ3YiIsInZlcnNpb24iOjF9.SD7BSPVASL91UHNj4vJ226sPAUteEXGoEF2KWc1pKhdwUh0ZBFlnMBYbaNH6Fey0M-Cc6kqQHsYyMpBbgBG0Cw
    - type: precision
      value: 0.9294663182278102
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDAzMjE3M2FmMjEwMzE2ZDA4NGI3ZDI1ZDlkMjhlZmEzNTlmZWM4NjRlMDNjODIzMTE1N2JiMTE5OTA2N2EzYSIsInZlcnNpb24iOjF9.O7Y0CljPErSGKRacqPcDuzlJEOFo_cnQMqmXcW94JFeq_jWHXEqxHb8Jszi2LCQOlDmFf81Yn1gr7qNbef0lDQ
    - type: recall
      value: 0.8859392810987465
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjVkODBlZTVlZmNiYjMyNDU2MDRiYWY4M2Y3MDRhNGQ0OTFlNDBiOGIwNGUxNzczMGFjMjg1YzNhNWI4N2QzMiIsInZlcnNpb24iOjF9.qBdhvXbJXKpoCQpJadg5rLlvTgfl4kitQlelAeCLNLTUyq6lBEg8onL78j2ln7m-njgF6dC0M10n4riIbTseDA
    - type: recall
      value: 0.9285
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2FlYjdmOWNiODUyNmI0OWViYjc2NWNhOTVlMDkyYWMxZjIyMDJlMjZkY2I3Yjg1ZjBlOTQ3MWY4ZDI3MDEwZCIsInZlcnNpb24iOjF9.ZaZNohPIOgvh5NQe6s5PWNyxwtMlrGQxsGz_zeqKshF9btY69cNQxyg9jlfXqrdmI4XhmC8K_MIEObkbfgqCBw
    - type: recall
      value: 0.9285
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNWQ2ODgzMjE2MGE2MmM4OGEyNWUxMWU5OGE3N2JmYTY0MWMzM2JkNjQ3ZDkzMWJkZmU5YWFlYTJhYzg3ODI5NCIsInZlcnNpb24iOjF9.ELxb_KXB0H-SaXOW97WUkTaNzAPH6itG0BpOtvcY-3J33Kr7Wi4eLEyX1fYjgY01LbkPmH4UN-rUQz2pXoRBCQ
    - type: f1
      value: 0.8863603878501328
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGYxOWRmYzVkYWE2YWRmMTY5ODFkNWU2MGYyZWZmZmIxOTQwN2E1MTJlZjFlMTAzNjNmMzM0OGM3MTAxNzNhYSIsInZlcnNpb24iOjF9.sgcxi41I9bPbli1HO0jS9tXEVIVwdmp2nw5_nG16wO-eF5R8m7uezIUbwf8SfwTDijsZPKU7n5GI1ugKKTXbCQ
    - type: f1
      value: 0.9285
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOWU0MGE3ZjViMzAzMTk1MzhiYjA1OTM4ZDRmZDU5NmRjODE0NThiOWY1MDVjNmU2OTI1OTAzYzY0NjY0NzMwZCIsInZlcnNpb24iOjF9.-_1WgnpD_qr18pp89fkgP651yW5YZ8Vm9i0M4gH8m8uosqOlnft8i7ppsDD5sp689aDoNjqtczPi_pGTvH8iAw
    - type: f1
      value: 0.9284728367890772
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDMwZDUwYThkYWU2ZDBkYzRlZGQ2YjE2MGE2YjJjNWEyMDcwM2Y2YjY1NTE1ODNmZDgzNjdhZmI4ZjFhZTM1NCIsInZlcnNpb24iOjF9.HeNsdbp4LC3pY_ZXA55xccmAvzP3LZe6ohrSuUFBInMTyO8ZExnnk5ysiXv9AJp-O3GBamQe8LKv_mxyboErAQ
    - type: loss
      value: 0.1349370777606964
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2RmN2U3YjVjNjg0NzU5NmMwOTcxM2NlMjNhNzdjMzVkMTVhYTJhNDhkMWEyMmFhZjg1NDgzODhjN2FlNzA4NiIsInZlcnNpb24iOjF9.mxi_oEnLE4QwXvm3LsT2wqa1zp7Ovul2SGpNdZjDOa0v-OWz6BfDwhNZFgQQFuls56Mi-yf9LkBevy0aNSBvAw
---

# bertweet-emotion-base

This model is a fine-tuned version of [Bertweet](https://huggingface.co/vinai/bertweet-base). It achieves the following results on the evaluation set:
- Loss: 0.1172
- Accuracy: 0.945

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 80
- eval_batch_size: 80
- lr_scheduler_type: linear
- num_epochs: 6.0 

### Framework versions
- Transformers 4.12.5
- Pytorch 1.10.0+cu113
- Datasets 1.15.1
- Tokenizers 0.10.3
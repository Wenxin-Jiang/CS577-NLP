---
language:
- pt
license: mit
tags:
- generated_from_trainer
datasets:
- lener_br
metrics:
- precision
- recall
- f1
- accuracy
model_index:
- name: bertimbau-base-lener_br
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: lener_br
      type: lener_br
      args: lener_br
    metric:
      name: Accuracy
      type: accuracy
      value: 0.9692504609383333
model-index:
- name: Luciano/bertimbau-base-lener_br
  results:
  - task:
      type: token-classification
      name: Token Classification
    dataset:
      name: lener_br
      type: lener_br
      config: lener_br
      split: test
    metrics:
    - type: accuracy
      value: 0.9824282794418222
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDZiZTRmMzRiZDFjOGMzZTM3ODRmNTEwNjI5OTM2ZDhlZjViMDk0YmJjOWViYjM3YmJmZGI2MjJiOTI3OGNmZCIsInZlcnNpb24iOjF9.7DVb3B_moqPXev5yxjcCvBCZDcJdmm3qZsSrp-RVOggLEr_AUfkBrF_76tDVLs9DszD1AlW4ERXcc0ZCqSCaDw
    - type: precision
      value: 0.9877557596262284
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTE2MGQ4ZGM1NTEwOGFmMjM3ODAyYTg3MWM1YjVhZGVlYThiNzFjYTE4NWJhOTU3OWZjMjhkODcwNGNiMmIxMyIsInZlcnNpb24iOjF9.G1e_jAOIDcuaOXWNjeRqlHTqJHVc_akZavhyvgBkAPiCTRgoTR24OUu9e_izofDMSTo4xhkMIwsC_O9tKzkNCA
    - type: recall
      value: 0.9870401674313772
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTkyZjEwMzk2NTBjY2RhMWVhYWVkOWQ2ZThkZDMwODczMDVkNDI2ZjM3OTA1ODg5NGQyYWUxMGQ5MDRkNjNlNiIsInZlcnNpb24iOjF9.qDL8618-ZTT_iO-eppn7JzVVfd_ayuj4mTT7eIc3zFYKJUp4KNpFgxnjuSVEZTcdOG48YrSISXJoHM5jVXg_DA
    - type: f1
      value: 0.9873978338768773
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjYwOWZkZmFiMTRjY2UyOTJmMDNjMzkzNjUxYTAzYzM2ZDNkMmU0NTQ5NDlmMzU5YWExMDNiZjUzOGVlZjc1OSIsInZlcnNpb24iOjF9.T7MDH4H4E6eiLZot4W_tNzVgi-ctOrSb148x9WttkJFaxh-2P4kNmm4bKJhF1ZZZKgja80hKp_Nm9dmqXU7gAg
    - type: loss
      value: 0.11542011797428131
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDA3OGRkY2Q2MjlkZWZlZTVhZDk0MjY3MDA0MzgwZjI4MTk3Y2Q2ZmRkMGI3OTQwMzcyMzVjMGE5MzU4ODY5MiIsInZlcnNpb24iOjF9.nHtVSN-vvFjDRCWC5dXPf8dmk9Rrj-JNqvehDSGCAGLl3WknpwNHzCrJM9sNlRiNgwEIA4ekBHOC_V_OHhp7Bw
  - task:
      type: token-classification
      name: Token Classification
    dataset:
      name: lener_br
      type: lener_br
      config: lener_br
      split: validation
    metrics:
    - type: accuracy
      value: 0.9692504609383333
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjY2N2VkZTIyMWM2ZTUxYzFiNjFhNzgwODgzNDQxNTMwODczMThjZDE5MzE3MTllN2ZlNjc4OWI0YTY0NzJkNCIsInZlcnNpb24iOjF9._atPyYtbN7AmDCZHNQHeBDFolzgKbQ04C1c1gfNBomkxlLXiZUVDSPwCNP9fveXhnXwkDsoy3hfm44BTsHtBAw
    - type: precision
      value: 0.9786866842043531
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZGQzMjM1M2U2MzZiZjJmNGQ1NmUxNjE0NWYyOWJkNGM3NmE0NDg2MjAwZGNkNGZmZDEwMjkwZGQ1MDgyMWU3ZSIsInZlcnNpb24iOjF9.1XNuw2s47lqZD-ywmdEcI6UpPyl_aR-8cxlU1laQYEsUNW1fEZwB90sr7cSbNNTndzEsuH9VzeKgHwlHarq7Dg
    - type: recall
      value: 0.9840619998315222
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjllM2VlZTI5NzZlNGFhMjIyN2ZmYmQzNzQ2NDYxZWNkMzY5NzM0YTY3MDE2OTMxMjdiYzkwNjc1ZjBkNDRjYSIsInZlcnNpb24iOjF9.C7SeMwbtrmD24YWsYsxi4RRaVSsuQU-Rj83b-vZ8_H1IggmyNMpv8Y2z1mDh6b5UgaHpuk9YQb9aRKbQuCjTCA
    - type: f1
      value: 0.9813669814173863
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDZjNjNiZjRhNThhNzBiMDNmODIyOTM0YjEwNWVhZTQ5MWRiYzU2ZjBkOGY3NzgzOGE2ZTJkOTNhZWZlMzgxYyIsInZlcnNpb24iOjF9.YDySY0KSF3PieEXXjx1y6GsXr9PQVNF1RW_zAQNTPcbgU8OEwyts_tUXFIT61QVGVchFOG4bLFs0ggOuwvZKBA
    - type: loss
      value: 0.22302456200122833
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzFhNTFiYzE1ZjY4MmRjMTI5NGY2YWEyYzY4NzBkYTVjMTk0MWVkODBhY2M0NWQ0ZjM1MmVjZTRmM2RhOTUxZiIsInZlcnNpb24iOjF9.-AXmb23GEbxQ282y9wL-Xvv5cZg0Z3SGQQks5As_BrXlCf8ay8sgd1VWEB4NTepn8MnKJgJkqyQK4JXxSSYCCQ
  - task:
      type: token-classification
      name: Token Classification
    dataset:
      name: lener_br
      type: lener_br
      config: lener_br
      split: train
    metrics:
    - type: accuracy
      value: 0.9990127507699392
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODEwMWUyNjU0ZjUyODQ2ZjQ3Y2VjOWY5YWNmZDczMDhhYzZiY2ZjMTFmZTUyZDZhOWJhMjcwMWJlZWNmMDIwOSIsInZlcnNpb24iOjF9.acwBn2no3TJ2cMGaGbQlNn9smS9XTsfKUat5JsKUVHTJa4H6okb5W6Va67KkrT383paAHOkoipb1wJwWfsseCg
    - type: precision
      value: 0.9992300721767728
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZmQyNDJhNTgzNjc4OWQ5ODcwN2RjM2JhZmNjODljZjIyYWI3MGIyOGNiYWYxNzczNDQyNTZjMDhiODYyYWRiMyIsInZlcnNpb24iOjF9.Z_W8fuCgV5KWChMZXaoJtX-u-SxBd8GcfVXBjFnf7BYqrWoTkcczJqJP1g74Gjrp6xp_VatQ-V1Por5Yzd3dCQ
    - type: recall
      value: 0.9993028952029684
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2ZiMjE4NDE0NmI1NjVhNzIyYjJjMTUyZDU2OGY3NTgyYTNhZDBjNWMzYWZmMmI5ZjczZjgyYmZjOGM0YTcyMiIsInZlcnNpb24iOjF9.jB5kEKsJMs40YVJ0RmFENEbKINKreAJN-EYeRrQMCwOrfTXxyxq0-cwgF_T2UJ1vl4eL-MAV2Lc3p449gaDUCg
    - type: f1
      value: 0.9992664823630992
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTQzMWRkZjIyNDY1NzU2NDNmNWJlMDIxOTY4Y2UyYjJlOTVkNTEwZGEwODdjZDMwYTg5ODE3NTlhN2JjMjZlZCIsInZlcnNpb24iOjF9.DspzVgqZh5jbRfx-89Ygh7dbbPBsiLyOostyQ4el1SIoGVRtEfxzYk780hEIRqqagWk63DXY3_eLIRyiBFf8BQ
    - type: loss
      value: 0.0035279043950140476
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMGQ1OWQxNjNmYzNlMzliODljNTY2YWNhMTUzNjVkMzA0NDYzZWY0ODFiMDlmZWZhNDlkODEyYWU5OWY3YjQyOSIsInZlcnNpb24iOjF9.6S7KwMDEBMWG95o3M0kOnKofgVnPwX8Sf2bQiXns-kZkcrOTXJCq7czloDbSk9d9-sumdxXYk9-oQFDfR6DTAw
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertimbau-base-lener_br

This model is a fine-tuned version of [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) on the lener_br dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2298
- Precision: 0.8501
- Recall: 0.9138
- F1: 0.8808
- Accuracy: 0.9693

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0686        | 1.0   | 1957  | 0.1399          | 0.7759    | 0.8669 | 0.8189 | 0.9641   |
| 0.0437        | 2.0   | 3914  | 0.1457          | 0.7997    | 0.8938 | 0.8441 | 0.9623   |
| 0.0313        | 3.0   | 5871  | 0.1675          | 0.8466    | 0.8744 | 0.8603 | 0.9651   |
| 0.0201        | 4.0   | 7828  | 0.1621          | 0.8713    | 0.8839 | 0.8775 | 0.9718   |
| 0.0137        | 5.0   | 9785  | 0.1811          | 0.7783    | 0.9159 | 0.8415 | 0.9645   |
| 0.0105        | 6.0   | 11742 | 0.1836          | 0.8568    | 0.9009 | 0.8783 | 0.9692   |
| 0.0105        | 7.0   | 13699 | 0.1649          | 0.8339    | 0.9125 | 0.8714 | 0.9725   |
| 0.0059        | 8.0   | 15656 | 0.2298          | 0.8501    | 0.9138 | 0.8808 | 0.9693   |
| 0.0051        | 9.0   | 17613 | 0.2210          | 0.8437    | 0.9045 | 0.8731 | 0.9693   |
| 0.0061        | 10.0  | 19570 | 0.2499          | 0.8627    | 0.8946 | 0.8784 | 0.9681   |
| 0.0041        | 11.0  | 21527 | 0.1985          | 0.8560    | 0.9052 | 0.8799 | 0.9720   |
| 0.003         | 12.0  | 23484 | 0.2204          | 0.8498    | 0.9065 | 0.8772 | 0.9699   |
| 0.0014        | 13.0  | 25441 | 0.2152          | 0.8425    | 0.9067 | 0.8734 | 0.9709   |
| 0.0005        | 14.0  | 27398 | 0.2317          | 0.8553    | 0.8987 | 0.8765 | 0.9705   |
| 0.0015        | 15.0  | 29355 | 0.2436          | 0.8543    | 0.8989 | 0.8760 | 0.9700   |


### Framework versions

- Transformers 4.8.2
- Pytorch 1.9.0+cu102
- Datasets 1.9.0
- Tokenizers 0.10.3

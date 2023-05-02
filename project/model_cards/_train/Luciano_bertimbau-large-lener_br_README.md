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
- name: bertimbau-large-lener_br
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
      value: 0.9801301293674859
model-index:
- name: Luciano/bertimbau-large-lener_br
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
      value: 0.9840898731012984
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTcwYjYxOGIzOGEwNjc4NzdkZjJjNGJhYTkzOTY4NmM5MWU0YjIxN2EwNmI4M2E0ZDkwYjUzYTk1NzYwOWYwNyIsInZlcnNpb24iOjF9.AZ4Xkl2_oUMeUxmB-Me7pdDwvQj6Y-6W2KvH6_5mkKuVnT551ffAtBbj8H9ruDvqE4aTlIT0eqrkgHUgcHP1Bg
    - type: precision
      value: 0.9895415357344292
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTBhMjRmNDZlMGRiZDJhNjg0ZWVhNzQzMzYzMTQ4MDY2ODEwNzcwYTgwYmEyZDExZmI0OWQ0N2Q5NzdjZDM2OCIsInZlcnNpb24iOjF9.50xubvWSuT0EDjsj-Ox0dFvsmsFQhCDojB15PzynBJBd2PsLOG2eKqWdFYV1iXNnOTum3xCFGKKSE8dvyK6GBQ
    - type: recall
      value: 0.9885856878370763
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTA4NzRkMzIwYzdhNmRlODg1YjI3MzA5NmQ5Yjk3NzMzZmQ4MDJjMWRlYzQ1NWNkZjA0MGQ2OTBiMWVlYjdiOCIsInZlcnNpb24iOjF9.5L9WHAEZIiM_rXqIu2kEVU-7Hed3oEi5IO_ulcEDJO-r4KQVXS9X4Rat5FSAjdWSRV_vnvM9Nc7LiOh738WzBA
    - type: f1
      value: 0.9890633808488363
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjIzYzllZWFjZmExN2Q2NDM4ZWY3YjMxZDNiZWFjNzU0ODcwYTBkNTU0ZWExYzM3YjI2MjQ4MTMxOTM5ODdhMyIsInZlcnNpb24iOjF9.tTxenqEcrfQMSbo53mewRPc4oDectJEKfzZyj_mChtQ-K41miMd1n_gNCT-zdT3u1wb5cc7nwgP-Mggo4Q6MAQ
    - type: loss
      value: 0.10151929408311844
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYmZkM2YzZmJmOGY0MDI0YzI0ZGQyYWM0YTU1YWQ3NDI3M2UxZjU3NjM0MzljODMwMTAyYzU4YWNmZTRhNGM3ZSIsInZlcnNpb24iOjF9.dF2SD2-HEHepUpbmgrndTM42MQ1mtMuuTgwqyv0cO_ZHlqRRQfyZtgLMlf8_5DwpPRKw_F3wwXLRETbL-5LJCw
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
      value: 0.9801301293674859
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYWY1M2Q5YzIxYzQ3NTU5YzQyMjUwNWY3MWNkMjJlMGM2YzkwMTdhZGM3NmYxZmVjZDc1N2NkMjBhNDEwMzIyOCIsInZlcnNpb24iOjF9.Mtp2ZBdksTfCQJEFiyLt4pILPH7RE8CXodYNcL8ydc7lTTwn5PiGdnglA7GJcd9HqxOU8UsVyaGzxFkjZGkGDw
    - type: precision
      value: 0.9864285473144053
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzc1M2NjNTFhNjZiNDU5NzQyZDYzOWViNGFhNzdlMGU4ODNhNDMxMWE1ZjIwZGIzOTIxNDAxZDcwNDM2MGNjYiIsInZlcnNpb24iOjF9.59674wBNKLrL5DC1vfPdEzpCiXRnhilpvnylmzkvLmBrJrZdy-rTP4AXir62BoUEyEZ6zMPRRNOYI9fduwfnBQ
    - type: recall
      value: 0.9845505854603656
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDc4YjVlYmQ1ZjllNzU3M2ZkN2QxNzI1MGZhMzhkMDNmMjNjODM3NGMzYzY2OGM1NGJmMDA4ZGUwM2RkMGY5MyIsInZlcnNpb24iOjF9.tYvf8mJ0XUmH3mZ0NIMdrXY5a93-2H9u5Ak6heCMBpmHhvgL8k_9y25cRmLeWoh9apsCIS6lQDpHlsJBXdhGDg
    - type: f1
      value: 0.9854886717201953
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMGY4YmJjYzkyNzU1ZDQ3MWFmZTY4MWU1OTg4NTRmOTIwM2I3NzdkYWI2YmNlYjdjODQyMmE2N2M5MDQ5MDEyYiIsInZlcnNpb24iOjF9.FxRrhWWfyA-oIXb5zzHO3-VboU6iFcnRc_kVPgLaOcyk8p5jIfV-egDHrql6e-h-6iS8xTDFV8fxIoq-kboRDQ
    - type: loss
      value: 0.11984097212553024
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZGE2NzM4MjE1MmU1ZTU4ZTU1NjAyYzk2YzdlNTUxOTAyZjdiMTkxYmZlMzExYmUwOTRhMTA3NzcwYWM2NzgxMiIsInZlcnNpb24iOjF9.PAlnc-tkJ7DEp9-qIR7KpYK9Yzy-umlhwKMH8bq1p-Gxf5pSIL_AtG8eP-JrbH71pJLYaBxSeeRHXWhIT-jBBA
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
      value: 0.9989004979420315
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTMwYWI4ZDdiZmNkYWYzNDNhZWI4MmNhNDE5MjRmMjRjYTZjYjI1YTllMzMyMDMxMTBmN2YwN2QxMmE3Y2ViYyIsInZlcnNpb24iOjF9.yihlFpU8AYKMsa4f_7P2J-JYifENGVm0nXGwKcvOV_axvv-Gj-Q-E93j0sHnb3TXTpTlJBgQ0ckBDh4Sohq3AQ
    - type: precision
      value: 0.9991129612205654
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzM3MTQ3ODU3MzBiY2RmNGVhMmQ2YTUzODlkZTk1M2EyOGU4Y2I5ZDI0ZGI5YWQ1YWQ4NDE2NGI1ZjYxNTM1YSIsInZlcnNpb24iOjF9.nnTSkmuvHdYFhXUofIEtjIaEveJCBlMrlmwSwRLojcXYvoaZWNFkWI8wSkQP0iDdDhKuEaZYkRc4kJ-Xd4_TCw
    - type: recall
      value: 0.9993219071519783
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTA1NGMzOGMwMWQ3Yzk0ZmY4YmYxZjVjODQwMDA1ZjgxNjQ2Y2IxMmIxYWJjOTJhOGQ2NjRlOTRjOTkzYjkwMyIsInZlcnNpb24iOjF9.2YuShB7RWqO6WeR9RCePUcDPv-Ho-6pYeFXmmnnYmW88BRN5jHSrJTWPXMxigVRPBHjU5LlE8j2EK3-IsNviCQ
    - type: f1
      value: 0.9992174232631231
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTE2YmMzMTI3MzQ5MTRmZGQ3NTdhODc3ZGI0MjIyOWMzZTc1MGQ4ZjVkY2JhYjYyM2I1NmI2MWI1OTZkYjViMyIsInZlcnNpb24iOjF9.TJkpCVwoTHFSwD8ckgn1dvD-H5HscuFmtsjEFYNVDZPnfm2PN7b45vZxNvWiK7L6ZVFW2fXbwgNJmMapuoeMCw
    - type: loss
      value: 0.0037613145541399717
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZmUxYWU2ODFkOTQ4NjIyODQ1NTU0NDQ2ZjhmYjExZmE3ZDNkZDBjNmIwY2JlNGRlNGZhOGExMDQ1MjA5Nzk0MiIsInZlcnNpb24iOjF9.ES0Kzjz3vvY5HedqYQzZafOPzQSbdWIbsdmft136SqIwb_-rZe-qQ38lveUYuUArP7NHk0wgo3NIkC6LqIsVAw
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertimbau-large-lener_br

This model is a fine-tuned version of [neuralmind/bert-large-portuguese-cased](https://huggingface.co/neuralmind/bert-large-portuguese-cased) on the lener_br dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1271
- Precision: 0.8965
- Recall: 0.9198
- F1: 0.9080
- Accuracy: 0.9801

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
| 0.0674        | 1.0   | 1957  | 0.1349          | 0.7617    | 0.8710 | 0.8127 | 0.9594   |
| 0.0443        | 2.0   | 3914  | 0.1867          | 0.6862    | 0.9194 | 0.7858 | 0.9575   |
| 0.0283        | 3.0   | 5871  | 0.1185          | 0.8206    | 0.8766 | 0.8477 | 0.9678   |
| 0.0226        | 4.0   | 7828  | 0.1405          | 0.8072    | 0.8978 | 0.8501 | 0.9708   |
| 0.0141        | 5.0   | 9785  | 0.1898          | 0.7224    | 0.9194 | 0.8090 | 0.9629   |
| 0.01          | 6.0   | 11742 | 0.1655          | 0.9062    | 0.8856 | 0.8958 | 0.9741   |
| 0.012         | 7.0   | 13699 | 0.1271          | 0.8965    | 0.9198 | 0.9080 | 0.9801   |
| 0.0091        | 8.0   | 15656 | 0.1919          | 0.8890    | 0.8886 | 0.8888 | 0.9719   |
| 0.0042        | 9.0   | 17613 | 0.1725          | 0.8977    | 0.8985 | 0.8981 | 0.9744   |
| 0.0043        | 10.0  | 19570 | 0.1530          | 0.8878    | 0.9034 | 0.8955 | 0.9761   |
| 0.0042        | 11.0  | 21527 | 0.1635          | 0.8792    | 0.9108 | 0.8947 | 0.9774   |
| 0.0033        | 12.0  | 23484 | 0.2009          | 0.8155    | 0.9138 | 0.8619 | 0.9719   |
| 0.0008        | 13.0  | 25441 | 0.1766          | 0.8737    | 0.9135 | 0.8932 | 0.9755   |
| 0.0005        | 14.0  | 27398 | 0.1868          | 0.8616    | 0.9129 | 0.8865 | 0.9743   |
| 0.0014        | 15.0  | 29355 | 0.1910          | 0.8694    | 0.9101 | 0.8893 | 0.9746   |


### Framework versions

- Transformers 4.8.2
- Pytorch 1.9.0+cu102
- Datasets 1.9.0
- Tokenizers 0.10.3

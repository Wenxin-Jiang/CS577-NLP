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
model-index:
- name: bertimbau-base-lener-br-finetuned-lener-br
  results:
  - task:
      type: token-classification
      name: Token Classification
    dataset:
      name: lener_br
      type: lener_br
      config: lener_br
      split: train
      args: lener_br
    metrics:
    - type: precision
      value: 0.8942967409948542
      name: Precision
    - type: recall
      value: 0.8969892473118279
      name: Recall
    - type: f1
      value: 0.8956409705819198
      name: F1
    - type: accuracy
      value: 0.9696009264479559
      name: Accuracy
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
      value: 0.981178408105048
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzNkNTFiM2M3NWNhMjFiZWI0YTg5YjA0NzdhMWZhNjFjNjNkNzU2Njc0YmUxNGJkODNkZjM1MGQ1OTA1MzZjZCIsInZlcnNpb24iOjF9.TFhSrPDOoDWDTWYdOwq2_xNpT-8qOz6sY_ssjyFtSe48yOMEYo4WsPSPye-k65_dC5fRoKkcDaNB5LI3MCpoAg
    - type: precision
      value: 0.98709417546121
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDk5ZDNmMGI1YzI1Y2E1MDgyZDc5ZTdmZTdjZDkwNDVhOTlhOWFkMGZkYzMxMzk4MzMxNDk0MzQ2YTI1ZmFmMCIsInZlcnNpb24iOjF9.neTDrpxoUh00ogYYaqMDWKyuJ5Vr4zvtDfe3qL6KaXQ4vwR01OogcRRU95_OPJ5SxeayuwOdwsFeB9VGneE1CQ
    - type: recall
      value: 0.9862996055703132
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNWQ3Y2JiZGFlN2RmNzY3ZjI4ZGYyYTVjMjBmOTQ2YjhiYTIxY2QxM2YyZDllNTc2ZDZhYjFjMTkzNzc5ZjFiZSIsInZlcnNpb24iOjF9.btGMRFJdxbcSeInckLfegVz7-3sBGPB2i70ASv6okG32yAnXEbiQ3MGEF0eyV4UXPvSrYeKac1pJWIViy0eyCQ
    - type: f1
      value: 0.986696730552424
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNmYyMjA0ZGM3MjcxMWJjMjUxMDlhODQ1OTE0OTY3ZGNkNTkwZjViMzg0ZTk5ODIxYmQ4MDRhNTRlNmNiZGMzNyIsInZlcnNpb24iOjF9.H9fYIIhKMM2-zOH_2M3YBtfTiTAze3HS3tqxHzJDB6jd5YGB3PMbn6h38KbbTQAVVJZI9jXKYnOZjV-0EjefBQ
    - type: loss
      value: 0.144147127866745
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNmM1ZDE5N2EyZGEyYzYzMmZjZDllZDhmYTgxNjIzODFhN2M2M2IyNWI3Y2IyMDdhOTkzZDA1MTE5NjkyODRlNiIsInZlcnNpb24iOjF9.L_Au7zxnzAtLRljLdlcFL1E-RWlmHty5W4YDMay9wH_PNZaI0X2MK5ifYP0871GHjAcmtk2M_Q-wIW7tHn0KAQ
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
      value: 0.9696009264479559
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjBhZGQxYzM3MjY2MDRmNWEyMzdiY2JlYTFjODVkZTg4YzVmYzEwY2ZlNjg1MWZmZjg4MjFkM2NkNjM5MjEzNyIsInZlcnNpb24iOjF9.NS7MqD-lX7_UE79cN4ehs6cpTwaOUUn5UUpojQtmy3jc1JzO1FbJg1yJJRWCHCKzjtfLNMj9SZMoAGclMXV_AQ
    - type: precision
      value: 0.974166236103935
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOWJkM2YzMjg3NjAwZTVmN2RjOTBiN2NjMjVmZjgzNzRlNTczOGM5NjQxM2UxMDEwZmFjOTUwOWNiYTRiZDBhNSIsInZlcnNpb24iOjF9.KYe08ccpe08hIRFRj5Pb36ikvbfN_jRfJd5Q90v1YQPLaqaisMhuN1601L6l0BSTT1lKzVbmso1HRUZsVwDACw
    - type: recall
      value: 0.9847359110437199
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMmYzY2VhODAwZTZlYTQzMmIxNDBkODgwYmIyYTM0YjJlOGE1ZGYwZDQ2Nzc1YjJkYjlhYmVmMjZiZTFhNDI5NSIsInZlcnNpb24iOjF9.ZLCjCyy5W7bHN2fsuxDgGrAPctgpuMJgRWPDXVMLxlZ8wHZisjOks4djo07CZMOu4mG1Eo3Lu-bFcA8-bj0fAQ
    - type: f1
      value: 0.9794225581044623
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzQ3ZTYzYTFjMmE5YTMwYzA5YTNkZTczNDA3MTI4ZGVkMGVhNWFjMTBjZjgzZjcwMDYxMzM4YWRhMTg2NmM1YiIsInZlcnNpb24iOjF9.xX25-TgY7x6kZxSt1ssxWNP9b6v3oUF8XtLWyzBQHxTXs60RoraAz9isRVkU4CgWKrY81cHhGoNY7G-C26xLAA
    - type: loss
      value: 0.26272761821746826
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzE4NmEzMjZlYmM1MzlkNzk5ZDE1M2IzYzNlNmM4YjgwNjRhZGVkZTFmNTBhZTVmOWEyZTVhNGM2MDljZjc2NSIsInZlcnNpb24iOjF9.xt17F4zNWnhlkLrjQv9tcl9ZeY68kr5UKCJhb8dDkwPIGS2u4ojyK8QtbKXO-_QY-X_oQZgdlbvQX4QYVVC4DQ
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertimbau-base-lener-br-finetuned-lener-br

This model is a fine-tuned version of [Luciano/bertimbau-base-finetuned-lener-br](https://huggingface.co/Luciano/bertimbau-base-finetuned-lener-br) on the lener_br dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Precision: 0.8943
- Recall: 0.8970
- F1: 0.8956
- Accuracy: 0.9696

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
| 0.0678        | 1.0   | 1957  | nan             | 0.8148    | 0.8882 | 0.8499 | 0.9689   |
| 0.0371        | 2.0   | 3914  | nan             | 0.8347    | 0.9022 | 0.8671 | 0.9671   |
| 0.0242        | 3.0   | 5871  | nan             | 0.8491    | 0.8905 | 0.8693 | 0.9716   |
| 0.0197        | 4.0   | 7828  | nan             | 0.9014    | 0.8772 | 0.8892 | 0.9780   |
| 0.0135        | 5.0   | 9785  | nan             | 0.8651    | 0.9060 | 0.8851 | 0.9765   |
| 0.013         | 6.0   | 11742 | nan             | 0.8882    | 0.9054 | 0.8967 | 0.9767   |
| 0.0084        | 7.0   | 13699 | nan             | 0.8559    | 0.9097 | 0.8820 | 0.9751   |
| 0.0069        | 8.0   | 15656 | nan             | 0.8916    | 0.8828 | 0.8872 | 0.9696   |
| 0.0047        | 9.0   | 17613 | nan             | 0.8964    | 0.8931 | 0.8948 | 0.9716   |
| 0.0028        | 10.0  | 19570 | nan             | 0.8864    | 0.9047 | 0.8955 | 0.9691   |
| 0.0023        | 11.0  | 21527 | nan             | 0.8860    | 0.9011 | 0.8935 | 0.9693   |
| 0.0009        | 12.0  | 23484 | nan             | 0.8952    | 0.8987 | 0.8970 | 0.9686   |
| 0.0014        | 13.0  | 25441 | nan             | 0.8929    | 0.8985 | 0.8957 | 0.9699   |
| 0.0025        | 14.0  | 27398 | nan             | 0.8914    | 0.8981 | 0.8947 | 0.9700   |
| 0.001         | 15.0  | 29355 | nan             | 0.8943    | 0.8970 | 0.8956 | 0.9696   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

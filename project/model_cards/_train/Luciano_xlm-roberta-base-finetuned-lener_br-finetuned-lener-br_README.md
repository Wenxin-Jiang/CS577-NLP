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
- name: xlm-roberta-base-finetuned-lener_br-finetuned-lener-br
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
      value: 0.9206349206349206
      name: Precision
    - type: recall
      value: 0.9294391315585423
      name: Recall
    - type: f1
      value: 0.925016077170418
      name: F1
    - type: accuracy
      value: 0.9832504071600401
      name: Accuracy
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
      value: 0.9832802904657313
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTk3YTgzYjU4MTQ4ZDU5ZDY1YjNlZTdjNzM1YTY1OGM0ZTcyNTc2NDA4MzFhYmY0NmQ2MDRiMWU3NTUwM2FlZSIsInZlcnNpb24iOjF9.yCQ8lJoSfokChcGn16603Md8wsFG83E_x8ijn1Fuy3dyFmtaHP8UXSzY1pGrWKUnTKeCcOp7W2MD51gP_WRQCA
    - type: precision
      value: 0.986258771429967
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTYyOTRhOTg2NWY0YTc4NjE1YjU2NGU3NmFlMmQyY2E5N2U2ZmU1YmMzYjZkYmEwYjY1YjcxYWQ3ZTVjMmZlYyIsInZlcnNpb24iOjF9.vP_avJP-puSp3lvxI2lbCsPXfH1lKGCLfrT4hshA_LVn8wjOUPrjgHH60NVM0fjXA35PB0aFnE9qCEvwyfzPBw
    - type: recall
      value: 0.9897717432152019
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODY1OWU0YzM5ZWE5YmYwOTQ5MGU1MTkzZjkxNDhkOTExZDBlNTI1ODUwMzFlOGUxYTQzZjMxMWNkODZhYWNlNCIsInZlcnNpb24iOjF9.QM6enyQUtL91odii7Iqa1Ya6Yc3S1hM-YYkPLqhqRn7chXPXhB58D7-3dLq_se2rRm7led_kwKBaVZhv7aJBDw
    - type: f1
      value: 0.9880121346555324
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOGEyOWQ5NTViNjZiNGFhNmQ3N2Y4ZWIxYmEwYTM4NjZhMGZkYjc3NWNiN2I5M2YwMjcyYzA3OTlmMWU5MDU1NiIsInZlcnNpb24iOjF9.5VArYd9p24-Wkhnn28wQzpBgKlXhF-fvIFJl6sZasr8FzLAp_yAE9kU8wPGhUc0UW9nsu7PBpH14xbhblsmuBg
    - type: loss
      value: 0.1050868034362793
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNWM0MTM2ODlkMjkxMTUyZDg4YmEyNTEzZjIyZWVkMmJhMGJjMmU1N2JmZDQ3Y2M2ZDZiNmYwZTI2ZjY2MDhmYSIsInZlcnNpb24iOjF9.JRkZwkuXovMIjiGlo38D3TPHImTTizTPf7iquVvoy4uWrdAwNympaMkqU78g9Fpky81-XWhCxK1pmrDhKQPTBg
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-lener_br-finetuned-lener-br

This model is a fine-tuned version of [Luciano/xlm-roberta-base-finetuned-lener_br](https://huggingface.co/Luciano/xlm-roberta-base-finetuned-lener_br) on the lener_br dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Precision: 0.9206
- Recall: 0.9294
- F1: 0.9250
- Accuracy: 0.9833

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0657        | 1.0   | 1957  | nan             | 0.7780    | 0.8687 | 0.8209 | 0.9718   |
| 0.0321        | 2.0   | 3914  | nan             | 0.8755    | 0.8708 | 0.8731 | 0.9793   |
| 0.0274        | 3.0   | 5871  | nan             | 0.8096    | 0.9124 | 0.8579 | 0.9735   |
| 0.0216        | 4.0   | 7828  | nan             | 0.7913    | 0.8842 | 0.8352 | 0.9718   |
| 0.0175        | 5.0   | 9785  | nan             | 0.7735    | 0.9248 | 0.8424 | 0.9721   |
| 0.0117        | 6.0   | 11742 | nan             | 0.9206    | 0.9294 | 0.9250 | 0.9833   |
| 0.0121        | 7.0   | 13699 | nan             | 0.8988    | 0.9318 | 0.9150 | 0.9819   |
| 0.0086        | 8.0   | 15656 | nan             | 0.8922    | 0.9175 | 0.9047 | 0.9801   |
| 0.007         | 9.0   | 17613 | nan             | 0.8482    | 0.8997 | 0.8732 | 0.9769   |
| 0.0051        | 10.0  | 19570 | nan             | 0.8730    | 0.9274 | 0.8994 | 0.9798   |
| 0.0045        | 11.0  | 21527 | nan             | 0.9172    | 0.9051 | 0.9111 | 0.9819   |
| 0.0014        | 12.0  | 23484 | nan             | 0.9138    | 0.9155 | 0.9147 | 0.9823   |
| 0.0029        | 13.0  | 25441 | nan             | 0.9099    | 0.9287 | 0.9192 | 0.9834   |
| 0.0035        | 14.0  | 27398 | nan             | 0.9019    | 0.9294 | 0.9155 | 0.9831   |
| 0.0005        | 15.0  | 29355 | nan             | 0.8886    | 0.9343 | 0.9109 | 0.9825   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1

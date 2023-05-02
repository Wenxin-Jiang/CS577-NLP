---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: roberta-large-finetuned-combined-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-finetuned-combined-DS

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2062
- Accuracy: 0.7001
- Precision: 0.6703
- Recall: 0.6700
- F1: 0.6701

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.8804        | 1.0   | 711   | 0.8517          | 0.6573   | 0.6786    | 0.6253 | 0.6231 |
| 0.6949        | 2.0   | 1422  | 0.7444          | 0.6833   | 0.6609    | 0.6647 | 0.6604 |
| 0.5674        | 3.0   | 2133  | 0.8379          | 0.6798   | 0.6571    | 0.6659 | 0.6575 |
| 0.433         | 3.99  | 2844  | 0.8703          | 0.7079   | 0.6947    | 0.6801 | 0.6809 |
| 0.3314        | 4.99  | 3555  | 1.1792          | 0.6861   | 0.6672    | 0.6558 | 0.6569 |
| 0.2519        | 5.99  | 4266  | 1.5574          | 0.6966   | 0.6761    | 0.6639 | 0.6662 |
| 0.2083        | 6.99  | 4977  | 1.8781          | 0.6952   | 0.6681    | 0.6592 | 0.6619 |
| 0.1773        | 7.99  | 5688  | 1.8687          | 0.6959   | 0.6677    | 0.6748 | 0.6675 |
| 0.1536        | 8.99  | 6399  | 2.2483          | 0.7037   | 0.6788    | 0.6674 | 0.6694 |
| 0.1305        | 9.99  | 7110  | 2.4602          | 0.6875   | 0.6597    | 0.6681 | 0.6612 |
| 0.0982        | 10.98 | 7821  | 2.5573          | 0.6994   | 0.6705    | 0.6728 | 0.6709 |
| 0.0858        | 11.98 | 8532  | 2.8048          | 0.6994   | 0.6765    | 0.6730 | 0.6737 |
| 0.0734        | 12.98 | 9243  | 3.0408          | 0.6945   | 0.6640    | 0.6628 | 0.6626 |
| 0.0625        | 13.98 | 9954  | 3.0047          | 0.7037   | 0.6784    | 0.6757 | 0.6764 |
| 0.0434        | 14.98 | 10665 | 3.0789          | 0.6987   | 0.6737    | 0.6669 | 0.6691 |
| 0.0432        | 15.98 | 11376 | 2.9647          | 0.6945   | 0.6649    | 0.6684 | 0.6663 |
| 0.0326        | 16.98 | 12087 | 3.3076          | 0.6931   | 0.6630    | 0.6563 | 0.6583 |
| 0.032         | 17.97 | 12798 | 3.1890          | 0.7022   | 0.6737    | 0.6702 | 0.6717 |
| 0.0275        | 18.97 | 13509 | 3.1798          | 0.7029   | 0.6738    | 0.6750 | 0.6744 |
| 0.0251        | 19.97 | 14220 | 3.2062          | 0.7001   | 0.6703    | 0.6700 | 0.6701 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1

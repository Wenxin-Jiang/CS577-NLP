---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: my_ner_model2_1_
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_ner_model2_1_

This model is a fine-tuned version of [dbmdz/bert-base-turkish-cased](https://huggingface.co/dbmdz/bert-base-turkish-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3810
- Precision: 0.6157
- Recall: 0.75
- F1: 0.6762
- Accuracy: 0.9298

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 72   | 0.2630          | 0.5114    | 0.6202 | 0.5606 | 0.9178   |
| No log        | 2.0   | 144  | 0.2351          | 0.56      | 0.6983 | 0.6216 | 0.9268   |
| No log        | 3.0   | 216  | 0.2496          | 0.5645    | 0.7338 | 0.6381 | 0.9243   |
| No log        | 4.0   | 288  | 0.2540          | 0.5769    | 0.7440 | 0.6499 | 0.9265   |
| No log        | 5.0   | 360  | 0.2559          | 0.6246    | 0.7398 | 0.6773 | 0.9289   |
| No log        | 6.0   | 432  | 0.2720          | 0.6137    | 0.7410 | 0.6714 | 0.9297   |
| 0.1489        | 7.0   | 504  | 0.2800          | 0.6305    | 0.7476 | 0.6841 | 0.9312   |
| 0.1489        | 8.0   | 576  | 0.3182          | 0.5866    | 0.7632 | 0.6634 | 0.9251   |
| 0.1489        | 9.0   | 648  | 0.3042          | 0.6127    | 0.75   | 0.6744 | 0.9285   |
| 0.1489        | 10.0  | 720  | 0.3182          | 0.6181    | 0.7518 | 0.6784 | 0.9293   |
| 0.1489        | 11.0  | 792  | 0.3347          | 0.6011    | 0.7506 | 0.6676 | 0.9278   |
| 0.1489        | 12.0  | 864  | 0.3572          | 0.6089    | 0.7596 | 0.6759 | 0.9281   |
| 0.1489        | 13.0  | 936  | 0.3516          | 0.6169    | 0.7548 | 0.6789 | 0.9297   |
| 0.0501        | 14.0  | 1008 | 0.3612          | 0.6175    | 0.7566 | 0.6800 | 0.9294   |
| 0.0501        | 15.0  | 1080 | 0.3683          | 0.6099    | 0.7488 | 0.6722 | 0.9289   |
| 0.0501        | 16.0  | 1152 | 0.3699          | 0.6265    | 0.75   | 0.6827 | 0.9306   |
| 0.0501        | 17.0  | 1224 | 0.3737          | 0.6210    | 0.7542 | 0.6811 | 0.9297   |
| 0.0501        | 18.0  | 1296 | 0.3754          | 0.6211    | 0.7476 | 0.6785 | 0.9291   |
| 0.0501        | 19.0  | 1368 | 0.3823          | 0.6132    | 0.7536 | 0.6762 | 0.9293   |
| 0.0501        | 20.0  | 1440 | 0.3810          | 0.6157    | 0.75   | 0.6762 | 0.9298   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu102
- Datasets 2.7.1
- Tokenizers 0.12.1

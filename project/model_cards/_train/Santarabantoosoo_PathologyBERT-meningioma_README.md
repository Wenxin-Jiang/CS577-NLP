---
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: PathologyBERT-meningioma
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PathologyBERT-meningioma

This model is a fine-tuned version of [tsantos/PathologyBERT](https://huggingface.co/tsantos/PathologyBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8123
- Accuracy: 0.8783
- Precision: 0.25
- Recall: 0.0833
- F1: 0.125

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 0
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.3723        | 1.0   | 71   | 0.5377          | 0.7652   | 0.0588    | 0.0833 | 0.0690 |
| 0.3363        | 2.0   | 142  | 0.4191          | 0.8783   | 0.25      | 0.0833 | 0.125  |
| 0.2773        | 3.0   | 213  | 0.4701          | 0.8870   | 0.3333    | 0.0833 | 0.1333 |
| 0.2303        | 4.0   | 284  | 0.5831          | 0.8957   | 0.5       | 0.0833 | 0.1429 |
| 0.1657        | 5.0   | 355  | 0.7083          | 0.8348   | 0.1111    | 0.0833 | 0.0952 |
| 0.1228        | 6.0   | 426  | 1.0324          | 0.8      | 0.0769    | 0.0833 | 0.08   |
| 0.0967        | 7.0   | 497  | 0.8103          | 0.8696   | 0.2       | 0.0833 | 0.1176 |
| 0.0729        | 8.0   | 568  | 0.8711          | 0.8696   | 0.2       | 0.0833 | 0.1176 |
| 0.0624        | 9.0   | 639  | 0.7968          | 0.8783   | 0.25      | 0.0833 | 0.125  |
| 0.0534        | 10.0  | 710  | 0.8123          | 0.8783   | 0.25      | 0.0833 | 0.125  |


### Framework versions

- Transformers 4.12.2
- Pytorch 1.10.1
- Datasets 1.15.0
- Tokenizers 0.10.3

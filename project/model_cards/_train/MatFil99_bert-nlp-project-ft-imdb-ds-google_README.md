---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-nlp-project-ft-imdb-ds-google
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-nlp-project-ft-imdb-ds-google

This model is a fine-tuned version of [jestemleon/bert-nlp-project-imdb](https://huggingface.co/jestemleon/bert-nlp-project-imdb) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3097
- Accuracy: 0.9124
- F1: 0.9197

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
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.3517        | 0.37  | 196  | 0.2556          | 0.9105   | 0.9187 |
| 0.27          | 0.75  | 392  | 0.2369          | 0.9038   | 0.9105 |
| 0.2246        | 1.12  | 588  | 0.2630          | 0.9133   | 0.9205 |
| 0.1869        | 1.49  | 784  | 0.2885          | 0.9038   | 0.9071 |
| 0.1696        | 1.86  | 980  | 0.2811          | 0.9152   | 0.9233 |
| 0.1474        | 2.24  | 1176 | 0.2918          | 0.9190   | 0.9243 |
| 0.1187        | 2.61  | 1372 | 0.3045          | 0.9133   | 0.9212 |
| 0.1077        | 2.98  | 1568 | 0.3097          | 0.9124   | 0.9197 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

---
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: AgitationTextV3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AgitationTextV3

This model is a fine-tuned version of [dmis-lab/biobert-base-cased-v1.1](https://huggingface.co/dmis-lab/biobert-base-cased-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5199
- Accuracy: 0.8
- Precision: 0.9636
- Recall: 0.7465
- F1: 0.8413

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.6797        | 1.0   | 50   | 0.6650          | 0.57     | 0.85      | 0.4789 | 0.6126 |
| 0.599         | 2.0   | 100  | 0.6180          | 0.65     | 0.86      | 0.6056 | 0.7107 |
| 0.5121        | 3.0   | 150  | 0.5714          | 0.75     | 0.8833    | 0.7465 | 0.8092 |
| 0.4049        | 4.0   | 200  | 0.5187          | 0.81     | 0.9194    | 0.8028 | 0.8571 |
| 0.3091        | 5.0   | 250  | 0.5034          | 0.77     | 0.9444    | 0.7183 | 0.816  |
| 0.2303        | 6.0   | 300  | 0.4673          | 0.78     | 0.9298    | 0.7465 | 0.8281 |
| 0.1773        | 7.0   | 350  | 0.4802          | 0.8      | 0.9322    | 0.7746 | 0.8462 |
| 0.1396        | 8.0   | 400  | 0.5260          | 0.8      | 0.9636    | 0.7465 | 0.8413 |
| 0.1204        | 9.0   | 450  | 0.5317          | 0.8      | 0.9636    | 0.7465 | 0.8413 |
| 0.0982        | 10.0  | 500  | 0.5199          | 0.8      | 0.9636    | 0.7465 | 0.8413 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

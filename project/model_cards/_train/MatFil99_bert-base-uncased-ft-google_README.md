---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-ft-google
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-ft-google

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the [steciuk/google](https://huggingface.co/datasets/steciuk/google) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3195
- Accuracy: 0.9105
- F1: 0.9174

and flowing results on the testing set:
- Accuracy: 0.9096
- F1: 0.9161

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
| 0.3651        | 0.37  | 196  | 0.2641          | 0.8962   | 0.9064 |
| 0.2765        | 0.75  | 392  | 0.2484          | 0.9019   | 0.9099 |
| 0.2349        | 1.12  | 588  | 0.2532          | 0.9133   | 0.9205 |
| 0.2015        | 1.49  | 784  | 0.2692          | 0.9095   | 0.9139 |
| 0.1817        | 1.86  | 980  | 0.2957          | 0.9095   | 0.9180 |
| 0.1683        | 2.24  | 1176 | 0.2941          | 0.9143   | 0.9213 |
| 0.1204        | 2.61  | 1372 | 0.3230          | 0.9143   | 0.9223 |
| 0.1271        | 2.98  | 1568 | 0.3195          | 0.9105   | 0.9174 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

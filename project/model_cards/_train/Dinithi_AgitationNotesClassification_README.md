---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: AgitationNotesClassification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AgitationNotesClassification

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4128
- F1: 0.8690

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

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.6567        | 1.0   | 50   | 0.6130          | 0.6500 |
| 0.6056        | 2.0   | 100  | 0.5807          | 0.6763 |
| 0.5172        | 3.0   | 150  | 0.5398          | 0.6675 |
| 0.4206        | 4.0   | 200  | 0.4111          | 0.8355 |
| 0.3361        | 5.0   | 250  | 0.3977          | 0.8667 |
| 0.2919        | 6.0   | 300  | 0.3874          | 0.8780 |
| 0.2233        | 7.0   | 350  | 0.3928          | 0.8690 |
| 0.1953        | 8.0   | 400  | 0.3908          | 0.8690 |
| 0.1633        | 9.0   | 450  | 0.4076          | 0.86   |
| 0.1494        | 10.0  | 500  | 0.4128          | 0.8690 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

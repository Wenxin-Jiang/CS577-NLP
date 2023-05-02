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
- name: clinical-finetuned-data10
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical-finetuned-data10

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5795
- Accuracy: 0.8
- Precision: 0.8507
- Recall: 0.8507
- F1: 0.8507

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
| 0.4903        | 1.0   | 50   | 0.5799          | 0.65     | 0.8810    | 0.5522 | 0.6789 |
| 0.4553        | 2.0   | 100  | 0.5528          | 0.71     | 0.8958    | 0.6418 | 0.7478 |
| 0.3538        | 3.0   | 150  | 0.5463          | 0.76     | 0.8644    | 0.7612 | 0.8095 |
| 0.2954        | 4.0   | 200  | 0.5511          | 0.78     | 0.8462    | 0.8209 | 0.8333 |
| 0.2644        | 5.0   | 250  | 0.5869          | 0.79     | 0.8485    | 0.8358 | 0.8421 |
| 0.2108        | 6.0   | 300  | 0.5418          | 0.79     | 0.8594    | 0.8209 | 0.8397 |
| 0.1881        | 7.0   | 350  | 0.5622          | 0.81     | 0.8636    | 0.8507 | 0.8571 |
| 0.1602        | 8.0   | 400  | 0.5796          | 0.8      | 0.8507    | 0.8507 | 0.8507 |
| 0.1617        | 9.0   | 450  | 0.5795          | 0.8      | 0.8507    | 0.8507 | 0.8507 |
| 0.1561        | 10.0  | 500  | 0.5795          | 0.8      | 0.8507    | 0.8507 | 0.8507 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

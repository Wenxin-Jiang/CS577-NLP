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
- name: clinicalAgitationTextClassificationModelV1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinicalAgitationTextClassificationModelV1

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7664
- Accuracy: 0.86
- Precision: 0.8986
- Recall: 0.8986
- F1: 0.8986

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
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.6593        | 1.0   | 50   | 0.5648          | 0.74     | 0.8525    | 0.7536 | 0.8    |
| 0.5082        | 2.0   | 100  | 0.4731          | 0.76     | 0.8814    | 0.7536 | 0.8125 |
| 0.3744        | 3.0   | 150  | 0.4516          | 0.84     | 0.8732    | 0.8986 | 0.8857 |
| 0.2618        | 4.0   | 200  | 0.5435          | 0.83     | 0.8514    | 0.9130 | 0.8811 |
| 0.2145        | 5.0   | 250  | 0.4750          | 0.85     | 0.95      | 0.8261 | 0.8837 |
| 0.1426        | 6.0   | 300  | 0.5433          | 0.86     | 0.8986    | 0.8986 | 0.8986 |
| 0.0971        | 7.0   | 350  | 0.5997          | 0.85     | 0.9355    | 0.8406 | 0.8855 |
| 0.0741        | 8.0   | 400  | 0.7534          | 0.86     | 0.8986    | 0.8986 | 0.8986 |
| 0.0513        | 9.0   | 450  | 0.8293          | 0.83     | 0.8611    | 0.8986 | 0.8794 |
| 0.0456        | 10.0  | 500  | 0.7664          | 0.86     | 0.8986    | 0.8986 | 0.8986 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

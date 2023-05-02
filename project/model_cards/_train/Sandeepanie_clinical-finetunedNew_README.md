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
- name: clinical-finetunedNew
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical-finetunedNew

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0423
- Accuracy: 0.84
- Precision: 0.8562
- Recall: 0.9191
- F1: 0.8865

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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.0707        | 1.0   | 50   | 0.9997          | 0.86     | 0.86      | 0.9485 | 0.9021 |
| 0.0593        | 2.0   | 100  | 0.9293          | 0.845    | 0.8777    | 0.8971 | 0.8873 |
| 0.0273        | 3.0   | 150  | 0.9836          | 0.83     | 0.8643    | 0.8897 | 0.8768 |
| 0.039         | 4.0   | 200  | 1.0028          | 0.85     | 0.8732    | 0.9118 | 0.8921 |
| 0.0121        | 5.0   | 250  | 1.0423          | 0.84     | 0.8562    | 0.9191 | 0.8865 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

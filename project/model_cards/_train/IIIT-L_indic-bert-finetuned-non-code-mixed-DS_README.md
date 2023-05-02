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
- name: indic-bert-finetuned-non-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indic-bert-finetuned-non-code-mixed-DS

This model is a fine-tuned version of [ai4bharat/indic-bert](https://huggingface.co/ai4bharat/indic-bert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9997
- Accuracy: 0.5620
- Precision: 0.5591
- Recall: 0.5203
- F1: 0.5078

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 32
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0673        | 3.99  | 926  | 1.0361          | 0.4142   | 0.4092    | 0.3851 | 0.2750 |
| 1.0144        | 7.98  | 1852 | 1.0147          | 0.5146   | 0.5851    | 0.4714 | 0.4184 |
| 0.9882        | 11.97 | 2778 | 1.0045          | 0.5599   | 0.5728    | 0.5191 | 0.5047 |
| 0.9699        | 15.97 | 3704 | 1.0004          | 0.5642   | 0.5620    | 0.5264 | 0.5193 |
| 0.9591        | 19.96 | 4630 | 0.9997          | 0.5620   | 0.5591    | 0.5203 | 0.5078 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1

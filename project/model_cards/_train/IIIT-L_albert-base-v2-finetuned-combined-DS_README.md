---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: albert-base-v2-finetuned-combined-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-v2-finetuned-combined-DS

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8777
- Accuracy: 0.6103
- Precision: 0.6156
- Recall: 0.5964
- F1: 0.5942

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.2531528713821575e-05
- train_batch_size: 8
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0726        | 0.5   | 711  | 1.0355          | 0.5028   | 0.3964    | 0.4551 | 0.3812 |
| 1.0367        | 1.0   | 1422 | 1.1449          | 0.3357   | 0.4627    | 0.3504 | 0.2166 |
| 1.0691        | 1.5   | 2133 | 1.0749          | 0.4993   | 0.4595    | 0.4282 | 0.3865 |
| 0.9844        | 2.0   | 2844 | 0.9458          | 0.5351   | 0.5383    | 0.5383 | 0.5249 |
| 0.9318        | 2.5   | 3555 | 0.9372          | 0.5569   | 0.5740    | 0.5596 | 0.5508 |
| 0.9313        | 3.0   | 4266 | 0.9221          | 0.5274   | 0.5772    | 0.5326 | 0.5222 |
| 0.8692        | 3.5   | 4977 | 0.9099          | 0.5611   | 0.5764    | 0.5585 | 0.5520 |
| 0.853         | 3.99  | 5688 | 0.8999          | 0.5990   | 0.6089    | 0.5840 | 0.5814 |
| 0.7954        | 4.49  | 6399 | 0.8821          | 0.6152   | 0.6177    | 0.6017 | 0.5988 |
| 0.8015        | 4.99  | 7110 | 0.8777          | 0.6103   | 0.6156    | 0.5964 | 0.5942 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

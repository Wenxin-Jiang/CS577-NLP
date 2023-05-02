---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-finetuned-10Epochs64Batch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-10Epochs64Batch

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6931
- Accuracy: 0.4993

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6962        | 1.0   | 569  | 0.6931          | 0.5094   |
| 0.6969        | 2.0   | 1138 | 0.6931          | 0.5062   |
| 0.6959        | 3.0   | 1707 | 0.6931          | 0.5106   |
| 0.6959        | 4.0   | 2276 | 0.6931          | 0.4975   |
| 0.6948        | 5.0   | 2845 | 0.6931          | 0.5109   |
| 0.6944        | 6.0   | 3414 | 0.6931          | 0.4948   |
| 0.695         | 7.0   | 3983 | 0.6931          | 0.5092   |
| 0.694         | 8.0   | 4552 | 0.6931          | 0.5054   |
| 0.6941        | 9.0   | 5121 | 0.6931          | 0.4998   |
| 0.6944        | 10.0  | 5690 | 0.6931          | 0.4993   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

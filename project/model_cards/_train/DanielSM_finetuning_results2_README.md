---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: finetuning_results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuning_results

This model is a fine-tuned version of [DanielSM/finetuning_results](https://huggingface.co/DanielSM/finetuning_results) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0000
- Accuracy: 1.0

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
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0555        | 1.0   | 50   | 0.0003          | 1.0      |
| 0.0064        | 2.0   | 100  | 0.0001          | 1.0      |
| 0.002         | 3.0   | 150  | 0.0000          | 1.0      |
| 0.0027        | 4.0   | 200  | 0.0000          | 1.0      |
| 0.0001        | 5.0   | 250  | 0.0000          | 1.0      |
| 0.0001        | 6.0   | 300  | 0.0000          | 1.0      |
| 0.0001        | 7.0   | 350  | 0.0000          | 1.0      |
| 0.0001        | 8.0   | 400  | 0.0000          | 1.0      |
| 0.0001        | 9.0   | 450  | 0.0000          | 1.0      |
| 0.0001        | 10.0  | 500  | 0.0000          | 1.0      |
| 0.0001        | 11.0  | 550  | 0.0000          | 1.0      |
| 0.0001        | 12.0  | 600  | 0.0000          | 1.0      |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

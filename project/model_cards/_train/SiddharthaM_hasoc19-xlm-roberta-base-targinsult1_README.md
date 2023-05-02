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
- name: hasoc19-xlm-roberta-base-targinsult1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hasoc19-xlm-roberta-base-targinsult1

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7512
- Accuracy: 0.7096
- Precision: 0.6720
- Recall: 0.6675
- F1: 0.6695

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 263  | 0.5619          | 0.6996   | 0.6660    | 0.6717 | 0.6684 |
| 0.5931        | 2.0   | 526  | 0.5350          | 0.7239   | 0.6880    | 0.6576 | 0.6655 |
| 0.5931        | 3.0   | 789  | 0.5438          | 0.7239   | 0.6872    | 0.6644 | 0.6714 |
| 0.5101        | 4.0   | 1052 | 0.5595          | 0.7196   | 0.6866    | 0.6909 | 0.6886 |
| 0.5101        | 5.0   | 1315 | 0.5580          | 0.7186   | 0.6818    | 0.6743 | 0.6774 |
| 0.4313        | 6.0   | 1578 | 0.6000          | 0.7039   | 0.6679    | 0.6692 | 0.6686 |
| 0.4313        | 7.0   | 1841 | 0.6429          | 0.7082   | 0.6765    | 0.6841 | 0.6794 |
| 0.3591        | 8.0   | 2104 | 0.6626          | 0.7115   | 0.6772    | 0.6803 | 0.6786 |
| 0.3591        | 9.0   | 2367 | 0.7231          | 0.7139   | 0.6764    | 0.6700 | 0.6727 |
| 0.3016        | 10.0  | 2630 | 0.7512          | 0.7096   | 0.6720    | 0.6675 | 0.6695 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1

---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: xlm-roberta-base-fa-aug-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-fa-aug-ner

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2714
- Precision: 0.5446
- Recall: 0.5882
- F1: 0.5655
- Accuracy: 0.9201

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.5864        | 1.0   | 784  | 0.3619          | 0.4741    | 0.4005 | 0.4342 | 0.8993   |
| 0.2659        | 2.0   | 1568 | 0.3057          | 0.5016    | 0.5178 | 0.5096 | 0.9093   |
| 0.2293        | 3.0   | 2352 | 0.2790          | 0.5380    | 0.5607 | 0.5491 | 0.9180   |
| 0.1945        | 4.0   | 3136 | 0.2715          | 0.5451    | 0.5672 | 0.5559 | 0.9191   |
| 0.1794        | 5.0   | 3920 | 0.2714          | 0.5446    | 0.5882 | 0.5655 | 0.9201   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

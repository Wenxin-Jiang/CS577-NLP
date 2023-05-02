---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: distilbert-base-uncased-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1137
- Accuracy: 0.9733
- F1: 0.9743

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

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.0868        | 1.0   | 1370 | 0.1098          | 0.9729   | 0.9738 |
| 0.0598        | 2.0   | 2740 | 0.1137          | 0.9733   | 0.9743 |
| 0.0383        | 3.0   | 4110 | 0.1604          | 0.9721   | 0.9731 |
| 0.0257        | 4.0   | 5480 | 0.1671          | 0.9717   | 0.9729 |
| 0.016         | 5.0   | 6850 | 0.1904          | 0.9709   | 0.9720 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0
- Datasets 2.5.1
- Tokenizers 0.10.3

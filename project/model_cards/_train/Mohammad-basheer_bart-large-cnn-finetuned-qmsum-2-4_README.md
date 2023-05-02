---
license: mit
tags:
- qmsum-summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-cnn-finetuned-qmsum-2-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-finetuned-qmsum-2-4

This model is a fine-tuned version of [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.0277
- Rouge1: 0.3053
- Rouge2: 0.0660
- Rougel: 0.1903
- Rougelsum: 0.2598

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 3.3773        | 1.0   | 629  | 3.2522          | 0.2964 | 0.0713 | 0.1958 | 0.2593    |
| 2.3656        | 2.0   | 1258 | 3.2001          | 0.2942 | 0.0694 | 0.1921 | 0.2540    |
| 1.5843        | 3.0   | 1887 | 3.4248          | 0.3086 | 0.0687 | 0.1938 | 0.2648    |
| 0.9854        | 4.0   | 2516 | 4.0277          | 0.3053 | 0.0660 | 0.1903 | 0.2598    |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

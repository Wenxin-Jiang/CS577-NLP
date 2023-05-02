---
license: mit
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-cnn-finetuned-random-sample-80
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-finetuned-random-sample-80

This model is a fine-tuned version of [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2424
- Rouge1: 0.3273
- Rouge2: 0.0961
- Rougel: 0.2088
- Rougelsum: 0.2886

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 3.3302        | 1.0   | 40   | 3.1922          | 0.2965 | 0.0789 | 0.1837 | 0.2565    |
| 1.9373        | 2.0   | 80   | 3.2424          | 0.3273 | 0.0961 | 0.2088 | 0.2886    |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

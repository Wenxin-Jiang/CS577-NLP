---
tags:
- generated_from_trainer
model-index:
- name: bert-base-cased-wikitext2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cased-wikitext2

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 6.9846

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 7.7422        | 1.0   | 782  | 7.1373          |
| 7.0302        | 2.0   | 1564 | 6.9972          |
| 6.9788        | 3.0   | 2346 | 7.0087          |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.12.0+cu102
- Datasets 1.14.0
- Tokenizers 0.10.3

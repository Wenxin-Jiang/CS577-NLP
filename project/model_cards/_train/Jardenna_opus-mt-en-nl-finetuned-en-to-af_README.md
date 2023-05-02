---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: opus-mt-en-nl-finetuned-en-to-af
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-en-nl-finetuned-en-to-af

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-nl](https://huggingface.co/Helsinki-NLP/opus-mt-en-nl) on the None dataset.

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
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu   | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:-------:|
| No log        | 1.0   | 241  | 4.1990          | 5.0127 | 21.973  |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

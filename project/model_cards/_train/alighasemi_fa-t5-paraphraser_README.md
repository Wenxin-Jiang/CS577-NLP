---
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: fa-t5-paraphraser
  results: []
datasets:
- alighasemi/fa-paraphrase
language:
- fa
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fa-t5-paraphraser

This model is a fine-tuned version of [alighasemi/fa-t5-base](https://huggingface.co/alighasemi/fa-t5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Bleu: 0.7025
- Gen Len: 5.8813

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu   | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:-------:|
| 0.0           | 1.0   | 55088 | nan             | 0.7025 | 5.8813  |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
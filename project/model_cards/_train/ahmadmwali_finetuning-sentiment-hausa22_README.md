---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: finetuning-sentiment-hausa22
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuning-sentiment-hausa22

This model is a fine-tuned version of [mbeukman/xlm-roberta-base-finetuned-hausa-finetuned-ner-swahili](https://huggingface.co/mbeukman/xlm-roberta-base-finetuned-hausa-finetuned-ner-swahili) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1854
- Accuracy: 0.9386
- F1: 0.9386

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results



### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

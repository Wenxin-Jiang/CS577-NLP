---
tags:
- generated_from_trainer
datasets:
- opus_books
model-index:
- name: mbart-large-50-finetuned-opus-en-pt-translation-finetuned-en-to-pt-dataset-opus-books
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart-large-50-finetuned-opus-en-pt-translation-finetuned-en-to-pt-dataset-opus-books

This model is a fine-tuned version of [Narrativa/mbart-large-50-finetuned-opus-en-pt-translation](https://huggingface.co/Narrativa/mbart-large-50-finetuned-opus-en-pt-translation) on the opus_books dataset.

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

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| No log        | 1.0   | 79   | 1.5854          | 31.2219 | 26.9149 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

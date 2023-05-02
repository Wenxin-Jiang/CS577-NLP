---
tags:
- summarization
- en
- ecnoder-decoder
- xlmroberta
- Abstractive Summarization
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: xlmroberta-finetune-en-cnn
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlmroberta-finetune-en-cnn

This model is a fine-tuned version of [](https://huggingface.co/) on the cnn_dailymail dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 5
- label_smoothing_factor: 0.1

### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.3.0
- Tokenizers 0.12.1

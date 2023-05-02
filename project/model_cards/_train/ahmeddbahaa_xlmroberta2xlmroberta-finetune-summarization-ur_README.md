---
tags:
- summarization
- ur
- encoder-decoder
- xlm-roberta
- Abstractive Summarization
- roberta
- generated_from_trainer
datasets:
- xlsum
model-index:
- name: xlmroberta2xlmroberta-finetune-summarization-ur
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlmroberta2xlmroberta-finetune-summarization-ur

This model is a fine-tuned version of [](https://huggingface.co/) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 5.4576
- Rouge-1: 26.51
- Rouge-2: 9.4
- Rouge-l: 23.21
- Gen Len: 19.99
- Bertscore: 68.15

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 48
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 5
- label_smoothing_factor: 0.1

### Training results



### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

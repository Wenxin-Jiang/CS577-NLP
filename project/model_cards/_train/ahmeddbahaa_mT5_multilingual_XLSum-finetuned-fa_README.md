---
tags:
- summarization
- fa
- mt5
- Abstractive Summarization
- generated_from_trainer
datasets:
- pn_summary
model-index:
- name: mT5_multilingual_XLSum-finetuned-fa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mT5_multilingual_XLSum-finetuned-fa

This model is a fine-tuned version of [csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum) on the pn_summary dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5703
- Rouge-1: 45.12
- Rouge-2: 26.25
- Rouge-l: 39.96
- Gen Len: 48.72
- Bertscore: 79.54

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 5
- label_smoothing_factor: 0.1

### Training results



### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

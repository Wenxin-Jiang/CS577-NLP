---
license: apache-2.0
tags:
- summarization
- t5
- ar
- abstractive summarization
- xlsum
- generated_from_trainer
datasets:
- xlsum
model-index:
- name: t5-arabic-base-finetuned-xlsum-ar
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-arabic-base-finetuned-xlsum-ar

This model is a fine-tuned version of [bakrianoo/t5-arabic-base](https://huggingface.co/bakrianoo/t5-arabic-base) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0328
- Rouge-1: 23.72
- Rouge-2: 10.95
- Rouge-l: 21.59
- Gen Len: 19.0
- Bertscore: 71.81

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
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 10
- label_smoothing_factor: 0.1

### Training results



### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

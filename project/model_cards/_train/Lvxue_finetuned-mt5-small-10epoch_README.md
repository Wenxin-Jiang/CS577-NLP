---
language:
- en
- ro
license: apache-2.0
tags:
- translation
- wmt16
- Lvxue
datasets:
- wmt16
metrics:
- sacrebleu
- bleu
model-index:
- name: Lvxue/finetuned-mt5-small-10epoch
  results:
  - task:
      type: translation
      name: Translation
    dataset:
      name: wmt16
      type: wmt16
      config: ro-en
      split: test
    metrics:
    - name: BLEU
      type: bleu
      value: 6.0012
      verified: true
    - name: loss
      type: loss
      value: 1.7407585382461548
      verified: true
    - name: gen_len
      type: gen_len
      value: 18.2281
      verified: true
---
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-mt5-small-10epoch

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the wmt16 ro-en dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7274

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
- train_batch_size: 48
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0

### Training results



### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1

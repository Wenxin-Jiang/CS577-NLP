---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- xlsum
metrics:
- rouge
model-index:
- name: mt5-small-finetuned-mt5-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: xlsum
      type: xlsum
      args: english
    metrics:
    - name: Rouge1
      type: rouge
      value: 23.8952
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetuned-mt5-en

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8345
- Rouge1: 23.8952
- Rouge2: 5.8792
- Rougel: 18.6495
- Rougelsum: 18.7057

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
- gradient_accumulation_steps: 10
- total_train_batch_size: 40
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| No log        | 1.0   | 224  | 3.0150          | 24.4639 | 5.3016 | 18.3987 | 18.4963   |
| No log        | 2.0   | 448  | 2.8738          | 24.5075 | 5.842  | 18.8133 | 18.9072   |
| No log        | 3.0   | 672  | 2.8345          | 23.8952 | 5.8792 | 18.6495 | 18.7057   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

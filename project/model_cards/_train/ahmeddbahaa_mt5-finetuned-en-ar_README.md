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
- name: mt5-finetuned-en-ar
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: xlsum
      type: xlsum
      args: arabic
    metrics:
    - name: Rouge1
      type: rouge
      value: 0.2824
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-finetuned-en-ar

This model is a fine-tuned version of [ahmeddbahaa/mt5-small-finetuned-mt5-en](https://huggingface.co/ahmeddbahaa/mt5-small-finetuned-mt5-en) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2314
- Rouge1: 0.2824
- Rouge2: 0.0
- Rougel: 0.2902
- Rougelsum: 0.298

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|
| 3.1685        | 1.0   | 4130  | 2.4262          | 0.0941 | 0.0235 | 0.1098 | 0.1098    |
| 2.686         | 2.0   | 8260  | 2.2853          | 0.2824 | 0.0    | 0.298  | 0.298     |
| 2.481         | 3.0   | 12390 | 2.2314          | 0.2824 | 0.0    | 0.2902 | 0.298     |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

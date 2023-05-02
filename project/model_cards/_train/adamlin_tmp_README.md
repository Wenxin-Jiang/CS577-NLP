---
language:
- zh_CN
- zh_CN
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- bleu
model_index:
- name: tmp
  results:
  - task:
      name: Translation
      type: translation
    metric:
      name: Bleu
      type: bleu
      value: 0.0099
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tmp

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unkown dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Bleu: 0.0099
- Gen Len: 3.3917

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
- train_batch_size: 1024
- eval_batch_size: 1024
- seed: 13
- gradient_accumulation_steps: 2
- total_train_batch_size: 2048
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu   | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:-------:|
| No log        | 1.0   | 1    | nan             | 0.0114 | 3.3338  |
| No log        | 2.0   | 2    | nan             | 0.0114 | 3.3338  |
| No log        | 3.0   | 3    | nan             | 0.0114 | 3.3338  |
| No log        | 4.0   | 4    | nan             | 0.0114 | 3.3338  |
| No log        | 5.0   | 5    | nan             | 0.0114 | 3.3338  |
| No log        | 6.0   | 6    | nan             | 0.0114 | 3.3338  |
| No log        | 7.0   | 7    | nan             | 0.0114 | 3.3338  |
| No log        | 8.0   | 8    | nan             | 0.0114 | 3.3338  |
| No log        | 9.0   | 9    | nan             | 0.0114 | 3.3338  |
| No log        | 10.0  | 10   | nan             | 0.0114 | 3.3338  |
| No log        | 11.0  | 11   | nan             | 0.0114 | 3.3338  |
| No log        | 12.0  | 12   | nan             | 0.0114 | 3.3338  |
| No log        | 13.0  | 13   | nan             | 0.0114 | 3.3338  |
| No log        | 14.0  | 14   | nan             | 0.0114 | 3.3338  |
| No log        | 15.0  | 15   | nan             | 0.0114 | 3.3338  |
| No log        | 16.0  | 16   | nan             | 0.0114 | 3.3338  |
| No log        | 17.0  | 17   | nan             | 0.0114 | 3.3338  |
| No log        | 18.0  | 18   | nan             | 0.0114 | 3.3338  |
| No log        | 19.0  | 19   | nan             | 0.0114 | 3.3338  |
| No log        | 20.0  | 20   | nan             | 0.0114 | 3.3338  |


### Framework versions

- Transformers 4.8.2
- Pytorch 1.8.1+cu111
- Datasets 1.9.0
- Tokenizers 0.10.3

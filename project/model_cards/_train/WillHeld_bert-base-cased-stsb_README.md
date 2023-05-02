---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- spearmanr
model-index:
- name: bert-base-cased-stsb
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE STSB
      type: glue
      args: stsb
    metrics:
    - name: Spearmanr
      type: spearmanr
      value: 0.8963451800582044
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cased-stsb

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the GLUE STSB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4322
- Pearson: 0.9007
- Spearmanr: 0.8963
- Combined Score: 0.8985

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Pearson | Spearmanr | Combined Score |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:---------:|:--------------:|
| 1.6464        | 1.39  | 500  | 0.5662          | 0.8820  | 0.8814    | 0.8817         |
| 0.3329        | 2.78  | 1000 | 0.5070          | 0.8913  | 0.8883    | 0.8898         |
| 0.173         | 4.17  | 1500 | 0.4465          | 0.8988  | 0.8943    | 0.8966         |
| 0.1085        | 5.56  | 2000 | 0.4537          | 0.8958  | 0.8917    | 0.8937         |
| 0.0816        | 6.94  | 2500 | 0.4594          | 0.8977  | 0.8933    | 0.8955         |
| 0.0621        | 8.33  | 3000 | 0.4450          | 0.8997  | 0.8950    | 0.8974         |
| 0.0519        | 9.72  | 3500 | 0.4322          | 0.9007  | 0.8963    | 0.8985         |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.7.1
- Datasets 1.18.3
- Tokenizers 0.11.6

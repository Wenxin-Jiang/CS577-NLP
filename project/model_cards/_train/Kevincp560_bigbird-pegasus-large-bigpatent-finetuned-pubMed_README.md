---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: bigbird-pegasus-large-bigpatent-finetuned-pubMed
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: pub_med_summarization_dataset
      type: pub_med_summarization_dataset
      args: document
    metrics:
    - name: Rouge1
      type: rouge
      value: 45.0851
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bigbird-pegasus-large-bigpatent-finetuned-pubMed

This model is a fine-tuned version of [google/bigbird-pegasus-large-bigpatent](https://huggingface.co/google/bigbird-pegasus-large-bigpatent) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5403
- Rouge1: 45.0851
- Rouge2: 19.5488
- Rougel: 27.391
- Rougelsum: 41.112
- Gen Len: 231.608

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.1198        | 1.0   | 500  | 1.6285          | 43.0579 | 18.1792 | 26.421  | 39.0769   | 214.924 |
| 1.6939        | 2.0   | 1000 | 1.5696          | 44.0679 | 18.9331 | 26.84   | 40.0684   | 222.814 |
| 1.6195        | 3.0   | 1500 | 1.5506          | 44.7352 | 19.3532 | 27.2418 | 40.7454   | 229.396 |
| 1.5798        | 4.0   | 2000 | 1.5403          | 45.0415 | 19.5019 | 27.2969 | 40.951    | 231.044 |
| 1.5592        | 5.0   | 2500 | 1.5403          | 45.0851 | 19.5488 | 27.391  | 41.112    | 231.608 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.9.1
- Datasets 1.18.4
- Tokenizers 0.11.6

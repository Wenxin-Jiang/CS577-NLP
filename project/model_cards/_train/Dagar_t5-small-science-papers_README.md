---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- scientific_papers
metrics:
- rouge
model-index:
- name: t5-small-science-papers
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: scientific_papers
      type: scientific_papers
      config: arxiv
      split: train
      args: arxiv
    metrics:
    - name: Rouge1
      type: rouge
      value: 12.3568
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-science-papers

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the scientific_papers dataset.
It achieves the following results on the evaluation set:
- Loss: 3.6405
- Rouge1: 12.3568
- Rouge2: 2.4449
- Rougel: 10.2371
- Rougelsum: 11.4209
- Gen Len: 19.0

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 4.4735        | 1.0   | 12690 | 4.3727          | 9.9604  | 1.7641 | 8.6213  | 9.2779    | 19.0    |
| 4.0104        | 2.0   | 25380 | 3.9384          | 11.4001 | 2.1474 | 9.6516  | 10.6602   | 19.0    |
| 3.8237        | 3.0   | 38070 | 3.7580          | 11.1806 | 2.1229 | 9.3881  | 10.3853   | 19.0    |
| 3.7382        | 4.0   | 50760 | 3.6738          | 11.9298 | 2.3222 | 9.9077  | 11.045    | 19.0    |
| 3.6994        | 5.0   | 63450 | 3.6405          | 12.3568 | 2.4449 | 10.2371 | 11.4209   | 19.0    |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1

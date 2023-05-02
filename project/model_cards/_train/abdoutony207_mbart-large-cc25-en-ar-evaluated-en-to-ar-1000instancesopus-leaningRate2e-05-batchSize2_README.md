---
license: mit
tags:
- generated_from_trainer
datasets:
- opus100
metrics:
- bleu
model-index:
- name: mbart-large-cc25-en-ar-evaluated-en-to-ar-1000instancesopus-leaningRate2e-05-batchSize2
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: opus100
      type: opus100
      args: ar-en
    metrics:
    - name: Bleu
      type: bleu
      value: 10.5645
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart-large-cc25-en-ar-evaluated-en-to-ar-1000instancesopus-leaningRate2e-05-batchSize2

This model is a fine-tuned version of [akhooli/mbart-large-cc25-en-ar](https://huggingface.co/akhooli/mbart-large-cc25-en-ar) on the opus100 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4673
- Bleu: 10.5645
- Meteor: 0.0783
- Gen Len: 10.23

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 11
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Meteor | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|
| 8.1731        | 0.25  | 100  | 2.8417          | 0.9599  | 0.028  | 230.885 |
| 0.6743        | 0.5   | 200  | 0.4726          | 6.4055  | 0.0692 | 14.81   |
| 0.3028        | 0.75  | 300  | 0.4572          | 6.7544  | 0.0822 | 23.92   |
| 0.2555        | 1.0   | 400  | 0.4172          | 8.4078  | 0.0742 | 13.655  |
| 0.1644        | 1.25  | 500  | 0.4236          | 9.284   | 0.071  | 13.03   |
| 0.1916        | 1.5   | 600  | 0.4222          | 4.8976  | 0.0779 | 32.225  |
| 0.2011        | 1.75  | 700  | 0.4305          | 7.6909  | 0.0738 | 16.675  |
| 0.1612        | 2.0   | 800  | 0.4416          | 10.8622 | 0.0855 | 10.91   |
| 0.116         | 2.25  | 900  | 0.4673          | 10.5645 | 0.0783 | 10.23   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

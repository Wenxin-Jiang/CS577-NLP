---
license: mit
tags:
- generated_from_trainer
datasets:
- opus100
metrics:
- bleu
model-index:
- name: m2m100_418M-evaluated-en-to-ar-2000instancesopus-leaningRate2e-05-batchSize16-20epoch-1
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
      value: 13.1835
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# m2m100_418M-evaluated-en-to-ar-2000instancesopus-leaningRate2e-05-batchSize16-20epoch-1

This model is a fine-tuned version of [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M) on the opus100 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3640
- Bleu: 13.1835
- Meteor: 0.1189
- Gen Len: 17.72

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
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Meteor | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|
| 6.1776        | 1.0   | 100  | 3.8904          | 10.5866 | 0.0995 | 16.64   |
| 2.4531        | 2.0   | 200  | 1.0928          | 12.3452 | 0.1108 | 17.0575 |
| 0.512         | 3.0   | 300  | 0.3625          | 10.5224 | 0.0982 | 17.2575 |
| 0.1924        | 4.0   | 400  | 0.3342          | 12.4242 | 0.1098 | 16.6325 |
| 0.1227        | 5.0   | 500  | 0.3403          | 13.0526 | 0.1185 | 17.3475 |
| 0.0889        | 6.0   | 600  | 0.3481          | 13.1323 | 0.1133 | 17.815  |
| 0.0651        | 7.0   | 700  | 0.3601          | 12.6684 | 0.1133 | 17.3525 |
| 0.0533        | 8.0   | 800  | 0.3640          | 13.1835 | 0.1189 | 17.72   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

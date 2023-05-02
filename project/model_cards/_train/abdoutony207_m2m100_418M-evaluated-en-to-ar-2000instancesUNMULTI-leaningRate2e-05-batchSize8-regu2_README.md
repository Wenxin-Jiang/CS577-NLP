---
license: mit
tags:
- generated_from_trainer
datasets:
- un_multi
metrics:
- bleu
model-index:
- name: m2m100_418M-evaluated-en-to-ar-2000instancesUNMULTI-leaningRate2e-05-batchSize8-regu2
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: un_multi
      type: un_multi
      args: ar-en
    metrics:
    - name: Bleu
      type: bleu
      value: 40.8245
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# m2m100_418M-evaluated-en-to-ar-2000instancesUNMULTI-leaningRate2e-05-batchSize8-regu2

This model is a fine-tuned version of [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M) on the un_multi dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3642
- Bleu: 40.8245
- Meteor: 0.4272
- Gen Len: 41.8075

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 11
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Meteor | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|
| 5.1584        | 0.5   | 100  | 3.2518          | 30.3723 | 0.3633 | 41.5    |
| 2.1351        | 1.0   | 200  | 0.9929          | 32.9915 | 0.3833 | 41.8225 |
| 0.568         | 1.5   | 300  | 0.4312          | 33.705  | 0.3896 | 42.6225 |
| 0.3749        | 2.0   | 400  | 0.3697          | 36.9316 | 0.4084 | 40.57   |
| 0.2376        | 2.5   | 500  | 0.3587          | 37.6782 | 0.4124 | 41.99   |
| 0.2435        | 3.0   | 600  | 0.3529          | 37.9931 | 0.4128 | 42.02   |
| 0.1706        | 3.5   | 700  | 0.3531          | 39.9972 | 0.4252 | 41.8025 |
| 0.165         | 4.0   | 800  | 0.3514          | 39.3155 | 0.42   | 41.0275 |
| 0.1273        | 4.5   | 900  | 0.3606          | 40.0765 | 0.4234 | 41.6175 |
| 0.1307        | 5.0   | 1000 | 0.3550          | 40.4468 | 0.428  | 41.72   |
| 0.0926        | 5.5   | 1100 | 0.3603          | 40.5454 | 0.4307 | 41.765  |
| 0.1096        | 6.0   | 1200 | 0.3613          | 40.5691 | 0.4298 | 42.31   |
| 0.0826        | 6.5   | 1300 | 0.3642          | 40.8245 | 0.4272 | 41.8075 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

---
license: mit
tags:
- generated_from_trainer
datasets:
- un_multi
metrics:
- bleu
model-index:
- name: m2m100_418M-evaluated-en-to-ar-2000instancesUNMULTI-leaningRate2e-05-batchSize8-regu1
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
      value: 41.8577
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# m2m100_418M-evaluated-en-to-ar-2000instancesUNMULTI-leaningRate2e-05-batchSize8-regu1

This model is a fine-tuned version of [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M) on the un_multi dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3603
- Bleu: 41.8577
- Meteor: 0.4199
- Gen Len: 41.9

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
| 5.111         | 0.5   | 100  | 3.2467          | 29.5017 | 0.3371 | 42.425  |
| 2.1491        | 1.0   | 200  | 1.0018          | 33.0563 | 0.3593 | 41.205  |
| 0.5911        | 1.5   | 300  | 0.4159          | 34.5818 | 0.3705 | 42.0625 |
| 0.3546        | 2.0   | 400  | 0.3723          | 36.6179 | 0.3823 | 40.925  |
| 0.2487        | 2.5   | 500  | 0.3595          | 39.0331 | 0.3956 | 41.56   |
| 0.2365        | 3.0   | 600  | 0.3485          | 39.5188 | 0.4023 | 41.6425 |
| 0.1687        | 3.5   | 700  | 0.3542          | 40.1728 | 0.4043 | 42.61   |
| 0.1791        | 4.0   | 800  | 0.3466          | 40.4858 | 0.4101 | 41.5575 |
| 0.1196        | 4.5   | 900  | 0.3493          | 41.2457 | 0.4123 | 41.755  |
| 0.1394        | 5.0   | 1000 | 0.3486          | 40.5606 | 0.4114 | 41.78   |
| 0.0958        | 5.5   | 1100 | 0.3568          | 41.1873 | 0.4157 | 41.7275 |
| 0.1043        | 6.0   | 1200 | 0.3557          | 41.2749 | 0.4165 | 41.935  |
| 0.073         | 6.5   | 1300 | 0.3603          | 41.8577 | 0.4199 | 41.9    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

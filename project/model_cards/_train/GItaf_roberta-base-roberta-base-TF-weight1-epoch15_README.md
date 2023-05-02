---
tags:
- generated_from_trainer
model-index:
- name: roberta-base-roberta-base-TF-weight1-epoch15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-roberta-base-TF-weight1-epoch15

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.8322
- Cls loss: 0.6900
- Lm loss: 4.1423
- Cls Accuracy: 0.5401
- Cls F1: 0.3788
- Cls Precision: 0.2917
- Cls Recall: 0.5401
- Perplexity: 62.95

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
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:-------:|:------------:|:------:|:-------------:|:----------:|:----------:|
| 5.3158        | 1.0   | 3470  | 4.9858          | 0.6910   | 4.2949  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 73.32      |
| 4.9772        | 2.0   | 6940  | 4.8876          | 0.6956   | 4.1920  | 0.4599       | 0.2898 | 0.2115        | 0.4599     | 66.15      |
| 4.8404        | 3.0   | 10410 | 4.8454          | 0.6901   | 4.1553  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 63.77      |
| 4.7439        | 4.0   | 13880 | 4.8177          | 0.6904   | 4.1274  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 62.02      |
| 4.6667        | 5.0   | 17350 | 4.8065          | 0.6903   | 4.1163  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 61.33      |
| 4.6018        | 6.0   | 20820 | 4.8081          | 0.6963   | 4.1119  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 61.06      |
| 4.5447        | 7.0   | 24290 | 4.8089          | 0.6912   | 4.1177  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 61.42      |
| 4.4944        | 8.0   | 27760 | 4.8128          | 0.6900   | 4.1228  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 61.73      |
| 4.4505        | 9.0   | 31230 | 4.8152          | 0.6905   | 4.1248  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 61.85      |
| 4.4116        | 10.0  | 34700 | 4.8129          | 0.6908   | 4.1221  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 61.69      |
| 4.3787        | 11.0  | 38170 | 4.8146          | 0.6906   | 4.1241  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 61.81      |
| 4.3494        | 12.0  | 41640 | 4.8229          | 0.6900   | 4.1329  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 62.36      |
| 4.3253        | 13.0  | 45110 | 4.8287          | 0.6900   | 4.1388  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 62.73      |
| 4.3075        | 14.0  | 48580 | 4.8247          | 0.6900   | 4.1347  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 62.47      |
| 4.2936        | 15.0  | 52050 | 4.8322          | 0.6900   | 4.1423  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 62.95      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
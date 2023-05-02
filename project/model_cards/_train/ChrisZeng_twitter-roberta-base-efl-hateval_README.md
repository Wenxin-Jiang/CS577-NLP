---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: twitter-roberta-base-efl-hateval
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-roberta-base-efl-hateval

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base-2021-124m](https://huggingface.co/cardiffnlp/twitter-roberta-base-2021-124m) on the HatEval dataset.
It achieves the following results on the evaluation set:
- Accuracy: 0.7913
- F1: 0.7899
- Loss: 0.3683

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Accuracy | F1     | Validation Loss |
|:-------------:|:-----:|:----:|:--------:|:------:|:---------------:|
| 0.5392        | 1.0   | 211  | 0.7      | 0.6999 | 0.4048          |
| 0.3725        | 2.0   | 422  | 0.759    | 0.7584 | 0.3489          |
| 0.3158        | 3.0   | 633  | 0.7613   | 0.7570 | 0.3287          |
| 0.289         | 4.0   | 844  | 0.769    | 0.7684 | 0.3307          |
| 0.2716        | 5.0   | 1055 | 0.7767   | 0.7750 | 0.3241          |
| 0.2575        | 6.0   | 1266 | 0.7787   | 0.7782 | 0.3272          |
| 0.2441        | 7.0   | 1477 | 0.7783   | 0.7776 | 0.3258          |
| 0.2363        | 8.0   | 1688 | 0.7777   | 0.7773 | 0.3316          |
| 0.2262        | 9.0   | 1899 | 0.7843   | 0.7815 | 0.3150          |
| 0.2191        | 10.0  | 2110 | 0.7813   | 0.7802 | 0.3241          |
| 0.2112        | 11.0  | 2321 | 0.7867   | 0.7860 | 0.3276          |
| 0.2047        | 12.0  | 2532 | 0.7897   | 0.7886 | 0.3266          |
| 0.1973        | 13.0  | 2743 | 0.7893   | 0.7884 | 0.3299          |
| 0.1897        | 14.0  | 2954 | 0.792    | 0.7907 | 0.3301          |
| 0.1862        | 15.0  | 3165 | 0.794    | 0.7925 | 0.3283          |
| 0.1802        | 16.0  | 3376 | 0.7907   | 0.7903 | 0.3465          |
| 0.1764        | 17.0  | 3587 | 0.7937   | 0.7922 | 0.3393          |
| 0.1693        | 18.0  | 3798 | 0.7903   | 0.7893 | 0.3494          |
| 0.1666        | 19.0  | 4009 | 0.7943   | 0.7930 | 0.3486          |
| 0.1631        | 20.0  | 4220 | 0.7927   | 0.7917 | 0.3516          |
| 0.1609        | 21.0  | 4431 | 0.7907   | 0.7893 | 0.3537          |
| 0.1581        | 22.0  | 4642 | 0.7913   | 0.7902 | 0.3586          |
| 0.1548        | 23.0  | 4853 | 0.789    | 0.7884 | 0.3698          |
| 0.1535        | 24.0  | 5064 | 0.7893   | 0.7880 | 0.3622          |
| 0.1522        | 25.0  | 5275 | 0.7923   | 0.7909 | 0.3625          |
| 0.15          | 26.0  | 5486 | 0.7913   | 0.7899 | 0.3632          |
| 0.1479        | 27.0  | 5697 | 0.792    | 0.7909 | 0.3677          |
| 0.1441        | 28.0  | 5908 | 0.792    | 0.7909 | 0.3715          |
| 0.145         | 29.0  | 6119 | 0.792    | 0.7906 | 0.3681          |
| 0.1432        | 30.0  | 6330 | 0.7913   | 0.7899 | 0.3683          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.0.0
- Tokenizers 0.11.6

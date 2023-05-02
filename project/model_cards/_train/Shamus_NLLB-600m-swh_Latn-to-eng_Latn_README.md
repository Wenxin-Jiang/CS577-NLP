---
license: cc-by-nc-4.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: NLLB-600m-swh_Latn-to-eng_Latn
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NLLB-600m-swh_Latn-to-eng_Latn

This model is a fine-tuned version of [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2490
- Bleu: 31.1907
- Gen Len: 34.464

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
- gradient_accumulation_steps: 7
- total_train_batch_size: 14
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 8000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| 2.8224        | 0.41  | 500  | 2.3121          | 8.4908  | 34.136  |
| 2.1656        | 0.83  | 1000 | 1.9451          | 14.9983 | 33.604  |
| 1.885         | 1.24  | 1500 | 1.7385          | 18.7049 | 33.928  |
| 1.6922        | 1.66  | 2000 | 1.6102          | 21.7399 | 33.648  |
| 1.5693        | 2.07  | 2500 | 1.5175          | 23.2299 | 34.912  |
| 1.4695        | 2.49  | 3000 | 1.4552          | 24.8572 | 32.612  |
| 1.4195        | 2.9   | 3500 | 1.3948          | 26.3956 | 33.56   |
| 1.3413        | 3.32  | 4000 | 1.3564          | 27.2599 | 32.824  |
| 1.3094        | 3.73  | 4500 | 1.3263          | 27.9728 | 33.42   |
| 1.2748        | 4.15  | 5000 | 1.3044          | 28.8956 | 33.56   |
| 1.227         | 4.56  | 5500 | 1.2844          | 29.8314 | 33.552  |
| 1.2255        | 4.97  | 6000 | 1.2692          | 30.4411 | 33.716  |
| 1.191         | 5.39  | 6500 | 1.2611          | 31.1336 | 34.432  |
| 1.1842        | 5.8   | 7000 | 1.2542          | 30.8819 | 33.716  |
| 1.1712        | 6.22  | 7500 | 1.2506          | 31.528  | 33.768  |
| 1.1606        | 6.63  | 8000 | 1.2490          | 31.1907 | 34.464  |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

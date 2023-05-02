---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- top_v2
model-index:
- name: t5-base-pointer-top_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-pointer-top_v2

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the top_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0256
- Exact Match: 0.8517

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 128
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 1.4545        | 0.82  | 200  | 0.2542          | 0.1294      |
| 0.1878        | 1.65  | 400  | 0.0668          | 0.2128      |
| 0.0796        | 2.47  | 600  | 0.0466          | 0.2276      |
| 0.0536        | 3.29  | 800  | 0.0356          | 0.2309      |
| 0.0424        | 4.12  | 1000 | 0.0317          | 0.2328      |
| 0.0356        | 4.94  | 1200 | 0.0295          | 0.2340      |
| 0.0306        | 5.76  | 1400 | 0.0288          | 0.2357      |
| 0.0277        | 6.58  | 1600 | 0.0271          | 0.2351      |
| 0.0243        | 7.41  | 1800 | 0.0272          | 0.2351      |
| 0.0225        | 8.23  | 2000 | 0.0272          | 0.2353      |
| 0.0206        | 9.05  | 2200 | 0.0267          | 0.2368      |
| 0.0187        | 9.88  | 2400 | 0.0260          | 0.2367      |
| 0.0173        | 10.7  | 2600 | 0.0256          | 0.2383      |
| 0.0161        | 11.52 | 2800 | 0.0260          | 0.2383      |
| 0.0153        | 12.35 | 3000 | 0.0257          | 0.2377      |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2

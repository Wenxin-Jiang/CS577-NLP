---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: sagemaker-bert-base-intent1018_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sagemaker-bert-base-intent1018_2

This model is a fine-tuned version of [asafaya/bert-base-arabic](https://huggingface.co/asafaya/bert-base-arabic) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5145
- Accuracy: 0.9017

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 88   | 4.0951          | 0.0470   |
| No log        | 2.0   | 176  | 3.7455          | 0.2158   |
| No log        | 3.0   | 264  | 3.0505          | 0.4252   |
| No log        | 4.0   | 352  | 2.0489          | 0.6303   |
| No log        | 5.0   | 440  | 1.3342          | 0.7735   |
| 2.9556        | 6.0   | 528  | 0.9592          | 0.8162   |
| 2.9556        | 7.0   | 616  | 0.7623          | 0.8162   |
| 2.9556        | 8.0   | 704  | 0.6262          | 0.8547   |
| 2.9556        | 9.0   | 792  | 0.5145          | 0.9017   |
| 2.9556        | 10.0  | 880  | 0.5328          | 0.8846   |
| 2.9556        | 11.0  | 968  | 0.5137          | 0.8932   |
| 0.3206        | 12.0  | 1056 | 0.5190          | 0.8846   |
| 0.3206        | 13.0  | 1144 | 0.5158          | 0.8953   |
| 0.3206        | 14.0  | 1232 | 0.5053          | 0.8974   |
| 0.3206        | 15.0  | 1320 | 0.5140          | 0.8953   |
| 0.3206        | 16.0  | 1408 | 0.5108          | 0.8996   |
| 0.3206        | 17.0  | 1496 | 0.5282          | 0.8932   |
| 0.0381        | 18.0  | 1584 | 0.5278          | 0.8974   |
| 0.0381        | 19.0  | 1672 | 0.5224          | 0.8996   |
| 0.0381        | 20.0  | 1760 | 0.5226          | 0.8996   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.9.1
- Datasets 1.15.1
- Tokenizers 0.10.3

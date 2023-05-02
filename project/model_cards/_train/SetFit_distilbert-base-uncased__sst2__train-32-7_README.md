---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-32-7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-32-7

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6736
- Accuracy: 0.5931

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7094        | 1.0   | 13   | 0.6887          | 0.5385   |
| 0.651         | 2.0   | 26   | 0.6682          | 0.6923   |
| 0.6084        | 3.0   | 39   | 0.6412          | 0.6923   |
| 0.4547        | 4.0   | 52   | 0.6095          | 0.6923   |
| 0.2903        | 5.0   | 65   | 0.6621          | 0.6923   |
| 0.1407        | 6.0   | 78   | 0.7130          | 0.7692   |
| 0.0444        | 7.0   | 91   | 0.9007          | 0.6923   |
| 0.0176        | 8.0   | 104  | 0.9525          | 0.7692   |
| 0.0098        | 9.0   | 117  | 1.0289          | 0.7692   |
| 0.0071        | 10.0  | 130  | 1.0876          | 0.7692   |
| 0.0052        | 11.0  | 143  | 1.1431          | 0.6923   |
| 0.0038        | 12.0  | 156  | 1.1687          | 0.7692   |
| 0.0034        | 13.0  | 169  | 1.1792          | 0.7692   |
| 0.0031        | 14.0  | 182  | 1.2033          | 0.7692   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

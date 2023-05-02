---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-32-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-32-6

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5072
- Accuracy: 0.7650

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
| 0.7057        | 1.0   | 13   | 0.6704          | 0.6923   |
| 0.6489        | 2.0   | 26   | 0.6228          | 0.8462   |
| 0.5475        | 3.0   | 39   | 0.5079          | 0.8462   |
| 0.4014        | 4.0   | 52   | 0.4203          | 0.8462   |
| 0.1923        | 5.0   | 65   | 0.3872          | 0.8462   |
| 0.1014        | 6.0   | 78   | 0.4909          | 0.8462   |
| 0.0349        | 7.0   | 91   | 0.5460          | 0.8462   |
| 0.0173        | 8.0   | 104  | 0.4867          | 0.8462   |
| 0.0098        | 9.0   | 117  | 0.5274          | 0.8462   |
| 0.0075        | 10.0  | 130  | 0.6086          | 0.8462   |
| 0.0057        | 11.0  | 143  | 0.6604          | 0.8462   |
| 0.0041        | 12.0  | 156  | 0.6904          | 0.8462   |
| 0.0037        | 13.0  | 169  | 0.7164          | 0.8462   |
| 0.0034        | 14.0  | 182  | 0.7368          | 0.8462   |
| 0.0031        | 15.0  | 195  | 0.7565          | 0.8462   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

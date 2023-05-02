---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- clinc_oos
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-distilled-clinc
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: clinc_oos
      type: clinc_oos
      args: plus
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9458064516129032
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-distilled-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2699
- Accuracy: 0.9458

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
- train_batch_size: 48
- eval_batch_size: 48
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 9

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 4.2203        | 1.0   | 318  | 3.1656          | 0.7532   |
| 2.4201        | 2.0   | 636  | 1.5891          | 0.8558   |
| 1.1961        | 3.0   | 954  | 0.8037          | 0.9152   |
| 0.5996        | 4.0   | 1272 | 0.4888          | 0.9326   |
| 0.3306        | 5.0   | 1590 | 0.3589          | 0.9439   |
| 0.2079        | 6.0   | 1908 | 0.3070          | 0.9439   |
| 0.1458        | 7.0   | 2226 | 0.2809          | 0.9458   |
| 0.1155        | 8.0   | 2544 | 0.2740          | 0.9461   |
| 0.1021        | 9.0   | 2862 | 0.2699          | 0.9458   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.13.0+cu116
- Datasets 1.16.1
- Tokenizers 0.10.3

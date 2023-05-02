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
      value: 0.9461290322580646
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-distilled-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2663
- Accuracy: 0.9461

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
| 4.1991        | 1.0   | 318  | 3.1495          | 0.7523   |
| 2.4112        | 2.0   | 636  | 1.5868          | 0.8510   |
| 1.1887        | 3.0   | 954  | 0.7975          | 0.9203   |
| 0.5952        | 4.0   | 1272 | 0.4870          | 0.9319   |
| 0.3275        | 5.0   | 1590 | 0.3571          | 0.9419   |
| 0.2066        | 6.0   | 1908 | 0.3070          | 0.9429   |
| 0.1456        | 7.0   | 2226 | 0.2809          | 0.9448   |
| 0.1154        | 8.0   | 2544 | 0.2697          | 0.9468   |
| 0.1011        | 9.0   | 2862 | 0.2663          | 0.9461   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0

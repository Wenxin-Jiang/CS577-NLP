---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- f1
- accuracy
model-index:
- name: glue_sst_classifier
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: sst2
    metrics:
    - name: F1
      type: f1
      value: 0.9033707865168539
    - name: Accuracy
      type: accuracy
      value: 0.9013761467889908
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# glue_sst_classifier

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2359
- F1: 0.9034
- Accuracy: 0.9014

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:--------:|
| 0.3653        | 0.19  | 100  | 0.3213          | 0.8717 | 0.8727   |
| 0.291         | 0.38  | 200  | 0.2662          | 0.8936 | 0.8911   |
| 0.2239        | 0.57  | 300  | 0.2417          | 0.9081 | 0.9060   |
| 0.2306        | 0.76  | 400  | 0.2359          | 0.9105 | 0.9094   |
| 0.2185        | 0.95  | 500  | 0.2371          | 0.9011 | 0.8991   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: albert-large-v2-finetuned-rte
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: rte
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.5487364620938628
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-large-v2-finetuned-rte

This model is a fine-tuned version of [albert-large-v2](https://huggingface.co/albert-large-v2) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6827
- Accuracy: 0.5487

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 18   | 0.6954          | 0.5271   |
| No log        | 2.0   | 36   | 0.6860          | 0.5379   |
| No log        | 3.0   | 54   | 0.6827          | 0.5487   |
| No log        | 4.0   | 72   | 0.7179          | 0.5235   |
| No log        | 5.0   | 90   | 0.7504          | 0.5379   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.1
- Tokenizers 0.10.3

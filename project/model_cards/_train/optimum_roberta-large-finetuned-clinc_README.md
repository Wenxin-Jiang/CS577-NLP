---
license: mit
tags:
- generated_from_trainer
datasets:
- clinc_oos
metrics:
- accuracy
model-index:
- name: roberta-large-finetuned-clinc
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
      value: 0.9729032258064516
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-finetuned-clinc

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1574
- Accuracy: 0.9729

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 239  | 0.8113          | 0.9035   |
| No log        | 2.0   | 478  | 0.2364          | 0.9548   |
| 1.7328        | 3.0   | 717  | 0.1760          | 0.9684   |
| 1.7328        | 4.0   | 956  | 0.1565          | 0.9723   |
| 0.0976        | 5.0   | 1195 | 0.1574          | 0.9729   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.11.0
- Datasets 1.16.1
- Tokenizers 0.10.3

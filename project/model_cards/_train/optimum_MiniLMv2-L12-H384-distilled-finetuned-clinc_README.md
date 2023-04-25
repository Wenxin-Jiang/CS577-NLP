---
tags:
- generated_from_trainer
datasets:
- clinc_oos
metrics:
- accuracy
model-index:
- name: MiniLMv2-L12-H384-distilled-from-RoBERTa-Large-distilled-clinc
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
      value: 0.94
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MiniLMv2-L12-H384-distilled-from-RoBERTa-Large-distilled-clinc

This model is a fine-tuned version of [nreimers/MiniLMv2-L12-H384-distilled-from-RoBERTa-Large](https://huggingface.co/nreimers/MiniLMv2-L12-H384-distilled-from-RoBERTa-Large) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3479
- Accuracy: 0.94

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 256
- eval_batch_size: 256
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 60   | 0.8171          | 0.2490   |
| No log        | 2.0   | 120  | 0.7039          | 0.6568   |
| No log        | 3.0   | 180  | 0.6067          | 0.7932   |
| 0.7269        | 4.0   | 240  | 0.5270          | 0.8674   |
| 0.7269        | 5.0   | 300  | 0.4659          | 0.9010   |
| 0.7269        | 6.0   | 360  | 0.4201          | 0.9194   |
| 0.7269        | 7.0   | 420  | 0.3867          | 0.9352   |
| 0.4426        | 8.0   | 480  | 0.3649          | 0.9352   |
| 0.4426        | 9.0   | 540  | 0.3520          | 0.9403   |
| 0.4426        | 10.0  | 600  | 0.3479          | 0.94     |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.11.0
- Datasets 1.16.1
- Tokenizers 0.10.3

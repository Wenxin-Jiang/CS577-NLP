---
tags:
- generated_from_trainer
datasets:
- clinc_oos
metrics:
- accuracy
model-index:
- name: MiniLMv2-L12-H384-distilled-from-RoBERTa-Large-finetuned-clinc
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
      value: 0.9319354838709677
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MiniLMv2-L12-H384-distilled-from-RoBERTa-Large-finetuned-clinc

This model is a fine-tuned version of [nreimers/MiniLMv2-L12-H384-distilled-from-RoBERTa-Large](https://huggingface.co/nreimers/MiniLMv2-L12-H384-distilled-from-RoBERTa-Large) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5252
- Accuracy: 0.9319

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
| No log        | 1.0   | 60   | 4.6555          | 0.1887   |
| No log        | 2.0   | 120  | 3.8771          | 0.4784   |
| No log        | 3.0   | 180  | 3.2507          | 0.7352   |
| 3.9668        | 4.0   | 240  | 2.7445          | 0.8365   |
| 3.9668        | 5.0   | 300  | 2.3475          | 0.8865   |
| 3.9668        | 6.0   | 360  | 2.0370          | 0.8926   |
| 3.9668        | 7.0   | 420  | 1.8099          | 0.9145   |
| 2.0924        | 8.0   | 480  | 1.6433          | 0.9190   |
| 2.0924        | 9.0   | 540  | 1.5563          | 0.9281   |
| 2.0924        | 10.0  | 600  | 1.5252          | 0.9319   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.11.0
- Datasets 1.16.1
- Tokenizers 0.10.3

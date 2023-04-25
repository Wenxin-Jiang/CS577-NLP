---
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: efl-finetuned-cola
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: cola
    metrics:
    - name: Matthews Correlation
      type: matthews_correlation
      value: 0.6097804486545971
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# efl-finetuned-cola

This model is a fine-tuned version of [nghuyong/ernie-2.0-en](https://huggingface.co/nghuyong/ernie-2.0-en) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4688
- Matthews Correlation: 0.6098

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| No log        | 1.0   | 134  | 0.4795          | 0.5403               |
| No log        | 2.0   | 268  | 0.4061          | 0.6082               |
| No log        | 3.0   | 402  | 0.4688          | 0.6098               |
| 0.2693        | 4.0   | 536  | 0.5332          | 0.6050               |
| 0.2693        | 5.0   | 670  | 0.6316          | 0.6098               |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.11.6

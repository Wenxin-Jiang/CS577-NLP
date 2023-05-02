---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: albert-base-v2-finetuned-ours-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-v2-finetuned-ours-DS

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8481
- Accuracy: 0.665
- Precision: 0.6202
- Recall: 0.6137
- F1: 0.5973

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.0031150633640573e-05
- train_batch_size: 8
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.053         | 0.49  | 99   | 1.0208          | 0.56     | 0.5650    | 0.4382 | 0.3908 |
| 0.8912        | 0.99  | 198  | 0.8648          | 0.59     | 0.3832    | 0.5279 | 0.4374 |
| 0.777         | 1.48  | 297  | 0.7986          | 0.665    | 0.6579    | 0.5985 | 0.5704 |
| 0.7391        | 1.98  | 396  | 0.8363          | 0.58     | 0.6389    | 0.5669 | 0.4966 |
| 0.5861        | 2.48  | 495  | 0.8394          | 0.685    | 0.6380    | 0.6313 | 0.6312 |
| 0.5711        | 2.97  | 594  | 0.9090          | 0.65     | 0.6102    | 0.5833 | 0.5900 |
| 0.4296        | 3.46  | 693  | 0.8481          | 0.665    | 0.6202    | 0.6137 | 0.5973 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

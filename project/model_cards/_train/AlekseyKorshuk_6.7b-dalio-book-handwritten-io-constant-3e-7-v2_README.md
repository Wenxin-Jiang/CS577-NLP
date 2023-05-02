---
license: other
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: 6.7b-dalio-book-handwritten-io-constant-3e-7-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 6.7b-dalio-book-handwritten-io-constant-3e-7-v2

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5293
- Accuracy: 0.2725

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-07
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 8
- total_eval_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.5856        | 0.08  | 6    | 2.5957          | 0.2697   |
| 2.6027        | 0.16  | 12   | 2.5938          | 0.2698   |
| 2.619         | 0.24  | 18   | 2.5879          | 0.2700   |
| 2.6121        | 0.32  | 24   | 2.5840          | 0.2702   |
| 2.6024        | 0.4   | 30   | 2.5762          | 0.2706   |
| 2.5878        | 0.48  | 36   | 2.5703          | 0.2707   |
| 2.5541        | 0.56  | 42   | 2.5625          | 0.2710   |
| 2.5207        | 0.64  | 48   | 2.5566          | 0.2713   |
| 2.4577        | 0.72  | 54   | 2.5488          | 0.2715   |
| 2.5614        | 0.8   | 60   | 2.5430          | 0.2718   |
| 2.6959        | 0.88  | 66   | 2.5352          | 0.2722   |
| 2.5084        | 0.96  | 72   | 2.5293          | 0.2725   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.12.1

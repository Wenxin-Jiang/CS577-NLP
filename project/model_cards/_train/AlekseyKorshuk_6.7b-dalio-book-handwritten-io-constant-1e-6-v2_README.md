---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2
metrics:
- accuracy
model-index:
- name: 6.7b-dalio-book-handwritten-io-constant-1e-6-v2
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2
      type: AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.27929113140380746
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 6.7b-dalio-book-handwritten-io-constant-1e-6-v2

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4238
- Accuracy: 0.2793

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
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
| 2.5852        | 0.08  | 6    | 2.5957          | 0.2697   |
| 2.5956        | 0.16  | 12   | 2.5762          | 0.2706   |
| 2.5961        | 0.24  | 18   | 2.5547          | 0.2711   |
| 2.5731        | 0.32  | 24   | 2.5312          | 0.2722   |
| 2.5415        | 0.4   | 30   | 2.5117          | 0.2734   |
| 2.5168        | 0.48  | 36   | 2.4961          | 0.2746   |
| 2.4972        | 0.56  | 42   | 2.4824          | 0.2756   |
| 2.4354        | 0.64  | 48   | 2.4727          | 0.2761   |
| 2.4055        | 0.72  | 54   | 2.4609          | 0.2768   |
| 2.4681        | 0.8   | 60   | 2.4492          | 0.2778   |
| 2.5866        | 0.88  | 66   | 2.4355          | 0.2784   |
| 2.4221        | 0.96  | 72   | 2.4238          | 0.2793   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/amazon-reviews-input-output
metrics:
- accuracy
model-index:
- name: amazon-reviews-input-output-13b
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/amazon-reviews-input-output
      type: AlekseyKorshuk/amazon-reviews-input-output
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.040426829268292684
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# amazon-reviews-input-output-13b

This model is a fine-tuned version of [facebook/opt-13b](https://huggingface.co/facebook/opt-13b) on the AlekseyKorshuk/amazon-reviews-input-output dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7168
- Accuracy: 0.0404
- Samples: 100
- Perplexity: 15.1318
- Table: <wandb.data_types.Table object at 0x7f8c9a3fb6d0>

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 8
- total_train_batch_size: 64
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 3.2134        | 0.96  | 15   | 2.7168          | 0.0404   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

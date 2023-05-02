---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/amazon-reviews-input-output
metrics:
- accuracy
model-index:
- name: amazon-reviews-input-output
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
      value: 0.037317073170731706
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# amazon-reviews-input-output

This model is a fine-tuned version of [facebook/opt-350m](https://huggingface.co/facebook/opt-350m) on the AlekseyKorshuk/amazon-reviews-input-output dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0486
- Accuracy: 0.0373
- Samples: 100
- Perplexity: 21.0867
- Table: <wandb.data_types.Table object at 0x7fa288d36880>

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
- train_batch_size: 4
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 3.2766        | 0.8   | 25   | 3.0587          | 0.0372   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

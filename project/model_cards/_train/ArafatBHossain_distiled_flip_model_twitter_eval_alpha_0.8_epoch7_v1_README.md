---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distiled_flip_model_twitter_eval_alpha_0.8_epoch7_v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distiled_flip_model_twitter_eval_alpha_0.8_epoch7_v1

This model is a fine-tuned version of [ArafatBHossain/distilbert-base-uncased_fine_tuned_sent140](https://huggingface.co/ArafatBHossain/distilbert-base-uncased_fine_tuned_sent140) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9772
- Accuracy: 0.7406

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.9422        | 1.0   | 408  | 0.9818          | 0.7193   |
| 0.8752        | 2.0   | 816  | 0.9302          | 0.7299   |
| 0.8253        | 3.0   | 1224 | 0.9979          | 0.7433   |
| 0.8392        | 4.0   | 1632 | 0.9786          | 0.7433   |
| 0.8036        | 5.0   | 2040 | 0.9793          | 0.7380   |
| 0.7921        | 6.0   | 2448 | 1.0107          | 0.7487   |
| 0.8221        | 7.0   | 2856 | 0.9772          | 0.7406   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.11.0
- Datasets 2.6.1
- Tokenizers 0.12.1

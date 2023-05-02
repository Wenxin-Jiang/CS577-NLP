---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: cont_medium_4_256
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# cont_medium_4_256

This model is a fine-tuned version of [sberbank-ai/rugpt3medium_based_on_gpt2](https://huggingface.co/sberbank-ai/rugpt3medium_based_on_gpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.7602
- Accuracy: 0.3436

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.5e-05
- train_batch_size: 6
- eval_batch_size: 12
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 3.4091        | 1.0   | 160  | 3.7238          | 0.3472   |
| 3.2338        | 2.0   | 320  | 3.7393          | 0.3446   |
| 3.1684        | 3.0   | 480  | 3.7518          | 0.3444   |
| 3.0989        | 4.0   | 640  | 3.7602          | 0.3436   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.8.1+cu111
- Datasets 2.5.2
- Tokenizers 0.13.1

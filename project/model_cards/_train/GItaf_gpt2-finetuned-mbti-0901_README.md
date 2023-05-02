---
license: mit
tags:
- generated_from_trainer
model-index:
- name: gpt2-finetuned-mbti-0901
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-finetuned-mbti-0901

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.9470

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 4.1073        | 1.0   | 9906  | 4.0111          |
| 4.0302        | 2.0   | 19812 | 3.9761          |
| 3.9757        | 3.0   | 29718 | 3.9578          |
| 3.9471        | 4.0   | 39624 | 3.9495          |
| 3.9187        | 5.0   | 49530 | 3.9470          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1

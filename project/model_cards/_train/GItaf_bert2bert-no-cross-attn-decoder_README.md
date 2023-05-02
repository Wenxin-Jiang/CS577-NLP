---
tags:
- generated_from_trainer
- text-generation
widget:
  parameters:
  - max_new_tokens = 100
model-index:
- name: bert-base-uncased-bert-base-uncased-finetuned-mbti-0909
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-bert-base-uncased-finetuned-mbti-0909

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 6.0549

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 5.2244        | 1.0   | 1735 | 5.7788          |
| 4.8483        | 2.0   | 3470 | 5.7647          |
| 4.7578        | 3.0   | 5205 | 5.9016          |
| 4.5606        | 4.0   | 6940 | 5.9895          |
| 4.4314        | 5.0   | 8675 | 6.0549          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1

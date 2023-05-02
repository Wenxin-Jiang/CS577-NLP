---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- superb
metrics:
- accuracy
model-index:
- name: wav2vec2-base-ks
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-ks

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0982
- Accuracy: 0.9825

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Accuracy | Validation Loss |
|:-------------:|:-----:|:----:|:--------:|:---------------:|
| 0.8465        | 1.0   | 399  | 0.8179   | 0.7516          |
| 0.2962        | 2.0   | 798  | 0.9771   | 0.2077          |
| 0.1891        | 3.0   | 1197 | 0.9819   | 0.1195          |
| 0.19          | 4.0   | 1596 | 0.9825   | 0.0982          |
| 0.1685        | 5.0   | 1995 | 0.9825   | 0.0952          |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.14.0
- Tokenizers 0.10.3

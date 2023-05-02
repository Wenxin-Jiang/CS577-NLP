---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- minds14
metrics:
- accuracy
model-index:
- name: wav2vec2-base-finetuned-ks
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-finetuned-ks

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the minds14 dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6374
- Accuracy: 0.0619

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 0.8   | 3    | 2.6374          | 0.0619   |
| No log        | 1.8   | 6    | 2.6433          | 0.0619   |
| No log        | 2.8   | 9    | 2.6508          | 0.0531   |
| 3.2258        | 3.8   | 12   | 2.6540          | 0.0531   |
| 3.2258        | 4.8   | 15   | 2.6592          | 0.0442   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.0
- Tokenizers 0.13.1

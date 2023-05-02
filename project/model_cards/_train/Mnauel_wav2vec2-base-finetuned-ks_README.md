---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-base-finetuned-ks
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-finetuned-ks

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5766
- Accuracy: 0.8308

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 7    | 0.7247          | 0.7462   |
| No log        | 2.0   | 14   | 0.6844          | 0.7615   |
| 0.4279        | 3.0   | 21   | 0.7254          | 0.7462   |
| 0.4279        | 4.0   | 28   | 0.5891          | 0.8      |
| 0.4279        | 5.0   | 35   | 0.6991          | 0.7462   |
| 0.4478        | 6.0   | 42   | 0.6579          | 0.7615   |
| 0.4478        | 7.0   | 49   | 0.6164          | 0.8      |
| 0.4478        | 8.0   | 56   | 0.6191          | 0.8077   |
| 0.4194        | 9.0   | 63   | 0.5766          | 0.8308   |
| 0.4194        | 10.0  | 70   | 0.5704          | 0.8154   |
| 0.4194        | 11.0  | 77   | 0.6518          | 0.8      |
| 0.3833        | 12.0  | 84   | 0.6190          | 0.8077   |
| 0.3833        | 13.0  | 91   | 0.5693          | 0.8231   |
| 0.3833        | 14.0  | 98   | 0.5628          | 0.8231   |
| 0.3607        | 15.0  | 105  | 0.5741          | 0.8154   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.10.3

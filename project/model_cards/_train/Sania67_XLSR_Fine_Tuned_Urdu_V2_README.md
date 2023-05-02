---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_8_0
model-index:
- name: XLSR_Fine_Tuned_Urdu_V2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# XLSR_Fine_Tuned_Urdu_V2

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the common_voice_8_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8023
- Wer: 0.4382

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 6.424         | 3.25  | 1000 | 2.9777          | 1.0    |
| 1.4315        | 6.49  | 2000 | 0.8493          | 0.5896 |
| 0.6938        | 9.74  | 3000 | 0.7438          | 0.4978 |
| 0.5129        | 12.99 | 4000 | 0.7480          | 0.4785 |
| 0.4133        | 16.23 | 5000 | 0.7568          | 0.4600 |
| 0.3496        | 19.48 | 6000 | 0.7387          | 0.4471 |
| 0.3133        | 22.73 | 7000 | 0.7655          | 0.4426 |
| 0.2767        | 25.97 | 8000 | 0.8081          | 0.4530 |
| 0.2581        | 29.22 | 9000 | 0.8023          | 0.4382 |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_8_0
model-index:
- name: XLSR_Fine_Tuned_URDU
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# XLSR_Fine_Tuned_URDU

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the common_voice_8_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8115
- Wer: 0.4815

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
| 6.7221        | 3.25  | 1000 | 3.0131          | 0.9985 |
| 1.6219        | 6.49  | 2000 | 0.9179          | 0.6336 |
| 0.7747        | 9.74  | 3000 | 0.7975          | 0.5804 |
| 0.5796        | 12.99 | 4000 | 0.7820          | 0.5524 |
| 0.4672        | 16.23 | 5000 | 0.8220          | 0.5317 |
| 0.4002        | 19.48 | 6000 | 0.8080          | 0.5107 |
| 0.3587        | 22.73 | 7000 | 0.7889          | 0.4926 |
| 0.3192        | 25.97 | 8000 | 0.8137          | 0.4875 |
| 0.3           | 29.22 | 9000 | 0.8115          | 0.4815 |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xlsr-53-demo-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-53-demo-colab

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6901
- Wer: 1.6299

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 8.5034        | 3.42  | 400  | 3.5852          | 1.0    |
| 1.7853        | 6.83  | 800  | 0.7430          | 1.6774 |
| 0.5675        | 10.26 | 1200 | 0.6513          | 1.6330 |
| 0.3761        | 13.67 | 1600 | 0.6208          | 1.6081 |
| 0.2776        | 17.09 | 2000 | 0.6401          | 1.6081 |
| 0.2266        | 20.51 | 2400 | 0.6410          | 1.6295 |
| 0.1949        | 23.93 | 2800 | 0.6910          | 1.6287 |
| 0.1672        | 27.35 | 3200 | 0.6901          | 1.6299 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.14.0
- Tokenizers 0.10.3

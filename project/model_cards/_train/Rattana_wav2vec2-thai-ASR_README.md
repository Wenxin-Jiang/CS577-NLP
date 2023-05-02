---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-thai-ASR
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-thai-ASR

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6108
- Wer: 0.5636

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
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 7.1123        | 2.65  | 400  | 3.3946          | 1.0002 |
| 1.5734        | 5.3   | 800  | 0.6881          | 0.7290 |
| 0.5934        | 7.94  | 1200 | 0.5789          | 0.6402 |
| 0.4059        | 10.59 | 1600 | 0.5496          | 0.5976 |
| 0.3136        | 13.24 | 2000 | 0.6109          | 0.5863 |
| 0.2546        | 15.89 | 2400 | 0.6113          | 0.5865 |
| 0.2184        | 18.54 | 2800 | 0.6108          | 0.5636 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0

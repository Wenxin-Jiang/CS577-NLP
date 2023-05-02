---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-colab

This model is a fine-tuned version of [facebook/wav2vec2-xlsr-53-espeak-cv-ft](https://huggingface.co/facebook/wav2vec2-xlsr-53-espeak-cv-ft) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: inf
- Wer: 0.9155

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 24
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 48
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.7628        | 7.83  | 400  | inf             | 0.9155 |
| 1.0544        | 15.68 | 800  | inf             | 0.9155 |
| 7.5478        | 23.52 | 1200 | inf             | 0.9155 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.10.0+cu113
- Datasets 2.8.0
- Tokenizers 0.13.2

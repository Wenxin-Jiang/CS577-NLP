---
tags:
- generated_from_trainer
datasets:
- uob_singlish
model-index:
- name: Malaya-speech_fine-tune_MrBrown_20_Jun
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Malaya-speech_fine-tune_MrBrown_20_Jun

This model is a fine-tuned version of [malay-huggingface/wav2vec2-xls-r-300m-mixed](https://huggingface.co/malay-huggingface/wav2vec2-xls-r-300m-mixed) on the uob_singlish dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8868
- Wer: 0.3244

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.8027        | 3.85  | 200  | 0.4800          | 0.2852 |
| 0.3773        | 7.69  | 400  | 0.6292          | 0.3316 |
| 0.3394        | 11.54 | 600  | 0.7376          | 0.3494 |
| 0.2653        | 15.38 | 800  | 0.9595          | 0.3137 |
| 0.1785        | 19.23 | 1000 | 0.7381          | 0.3440 |
| 0.1669        | 23.08 | 1200 | 0.9534          | 0.3529 |
| 0.0971        | 26.92 | 1400 | 0.8868          | 0.3244 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

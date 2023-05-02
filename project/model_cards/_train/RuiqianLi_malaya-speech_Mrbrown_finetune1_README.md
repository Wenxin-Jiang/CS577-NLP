---
tags:
- generated_from_trainer
datasets:
- uob_singlish
model-index:
- name: malaya-speech_Mrbrown_finetune1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# malaya-speech_Mrbrown_finetune1

This model is a fine-tuned version of [malay-huggingface/wav2vec2-xls-r-300m-mixed](https://huggingface.co/malay-huggingface/wav2vec2-xls-r-300m-mixed) on the uob_singlish dataset.

## This time use self-made dataset(cut the audio of "https://www.youtube.com/watch?v=a2ZOTD3R7JI" into slices and write the corresponding transcript, totally 4 mins), get really bad fine-tuning result, that may mean the training/fine-tuning dataset must be high quality/at least several hours? Or maybe is because the learning rate is set too high(0.01) ? Still searching for the important factors.

It achieves the following results on the evaluation set:
- Loss: 3.8458
- Wer: 1.01

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.01
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer  |
|:-------------:|:-----:|:----:|:---------------:|:----:|
| 0.3186        | 20.0  | 200  | 4.2225          | 1.13 |
| 0.4911        | 40.0  | 400  | 4.0427          | 0.99 |
| 0.9014        | 60.0  | 600  | 5.3285          | 1.04 |
| 1.0955        | 80.0  | 800  | 3.6922          | 1.02 |
| 0.7533        | 100.0 | 1000 | 3.8458          | 1.01 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

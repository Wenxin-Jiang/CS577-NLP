---
language:
- ba
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- mozilla-foundation/common_voice_7_0
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_7_0
model-index:
- name: wav2vec2-large-xls-r-300m-bashkir-cv7_opt
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: ba
    metrics:
    - name: Test WER
      type: wer
      value: 0.04440795062008041
    - name: "Test CER"
      type: "cer"
      value: 0.010491234992390509
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-bashkir-cv7_opt

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - BA dataset.
It achieves the following results on the evaluation set:
- Training Loss: 0.268400
- Validation Loss: 0.088252
- WER without LM: 0.085588
- WER with LM: 0.04440795062008041
- CER with LM: 0.010491234992390509


## Model description

Trained with this [jupiter notebook](https://drive.google.com/file/d/1KohDXZtKBWXVPZYlsLtqfxJGBzKmTtSh/view?usp=sharing)



## Intended uses & limitations

In order to reduce the number of characters, the following letters have been replaced or removed:

- 'я' -> 'йа'
- 'ю' -> 'йу'
- 'ё' -> 'йо'
- 'е' -> 'йэ' for first letter
- 'е' -> 'э' for other cases
- 'ъ' -> deleted
- 'ь' -> deleted

Therefore, in order to get the correct text, you need to do the reverse transformation and use the language model.

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 300
- num_epochs: 50
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.16.1
- Pytorch 1.10.0+cu113
- Datasets 1.18.2
- Tokenizers 0.10.3

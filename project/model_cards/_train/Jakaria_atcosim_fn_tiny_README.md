---
language:
- en
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- atcosim_corpus
metrics:
- wer
model-index:
- name: atcosim_corpus
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: atcosim_corpus
      type: atcosim_corpus
      args: 'split: test'
    metrics:
    - name: Wer
      type: wer
      value: 2.490946029502694
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# atcosim_corpus

This model is a fine-tuned version of [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) on the atcosim_corpus dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0623
- Wer: 2.4909

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0281        | 2.1   | 1000 | 0.0716          | 4.1957 |
| 0.0051        | 4.19  | 2000 | 0.0650          | 2.7162 |
| 0.0009        | 6.29  | 3000 | 0.0624          | 2.4733 |
| 0.0005        | 8.39  | 4000 | 0.0623          | 2.4909 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.6.1
- Tokenizers 0.13.2

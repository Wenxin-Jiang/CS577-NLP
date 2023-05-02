---
language:
- ka
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Georgian
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 kab
      type: mozilla-foundation/common_voice_11_0
      config: kab
      split: test
      args: kab
    metrics:
    - name: Wer
      type: wer
      value: 41.47529142173956
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Georgian

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 kab dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5547
- Wer: 41.4753

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
- train_batch_size: 64
- eval_batch_size: 32
- seed: 42
- distributed_type: multi-GPU
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 400
- training_steps: 5000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.4105        | 1.42  | 1000 | 0.5508          | 48.1244 |
| 0.258         | 2.84  | 2000 | 0.4905          | 42.0295 |
| 0.0998        | 4.27  | 3000 | 0.5220          | 41.6808 |
| 0.064         | 5.69  | 4000 | 0.5547          | 41.4753 |
| 0.0356        | 7.11  | 5000 | 0.5889          | 41.5737 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2

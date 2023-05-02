---
language:
- tr
license: apache-2.0
tags:
- automatic-speech-recognition
- common_voice
- generated_from_trainer
datasets:
- common_voice
metrics:
- wer
model-index:
- name: wav2vec2-common_voice-tr-demo
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: COMMON_VOICE - TR
      type: common_voice
      config: tr
      split: test
      args: 'Config: tr, Training split: train+validation, Eval split: test'
    metrics:
    - name: Wer
      type: wer
      value: 0.3446021856807272
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-common_voice-tr-demo

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the COMMON_VOICE - TR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3794
- Wer: 0.3446

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
- num_epochs: 15.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 0.92  | 100  | 3.5956          | 1.0    |
| No log        | 1.83  | 200  | 3.0269          | 0.9999 |
| No log        | 2.75  | 300  | 0.9827          | 0.8111 |
| No log        | 3.67  | 400  | 0.6236          | 0.6304 |
| 3.1866        | 4.59  | 500  | 0.5016          | 0.5264 |
| 3.1866        | 5.5   | 600  | 0.4523          | 0.4935 |
| 3.1866        | 6.42  | 700  | 0.4306          | 0.4528 |
| 3.1866        | 7.34  | 800  | 0.4328          | 0.4329 |
| 3.1866        | 8.26  | 900  | 0.4026          | 0.4105 |
| 0.227         | 9.17  | 1000 | 0.4096          | 0.4080 |
| 0.227         | 10.09 | 1100 | 0.3921          | 0.3915 |
| 0.227         | 11.01 | 1200 | 0.3830          | 0.3778 |
| 0.227         | 11.93 | 1300 | 0.3846          | 0.3616 |
| 0.227         | 12.84 | 1400 | 0.3888          | 0.3619 |
| 0.1046        | 13.76 | 1500 | 0.3861          | 0.3509 |
| 0.1046        | 14.68 | 1600 | 0.3798          | 0.3455 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
metrics:
- wer
model-index:
- name: firstcolab
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: common_voice
      type: common_voice
      config: th
      split: train+validation
      args: th
    metrics:
    - name: Wer
      type: wer
      value: 0.9641604986365407
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# firstcolab

This model is a fine-tuned version of [Thanapon1998/firstcolab](https://huggingface.co/Thanapon1998/firstcolab) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9090
- Wer: 0.9642
- Cer: 0.2127

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
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 1.5413        | 0.66  | 100  | 1.1761          | 0.9887 | 0.2718 |
| 1.4052        | 1.32  | 200  | 1.0352          | 0.9809 | 0.2396 |
| 1.2922        | 1.97  | 300  | 0.9090          | 0.9642 | 0.2127 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2

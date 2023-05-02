---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
metrics:
- wer
language:
- ga
model-index:
- name: wav2vec2-large-xls-r-1b-irish-colab
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: ga-IE
      split: train+validation
      args: ga-IE
    metrics:
    - name: Wer
      type: wer
      value: 46.911764705882353
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-1b-irish-colab

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0795
- Wer: 46.91

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
| 1.6902        | 12.12 | 400  | 1.1158          | 0.5959 |
| 0.2988        | 24.24 | 800  | 1.1375          | 0.5094 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.10.0+cu113
- Datasets 2.0.0
- Tokenizers 0.13.2

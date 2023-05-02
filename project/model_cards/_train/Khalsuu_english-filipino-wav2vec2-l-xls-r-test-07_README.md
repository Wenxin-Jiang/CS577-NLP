---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- filipino_voice
model-index:
- name: english-filipino-wav2vec2-l-xls-r-test-07
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# english-filipino-wav2vec2-l-xls-r-test-07

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) on the filipino_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6768
- Wer: 0.3755

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.9255        | 2.09  | 400  | 0.7742          | 0.7694 |
| 0.5792        | 4.19  | 800  | 0.5368          | 0.5250 |
| 0.3611        | 6.28  | 1200 | 0.4796          | 0.4718 |
| 0.2742        | 8.38  | 1600 | 0.5308          | 0.4764 |
| 0.201         | 10.47 | 2000 | 0.5885          | 0.4723 |
| 0.164         | 12.57 | 2400 | 0.5595          | 0.4750 |
| 0.1374        | 14.66 | 2800 | 0.5836          | 0.4366 |
| 0.1138        | 16.75 | 3200 | 0.6110          | 0.4628 |
| 0.0991        | 18.85 | 3600 | 0.6179          | 0.4174 |
| 0.0837        | 20.94 | 4000 | 0.6681          | 0.4170 |
| 0.0722        | 23.04 | 4400 | 0.6665          | 0.4103 |
| 0.0576        | 25.13 | 4800 | 0.7538          | 0.4068 |
| 0.052         | 27.23 | 5200 | 0.6808          | 0.3844 |
| 0.0449        | 29.32 | 5600 | 0.6768          | 0.3755 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

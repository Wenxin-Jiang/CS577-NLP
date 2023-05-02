---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-en-demo
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-en-demo

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1356
- Wer: 0.2015

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
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 5.3911        | 0.5   | 500  | 0.5397          | 0.2615 |
| 0.3413        | 1.01  | 1000 | 0.1423          | 0.2137 |
| 0.243         | 1.51  | 1500 | 0.1458          | 0.2210 |
| 0.2232        | 2.01  | 2000 | 0.1380          | 0.2143 |
| 0.162         | 2.51  | 2500 | 0.1464          | 0.2149 |
| 0.1384        | 3.02  | 3000 | 0.1348          | 0.2109 |
| 0.1164        | 3.52  | 3500 | 0.1324          | 0.2040 |
| 0.1103        | 4.02  | 4000 | 0.1310          | 0.2051 |
| 0.0857        | 4.53  | 4500 | 0.1356          | 0.2015 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1

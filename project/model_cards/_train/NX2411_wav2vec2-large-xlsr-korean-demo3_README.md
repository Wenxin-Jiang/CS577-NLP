---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- zeroth_korean
model-index:
- name: wav2vec2-large-xlsr-korean-demo3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-korean-demo3

This model is a fine-tuned version of [NX2411/wav2vec2-large-xlsr-korean-demo-no-LM](https://huggingface.co/NX2411/wav2vec2-large-xlsr-korean-demo-no-LM) on the zeroth_korean dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8265
- Wer: 0.5090

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.6157        | 2.6   | 400  | 0.6686          | 0.6386 |
| 0.4643        | 5.19  | 800  | 0.7036          | 0.6086 |
| 0.3038        | 7.79  | 1200 | 0.6960          | 0.5817 |
| 0.2229        | 10.39 | 1600 | 0.7358          | 0.5571 |
| 0.178         | 12.99 | 2000 | 0.8221          | 0.5636 |
| 0.153         | 15.58 | 2400 | 0.8575          | 0.5691 |
| 0.129         | 18.18 | 2800 | 0.7809          | 0.5297 |
| 0.1141        | 20.78 | 3200 | 0.8077          | 0.5441 |
| 0.0994        | 23.38 | 3600 | 0.8087          | 0.5209 |
| 0.0917        | 25.97 | 4000 | 0.8176          | 0.5149 |
| 0.0823        | 28.57 | 4400 | 0.8265          | 0.5090 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

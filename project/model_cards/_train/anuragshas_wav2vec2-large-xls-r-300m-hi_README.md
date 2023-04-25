---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-hi
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-hi

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4156
- Wer: 0.7181

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

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 5.7703        | 2.72  | 400  | 2.2274          | 0.9259 |
| 0.6515        | 5.44  | 800  | 1.5812          | 0.7581 |
| 0.339         | 8.16  | 1200 | 2.0590          | 0.7825 |
| 0.2262        | 10.88 | 1600 | 2.0324          | 0.7603 |
| 0.1665        | 13.6  | 2000 | 2.1396          | 0.7481 |
| 0.1311        | 16.33 | 2400 | 2.2090          | 0.7379 |
| 0.1079        | 19.05 | 2800 | 2.3907          | 0.7612 |
| 0.0927        | 21.77 | 3200 | 2.5294          | 0.7478 |
| 0.0748        | 24.49 | 3600 | 2.5024          | 0.7452 |
| 0.0644        | 27.21 | 4000 | 2.4715          | 0.7307 |
| 0.0569        | 29.93 | 4400 | 2.4156          | 0.7181 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3

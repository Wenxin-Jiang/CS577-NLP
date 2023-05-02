---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- filipino_voice
model-index:
- name: filipino-wav2vec2-l-xls-r-300m-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# filipino-wav2vec2-l-xls-r-300m-test

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the filipino_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7753
- Wer: 0.4831

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
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.7314        | 2.09  | 400  | 0.7541          | 0.7262 |
| 0.6065        | 4.19  | 800  | 0.6738          | 0.6314 |
| 0.4063        | 6.28  | 1200 | 0.6310          | 0.5992 |
| 0.2986        | 8.38  | 1600 | 0.6301          | 0.5340 |
| 0.2263        | 10.47 | 2000 | 0.6598          | 0.5391 |
| 0.1714        | 12.57 | 2400 | 0.7778          | 0.5593 |
| 0.1303        | 14.66 | 2800 | 0.7231          | 0.4907 |
| 0.1056        | 16.75 | 3200 | 0.8031          | 0.4885 |
| 0.0851        | 18.85 | 3600 | 0.7753          | 0.4831 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3

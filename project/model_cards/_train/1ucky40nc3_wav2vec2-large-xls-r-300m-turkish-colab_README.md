---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-turkish-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-turkish-colab

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4409
- Wer: 0.3676

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
| 3.9829        | 3.67  | 400  | 0.7245          | 0.7504 |
| 0.4544        | 7.34  | 800  | 0.4710          | 0.5193 |
| 0.2201        | 11.01 | 1200 | 0.4801          | 0.4815 |
| 0.1457        | 14.68 | 1600 | 0.4397          | 0.4324 |
| 0.1079        | 18.35 | 2000 | 0.4770          | 0.4287 |
| 0.0877        | 22.02 | 2400 | 0.4583          | 0.3813 |
| 0.0698        | 25.69 | 2800 | 0.4421          | 0.3892 |
| 0.0554        | 29.36 | 3200 | 0.4409          | 0.3676 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

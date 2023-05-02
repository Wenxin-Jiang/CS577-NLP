---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- li_singlish
model-index:
- name: wav2vec2-large-xls-r-300m-singlish-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-singlish-colab

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the li_singlish dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7199
- Wer: 0.3337

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
| 4.2984        | 4.76  | 400  | 2.9046          | 1.0    |
| 1.1895        | 9.52  | 800  | 0.7725          | 0.4535 |
| 0.1331        | 14.28 | 1200 | 0.7068          | 0.3847 |
| 0.0701        | 19.05 | 1600 | 0.7547          | 0.3617 |
| 0.0509        | 23.8  | 2000 | 0.7123          | 0.3444 |
| 0.0385        | 28.57 | 2400 | 0.7199          | 0.3337 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_10_0
model-index:
- name: wav2vec2-large-xls-r-300m-pl-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-pl-colab

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice_10_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1589
- Wer: 0.1338

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 765
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.9573        | 1.31  | 1000 | 3.2143          | 1.0    |
| 1.0216        | 2.61  | 2000 | 0.2310          | 0.2064 |
| 0.2925        | 3.92  | 3000 | 0.1888          | 0.1689 |
| 0.2252        | 5.23  | 4000 | 0.1731          | 0.1507 |
| 0.1983        | 6.54  | 5000 | 0.1722          | 0.1446 |
| 0.1757        | 7.84  | 6000 | 0.1637          | 0.1367 |
| 0.1656        | 9.15  | 7000 | 0.1589          | 0.1338 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

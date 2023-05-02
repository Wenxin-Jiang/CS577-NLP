---
tags:
- generated_from_trainer
model-index:
- name: timit-supervised
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# timit-supervised

This model is a fine-tuned version of [Experiments/single_dataset/timit-supervised/checkpoint-3500](https://huggingface.co/Experiments/single_dataset/timit-supervised/checkpoint-3500) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1272
- Wer: 0.0532

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0554        | 1.77  | 500  | 0.1310          | 0.0697 |
| 0.0509        | 3.53  | 1000 | 0.1497          | 0.0710 |
| 0.038         | 5.3   | 1500 | 0.1190          | 0.0659 |
| 0.0328        | 7.07  | 2000 | 0.0926          | 0.0596 |
| 0.0247        | 8.83  | 2500 | 0.0873          | 0.0570 |
| 0.0229        | 10.6  | 3000 | 0.0890          | 0.0532 |
| 0.0183        | 12.37 | 3500 | 0.0969          | 0.0532 |
| 0.0326        | 14.13 | 4000 | 0.0809          | 0.0469 |
| 0.03          | 15.9  | 4500 | 0.0758          | 0.0444 |
| 0.0264        | 17.67 | 5000 | 0.0973          | 0.0520 |
| 0.0244        | 19.43 | 5500 | 0.1272          | 0.0532 |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.2
- Datasets 1.18.2
- Tokenizers 0.10.3

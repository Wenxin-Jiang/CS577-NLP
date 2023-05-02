---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: 84rry-xlsr-53-arabic
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 84rry-xlsr-53-arabic

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0025
- Wer: 0.4977

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.4906        | 2.25  | 500  | 1.3179          | 0.8390 |
| 0.8851        | 4.5   | 1000 | 0.7385          | 0.6221 |
| 0.6884        | 6.76  | 1500 | 0.7005          | 0.5765 |
| 0.5525        | 9.01  | 2000 | 0.6931          | 0.5610 |
| 0.474         | 11.26 | 2500 | 0.7977          | 0.5560 |
| 0.3976        | 13.51 | 3000 | 0.7750          | 0.5375 |
| 0.343         | 15.76 | 3500 | 0.7553          | 0.5206 |
| 0.2838        | 18.02 | 4000 | 0.8162          | 0.5099 |
| 0.2369        | 20.27 | 4500 | 0.8574          | 0.5124 |
| 0.2298        | 22.52 | 5000 | 0.8848          | 0.5057 |
| 0.1727        | 24.77 | 5500 | 0.9193          | 0.5070 |
| 0.1675        | 27.03 | 6000 | 0.9959          | 0.4988 |
| 0.1457        | 29.28 | 6500 | 1.0025          | 0.4977 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1

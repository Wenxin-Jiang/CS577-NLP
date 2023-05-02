---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: mt5-base-finetuned-ar-to-en
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-finetuned-ar-to-en

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Bleu: 0.0111
- Gen Len: 6.732

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu   | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:-------:|
| 163.1788      | 1.0   | 816  | nan             | 0.0111 | 6.732   |
| 1.1396        | 2.0   | 1632 | nan             | 0.0111 | 6.732   |
| 0.0381        | 3.0   | 2448 | nan             | 0.0111 | 6.732   |
| 0.0           | 4.0   | 3264 | nan             | 0.0111 | 6.732   |
| 155.5697      | 5.0   | 4080 | nan             | 0.0111 | 6.732   |
| 74.9948       | 6.0   | 4896 | nan             | 0.0111 | 6.732   |
| 0.116         | 6.13  | 5000 | nan             | 0.0111 | 6.732   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

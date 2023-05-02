---
tags:
- summarization
- mT5_multilingual_XLSum
- mt5
- abstractive summarization
- ar
- xlsum
- generated_from_trainer
datasets:
- xlsum
model-index:
- name: mT5_multilingual_XLSum-finetune-ar-xlsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mT5_multilingual_XLSum-finetune-ar-xlsum

This model is a fine-tuned version of [csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2497
- Rouge-1: 32.52
- Rouge-2: 14.71
- Rouge-l: 27.88
- Gen Len: 41.45
- Bertscore: 74.65

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge-1 | Rouge-2 | Rouge-l | Gen Len | Bertscore |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:-------:|:---------:|
| 3.5465        | 1.0   | 585  | 3.3215          | 30.09   | 13.23   | 26.07   | 36.31   | 73.97     |
| 3.3564        | 2.0   | 1170 | 3.2547          | 31.29   | 13.93   | 26.75   | 41.68   | 74.22     |
| 3.2185        | 3.0   | 1755 | 3.2421          | 31.78   | 14.1    | 27.07   | 41.64   | 74.4      |
| 3.1145        | 4.0   | 2340 | 3.2241          | 31.98   | 14.38   | 27.51   | 40.29   | 74.46     |
| 3.031         | 5.0   | 2925 | 3.2313          | 32.3    | 14.67   | 27.83   | 39.81   | 74.61     |
| 2.9627        | 6.0   | 3510 | 3.2348          | 32.39   | 14.65   | 27.76   | 40.02   | 74.6      |
| 2.9088        | 7.0   | 4095 | 3.2439          | 32.5    | 14.66   | 27.81   | 41.2    | 74.65     |
| 2.8649        | 8.0   | 4680 | 3.2497          | 32.52   | 14.71   | 27.88   | 41.45   | 74.65     |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

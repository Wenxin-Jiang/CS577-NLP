---
license: apache-2.0
tags:
- summarization
- fa
- mt5
- Abstractive Summarization
- generated_from_trainer
datasets:
- pn_summary
model-index:
- name: mt5-base-finetuned-fa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-finetuned-fa

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the pn_summary dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6477
- Rouge-1: 33.7
- Rouge-2: 21.28
- Rouge-l: 31.69
- Gen Len: 19.0
- Bertscore: 74.52

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
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 5
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge-1 | Rouge-2 | Rouge-l | Gen Len | Bertscore |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:-------:|:---------:|
| 3.3828        | 1.0   | 1875 | 2.8114          | 32.17   | 19.47   | 30.12   | 18.99   | 74.25     |
| 2.8204        | 2.0   | 3750 | 2.7080          | 32.67   | 19.92   | 30.56   | 19.0    | 74.31     |
| 2.6907        | 3.0   | 5625 | 2.6724          | 33.22   | 20.44   | 31.11   | 19.0    | 74.47     |
| 2.6029        | 4.0   | 7500 | 2.6513          | 33.46   | 20.75   | 31.38   | 19.0    | 74.54     |
| 2.5414        | 5.0   | 9375 | 2.6477          | 33.68   | 20.91   | 31.62   | 19.0    | 74.58     |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

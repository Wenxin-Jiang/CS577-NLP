---
tags:
- summarization
- persian
- MBart50
- Abstractive Summarization
- generated_from_trainer
datasets:
- xlsum
model-index:
- name: mbart-large-50-finetuned-persian
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart-large-50-finetuned-persian

This model is a fine-tuned version of [facebook/mbart-large-50](https://huggingface.co/facebook/mbart-large-50) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 4.1932
- Rouge-1: 26.11
- Rouge-2: 8.11
- Rouge-l: 21.09
- Gen Len: 37.29
- Bertscore: 71.08

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
- num_epochs: 5
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge-1 | Rouge-2 | Rouge-l | Gen Len | Bertscore |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:-------:|:---------:|
| 5.5612        | 1.0   | 1476 | 4.5015          | 17.07   | 3.14    | 13.54   | 47.49   | 66.83     |
| 4.3049        | 2.0   | 2952 | 4.1055          | 22.63   | 5.89    | 18.03   | 40.43   | 69.23     |
| 3.8154        | 3.0   | 4428 | 3.9822          | 24.57   | 7.15    | 19.74   | 37.35   | 70.36     |
| 3.3401        | 4.0   | 5904 | 4.0088          | 25.84   | 7.96    | 20.95   | 37.56   | 70.83     |
| 2.8879        | 5.0   | 7380 | 4.1932          | 26.24   | 8.26    | 21.23   | 37.78   | 71.05     |


### Framework versions

- Transformers 4.19.1
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1

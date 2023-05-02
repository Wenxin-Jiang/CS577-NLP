---
tags:
- summarization
- ar
- encoder-decoder
- xlm-roberta
- Abstractive Summarization
- roberta
- generated_from_trainer
datasets:
- xlsum
model-index:
- name: xlmroberta2xlmroberta-finetune-summarization-ar
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlmroberta2xlmroberta-finetune-summarization-ar

This model is a fine-tuned version of [](https://huggingface.co/) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 4.1298
- Rouge-1: 21.69
- Rouge-2: 8.73
- Rouge-l: 19.52
- Gen Len: 19.96
- Bertscore: 71.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 10
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge-1 | Rouge-2 | Rouge-l | Gen Len | Bertscore |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:-------:|:---------:|
| 8.0645        | 1.0   | 1172  | 7.3567          | 8.22    | 0.66    | 7.94    | 20.0    | 58.18     |
| 7.2042        | 2.0   | 2344  | 6.6058          | 12.12   | 2.19    | 11.4    | 20.0    | 63.24     |
| 6.4168        | 3.0   | 3516  | 5.8784          | 16.46   | 4.31    | 15.15   | 20.0    | 66.3      |
| 5.4622        | 4.0   | 4688  | 4.7931          | 17.6    | 5.87    | 15.9    | 19.99   | 69.21     |
| 4.7829        | 5.0   | 5860  | 4.4418          | 19.17   | 6.74    | 17.22   | 19.98   | 70.23     |
| 4.4829        | 6.0   | 7032  | 4.2950          | 19.8    | 7.11    | 17.74   | 19.98   | 70.38     |
| 4.304         | 7.0   | 8204  | 4.2155          | 20.71   | 7.59    | 18.56   | 19.98   | 70.66     |
| 4.1778        | 8.0   | 9376  | 4.1632          | 21.1    | 7.94    | 18.99   | 19.98   | 70.86     |
| 4.0886        | 9.0   | 10548 | 4.1346          | 21.44   | 8.03    | 19.28   | 19.98   | 70.93     |
| 4.0294        | 10.0  | 11720 | 4.1298          | 21.51   | 8.14    | 19.33   | 19.98   | 71.02     |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

---
tags:
- summarization
- Arat5-base
- abstractive summarization
- ar
- xlsum
- generated_from_trainer
datasets:
- xlsum
model-index:
- name: AraT5-base-finetune-ar-xlsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AraT5-base-finetune-ar-xlsum

This model is a fine-tuned version of [UBC-NLP/AraT5-base](https://huggingface.co/UBC-NLP/AraT5-base) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 4.4714
- Rouge-1: 29.55
- Rouge-2: 12.63
- Rouge-l: 25.8
- Gen Len: 18.76
- Bertscore: 73.3

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
- gradient_accumulation_steps: 16
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 10
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge-1 | Rouge-2 | Rouge-l | Gen Len | Bertscore |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:-------:|:---------:|
| 11.9753       | 1.0   | 293  | 7.0887          | 11.93   | 2.56    | 10.93   | 17.19   | 63.85     |
| 6.7818        | 2.0   | 586  | 5.7712          | 19.94   | 6.34    | 17.65   | 18.64   | 69.0      |
| 5.9434        | 3.0   | 879  | 5.1083          | 23.51   | 8.56    | 20.66   | 18.88   | 70.78     |
| 5.451         | 4.0   | 1172 | 4.8538          | 25.84   | 10.05   | 22.63   | 18.42   | 72.04     |
| 5.1643        | 5.0   | 1465 | 4.6910          | 27.23   | 11.13   | 23.83   | 18.78   | 72.45     |
| 4.9693        | 6.0   | 1758 | 4.5950          | 28.42   | 11.71   | 24.82   | 18.74   | 72.94     |
| 4.8308        | 7.0   | 2051 | 4.5323          | 28.95   | 12.19   | 25.3    | 18.74   | 73.13     |
| 4.7284        | 8.0   | 2344 | 4.4956          | 29.19   | 12.37   | 25.53   | 18.76   | 73.18     |
| 4.653         | 9.0   | 2637 | 4.4757          | 29.44   | 12.48   | 25.63   | 18.78   | 73.23     |
| 4.606         | 10.0  | 2930 | 4.4714          | 29.55   | 12.63   | 25.8    | 18.76   | 73.3      |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

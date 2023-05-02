---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: medium
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medium

This model is a fine-tuned version of [prithivida/parrot_paraphraser_on_T5](https://huggingface.co/prithivida/parrot_paraphraser_on_T5) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6025
- Rouge1: 81.6007
- Rouge2: 75.1196
- Rougel: 81.4213
- Rougelsum: 81.4956
- Gen Len: 32.4286

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 63   | 0.5775          | 65.0748 | 58.8985 | 64.5731 | 63.6249   | 19.0    |
| No log        | 2.0   | 126  | 0.5806          | 74.3055 | 69.2025 | 73.4922 | 73.0941   | 17.8571 |
| No log        | 3.0   | 189  | 0.6025          | 71.3808 | 66.0359 | 70.1235 | 69.4614   | 18.0    |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.17.0
- Tokenizers 0.10.3

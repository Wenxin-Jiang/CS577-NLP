---
tags:
- generated_from_trainer
model-index:
- name: BertjeWDialDataALLQonly
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BertjeWDialDataALLQonly

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9438

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.2122        | 1.0   | 871   | 2.0469          |
| 2.0961        | 2.0   | 1742  | 2.0117          |
| 2.0628        | 3.0   | 2613  | 2.0040          |
| 2.0173        | 4.0   | 3484  | 1.9901          |
| 1.9772        | 5.0   | 4355  | 1.9711          |
| 1.9455        | 6.0   | 5226  | 1.9785          |
| 1.917         | 7.0   | 6097  | 1.9380          |
| 1.8933        | 8.0   | 6968  | 1.9651          |
| 1.8708        | 9.0   | 7839  | 1.9915          |
| 1.862         | 10.0  | 8710  | 1.9310          |
| 1.8545        | 11.0  | 9581  | 1.9422          |
| 1.8231        | 12.0  | 10452 | 1.9310          |
| 1.8141        | 13.0  | 11323 | 1.9362          |
| 1.7939        | 14.0  | 12194 | 1.9334          |
| 1.8035        | 15.0  | 13065 | 1.9197          |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3

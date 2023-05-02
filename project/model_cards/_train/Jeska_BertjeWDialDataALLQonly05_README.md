---
tags:
- generated_from_trainer
model-index:
- name: BertjeWDialDataALLQonly05
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BertjeWDialDataALLQonly05

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3921

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 12.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.9349        | 1.0   | 871   | 2.9642          |
| 2.9261        | 2.0   | 1742  | 2.9243          |
| 2.8409        | 3.0   | 2613  | 2.8895          |
| 2.7308        | 4.0   | 3484  | 2.8394          |
| 2.6042        | 5.0   | 4355  | 2.7703          |
| 2.4671        | 6.0   | 5226  | 2.7522          |
| 2.3481        | 7.0   | 6097  | 2.6339          |
| 2.2493        | 8.0   | 6968  | 2.6224          |
| 2.1233        | 9.0   | 7839  | 2.5637          |
| 2.0194        | 10.0  | 8710  | 2.4896          |
| 1.9178        | 11.0  | 9581  | 2.4689          |
| 1.8588        | 12.0  | 10452 | 2.4663          |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3

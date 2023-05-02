---
tags:
- generated_from_trainer
model-index:
- name: BertjeWDialDataALLQonly128
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BertjeWDialDataALLQonly128

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0364

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
| 2.2326        | 1.0   | 871   | 2.1509          |
| 2.1375        | 2.0   | 1742  | 2.1089          |
| 2.0442        | 3.0   | 2613  | 2.0655          |
| 2.0116        | 4.0   | 3484  | 2.0433          |
| 1.9346        | 5.0   | 4355  | 2.0134          |
| 1.9056        | 6.0   | 5226  | 1.9956          |
| 1.8295        | 7.0   | 6097  | 2.0287          |
| 1.8204        | 8.0   | 6968  | 2.0173          |
| 1.7928        | 9.0   | 7839  | 2.0251          |
| 1.7357        | 10.0  | 8710  | 2.0148          |
| 1.7318        | 11.0  | 9581  | 1.9274          |
| 1.7311        | 12.0  | 10452 | 1.9314          |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3

---
tags:
- generated_from_trainer
model-index:
- name: BertjeWDialDataALLQonly07
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BertjeWDialDataALLQonly07

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1135

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 18.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.3589        | 1.0   | 871   | 2.2805          |
| 2.2563        | 2.0   | 1742  | 2.2501          |
| 2.1936        | 3.0   | 2613  | 2.2419          |
| 2.11          | 4.0   | 3484  | 2.2301          |
| 2.0311        | 5.0   | 4355  | 2.2320          |
| 1.969         | 6.0   | 5226  | 2.2276          |
| 1.9148        | 7.0   | 6097  | 2.1621          |
| 1.8569        | 8.0   | 6968  | 2.1876          |
| 1.7978        | 9.0   | 7839  | 2.2011          |
| 1.7602        | 10.0  | 8710  | 2.1280          |
| 1.7166        | 11.0  | 9581  | 2.1644          |
| 1.6651        | 12.0  | 10452 | 2.1246          |
| 1.6141        | 13.0  | 11323 | 2.1264          |
| 1.5759        | 14.0  | 12194 | 2.1143          |
| 1.5478        | 15.0  | 13065 | 2.0982          |
| 1.5311        | 16.0  | 13936 | 2.0993          |
| 1.5187        | 17.0  | 14807 | 2.0979          |
| 1.4809        | 18.0  | 15678 | 2.0338          |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3

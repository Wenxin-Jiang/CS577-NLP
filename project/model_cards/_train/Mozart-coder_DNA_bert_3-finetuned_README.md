---
tags:
- generated_from_trainer
model-index:
- name: DNA_bert_3-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DNA_bert_3-finetuned

This model is a fine-tuned version of [armheb/DNA_bert_3](https://huggingface.co/armheb/DNA_bert_3) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5788

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.8244        | 1.0   | 62   | 0.6044          |
| 0.5987        | 2.0   | 124  | 0.5933          |
| 0.5915        | 3.0   | 186  | 0.5856          |
| 0.585         | 4.0   | 248  | 0.5844          |
| 0.5817        | 5.0   | 310  | 0.5818          |
| 0.5791        | 6.0   | 372  | 0.5809          |
| 0.5801        | 7.0   | 434  | 0.5807          |
| 0.5768        | 8.0   | 496  | 0.5796          |
| 0.5741        | 9.0   | 558  | 0.5790          |
| 0.574         | 10.0  | 620  | 0.5788          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

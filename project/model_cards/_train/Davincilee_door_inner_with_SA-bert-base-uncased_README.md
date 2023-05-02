---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: door_inner_with_SA-bert-base-uncased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# door_inner_with_SA-bert-base-uncased

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1513

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
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.5492        | 1.0   | 96   | 2.3831          |
| 2.4031        | 2.0   | 192  | 2.2963          |
| 2.3391        | 3.0   | 288  | 2.2000          |
| 2.2951        | 4.0   | 384  | 2.2505          |
| 2.2151        | 5.0   | 480  | 2.1691          |
| 2.2237        | 6.0   | 576  | 2.1855          |
| 2.1984        | 7.0   | 672  | 2.2558          |
| 2.1749        | 8.0   | 768  | 2.2019          |
| 2.1475        | 9.0   | 864  | 2.1310          |
| 2.1446        | 10.0  | 960  | 2.1334          |
| 2.1374        | 11.0  | 1056 | 2.1909          |
| 2.1117        | 12.0  | 1152 | 2.2028          |


### Framework versions

- Transformers 4.19.0
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1

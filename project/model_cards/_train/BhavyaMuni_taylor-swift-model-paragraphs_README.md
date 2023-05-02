---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: taylor-swift-model-paragraphs
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# taylor-swift-model-paragraphs

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.3564

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 25

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.9316        | 1.0   | 59   | 3.8227          |
| 3.824         | 2.0   | 118  | 3.7301          |
| 3.5808        | 3.0   | 177  | 3.6658          |
| 3.625         | 4.0   | 236  | 3.6205          |
| 3.643         | 5.0   | 295  | 3.5862          |
| 3.5443        | 6.0   | 354  | 3.5545          |
| 3.4535        | 7.0   | 413  | 3.5274          |
| 3.398         | 8.0   | 472  | 3.5072          |
| 3.3253        | 9.0   | 531  | 3.4833          |
| 3.4111        | 10.0  | 590  | 3.4688          |
| 3.3461        | 11.0  | 649  | 3.4503          |
| 3.3133        | 12.0  | 708  | 3.4373          |
| 3.3921        | 13.0  | 767  | 3.4246          |
| 3.2661        | 14.0  | 826  | 3.4102          |
| 3.2257        | 15.0  | 885  | 3.4052          |
| 3.1837        | 16.0  | 944  | 3.3911          |
| 3.1935        | 17.0  | 1003 | 3.3849          |
| 2.9369        | 18.0  | 1062 | 3.3774          |
| 3.2486        | 19.0  | 1121 | 3.3721          |
| 3.1542        | 20.0  | 1180 | 3.3681          |
| 3.0771        | 21.0  | 1239 | 3.3624          |
| 3.1206        | 22.0  | 1298 | 3.3581          |
| 3.0358        | 23.0  | 1357 | 3.3585          |
| 2.9207        | 24.0  | 1416 | 3.3568          |
| 3.0496        | 25.0  | 1475 | 3.3564          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

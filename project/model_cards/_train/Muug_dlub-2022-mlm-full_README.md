---
tags:
- generated_from_trainer
model-index:
- name: dlub-2022-mlm-full
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dlub-2022-mlm-full

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 8.4308

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
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 9.7809        | 1.0   | 21   | 9.4572          |
| 9.4021        | 2.0   | 42   | 9.2312          |
| 9.1448        | 3.0   | 63   | 9.0206          |
| 8.9608        | 4.0   | 84   | 8.8606          |
| 8.8125        | 5.0   | 105  | 8.6954          |
| 8.6717        | 6.0   | 126  | 8.5819          |
| 8.5944        | 7.0   | 147  | 8.5012          |
| 8.5245        | 8.0   | 168  | 8.4900          |
| 8.4856        | 9.0   | 189  | 8.4448          |
| 8.4563        | 10.0  | 210  | 8.4308          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-16-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-16-4

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6329
- Accuracy: 0.6392

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6945        | 1.0   | 7    | 0.7381          | 0.2857   |
| 0.7072        | 2.0   | 14   | 0.7465          | 0.2857   |
| 0.6548        | 3.0   | 21   | 0.7277          | 0.4286   |
| 0.5695        | 4.0   | 28   | 0.6738          | 0.5714   |
| 0.4615        | 5.0   | 35   | 0.8559          | 0.5714   |
| 0.0823        | 6.0   | 42   | 1.0983          | 0.5714   |
| 0.0274        | 7.0   | 49   | 1.9937          | 0.5714   |
| 0.0106        | 8.0   | 56   | 2.2209          | 0.5714   |
| 0.0039        | 9.0   | 63   | 2.2114          | 0.5714   |
| 0.0031        | 10.0  | 70   | 2.2808          | 0.5714   |
| 0.0013        | 11.0  | 77   | 2.3707          | 0.5714   |
| 0.0008        | 12.0  | 84   | 2.4902          | 0.5714   |
| 0.0005        | 13.0  | 91   | 2.5208          | 0.5714   |
| 0.0007        | 14.0  | 98   | 2.5683          | 0.5714   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

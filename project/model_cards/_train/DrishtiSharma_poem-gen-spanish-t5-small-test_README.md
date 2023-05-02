---
license: mit
tags:
- generated_from_trainer
model-index:
- name: poem-gen-spanish-t5-small-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# poem-gen-spanish-t5-small-test

This model is a fine-tuned version of [hackathon-pln-es/poem-gen-spanish-t5-small](https://huggingface.co/hackathon-pln-es/poem-gen-spanish-t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2170

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
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 2.8391        | 0.73  | 30000  | 2.9486          |
| 2.6782        | 1.46  | 60000  | 2.8990          |
| 2.5323        | 2.19  | 90000  | 2.9193          |
| 2.5191        | 2.93  | 120000 | 2.8982          |
| 2.4007        | 3.66  | 150000 | 2.9241          |
| 2.2909        | 4.39  | 180000 | 2.9418          |
| 2.1741        | 5.12  | 210000 | 2.9783          |
| 2.1973        | 5.85  | 240000 | 2.9671          |
| 2.0969        | 6.58  | 270000 | 3.0179          |
| 1.9818        | 7.31  | 300000 | 3.0582          |
| 1.8639        | 8.05  | 330000 | 3.0918          |
| 1.8824        | 8.78  | 360000 | 3.1095          |
| 1.7929        | 9.51  | 390000 | 3.1502          |
| 1.7247        | 10.24 | 420000 | 3.1855          |
| 1.7039        | 10.97 | 450000 | 3.1953          |
| 1.6475        | 11.7  | 480000 | 3.2180          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

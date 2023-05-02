---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: closure_system_door_inne-bert-base-uncased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# closure_system_door_inne-bert-base-uncased

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7907

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
- train_batch_size: 7
- eval_batch_size: 7
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.7321        | 1.0   | 2    | 2.5801          |
| 2.6039        | 2.0   | 4    | 2.0081          |
| 2.4556        | 3.0   | 6    | 2.3329          |
| 2.3587        | 4.0   | 8    | 2.4156          |
| 2.2565        | 5.0   | 10   | 2.0009          |
| 2.3489        | 6.0   | 12   | 1.7774          |
| 2.2622        | 7.0   | 14   | 2.2064          |
| 2.415         | 8.0   | 16   | 1.9671          |
| 2.1873        | 9.0   | 18   | 2.0729          |
| 2.2377        | 10.0  | 20   | 2.0052          |
| 2.352         | 11.0  | 22   | 1.9614          |
| 2.2347        | 12.0  | 24   | 2.2437          |
| 2.1113        | 13.0  | 26   | 1.7145          |
| 2.1939        | 14.0  | 28   | 1.5418          |
| 2.0645        | 15.0  | 30   | 2.1882          |
| 2.1499        | 16.0  | 32   | 2.0266          |
| 2.1432        | 17.0  | 34   | 2.3583          |
| 2.0656        | 18.0  | 36   | 2.3147          |
| 2.0348        | 19.0  | 38   | 2.2807          |
| 2.0502        | 20.0  | 40   | 1.7122          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1

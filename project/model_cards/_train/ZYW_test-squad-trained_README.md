---

model-index:
- name: test-squad-trained
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test-squad-trained

This model was trained from scratch on an unkown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2026

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.988         | 1.0   | 5486  | 1.1790          |
| 0.7793        | 2.0   | 10972 | 1.2026          |
| 0.8068        | 3.0   | 16458 | 1.2026          |


### Framework versions

- Transformers 4.6.1
- Pytorch 1.8.1+cu101
- Datasets 1.6.2
- Tokenizers 0.10.3

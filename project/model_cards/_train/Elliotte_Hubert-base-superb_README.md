---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- superb
model-index:
- name: Hubert-base-superb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Hubert-base-superb

This model is a fine-tuned version of [ntu-spml/distilhubert](https://huggingface.co/ntu-spml/distilhubert) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6712
- Wer: 0.4781

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.7884        | 0.8   | 500  | 0.8900          | 0.6940 |
| 0.6603        | 1.6   | 1000 | 0.7378          | 0.6103 |
| 0.5401        | 2.4   | 1500 | 0.7107          | 0.5762 |
| 0.4604        | 3.2   | 2000 | 0.6563          | 0.5320 |
| 0.3936        | 4.0   | 2500 | 0.6315          | 0.5244 |
| 0.3186        | 4.8   | 3000 | 0.6525          | 0.5007 |
| 0.2727        | 5.6   | 3500 | 0.6553          | 0.4855 |
| 0.2296        | 6.4   | 4000 | 0.6712          | 0.4781 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

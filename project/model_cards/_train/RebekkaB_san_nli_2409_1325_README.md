---
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: san_nli_2409_1325
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# san_nli_2409_1325

This model is a fine-tuned version of [svalabs/gbert-large-zeroshot-nli](https://huggingface.co/svalabs/gbert-large-zeroshot-nli) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3856
- F1: 0.9219

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 0.93  | 10   | 0.2410          | 0.9219 |
| No log        | 1.93  | 20   | 0.5240          | 0.9149 |
| No log        | 2.93  | 30   | 0.4756          | 0.9219 |
| No log        | 3.93  | 40   | 0.3856          | 0.9219 |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

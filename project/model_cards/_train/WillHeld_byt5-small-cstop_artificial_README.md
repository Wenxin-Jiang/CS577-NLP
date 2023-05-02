---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cstop_artificial
model-index:
- name: byt5-small-cstop_artificial
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# byt5-small-cstop_artificial

This model is a fine-tuned version of [google/byt5-small](https://huggingface.co/google/byt5-small) on the cstop_artificial dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0414
- Exact Match: 0.8283

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 0.2091        | 25.0  | 200  | 0.0555          | 0.0107      |
| 0.0129        | 50.0  | 400  | 0.0414          | 0.0411      |
| 0.004         | 75.0  | 600  | 0.0483          | 0.0394      |
| 0.0018        | 100.0 | 800  | 0.0556          | 0.0394      |
| 0.0011        | 125.0 | 1000 | 0.0598          | 0.0394      |
| 0.0008        | 150.0 | 1200 | 0.0580          | 0.0376      |
| 0.0008        | 175.0 | 1400 | 0.0627          | 0.0394      |
| 0.0005        | 200.0 | 1600 | 0.0658          | 0.0376      |
| 0.0005        | 225.0 | 1800 | 0.0657          | 0.0376      |
| 0.0004        | 250.0 | 2000 | 0.0687          | 0.0376      |
| 0.0003        | 275.0 | 2200 | 0.0731          | 0.0376      |
| 0.0003        | 300.0 | 2400 | 0.0723          | 0.0376      |
| 0.0002        | 325.0 | 2600 | 0.0736          | 0.0376      |
| 0.0002        | 350.0 | 2800 | 0.0741          | 0.0394      |
| 0.0002        | 375.0 | 3000 | 0.0745          | 0.0394      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2

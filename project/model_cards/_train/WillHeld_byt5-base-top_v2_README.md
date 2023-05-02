---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- top_v2
model-index:
- name: byt5-base-top_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# byt5-base-top_v2

This model is a fine-tuned version of [google/byt5-base](https://huggingface.co/google/byt5-base) on the top_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0154
- Exact Match: 0.8533

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 64
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 0.3866        | 0.82  | 200  | 0.0434          | 0.0278      |
| 0.0335        | 1.65  | 400  | 0.0224          | 0.0396      |
| 0.0206        | 2.47  | 600  | 0.0184          | 0.0403      |
| 0.0162        | 3.29  | 800  | 0.0189          | 0.0409      |
| 0.0165        | 4.12  | 1000 | 0.0167          | 0.0410      |
| 0.0116        | 4.94  | 1200 | 0.0154          | 0.0413      |
| 0.0093        | 5.76  | 1400 | 0.0154          | 0.0415      |
| 0.008         | 6.58  | 1600 | 0.0161          | 0.0413      |
| 0.0071        | 7.41  | 1800 | 0.0167          | 0.0414      |
| 0.0064        | 8.23  | 2000 | 0.0171          | 0.0414      |
| 0.0055        | 9.05  | 2200 | 0.0168          | 0.0415      |
| 0.0046        | 9.88  | 2400 | 0.0177          | 0.0415      |
| 0.0039        | 10.7  | 2600 | 0.0183          | 0.0416      |
| 0.0034        | 11.52 | 2800 | 0.0190          | 0.0414      |
| 0.0029        | 12.35 | 3000 | 0.0192          | 0.0415      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2

---
tags:
- generated_from_trainer
datasets:
- squad_modified_for_t5_qg
model-index:
- name: t5-end2end-questions-generation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-end2end-questions-generation

This model is a fine-tuned version of [digit82/kolang-t5-base](https://huggingface.co/digit82/kolang-t5-base) on the korquad_modified_for_t5_qg dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1449

## Model description

More information needed

## Training and evaluation data

KorQuAD V1.0

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.6685        | 0.66  | 100  | 2.4355          |
| 2.3957        | 1.32  | 200  | 2.2428          |
| 2.1795        | 1.98  | 300  | 2.1664          |
| 1.9408        | 2.65  | 400  | 2.1467          |
| 1.8333        | 3.31  | 500  | 2.1470          |
| 1.7319        | 3.97  | 600  | 2.1194          |
| 1.6095        | 4.63  | 700  | 2.1348          |
| 1.5662        | 5.3   | 800  | 2.1433          |
| 1.5038        | 5.96  | 900  | 2.1319          |
| 1.45          | 6.62  | 1000 | 2.1449          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

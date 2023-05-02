---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: Copilot_for_poors
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Copilot_for_poors

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8084

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
- train_batch_size: 12
- eval_batch_size: 12
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 65   | 2.9425          |
| No log        | 2.0   | 130  | 2.5889          |
| No log        | 3.0   | 195  | 2.3886          |
| No log        | 4.0   | 260  | 2.2679          |
| No log        | 5.0   | 325  | 2.1732          |
| No log        | 6.0   | 390  | 2.0942          |
| No log        | 7.0   | 455  | 2.0343          |
| 2.7389        | 8.0   | 520  | 1.9956          |
| 2.7389        | 9.0   | 585  | 1.9557          |
| 2.7389        | 10.0  | 650  | 1.9284          |
| 2.7389        | 11.0  | 715  | 1.9024          |
| 2.7389        | 12.0  | 780  | 1.8811          |
| 2.7389        | 13.0  | 845  | 1.8612          |
| 2.7389        | 14.0  | 910  | 1.8443          |
| 2.7389        | 15.0  | 975  | 1.8331          |
| 2.1064        | 16.0  | 1040 | 1.8228          |
| 2.1064        | 17.0  | 1105 | 1.8178          |
| 2.1064        | 18.0  | 1170 | 1.8130          |
| 2.1064        | 19.0  | 1235 | 1.8093          |
| 2.1064        | 20.0  | 1300 | 1.8084          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

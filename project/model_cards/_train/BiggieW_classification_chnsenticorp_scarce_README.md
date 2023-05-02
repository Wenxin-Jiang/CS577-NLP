---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: classification_chnsenticorp_scarce
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# classification_chnsenticorp_scarce

This model is a fine-tuned version of [hfl/chinese-roberta-wwm-ext](https://huggingface.co/hfl/chinese-roberta-wwm-ext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7194
- Accuracy: 0.5

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
- train_batch_size: 10
- eval_batch_size: 10
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7839        | 1.0   | 2    | 0.7446          | 0.4      |
| 0.6498        | 2.0   | 4    | 0.7266          | 0.45     |
| 0.5516        | 3.0   | 6    | 0.7208          | 0.35     |
| 0.5203        | 4.0   | 8    | 0.7190          | 0.35     |
| 0.4611        | 5.0   | 10   | 0.7162          | 0.45     |
| 0.4248        | 6.0   | 12   | 0.7178          | 0.45     |
| 0.3504        | 7.0   | 14   | 0.7153          | 0.45     |
| 0.3418        | 8.0   | 16   | 0.7170          | 0.5      |
| 0.315         | 9.0   | 18   | 0.7192          | 0.5      |
| 0.3125        | 10.0  | 20   | 0.7194          | 0.5      |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

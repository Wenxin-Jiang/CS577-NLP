---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: classification_tnews_eda_aug
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# classification_tnews_eda_aug

This model is a fine-tuned version of [hfl/chinese-roberta-wwm-ext](https://huggingface.co/hfl/chinese-roberta-wwm-ext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4212
- Accuracy: 0.6533

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.4947        | 1.0   | 135  | 1.3206          | 0.6267   |
| 0.1659        | 2.0   | 270  | 1.2521          | 0.68     |
| 0.0274        | 3.0   | 405  | 1.3476          | 0.66     |
| 0.0161        | 4.0   | 540  | 1.3907          | 0.66     |
| 0.0136        | 5.0   | 675  | 1.4212          | 0.6533   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

---
license: mit
tags:
- generated_from_trainer
model-index:
- name: camembert-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# camembert-ner

This model is a fine-tuned version of [Jean-Baptiste/camembert-ner](https://huggingface.co/Jean-Baptiste/camembert-ner) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1179
- Overall Precision: 0.7367
- Overall Recall: 0.7522
- Overall F1: 0.7444
- Overall Accuracy: 0.9728
- Humanprod F1: 0.1639
- Loc F1: 0.7657
- Org F1: 0.5352
- Per F1: 0.7961

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Overall Precision | Overall Recall | Overall F1 | Overall Accuracy | Humanprod F1 | Loc F1 | Org F1 | Per F1 |
|:-------------:|:-----:|:----:|:---------------:|:-----------------:|:--------------:|:----------:|:----------------:|:------------:|:------:|:------:|:------:|
| No log        | 1.0   | 307  | 0.1254          | 0.7185            | 0.7420         | 0.7300     | 0.9715           | 0.0357       | 0.7579 | 0.5052 | 0.7778 |
| 0.1195        | 2.0   | 614  | 0.1179          | 0.7367            | 0.7522         | 0.7444     | 0.9728           | 0.1639       | 0.7657 | 0.5352 | 0.7961 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.7.1+cpu
- Datasets 2.7.1
- Tokenizers 0.13.2

---
tags:
- generated_from_trainer
datasets:
- skript
model-index:
- name: bert-base-NER-reptile-5-datasets-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-NER-reptile-5-datasets-finetuned-ner

This model is a fine-tuned version of [sberbank-ai/bert-base-NER-reptile-5-datasets](https://huggingface.co/sberbank-ai/bert-base-NER-reptile-5-datasets) on the skript dataset.

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
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 298  | 0.4198          | 0.6385    | 0.5297 | 0.5790 | 0.8699   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

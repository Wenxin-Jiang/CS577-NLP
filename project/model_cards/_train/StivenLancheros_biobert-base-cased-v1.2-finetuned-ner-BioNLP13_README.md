---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: biobert-base-cased-v1.2-finetuned-ner-BioNLP13
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-base-cased-v1.2-finetuned-ner-BioNLP13

This model is a fine-tuned version of [dmis-lab/biobert-base-cased-v1.2](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2042
- Precision: 0.9550
- Recall: 0.9559
- F1: 0.9555
- Accuracy: 0.9552

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.3114        | 1.0   | 692  | 0.1693          | 0.9453    | 0.9452 | 0.9453 | 0.9461   |
| 0.1292        | 2.0   | 1384 | 0.1754          | 0.9492    | 0.9525 | 0.9509 | 0.9508   |
| 0.0522        | 3.0   | 2076 | 0.1895          | 0.9529    | 0.9540 | 0.9534 | 0.9530   |
| 0.032         | 4.0   | 2768 | 0.2042          | 0.9550    | 0.9559 | 0.9555 | 0.9552   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0

---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: xlm-roberta-base-it-aug-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-it-aug-ner

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2626
- Precision: 0.6778
- Recall: 0.6981
- F1: 0.6878
- Accuracy: 0.9266

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.6114        | 1.0   | 882  | 0.3615          | 0.5708    | 0.5680 | 0.5694 | 0.9023   |
| 0.2401        | 2.0   | 1764 | 0.2841          | 0.6274    | 0.6674 | 0.6468 | 0.9170   |
| 0.1886        | 3.0   | 2646 | 0.2720          | 0.6580    | 0.6853 | 0.6713 | 0.9224   |
| 0.1594        | 4.0   | 3528 | 0.2626          | 0.6778    | 0.6981 | 0.6878 | 0.9266   |
| 0.1454        | 5.0   | 4410 | 0.2632          | 0.6660    | 0.6974 | 0.6813 | 0.9257   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

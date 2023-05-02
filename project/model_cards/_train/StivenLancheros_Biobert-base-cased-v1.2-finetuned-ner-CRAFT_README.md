---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Biobert-base-cased-v1.2-finetuned-ner-CRAFT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Biobert-base-cased-v1.2-finetuned-ner-CRAFT

This model is a fine-tuned version of [dmis-lab/biobert-base-cased-v1.2](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1878
- Precision: 0.8397
- Recall: 0.8366
- F1: 0.8382
- Accuracy: 0.9683

## Model description

This model performs Named Entity Recognition for 6 entity tags: Sequence, Cell, Protein, Gene, Taxon, and Chemical from the [CRAFT](https://github.com/UCDenver-ccp/CRAFT/releases)(Colorado Richly Annotated Full Text) Corpus in English. 
Entity tags have been normalized and replaced from the original three letter code to a full name e.g. B-Protein, I-Chemical.

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
| 0.11          | 1.0   | 1360 | 0.1668          | 0.7952    | 0.7917 | 0.7934 | 0.9611   |
| 0.0484        | 2.0   | 2720 | 0.1640          | 0.8224    | 0.8371 | 0.8297 | 0.9661   |
| 0.0261        | 3.0   | 4080 | 0.1812          | 0.8143    | 0.8447 | 0.8292 | 0.9662   |
| 0.0112        | 4.0   | 5440 | 0.1878          | 0.8397    | 0.8366 | 0.8382 | 0.9683   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.11.6

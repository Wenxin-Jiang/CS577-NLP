---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Biobert-base-cased-v1.2-finetuned-ner-CRAFT_es_en
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Biobert-base-cased-v1.2-finetuned-ner-CRAFT_es_en

This model is a fine-tuned version of [dmis-lab/biobert-base-cased-v1.2](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2) on the CRAFT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1811
- Precision: 0.8555
- Recall: 0.8539
- F1: 0.8547
- Accuracy: 0.9706

## Model description

This model performs Named Entity Recognition for 6 entity tags: Sequence, Cell, Protein, Gene, Taxon, and Chemical from the [CRAFT](https://github.com/UCDenver-ccp/CRAFT/releases)(Colorado Richly Annotated Full Text) Corpus in Spanish and English. 
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
| 0.052         | 1.0   | 1360 | 0.1413          | 0.8300    | 0.8442 | 0.8370 | 0.9677   |
| 0.0199        | 2.0   | 2720 | 0.1673          | 0.8461    | 0.8458 | 0.8459 | 0.9689   |
| 0.011         | 3.0   | 4080 | 0.1647          | 0.8588    | 0.8528 | 0.8558 | 0.9704   |
| 0.0031        | 4.0   | 5440 | 0.1811          | 0.8555    | 0.8539 | 0.8547 | 0.9706   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.11.6

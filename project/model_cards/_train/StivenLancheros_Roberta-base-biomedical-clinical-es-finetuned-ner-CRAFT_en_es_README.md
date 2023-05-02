---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_en_es
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_en_es

This model is a fine-tuned version of [PlanTL-GOB-ES/roberta-base-biomedical-clinical-es](https://huggingface.co/PlanTL-GOB-ES/roberta-base-biomedical-clinical-es) on the CRAFT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1750
- Precision: 0.8664
- Recall: 0.8587
- F1: 0.8625
- Accuracy: 0.9727

## Model description

This model performs Named Entity Recognition for 6 entity tags: Sequence, Cell, Protein, Gene, Taxon, and Chemical from the [CRAFT](https://github.com/UCDenver-ccp/CRAFT/releases)(Colorado Richly Annotated Full Text) Corpus in Spanish and English. 
Entity tags have been normalized and replaced from the original three letter code to a full name e.g. B-Protein, I-Chemical.

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed



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
| 0.0564        | 1.0   | 1360 | 0.1459          | 0.8296    | 0.8489 | 0.8392 | 0.9696   |
| 0.0222        | 2.0   | 2720 | 0.1554          | 0.8650    | 0.8320 | 0.8482 | 0.9702   |
| 0.0124        | 3.0   | 4080 | 0.1670          | 0.8588    | 0.8564 | 0.8576 | 0.9717   |
| 0.0052        | 4.0   | 5440 | 0.1750          | 0.8664    | 0.8587 | 0.8625 | 0.9727   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.11.6

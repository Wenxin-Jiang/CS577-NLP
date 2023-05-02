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
- name: roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT

This model is a fine-tuned version of [PlanTL-GOB-ES/roberta-base-biomedical-clinical-es](https://huggingface.co/PlanTL-GOB-ES/roberta-base-biomedical-clinical-es) on the CRAFT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1720
- Precision: 0.8253
- Recall: 0.8147
- F1: 0.8200
- Accuracy: 0.9660

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
| 0.1133        | 1.0   | 1360 | 0.1629          | 0.7985    | 0.7782 | 0.7882 | 0.9610   |
| 0.049         | 2.0   | 2720 | 0.1530          | 0.8165    | 0.8084 | 0.8124 | 0.9651   |
| 0.0306        | 3.0   | 4080 | 0.1603          | 0.8198    | 0.8075 | 0.8136 | 0.9650   |
| 0.0158        | 4.0   | 5440 | 0.1720          | 0.8253    | 0.8147 | 0.8200 | 0.9660   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.6

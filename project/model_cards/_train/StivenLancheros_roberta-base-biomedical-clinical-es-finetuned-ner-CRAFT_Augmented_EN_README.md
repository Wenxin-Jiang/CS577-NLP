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
- name: roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_Augmented_EN
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_Augmented_EN

This model is a fine-tuned version of [PlanTL-GOB-ES/roberta-base-biomedical-clinical-es](https://huggingface.co/PlanTL-GOB-ES/roberta-base-biomedical-clinical-es) on the CRAFT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2276
- Precision: 0.8078
- Recall: 0.8258
- F1: 0.8167
- Accuracy: 0.9629

## Model description

This model performs Named Entity Recognition for 6 entity tags: Sequence, Cell, Protein, Gene, Taxon, and Chemical from the CRAFT(Colorado Richly Annotated Full Text) Corpus in English. Entity tags have been normalized and replaced from the original three letter code to a full name e.g. B-Protein, I-Chemical. This model is trained on augmented data created using Entity Replacement. 20% of the entities were replaced using a list of entities for each entity tag obtained from the official ontologies for each entity class. Both datasets (original, augmented) were concatenated.

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

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0842        | 1.0   | 2719  | 0.1765          | 0.7606    | 0.7785 | 0.7695 | 0.9542   |
| 0.0392        | 2.0   | 5438  | 0.1971          | 0.7990    | 0.7958 | 0.7974 | 0.9596   |
| 0.0138        | 3.0   | 8157  | 0.2094          | 0.8013    | 0.8196 | 0.8103 | 0.9620   |
| 0.0082        | 4.0   | 10876 | 0.2276          | 0.8078    | 0.8258 | 0.8167 | 0.9629   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

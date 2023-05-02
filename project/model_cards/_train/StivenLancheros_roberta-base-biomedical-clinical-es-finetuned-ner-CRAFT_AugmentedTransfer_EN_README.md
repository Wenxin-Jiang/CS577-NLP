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
- name: roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_AugmentedTransfer_EN
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_AugmentedTransfer_EN

This model is a fine-tuned version of [StivenLancheros/roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_Augmented_EN](https://huggingface.co/StivenLancheros/roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_Augmented_EN) on the CRAFT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2308
- Precision: 0.8366
- Recall: 0.8513
- F1: 0.8439
- Accuracy: 0.9681

## Model description

This model performs Named Entity Recognition for 6 entity tags: Sequence, Cell, Protein, Gene, Taxon, and Chemical from the CRAFT(Colorado Richly Annotated Full Text) Corpus in Spanish and English. Entity tags have been normalized and replaced from the original three letter code to a full name e.g. B-Protein, I-Chemical. This model is trained on augmented data created using Entity Replacement. 20% of the entities were replaced using a list of entities for each entity tag obtained from the official ontologies for each entity class. Both datasets (original, augmented) were concatenated. To improve F1 score the transfer learning was completed in two steps. Using [StivenLancheros/roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_Augmented_EN](https://huggingface.co/StivenLancheros/roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_Augmented_EN as a base model, I finetuned once more on the original CRAFT dataset in English.

Biobert --> Augmented CRAFT --> CRAFT

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
| 0.0129        | 1.0   | 1360 | 0.2119          | 0.8404    | 0.8364 | 0.8384 | 0.9666   |
| 0.0072        | 2.0   | 2720 | 0.2132          | 0.8173    | 0.8583 | 0.8373 | 0.9662   |
| 0.0042        | 3.0   | 4080 | 0.2180          | 0.8410    | 0.8515 | 0.8462 | 0.9686   |
| 0.0019        | 4.0   | 5440 | 0.2308          | 0.8366    | 0.8513 | 0.8439 | 0.9681   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

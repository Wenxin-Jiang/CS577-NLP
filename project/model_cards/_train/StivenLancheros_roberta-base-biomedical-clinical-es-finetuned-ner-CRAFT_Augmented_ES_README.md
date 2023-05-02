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
- name: roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_Augmented_ES
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_Augmented_ES

This model is a fine-tuned version of [PlanTL-GOB-ES/roberta-base-biomedical-clinical-es](https://huggingface.co/PlanTL-GOB-ES/roberta-base-biomedical-clinical-es) on the CRAFT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2224
- Precision: 0.8298
- Recall: 0.8306
- F1: 0.8302
- Accuracy: 0.9659

## Model description

This model performs Named Entity Recognition for 6 entity tags: Sequence, Cell, Protein, Gene, Taxon, and Chemical from the CRAFT(Colorado Richly Annotated Full Text) Corpus in English. Entity tags have been normalized and replaced from the original three letter code to a full name e.g. B-Protein, I-Chemical.

This model is trained on augmented data created using Entity Replacement. 20% of the entities were replaced using a list of entities for each entity tag obtained from the official ontologies for each entity class. Three datasets (original, augmented, MT translated CRAFT) were concatenated.

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
| 0.0624        | 1.0   | 4078  | 0.1844          | 0.8002    | 0.7923 | 0.7963 | 0.9607   |
| 0.0284        | 2.0   | 8156  | 0.1937          | 0.8394    | 0.7988 | 0.8186 | 0.9637   |
| 0.0118        | 3.0   | 12234 | 0.2007          | 0.8285    | 0.8232 | 0.8258 | 0.9649   |
| 0.0043        | 4.0   | 16312 | 0.2224          | 0.8298    | 0.8306 | 0.8302 | 0.9659   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

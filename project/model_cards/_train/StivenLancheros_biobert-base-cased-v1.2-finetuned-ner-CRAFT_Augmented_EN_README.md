---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: biobert-base-cased-v1.2-finetuned-ner-CRAFT_Augmented_EN
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-base-cased-v1.2-finetuned-ner-CRAFT_Augmented_EN

This model is a fine-tuned version of [dmis-lab/biobert-base-cased-v1.2](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2) on the CRAFT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2299
- Precision: 0.8122
- Recall: 0.8475
- F1: 0.8294
- Accuracy: 0.9661

## Model description

This model performs Named Entity Recognition for 6 entity tags: Sequence, Cell, Protein, Gene, Taxon, and Chemical from the CRAFT(Colorado Richly Annotated Full Text) Corpus in Spanish and English. Entity tags have been normalized and replaced from the original three letter code to a full name e.g. B-Protein, I-Chemical.
This model is trained on augmented data created using Entity Replacement. 20% of the entities were replaced using a list of entities for each entity tag obtained from the official ontologies for each entity class. Both datasets (original, augmented) were concatenated.

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
| 0.0542        | 1.0   | 2719  | 0.1540          | 0.7834    | 0.8300 | 0.8060 | 0.9622   |
| 0.0229        | 2.0   | 5438  | 0.1920          | 0.8092    | 0.8219 | 0.8155 | 0.9644   |
| 0.0069        | 3.0   | 8157  | 0.2054          | 0.8130    | 0.8481 | 0.8302 | 0.9656   |
| 0.0023        | 4.0   | 10876 | 0.2299          | 0.8122    | 0.8475 | 0.8294 | 0.9661   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

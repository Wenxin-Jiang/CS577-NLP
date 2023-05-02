---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: biobert-base-cased-v1.2-finetuned-ner-CRAFT_Augmented_ES
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-base-cased-v1.2-finetuned-ner-CRAFT_Augmented_ES

This model is a fine-tuned version of [dmis-lab/biobert-base-cased-v1.2](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2) on the CRAFT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2251
- Precision: 0.8276
- Recall: 0.8411
- F1: 0.8343
- Accuracy: 0.9676

## Model description

This model performs Named Entity Recognition for 6 entity tags: Sequence, Cell, Protein, Gene, Taxon, and Chemical from the CRAFT(Colorado Richly Annotated Full Text) Corpus in Spanish (MT translated) and English. Entity tags have been normalized and replaced from the original three letter code to a full name e.g. B-Protein, I-Chemical.

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
| 0.0549        | 1.0   | 4078  | 0.1673          | 0.8056    | 0.8112 | 0.8084 | 0.9640   |
| 0.0233        | 2.0   | 8156  | 0.1733          | 0.8321    | 0.8244 | 0.8283 | 0.9662   |
| 0.0101        | 3.0   | 12234 | 0.1972          | 0.8336    | 0.8391 | 0.8363 | 0.9678   |
| 0.0036        | 4.0   | 16312 | 0.2251          | 0.8276    | 0.8411 | 0.8343 | 0.9676   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

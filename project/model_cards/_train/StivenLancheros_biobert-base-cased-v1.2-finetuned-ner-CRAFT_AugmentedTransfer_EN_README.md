---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: biobert-base-cased-v1.2-finetuned-ner-CRAFT_AugmentedTransfer_EN
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-base-cased-v1.2-finetuned-ner-CRAFT_AugmentedTransfer_EN

This model is a fine-tuned version of [StivenLancheros/biobert-base-cased-v1.2-finetuned-ner-CRAFT_Augmented_EN](https://huggingface.co/StivenLancheros/biobert-base-cased-v1.2-finetuned-ner-CRAFT_Augmented_EN) on the CRAFTone dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2213
- Precision: 0.8528
- Recall: 0.8617
- F1: 0.8572
- Accuracy: 0.9709

## Model description

This model performs Named Entity Recognition for 6 entity tags: Sequence, Cell, Protein, Gene, Taxon, and Chemical from the CRAFT(Colorado Richly Annotated Full Text) Corpus in Spanish and English. Entity tags have been normalized and replaced from the original three letter code to a full name e.g. B-Protein, I-Chemical.
This model is trained on augmented data created using Entity Replacement. 20% of the entities were replaced using a list of entities for each entity tag obtained from the official ontologies for each entity class. Both datasets (original, augmented) were concatenated.
To improve F1 score the transfer learning was completed in two steps. 
Using [StivenLancheros/biobert-base-cased-v1.2-finetuned-ner-CRAFT_Augmented_EN](https://huggingface.co/StivenLancheros/biobert-base-cased-v1.2-finetuned-ner-CRAFT_Augmented_EN) as a base model, I finetuned once more on the original CRAFT dataset in English.

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
| 0.0106        | 1.0   | 1360 | 0.1866          | 0.8343    | 0.8661 | 0.8499 | 0.9698   |
| 0.0063        | 2.0   | 2720 | 0.2100          | 0.8536    | 0.8537 | 0.8537 | 0.9701   |
| 0.0031        | 3.0   | 4080 | 0.2133          | 0.8506    | 0.8578 | 0.8542 | 0.9705   |
| 0.0008        | 4.0   | 5440 | 0.2213          | 0.8528    | 0.8617 | 0.8572 | 0.9709   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

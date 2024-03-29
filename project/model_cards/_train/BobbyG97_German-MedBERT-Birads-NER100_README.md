---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: German-MedBERT-Birads-NER
  results: []
widget:
- text: "Beurteilung  Mammographisch beidseits kein Anhalt für Malignität.  Links ACR-Typ d.  Rechts BIRADS 4. Links BIRADS 1."
  example_title: "NER Example"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# German-MedBERT-Birads-NER

This model is a fine-tuned version of [smanjil/German-MedBERT](https://huggingface.co/smanjil/German-MedBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0617
- Precision: 0.5
- Recall: 0.6667
- F1: 0.5714
- Accuracy: 0.9987

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 10   | 0.0125          | 1.0       | 1.0    | 1.0    | 1.0      |
| No log        | 2.0   | 20   | 0.0718          | 0.5       | 0.6667 | 0.5714 | 0.9987   |
| No log        | 3.0   | 30   | 0.0617          | 0.5       | 0.6667 | 0.5714 | 0.9987   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

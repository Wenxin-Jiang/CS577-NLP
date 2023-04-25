---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: biobert-base-cased-v1.2-finetuned-ner-Concat_CRAFT_es
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-base-cased-v1.2-finetuned-ner-Concat_CRAFT_es

This model is a fine-tuned version of [dmis-lab/biobert-base-cased-v1.2](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2079
- Precision: 0.8487
- Recall: 0.8443
- F1: 0.8465
- Accuracy: 0.9693

## Model description

More information needed

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
| 0.0698        | 1.0   | 2719  | 0.1463          | 0.8132    | 0.8233 | 0.8182 | 0.9643   |
| 0.0321        | 2.0   | 5438  | 0.1612          | 0.8321    | 0.8463 | 0.8392 | 0.9681   |
| 0.0154        | 3.0   | 8157  | 0.1832          | 0.8448    | 0.8404 | 0.8426 | 0.9683   |
| 0.0058        | 4.0   | 10876 | 0.2079          | 0.8487    | 0.8443 | 0.8465 | 0.9693   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.11.6

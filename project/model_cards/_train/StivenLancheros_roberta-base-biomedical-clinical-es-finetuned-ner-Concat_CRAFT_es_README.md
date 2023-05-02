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
- name: roberta-base-biomedical-clinical-es-finetuned-ner-Concat_CRAFT_es
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-biomedical-clinical-es-finetuned-ner-Concat_CRAFT_es

This model is a fine-tuned version of [PlanTL-GOB-ES/roberta-base-biomedical-clinical-es](https://huggingface.co/PlanTL-GOB-ES/roberta-base-biomedical-clinical-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1874
- Precision: 0.8559
- Recall: 0.8425
- F1: 0.8492
- Accuracy: 0.9696

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
| 0.072         | 1.0   | 2719  | 0.1500          | 0.8138    | 0.8224 | 0.8181 | 0.9644   |
| 0.0305        | 2.0   | 5438  | 0.1555          | 0.8417    | 0.8253 | 0.8334 | 0.9674   |
| 0.014         | 3.0   | 8157  | 0.1743          | 0.8429    | 0.8412 | 0.8421 | 0.9685   |
| 0.0076        | 4.0   | 10876 | 0.1874          | 0.8559    | 0.8425 | 0.8492 | 0.9696   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.11.6

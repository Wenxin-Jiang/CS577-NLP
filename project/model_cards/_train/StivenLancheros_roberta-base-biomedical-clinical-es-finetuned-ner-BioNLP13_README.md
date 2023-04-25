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
- name: roberta-base-biomedical-clinical-es-finetuned-ner-BioNLP13
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-biomedical-clinical-es-finetuned-ner-BioNLP13

This model is a fine-tuned version of [PlanTL-GOB-ES/roberta-base-biomedical-clinical-es](https://huggingface.co/PlanTL-GOB-ES/roberta-base-biomedical-clinical-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2217
- Precision: 0.7936
- Recall: 0.8067
- F1: 0.8001
- Accuracy: 0.9451

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.4206        | 1.0   | 692  | 0.2182          | 0.7513    | 0.7757 | 0.7633 | 0.9342   |
| 0.1872        | 2.0   | 1384 | 0.2032          | 0.7779    | 0.7865 | 0.7821 | 0.9398   |
| 0.0982        | 3.0   | 2076 | 0.2043          | 0.7995    | 0.7904 | 0.7949 | 0.9443   |
| 0.0735        | 4.0   | 2768 | 0.2217          | 0.7936    | 0.8067 | 0.8001 | 0.9451   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0

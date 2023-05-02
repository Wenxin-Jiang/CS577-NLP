---
license: mit
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: xlm-roberta-base-finetuned-ner-false-finetuned-ner-2002
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.941186271242919
    - name: Recall
      type: recall
      value: 0.9506900033658701
    - name: F1
      type: f1
      value: 0.945914266577361
    - name: Accuracy
      type: accuracy
      value: 0.9904209337642615
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-ner-false-finetuned-ner-2002

This model is a fine-tuned version of [StivenLancheros/xlm-roberta-base-finetuned-ner-false](https://huggingface.co/StivenLancheros/xlm-roberta-base-finetuned-ner-false) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0725
- Precision: 0.9412
- Recall: 0.9507
- F1: 0.9459
- Accuracy: 0.9904

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.086         | 1.0   | 7021  | 0.0709          | 0.9221    | 0.9261 | 0.9241 | 0.9872   |
| 0.0352        | 2.0   | 14042 | 0.0871          | 0.9243    | 0.9354 | 0.9298 | 0.9879   |
| 0.0203        | 3.0   | 21063 | 0.0747          | 0.9398    | 0.9490 | 0.9444 | 0.9901   |
| 0.0184        | 4.0   | 28084 | 0.0725          | 0.9412    | 0.9507 | 0.9459 | 0.9904   |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3

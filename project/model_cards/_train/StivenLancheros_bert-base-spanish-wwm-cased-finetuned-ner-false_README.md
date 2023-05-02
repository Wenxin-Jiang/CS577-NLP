---
tags:
- generated_from_trainer
datasets:
- conll2002
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-base-spanish-wwm-cased-finetuned-ner-false
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2002
      type: conll2002
      args: es
    metrics:
    - name: Precision
      type: precision
      value: 0.8527941844616084
    - name: Recall
      type: recall
      value: 0.8625919117647058
    - name: F1
      type: f1
      value: 0.8576650673977612
    - name: Accuracy
      type: accuracy
      value: 0.9780246773614496
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-spanish-wwm-cased-finetuned-ner-false

This model is a fine-tuned version of [dccuchile/bert-base-spanish-wwm-cased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) on the conll2002 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1154
- Precision: 0.8528
- Recall: 0.8626
- F1: 0.8577
- Accuracy: 0.9780

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
- train_batch_size: 10
- eval_batch_size: 10
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1072        | 1.0   | 833  | 0.0905          | 0.8432    | 0.8451 | 0.8442 | 0.9779   |
| 0.0347        | 2.0   | 1666 | 0.0934          | 0.8592    | 0.8612 | 0.8602 | 0.9782   |
| 0.0218        | 3.0   | 2499 | 0.1078          | 0.8537    | 0.8568 | 0.8553 | 0.9776   |
| 0.0106        | 4.0   | 3332 | 0.1154          | 0.8528    | 0.8626 | 0.8577 | 0.9780   |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3

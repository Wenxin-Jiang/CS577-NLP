---
license: gpl-3.0
tags:
- generated_from_trainer
datasets:
- mim_gold_ner
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: IceBERT-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: mim_gold_ner
      type: mim_gold_ner
      args: mim-gold-ner
    metrics:
    - name: Precision
      type: precision
      value: 0.8927335640138409
    - name: Recall
      type: recall
      value: 0.8631855657784682
    - name: F1
      type: f1
      value: 0.8777109531620194
    - name: Accuracy
      type: accuracy
      value: 0.9849836396073506
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# IceBERT-finetuned-ner

This model is a fine-tuned version of [vesteinn/IceBERT](https://huggingface.co/vesteinn/IceBERT) on the mim_gold_ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0807
- Precision: 0.8927
- Recall: 0.8632
- F1: 0.8777
- Accuracy: 0.9850

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0544        | 1.0   | 2904 | 0.0774          | 0.8859    | 0.8490 | 0.8670 | 0.9833   |
| 0.0284        | 2.0   | 5808 | 0.0781          | 0.8709    | 0.8590 | 0.8649 | 0.9840   |
| 0.0166        | 3.0   | 8712 | 0.0807          | 0.8927    | 0.8632 | 0.8777 | 0.9850   |


### Framework versions

- Transformers 4.11.2
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3

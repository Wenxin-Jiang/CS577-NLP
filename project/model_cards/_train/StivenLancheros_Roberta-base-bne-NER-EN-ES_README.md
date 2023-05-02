---
license: apache-2.0
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
- name: roberta-base-bne-finetuned-ner-finetuned2-ner
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
      value: 0.8697727272727273
    - name: Recall
      type: recall
      value: 0.8793658088235294
    - name: F1
      type: f1
      value: 0.8745429616087752
    - name: Accuracy
      type: accuracy
      value: 0.9808778791829639
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-bne-finetuned-ner-finetuned2-ner

This model is a fine-tuned version of [StivenLancheros/roberta-base-bne-finetuned-ner](https://huggingface.co/StivenLancheros/roberta-base-bne-finetuned-ner) on the conll2002 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1067
- Precision: 0.8698
- Recall: 0.8794
- F1: 0.8745
- Accuracy: 0.9809

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
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0582        | 1.0   | 1665 | 0.0852          | 0.8697    | 0.8759 | 0.8728 | 0.9800   |
| 0.0297        | 2.0   | 3330 | 0.0919          | 0.8841    | 0.8867 | 0.8854 | 0.9817   |
| 0.0121        | 3.0   | 4995 | 0.0950          | 0.8751    | 0.8807 | 0.8779 | 0.9812   |
| 0.0056        | 4.0   | 6660 | 0.1067          | 0.8698    | 0.8794 | 0.8745 | 0.9809   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.10.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3

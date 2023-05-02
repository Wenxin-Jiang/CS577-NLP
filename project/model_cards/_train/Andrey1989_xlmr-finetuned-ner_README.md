---
license: mit
tags:
- generated_from_trainer
datasets:
- wikiann
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: xlmr-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikiann
      type: wikiann
      args: et
    metrics:
    - name: Precision
      type: precision
      value: 0.9044097027481772
    - name: Recall
      type: recall
      value: 0.9136978539556626
    - name: F1
      type: f1
      value: 0.9090300532008596
    - name: Accuracy
      type: accuracy
      value: 0.9649304793632428
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlmr-finetuned-ner

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1395
- Precision: 0.9044
- Recall: 0.9137
- F1: 0.9090
- Accuracy: 0.9649

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
| 0.4215        | 1.0   | 938  | 0.1650          | 0.8822    | 0.8781 | 0.8802 | 0.9529   |
| 0.1559        | 2.0   | 1876 | 0.1412          | 0.9018    | 0.9071 | 0.9045 | 0.9631   |
| 0.1051        | 3.0   | 2814 | 0.1395          | 0.9044    | 0.9137 | 0.9090 | 0.9649   |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

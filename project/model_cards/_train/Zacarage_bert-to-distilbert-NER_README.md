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
- name: bert-to-distilbert-NER
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.014729299363057325
    - name: Recall
      type: recall
      value: 0.018680578929653316
    - name: F1
      type: f1
      value: 0.016471286541029827
    - name: Accuracy
      type: accuracy
      value: 0.7599340672278802
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-to-distilbert-NER

This model is a fine-tuned version of [dslim/bert-base-NER](https://huggingface.co/dslim/bert-base-NER) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 43.2398
- Precision: 0.0147
- Recall: 0.0187
- F1: 0.0165
- Accuracy: 0.7599

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-05
- train_batch_size: 128
- eval_batch_size: 128
- seed: 33
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 190.2685      | 1.0   | 110  | 127.2351        | 0.0157    | 0.0098 | 0.0120 | 0.7569   |
| 105.4389      | 2.0   | 220  | 97.1100         | 0.0281    | 0.0298 | 0.0289 | 0.7587   |
| 77.0337       | 3.0   | 330  | 76.9433         | 0.0136    | 0.0173 | 0.0152 | 0.7615   |
| 60.3477       | 4.0   | 440  | 65.9181         | 0.0130    | 0.0158 | 0.0143 | 0.7603   |
| 50.4086       | 5.0   | 550  | 58.5255         | 0.0170    | 0.0220 | 0.0192 | 0.7603   |
| 43.298        | 6.0   | 660  | 54.5405         | 0.0144    | 0.0187 | 0.0163 | 0.7594   |
| 39.0911       | 7.0   | 770  | 52.4767         | 0.0155    | 0.0195 | 0.0172 | 0.7613   |
| 35.07         | 8.0   | 880  | 49.1975         | 0.0170    | 0.0219 | 0.0192 | 0.7602   |
| 32.215        | 9.0   | 990  | 47.4422         | 0.0144    | 0.0187 | 0.0163 | 0.7599   |
| 29.9923       | 10.0  | 1100 | 46.5558         | 0.0167    | 0.0212 | 0.0187 | 0.7606   |
| 28.3599       | 11.0  | 1210 | 45.6301         | 0.0171    | 0.0214 | 0.0190 | 0.7613   |
| 26.8163       | 12.0  | 1320 | 45.0483         | 0.0141    | 0.0177 | 0.0157 | 0.7606   |
| 25.7434       | 13.0  | 1430 | 44.0639         | 0.0176    | 0.0222 | 0.0196 | 0.7605   |
| 24.9853       | 14.0  | 1540 | 43.6618         | 0.0148    | 0.0187 | 0.0165 | 0.7606   |
| 24.3179       | 15.0  | 1650 | 43.2398         | 0.0147    | 0.0187 | 0.0165 | 0.7599   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

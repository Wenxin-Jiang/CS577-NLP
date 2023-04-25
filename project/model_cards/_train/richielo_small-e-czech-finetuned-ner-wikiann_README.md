---
license: cc-by-4.0
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
- name: small-e-czech-finetuned-ner-wikiann
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikiann
      type: wikiann
      args: cs
    metrics:
    - name: Precision
      type: precision
      value: 0.8713322894683097
    - name: Recall
      type: recall
      value: 0.8970423324922905
    - name: F1
      type: f1
      value: 0.8840004144075699
    - name: Accuracy
      type: accuracy
      value: 0.9557089381093997
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# small-e-czech-finetuned-ner-wikiann

This model is a fine-tuned version of [Seznam/small-e-czech](https://huggingface.co/Seznam/small-e-czech) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2547
- Precision: 0.8713
- Recall: 0.8970
- F1: 0.8840
- Accuracy: 0.9557

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2924        | 1.0   | 2500  | 0.2449          | 0.7686    | 0.8088 | 0.7882 | 0.9320   |
| 0.2042        | 2.0   | 5000  | 0.2137          | 0.8050    | 0.8398 | 0.8220 | 0.9400   |
| 0.1699        | 3.0   | 7500  | 0.1912          | 0.8236    | 0.8593 | 0.8411 | 0.9466   |
| 0.1419        | 4.0   | 10000 | 0.1931          | 0.8349    | 0.8671 | 0.8507 | 0.9488   |
| 0.1316        | 5.0   | 12500 | 0.1892          | 0.8470    | 0.8776 | 0.8620 | 0.9519   |
| 0.1042        | 6.0   | 15000 | 0.2058          | 0.8433    | 0.8811 | 0.8618 | 0.9508   |
| 0.0884        | 7.0   | 17500 | 0.2020          | 0.8602    | 0.8849 | 0.8724 | 0.9531   |
| 0.0902        | 8.0   | 20000 | 0.2118          | 0.8551    | 0.8837 | 0.8692 | 0.9528   |
| 0.0669        | 9.0   | 22500 | 0.2171          | 0.8634    | 0.8906 | 0.8768 | 0.9550   |
| 0.0529        | 10.0  | 25000 | 0.2228          | 0.8638    | 0.8912 | 0.8773 | 0.9545   |
| 0.0613        | 11.0  | 27500 | 0.2293          | 0.8626    | 0.8898 | 0.8760 | 0.9544   |
| 0.0549        | 12.0  | 30000 | 0.2276          | 0.8694    | 0.8958 | 0.8824 | 0.9554   |
| 0.0516        | 13.0  | 32500 | 0.2384          | 0.8717    | 0.8940 | 0.8827 | 0.9552   |
| 0.0412        | 14.0  | 35000 | 0.2443          | 0.8701    | 0.8931 | 0.8815 | 0.9554   |
| 0.0345        | 15.0  | 37500 | 0.2464          | 0.8723    | 0.8958 | 0.8839 | 0.9557   |
| 0.0412        | 16.0  | 40000 | 0.2477          | 0.8705    | 0.8948 | 0.8825 | 0.9552   |
| 0.0363        | 17.0  | 42500 | 0.2525          | 0.8742    | 0.8973 | 0.8856 | 0.9559   |
| 0.0341        | 18.0  | 45000 | 0.2529          | 0.8727    | 0.8962 | 0.8843 | 0.9561   |
| 0.0194        | 19.0  | 47500 | 0.2533          | 0.8699    | 0.8966 | 0.8830 | 0.9557   |
| 0.0247        | 20.0  | 50000 | 0.2547          | 0.8713    | 0.8970 | 0.8840 | 0.9557   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.11.6

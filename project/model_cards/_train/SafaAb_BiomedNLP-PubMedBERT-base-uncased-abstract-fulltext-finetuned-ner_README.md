---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext-finetuned-ner

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) fine tuned on the CORD-19 dataset.
It achieves the following results on the evaluation set:
- Accuracy: 0.8988
- Loss: 0.4018
- Precision: 0.63
- Recall: 0.4701
- F1: 0.5385


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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 4    | 0.4300          | 0.6667    | 0.3134 | 0.4264 | 0.8774   |
| No log        | 2.0   | 8    | 0.4085          | 0.7442    | 0.2388 | 0.3616 | 0.8703   |
| No log        | 3.0   | 12   | 0.3942          | 0.7273    | 0.2388 | 0.3596 | 0.8686   |
| No log        | 4.0   | 16   | 0.3650          | 0.6712    | 0.3657 | 0.4734 | 0.8828   |
| No log        | 5.0   | 20   | 0.4018          | 0.7234    | 0.2537 | 0.3757 | 0.8739   |
| No log        | 6.0   | 24   | 0.3835          | 0.7188    | 0.3433 | 0.4646 | 0.8881   |
| No log        | 7.0   | 28   | 0.3521          | 0.6277    | 0.4403 | 0.5175 | 0.8952   |
| No log        | 8.0   | 32   | 0.3612          | 0.6047    | 0.3881 | 0.4727 | 0.8917   |
| No log        | 9.0   | 36   | 0.3660          | 0.6118    | 0.3881 | 0.4749 | 0.8917   |
| No log        | 10.0  | 40   | 0.3585          | 0.5660    | 0.4478 | 0.5    | 0.8917   |
| No log        | 11.0  | 44   | 0.3781          | 0.5745    | 0.4030 | 0.4737 | 0.8917   |
| No log        | 12.0  | 48   | 0.3847          | 0.5816    | 0.4254 | 0.4914 | 0.8934   |
| No log        | 13.0  | 52   | 0.3799          | 0.5962    | 0.4627 | 0.5210 | 0.8934   |
| No log        | 14.0  | 56   | 0.3804          | 0.6038    | 0.4776 | 0.5333 | 0.8952   |
| No log        | 15.0  | 60   | 0.3894          | 0.6154    | 0.4776 | 0.5378 | 0.8970   |
| No log        | 16.0  | 64   | 0.3841          | 0.6038    | 0.4776 | 0.5333 | 0.8952   |
| No log        | 17.0  | 68   | 0.3876          | 0.6095    | 0.4776 | 0.5356 | 0.8988   |
| No log        | 18.0  | 72   | 0.3945          | 0.6154    | 0.4776 | 0.5378 | 0.8970   |
| No log        | 19.0  | 76   | 0.4000          | 0.6275    | 0.4776 | 0.5424 | 0.8988   |
| No log        | 20.0  | 80   | 0.4018          | 0.63      | 0.4701 | 0.5385 | 0.8988   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

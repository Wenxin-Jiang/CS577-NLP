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
- name: bert-finetuned-mutation-recognition-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-mutation-recognition-3

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0727
- Dnamutation F1: 0.6484
- Proteinmutation F1: 0.8571
- Snp F1: 1.0
- Precision: 0.7966
- Recall: 0.7625
- F1: 0.7792
- Accuracy: 0.9872

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Dnamutation F1 | Proteinmutation F1 | Snp F1 | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:------------------:|:------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 324  | 0.0323          | 0.5996         | 0.7886             | 1.0    | 0.6583    | 0.7982 | 0.7215 | 0.9901   |
| 0.0788        | 2.0   | 648  | 0.0314          | 0.6765         | 0.8783             | 1.0    | 0.7453    | 0.8571 | 0.7973 | 0.9907   |
| 0.0788        | 3.0   | 972  | 0.0306          | 0.6391         | 0.8679             | 1.0    | 0.7341    | 0.8232 | 0.7761 | 0.9903   |
| 0.0273        | 4.0   | 1296 | 0.0424          | 0.6360         | 0.8714             | 1.0    | 0.7792    | 0.775  | 0.7771 | 0.9885   |
| 0.0178        | 5.0   | 1620 | 0.0462          | 0.5885         | 0.8683             | 1.0    | 0.7576    | 0.7589 | 0.7583 | 0.9869   |
| 0.0178        | 6.0   | 1944 | 0.0531          | 0.6176         | 0.8701             | 1.0    | 0.7734    | 0.7679 | 0.7706 | 0.9873   |
| 0.0165        | 7.0   | 2268 | 0.0573          | 0.6597         | 0.8658             | 1.0    | 0.8022    | 0.775  | 0.7884 | 0.9881   |
| 0.0144        | 8.0   | 2592 | 0.0636          | 0.6596         | 0.8454             | 1.0    | 0.7919    | 0.7679 | 0.7797 | 0.9871   |
| 0.0144        | 9.0   | 2916 | 0.0710          | 0.6568         | 0.8748             | 1.0    | 0.8159    | 0.7679 | 0.7912 | 0.9872   |
| 0.0108        | 10.0  | 3240 | 0.0727          | 0.6484         | 0.8571             | 1.0    | 0.7966    | 0.7625 | 0.7792 | 0.9872   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2
- Datasets 2.0.0
- Tokenizers 0.12.1

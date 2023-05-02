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
- name: bert-finetuned-mutation-recognition-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-mutation-recognition-1

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0380
- Proteinmutation F1: 0.8631
- Dnamutation F1: 0.7522
- Snp F1: 1.0
- Precision: 0.8061
- Recall: 0.8386
- F1: 0.8221
- Accuracy: 0.9942

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

| Training Loss | Epoch | Step | Validation Loss | Proteinmutation F1 | Dnamutation F1 | Snp F1 | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------------------:|:--------------:|:------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 259  | 0.0273          | 0.8072             | 0.5762         | 0.975  | 0.6685    | 0.7580 | 0.7104 | 0.9924   |
| 0.0597        | 2.0   | 518  | 0.0260          | 0.8148             | 0.6864         | 0.9873 | 0.7363    | 0.8004 | 0.7670 | 0.9936   |
| 0.0597        | 3.0   | 777  | 0.0338          | 0.8252             | 0.7221         | 1.0    | 0.7857    | 0.7941 | 0.7899 | 0.9935   |
| 0.0046        | 4.0   | 1036 | 0.0299          | 0.8707             | 0.7214         | 0.9873 | 0.7773    | 0.8450 | 0.8098 | 0.9941   |
| 0.0046        | 5.0   | 1295 | 0.0353          | 0.9035             | 0.7364         | 0.9873 | 0.8130    | 0.8493 | 0.8307 | 0.9941   |
| 0.0014        | 6.0   | 1554 | 0.0361          | 0.8941             | 0.7391         | 0.9873 | 0.8093    | 0.8471 | 0.8278 | 0.9941   |
| 0.0014        | 7.0   | 1813 | 0.0367          | 0.8957             | 0.7249         | 1.0    | 0.8090    | 0.8365 | 0.8225 | 0.9940   |
| 0.0004        | 8.0   | 2072 | 0.0381          | 0.8714             | 0.7578         | 1.0    | 0.8266    | 0.8301 | 0.8284 | 0.9940   |
| 0.0004        | 9.0   | 2331 | 0.0380          | 0.8732             | 0.7550         | 1.0    | 0.8148    | 0.8408 | 0.8276 | 0.9942   |
| 0.0002        | 10.0  | 2590 | 0.0380          | 0.8631             | 0.7522         | 1.0    | 0.8061    | 0.8386 | 0.8221 | 0.9942   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2
- Datasets 2.0.0
- Tokenizers 0.12.1

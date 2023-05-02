---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
model-index:
- name: bert-base-uncased-finetuned-math_punctuation-ignore_word_parts
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-math_punctuation-ignore_word_parts

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1981
- Precision: 0.7843
- Recall: 0.7485
- F Score: 0.7648
- Auc: 0.9248

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F Score | Auc    |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:-------:|:------:|
| 0.1064        | 0.64  | 500  | 0.1082          | 0.7558    | 0.6580 | 0.6964  | 0.9086 |
| 0.0781        | 1.27  | 1000 | 0.1025          | 0.7594    | 0.7226 | 0.7365  | 0.9261 |
| 0.0757        | 1.91  | 1500 | 0.1001          | 0.7945    | 0.6899 | 0.7302  | 0.9272 |
| 0.0538        | 2.54  | 2000 | 0.1061          | 0.7689    | 0.7348 | 0.7480  | 0.9298 |
| 0.0425        | 3.18  | 2500 | 0.1123          | 0.7806    | 0.7361 | 0.7560  | 0.9300 |
| 0.0377        | 3.81  | 3000 | 0.1159          | 0.7841    | 0.7437 | 0.7610  | 0.9292 |
| 0.0235        | 4.45  | 3500 | 0.1259          | 0.7786    | 0.7368 | 0.7561  | 0.9276 |
| 0.0227        | 5.08  | 4000 | 0.1436          | 0.7699    | 0.7448 | 0.7555  | 0.9277 |
| 0.0159        | 5.72  | 4500 | 0.1466          | 0.7715    | 0.7333 | 0.7514  | 0.9252 |
| 0.0106        | 6.35  | 5000 | 0.1574          | 0.7710    | 0.7456 | 0.7566  | 0.9276 |
| 0.0111        | 6.99  | 5500 | 0.1560          | 0.7694    | 0.7500 | 0.7595  | 0.9286 |
| 0.0074        | 7.62  | 6000 | 0.1645          | 0.7789    | 0.7511 | 0.7639  | 0.9305 |
| 0.0056        | 8.26  | 6500 | 0.1745          | 0.7887    | 0.7453 | 0.7648  | 0.9265 |
| 0.005         | 8.89  | 7000 | 0.1760          | 0.7779    | 0.7497 | 0.7629  | 0.9281 |
| 0.0038        | 9.53  | 7500 | 0.1873          | 0.7826    | 0.7505 | 0.7634  | 0.9273 |
| 0.0031        | 10.17 | 8000 | 0.1896          | 0.7855    | 0.7477 | 0.7644  | 0.9258 |
| 0.0026        | 10.8  | 8500 | 0.1929          | 0.7849    | 0.7485 | 0.7650  | 0.9263 |
| 0.0017        | 11.44 | 9000 | 0.1981          | 0.7843    | 0.7485 | 0.7648  | 0.9248 |


### Framework versions

- Transformers 4.25.1
- Pytorch 2.0.0.dev20230111
- Datasets 2.8.0
- Tokenizers 0.13.2

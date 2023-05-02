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
- name: bert-base-multilingual-cased-finetuned-multilingual-pos
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-cased-finetuned-multilingual-pos

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1999
- Precision: 0.9438
- Recall: 0.9438
- F1: 0.9438
- Accuracy: 0.9541

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 1.0385        | 0.29  | 100  | 0.4411          | 0.8523    | 0.8473 | 0.8498 | 0.8739   |
| 0.3849        | 0.57  | 200  | 0.3275          | 0.8907    | 0.8913 | 0.8910 | 0.9103   |
| 0.2976        | 0.86  | 300  | 0.2879          | 0.9034    | 0.9037 | 0.9036 | 0.9203   |
| 0.2487        | 1.14  | 400  | 0.2599          | 0.9132    | 0.9115 | 0.9123 | 0.9285   |
| 0.2027        | 1.43  | 500  | 0.2444          | 0.9224    | 0.9198 | 0.9211 | 0.9349   |
| 0.1899        | 1.71  | 600  | 0.2287          | 0.9239    | 0.9246 | 0.9243 | 0.9378   |
| 0.18          | 2.0   | 700  | 0.2184          | 0.9282    | 0.9297 | 0.9289 | 0.9418   |
| 0.1351        | 2.29  | 800  | 0.2214          | 0.9297    | 0.9291 | 0.9294 | 0.9424   |
| 0.134         | 2.57  | 900  | 0.2123          | 0.9337    | 0.9333 | 0.9335 | 0.9458   |
| 0.1294        | 2.86  | 1000 | 0.1993          | 0.9359    | 0.9344 | 0.9352 | 0.9476   |
| 0.1156        | 3.14  | 1100 | 0.2018          | 0.9377    | 0.9377 | 0.9377 | 0.9494   |
| 0.1007        | 3.43  | 1200 | 0.2027          | 0.9375    | 0.9384 | 0.9380 | 0.9495   |
| 0.0959        | 3.71  | 1300 | 0.1971          | 0.9387    | 0.9394 | 0.9390 | 0.9505   |
| 0.0982        | 4.0   | 1400 | 0.1953          | 0.9408    | 0.9414 | 0.9411 | 0.9522   |
| 0.0761        | 4.29  | 1500 | 0.1987          | 0.9404    | 0.9412 | 0.9408 | 0.9517   |
| 0.0788        | 4.57  | 1600 | 0.1994          | 0.9405    | 0.9411 | 0.9408 | 0.9518   |
| 0.0755        | 4.86  | 1700 | 0.2009          | 0.9413    | 0.9420 | 0.9417 | 0.9525   |
| 0.0671        | 5.14  | 1800 | 0.2011          | 0.9421    | 0.9423 | 0.9422 | 0.9527   |
| 0.0636        | 5.43  | 1900 | 0.2002          | 0.9428    | 0.9431 | 0.9430 | 0.9532   |
| 0.0628        | 5.71  | 2000 | 0.1993          | 0.9422    | 0.9433 | 0.9428 | 0.9532   |
| 0.0645        | 6.0   | 2100 | 0.1979          | 0.9434    | 0.9430 | 0.9432 | 0.9536   |
| 0.0543        | 6.29  | 2200 | 0.2017          | 0.9427    | 0.9434 | 0.9430 | 0.9532   |
| 0.0558        | 6.57  | 2300 | 0.1992          | 0.9427    | 0.9432 | 0.9430 | 0.9534   |
| 0.0529        | 6.86  | 2400 | 0.1999          | 0.9438    | 0.9438 | 0.9438 | 0.9541   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1

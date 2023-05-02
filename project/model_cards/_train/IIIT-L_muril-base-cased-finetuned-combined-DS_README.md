---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: muril-base-cased-finetuned-combined-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# muril-base-cased-finetuned-combined-DS

This model is a fine-tuned version of [google/muril-base-cased](https://huggingface.co/google/muril-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5291
- Accuracy: 0.6657
- Precision: 0.6355
- Recall: 0.6275
- F1: 0.6294

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 25

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9961        | 2.0   | 711  | 0.9148          | 0.5625   | 0.5495    | 0.5636 | 0.5265 |
| 0.8211        | 3.99  | 1422 | 0.8542          | 0.6096   | 0.6023    | 0.6071 | 0.5928 |
| 0.6667        | 5.99  | 2133 | 0.8459          | 0.6601   | 0.6366    | 0.6379 | 0.6361 |
| 0.5272        | 7.99  | 2844 | 0.9667          | 0.6517   | 0.6190    | 0.6223 | 0.6201 |
| 0.4327        | 9.99  | 3555 | 1.0185          | 0.6503   | 0.6351    | 0.6222 | 0.6229 |
| 0.3608        | 11.98 | 4266 | 1.1409          | 0.6313   | 0.6053    | 0.6100 | 0.6049 |
| 0.3038        | 13.98 | 4977 | 1.2336          | 0.6601   | 0.6287    | 0.6269 | 0.6273 |
| 0.2631        | 15.98 | 5688 | 1.3151          | 0.6503   | 0.6199    | 0.6167 | 0.6177 |
| 0.2368        | 17.97 | 6399 | 1.4230          | 0.6594   | 0.6315    | 0.6233 | 0.6251 |
| 0.2093        | 19.97 | 7110 | 1.4881          | 0.6629   | 0.6332    | 0.6220 | 0.6239 |
| 0.1968        | 21.97 | 7821 | 1.5003          | 0.6559   | 0.6279    | 0.6230 | 0.6242 |
| 0.1824        | 23.97 | 8532 | 1.5291          | 0.6657   | 0.6355    | 0.6275 | 0.6294 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1

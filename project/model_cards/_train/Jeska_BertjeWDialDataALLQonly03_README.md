---
tags:
- generated_from_trainer
model-index:
- name: BertjeWDialDataALLQonly03
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BertjeWDialDataALLQonly03

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9995

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
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 24.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| No log        | 1.0   | 435   | 2.0751          |
| 2.1982        | 2.0   | 870   | 2.0465          |
| 2.0841        | 3.0   | 1305  | 2.0420          |
| 2.0374        | 4.0   | 1740  | 2.0325          |
| 1.9731        | 5.0   | 2175  | 2.0075          |
| 1.9248        | 6.0   | 2610  | 2.0219          |
| 1.8848        | 7.0   | 3045  | 1.9770          |
| 1.8848        | 8.0   | 3480  | 2.0093          |
| 1.8419        | 9.0   | 3915  | 2.0298          |
| 1.804         | 10.0  | 4350  | 1.9681          |
| 1.7817        | 11.0  | 4785  | 1.9938          |
| 1.7472        | 12.0  | 5220  | 1.9654          |
| 1.7075        | 13.0  | 5655  | 1.9797          |
| 1.6976        | 14.0  | 6090  | 1.9691          |
| 1.6748        | 15.0  | 6525  | 1.9568          |
| 1.6748        | 16.0  | 6960  | 1.9618          |
| 1.6528        | 17.0  | 7395  | 1.9843          |
| 1.6335        | 18.0  | 7830  | 1.9265          |
| 1.6179        | 19.0  | 8265  | 1.9598          |
| 1.5992        | 20.0  | 8700  | 1.9331          |
| 1.583         | 21.0  | 9135  | 1.9795          |
| 1.5699        | 22.0  | 9570  | 2.0073          |
| 1.5703        | 23.0  | 10005 | 1.9308          |
| 1.5703        | 24.0  | 10440 | 1.9285          |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3

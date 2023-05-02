---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-base-uncased-finetuned-detests-29-10-2022
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-detests-29-10-2022

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1346
- Accuracy: 0.7921

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2105        | 0.33  | 50   | 0.5718          | 0.8265   |
| 0.2156        | 0.65  | 100  | 0.5998          | 0.8232   |
| 0.215         | 0.98  | 150  | 0.5778          | 0.8232   |
| 0.1353        | 1.31  | 200  | 0.6240          | 0.8069   |
| 0.0664        | 1.63  | 250  | 0.7277          | 0.7938   |
| 0.2339        | 1.96  | 300  | 0.8471          | 0.7758   |
| 0.1518        | 2.29  | 350  | 0.9487          | 0.7938   |
| 0.0766        | 2.61  | 400  | 0.9715          | 0.8069   |
| 0.0524        | 2.94  | 450  | 1.0911          | 0.7610   |
| 0.0836        | 3.27  | 500  | 1.0099          | 0.8101   |
| 0.0935        | 3.59  | 550  | 0.9368          | 0.8020   |
| 0.1065        | 3.92  | 600  | 0.9528          | 0.8282   |
| 0.0139        | 4.25  | 650  | 1.0382          | 0.7971   |
| 0.0642        | 4.58  | 700  | 1.1667          | 0.7774   |
| 0.1584        | 4.9   | 750  | 1.1346          | 0.7921   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1

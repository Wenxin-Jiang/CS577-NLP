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
- name: correct_distilBERT_token_itr0_1e-05_webDiscourse_01_03_2022-15_40_24
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# correct_distilBERT_token_itr0_1e-05_webDiscourse_01_03_2022-15_40_24

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5794
- Precision: 0.0094
- Recall: 0.0147
- F1: 0.0115
- Accuracy: 0.7156

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
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 10   | 0.6319          | 0.08      | 0.0312 | 0.0449 | 0.6753   |
| No log        | 2.0   | 20   | 0.6265          | 0.0364    | 0.0312 | 0.0336 | 0.6764   |
| No log        | 3.0   | 30   | 0.6216          | 0.0351    | 0.0312 | 0.0331 | 0.6762   |
| No log        | 4.0   | 40   | 0.6193          | 0.0274    | 0.0312 | 0.0292 | 0.6759   |
| No log        | 5.0   | 50   | 0.6183          | 0.0222    | 0.0312 | 0.0260 | 0.6773   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

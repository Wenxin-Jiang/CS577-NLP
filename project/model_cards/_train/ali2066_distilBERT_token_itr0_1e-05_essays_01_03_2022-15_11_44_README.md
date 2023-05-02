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
- name: distilBERT_token_itr0_1e-05_essays_01_03_2022-15_11_44
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilBERT_token_itr0_1e-05_essays_01_03_2022-15_11_44

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3082
- Precision: 0.2796
- Recall: 0.4373
- F1: 0.3411
- Accuracy: 0.8887

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
| No log        | 1.0   | 11   | 0.5018          | 0.0192    | 0.0060 | 0.0091 | 0.7370   |
| No log        | 2.0   | 22   | 0.4066          | 0.1541    | 0.2814 | 0.1992 | 0.8340   |
| No log        | 3.0   | 33   | 0.3525          | 0.1768    | 0.3234 | 0.2286 | 0.8612   |
| No log        | 4.0   | 44   | 0.3250          | 0.2171    | 0.3503 | 0.2680 | 0.8766   |
| No log        | 5.0   | 55   | 0.3160          | 0.2353    | 0.3713 | 0.2880 | 0.8801   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

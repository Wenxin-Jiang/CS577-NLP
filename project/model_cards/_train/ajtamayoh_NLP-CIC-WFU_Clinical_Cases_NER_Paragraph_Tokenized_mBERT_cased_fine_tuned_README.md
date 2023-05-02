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
- name: NLP-CIC-WFU_Clinical_Cases_NER_Paragraph_Tokenized_mBERT_cased_fine_tuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NLP-CIC-WFU_Clinical_Cases_NER_Paragraph_Tokenized_mBERT_cased_fine_tuned

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0537
- Precision: 0.8585
- Recall: 0.7101
- F1: 0.7773
- Accuracy: 0.9893

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0693        | 1.0   | 514  | 0.0416          | 0.9485    | 0.6492 | 0.7708 | 0.9884   |
| 0.0367        | 2.0   | 1028 | 0.0396          | 0.9391    | 0.6710 | 0.7827 | 0.9892   |
| 0.0283        | 3.0   | 1542 | 0.0385          | 0.9388    | 0.6889 | 0.7947 | 0.9899   |
| 0.0222        | 4.0   | 2056 | 0.0422          | 0.9456    | 0.6790 | 0.7904 | 0.9898   |
| 0.0182        | 5.0   | 2570 | 0.0457          | 0.9349    | 0.6925 | 0.7956 | 0.9901   |
| 0.013         | 6.0   | 3084 | 0.0484          | 0.8947    | 0.7062 | 0.7894 | 0.9899   |
| 0.0084        | 7.0   | 3598 | 0.0537          | 0.8585    | 0.7101 | 0.7773 | 0.9893   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

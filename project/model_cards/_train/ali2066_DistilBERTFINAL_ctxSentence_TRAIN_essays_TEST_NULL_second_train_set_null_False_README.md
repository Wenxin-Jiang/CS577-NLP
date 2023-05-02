---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: DistilBERTFINAL_ctxSentence_TRAIN_essays_TEST_NULL_second_train_set_null_False
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilBERTFINAL_ctxSentence_TRAIN_essays_TEST_NULL_second_train_set_null_False

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7680
- Precision: 0.9838
- Recall: 0.6632
- F1: 0.7923
- Accuracy: 0.6624

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
| No log        | 1.0   | 130  | 0.2980          | 0.9315    | 0.9533 | 0.9423 | 0.9081   |
| No log        | 2.0   | 260  | 0.2053          | 0.9537    | 0.9626 | 0.9581 | 0.9338   |
| No log        | 3.0   | 390  | 0.1873          | 0.9464    | 0.9907 | 0.9680 | 0.9485   |
| 0.3064        | 4.0   | 520  | 0.1811          | 0.9585    | 0.9720 | 0.9652 | 0.9449   |
| 0.3064        | 5.0   | 650  | 0.1887          | 0.9587    | 0.9766 | 0.9676 | 0.9485   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

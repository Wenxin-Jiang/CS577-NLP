---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: biobert-base-cased-v1.2-finetuned-ner-CRAFT_English
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-base-cased-v1.2-finetuned-ner-CRAFT_English

This model is a fine-tuned version of [dmis-lab/biobert-base-cased-v1.2](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1614
- Precision: 0.8585
- Recall: 0.8623
- F1: 0.8604
- Accuracy: 0.9724

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0725        | 1.0   | 1360 | 0.1242          | 0.8090    | 0.8698 | 0.8383 | 0.9681   |
| 0.0281        | 2.0   | 2720 | 0.1541          | 0.8497    | 0.8549 | 0.8523 | 0.9705   |
| 0.0162        | 3.0   | 4080 | 0.1510          | 0.8390    | 0.8681 | 0.8533 | 0.9711   |
| 0.0053        | 4.0   | 5440 | 0.1614          | 0.8585    | 0.8623 | 0.8604 | 0.9724   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.11.6

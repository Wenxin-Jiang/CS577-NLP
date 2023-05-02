---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- recall
- precision
model-index:
- name: Bio_ClinicalBERT-finetuned-skinwound
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Bio_ClinicalBERT-finetuned-skinwound

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3435
- Accuracy: 0.8938
- F1: 0.8884
- Recall: 0.8938
- Precision: 0.8857

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Recall | Precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:------:|:---------:|
| 0.5905        | 1.0   | 154  | 0.3423          | 0.8828   | 0.8416 | 0.8828 | 0.8064    |
| 0.3472        | 2.0   | 308  | 0.2942          | 0.8901   | 0.8753 | 0.8901 | 0.8800    |
| 0.2651        | 3.0   | 462  | 0.2977          | 0.8974   | 0.8858 | 0.8974 | 0.8889    |
| 0.2203        | 4.0   | 616  | 0.3224          | 0.9011   | 0.8945 | 0.9011 | 0.8930    |
| 0.164         | 5.0   | 770  | 0.3435          | 0.8938   | 0.8884 | 0.8938 | 0.8857    |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

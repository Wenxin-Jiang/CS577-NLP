---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-nlp-project-ft-google
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-nlp-project-ft-google

This model is a fine-tuned version of [jestemleon/bert-nlp-project-google](https://huggingface.co/jestemleon/bert-nlp-project-google) on the [steciuk/google](https://huggingface.co/datasets/steciuk/google) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3255
- Accuracy: 0.9105
- F1: 0.9174

and flowing results on the testing set:
- Accuracy: 0.9115
- F1: 0.9180

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
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.3506        | 0.37  | 196  | 0.2922          | 0.8876   | 0.9017 |
| 0.2724        | 0.75  | 392  | 0.2456          | 0.9038   | 0.9099 |
| 0.2299        | 1.12  | 588  | 0.2781          | 0.9124   | 0.9192 |
| 0.2009        | 1.49  | 784  | 0.2934          | 0.8981   | 0.9016 |
| 0.182         | 1.86  | 980  | 0.2854          | 0.9095   | 0.9164 |
| 0.1569        | 2.24  | 1176 | 0.2932          | 0.9086   | 0.9150 |
| 0.118         | 2.61  | 1372 | 0.3258          | 0.9067   | 0.9139 |
| 0.1188        | 2.98  | 1568 | 0.3255          | 0.9105   | 0.9174 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

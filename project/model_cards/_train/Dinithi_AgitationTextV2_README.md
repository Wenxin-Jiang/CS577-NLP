---
license: cc0-1.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: AgitationTextV2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AgitationTextV2

This model is a fine-tuned version of [bionlp/bluebert_pubmed_uncased_L-12_H-768_A-12](https://huggingface.co/bionlp/bluebert_pubmed_uncased_L-12_H-768_A-12) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6268
- Accuracy: 0.73
- Precision: 0.8036
- Recall: 0.7377
- F1: 0.7692

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.6535        | 1.0   | 50   | 0.6682          | 0.66     | 0.7547    | 0.6557 | 0.7018 |
| 0.5874        | 2.0   | 100  | 0.6695          | 0.66     | 0.7455    | 0.6721 | 0.7069 |
| 0.5373        | 3.0   | 150  | 0.6141          | 0.6      | 0.7838    | 0.4754 | 0.5918 |
| 0.4671        | 4.0   | 200  | 0.6017          | 0.71     | 0.7667    | 0.7541 | 0.7603 |
| 0.4111        | 5.0   | 250  | 0.5507          | 0.75     | 0.8333    | 0.7377 | 0.7826 |
| 0.3828        | 6.0   | 300  | 0.6090          | 0.7      | 0.7541    | 0.7541 | 0.7541 |
| 0.3034        | 7.0   | 350  | 0.6073          | 0.71     | 0.8333    | 0.6557 | 0.7339 |
| 0.2702        | 8.0   | 400  | 0.5790          | 0.71     | 0.8077    | 0.6885 | 0.7434 |
| 0.246         | 9.0   | 450  | 0.7061          | 0.71     | 0.7424    | 0.8033 | 0.7717 |
| 0.2229        | 10.0  | 500  | 0.6268          | 0.73     | 0.8036    | 0.7377 | 0.7692 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

---
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: bert-base-codemixed-uncased-sentiment-hatespeech-multilanguage
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results_6_to_11_with_embedding2

This model is a fine-tuned version of [rohanrajpal/bert-base-codemixed-uncased-sentiment](https://huggingface.co/rohanrajpal/bert-base-codemixed-uncased-sentiment) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3507
- Accuracy: 0.8759
- Precision: 0.8751
- Recall: 0.8759
- F1: 0.8755

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.3889        | 1.0   | 1460  | 0.3761          | 0.8335   | 0.8484    | 0.8335 | 0.8371 |
| 0.3273        | 2.0   | 2920  | 0.3196          | 0.8542   | 0.8602    | 0.8542 | 0.8561 |
| 0.2955        | 3.0   | 4380  | 0.3116          | 0.8645   | 0.8644    | 0.8645 | 0.8645 |
| 0.27          | 4.0   | 5840  | 0.3014          | 0.8704   | 0.8695    | 0.8704 | 0.8699 |
| 0.2601        | 5.0   | 7300  | 0.3285          | 0.8676   | 0.8714    | 0.8676 | 0.8689 |
| 0.2376        | 6.0   | 8760  | 0.3147          | 0.8726   | 0.8737    | 0.8726 | 0.8731 |
| 0.213         | 7.0   | 10220 | 0.3103          | 0.8699   | 0.8714    | 0.8699 | 0.8706 |
| 0.2013        | 8.0   | 11680 | 0.3424          | 0.8737   | 0.8733    | 0.8737 | 0.8735 |
| 0.192         | 9.0   | 13140 | 0.3398          | 0.8758   | 0.8746    | 0.8758 | 0.8750 |
| 0.1763        | 10.0  | 14600 | 0.3507          | 0.8759   | 0.8751    | 0.8759 | 0.8755 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

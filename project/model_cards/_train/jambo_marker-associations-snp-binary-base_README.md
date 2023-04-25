---
license: mit
tags:
- generated_from_trainer
datasets:
- marker-associations-snp-binary-base
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: marker-associations-snp-binary-base
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: marker-associations-snp-binary-base
      type: marker-associations-snp-binary-base
    metrics:
    - name: Precision
      type: precision
      value: 0.9384057971014492
    - name: Recall
      type: recall
      value: 0.9055944055944056
    - name: F1
      type: f1
      value: 0.9217081850533808
    - name: Accuracy
      type: accuracy
      value: 0.9107505070993914
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# marker-associations-snp-binary-base

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the marker-associations-snp-binary-base dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4027
- Precision: 0.9384
- Recall: 0.9056
- F1: 0.9217
- Accuracy: 0.9108
- Auc: 0.9578

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 1
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy | Auc    |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|:------:|
| No log        | 1.0   | 153  | 0.2776          | 0.9       | 0.9441 | 0.9215 | 0.9067   | 0.9613 |
| No log        | 2.0   | 306  | 0.4380          | 0.9126    | 0.9126 | 0.9126 | 0.8986   | 0.9510 |
| No log        | 3.0   | 459  | 0.4027          | 0.9384    | 0.9056 | 0.9217 | 0.9108   | 0.9578 |
| 0.2215        | 4.0   | 612  | 0.3547          | 0.9449    | 0.8986 | 0.9211 | 0.9108   | 0.9642 |
| 0.2215        | 5.0   | 765  | 0.4465          | 0.9107    | 0.9266 | 0.9185 | 0.9047   | 0.9636 |
| 0.2215        | 6.0   | 918  | 0.5770          | 0.8970    | 0.9441 | 0.9199 | 0.9047   | 0.9666 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Tokenizers 0.10.3

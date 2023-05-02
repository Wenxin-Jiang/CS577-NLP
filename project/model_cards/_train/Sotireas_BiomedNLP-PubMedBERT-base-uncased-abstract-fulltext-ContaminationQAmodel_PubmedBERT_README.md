---
license: mit
tags:
- generated_from_trainer
model-index:
- name: BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext-ContaminationQAmodel_PubmedBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext-ContaminationQAmodel_PubmedBERT

This model is a fine-tuned version of [Sotireas/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext-ContaminationQAmodel_PubmedBERT](https://huggingface.co/Sotireas/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext-ContaminationQAmodel_PubmedBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0853

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 21   | 3.8118          |
| No log        | 2.0   | 42   | 3.5006          |
| No log        | 3.0   | 63   | 3.1242          |
| No log        | 4.0   | 84   | 2.9528          |
| No log        | 5.0   | 105  | 2.9190          |
| No log        | 6.0   | 126  | 2.9876          |
| No log        | 7.0   | 147  | 3.0574          |
| No log        | 8.0   | 168  | 3.0718          |
| No log        | 9.0   | 189  | 3.0426          |
| No log        | 10.0  | 210  | 3.0853          |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

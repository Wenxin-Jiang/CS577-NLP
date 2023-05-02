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
- name: Negation_Scope_Detection_SFU_Spanish_NLP-CIC-WFU_DisTEMIST_fine_tuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Negation_Scope_Detection_SFU_Spanish_NLP-CIC-WFU_DisTEMIST_fine_tuned

This model is a fine-tuned version of [ajtamayoh/NER_EHR_Spanish_model_Mulitlingual_BERT](https://huggingface.co/ajtamayoh/NER_EHR_Spanish_model_Mulitlingual_BERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3219
- Precision: 0.7403
- Recall: 0.7571
- F1: 0.7486
- Accuracy: 0.9518

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
| No log        | 1.0   | 72   | 0.2142          | 0.5227    | 0.6497 | 0.5793 | 0.9267   |
| No log        | 2.0   | 144  | 0.2019          | 0.625     | 0.7062 | 0.6631 | 0.9420   |
| No log        | 3.0   | 216  | 0.3089          | 0.6444    | 0.6554 | 0.6499 | 0.9432   |
| No log        | 4.0   | 288  | 0.2376          | 0.6952    | 0.7345 | 0.7143 | 0.9478   |
| No log        | 5.0   | 360  | 0.2876          | 0.7037    | 0.7514 | 0.7268 | 0.9538   |
| No log        | 6.0   | 432  | 0.3077          | 0.7278    | 0.7401 | 0.7339 | 0.9534   |
| 0.091         | 7.0   | 504  | 0.3219          | 0.7403    | 0.7571 | 0.7486 | 0.9518   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

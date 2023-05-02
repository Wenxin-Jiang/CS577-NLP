---
license: cc-by-4.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: NLP-CIC-WFU_Clinical_Cases_NER_Sents_Tokenized_bertin_roberta_base_spanish_fine_tuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NLP-CIC-WFU_Clinical_Cases_NER_Sents_Tokenized_bertin_roberta_base_spanish_fine_tuned

This model is a fine-tuned version of [bertin-project/bertin-roberta-base-spanish](https://huggingface.co/bertin-project/bertin-roberta-base-spanish) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0973
- Precision: 0.9012
- Recall: 0.6942
- F1: 0.7842
- Accuracy: 0.9857

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

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0605        | 1.0   | 2568  | 0.0625          | 0.9400    | 0.6322 | 0.7560 | 0.9836   |
| 0.0475        | 2.0   | 5136  | 0.0622          | 0.9533    | 0.6572 | 0.7781 | 0.9849   |
| 0.0374        | 3.0   | 7704  | 0.0552          | 0.9261    | 0.6784 | 0.7831 | 0.9855   |
| 0.0246        | 4.0   | 10272 | 0.0693          | 0.9381    | 0.6658 | 0.7788 | 0.9849   |
| 0.0126        | 5.0   | 12840 | 0.0974          | 0.8918    | 0.6830 | 0.7735 | 0.9849   |
| 0.0061        | 6.0   | 15408 | 0.0886          | 0.8771    | 0.7099 | 0.7847 | 0.9850   |
| 0.0031        | 7.0   | 17976 | 0.0973          | 0.9012    | 0.6942 | 0.7842 | 0.9857   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

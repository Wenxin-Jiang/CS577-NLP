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
- name: distilbert-base-uncased-finetuned-ner-TRANS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner-TRANS

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1053
- Precision: 0.7911
- Recall: 0.8114
- F1: 0.8011
- Accuracy: 0.9815

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
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.077         | 1.0   | 3762  | 0.0724          | 0.7096    | 0.7472 | 0.7279 | 0.9741   |
| 0.0538        | 2.0   | 7524  | 0.0652          | 0.7308    | 0.7687 | 0.7493 | 0.9766   |
| 0.0412        | 3.0   | 11286 | 0.0643          | 0.7672    | 0.7875 | 0.7772 | 0.9788   |
| 0.0315        | 4.0   | 15048 | 0.0735          | 0.7646    | 0.7966 | 0.7803 | 0.9793   |
| 0.0249        | 5.0   | 18810 | 0.0772          | 0.7805    | 0.7981 | 0.7892 | 0.9801   |
| 0.0213        | 6.0   | 22572 | 0.0783          | 0.7829    | 0.8063 | 0.7944 | 0.9805   |
| 0.0187        | 7.0   | 26334 | 0.0858          | 0.7821    | 0.8010 | 0.7914 | 0.9809   |
| 0.0157        | 8.0   | 30096 | 0.0860          | 0.7837    | 0.8120 | 0.7976 | 0.9812   |
| 0.0122        | 9.0   | 33858 | 0.0963          | 0.7857    | 0.8129 | 0.7990 | 0.9813   |
| 0.0107        | 10.0  | 37620 | 0.0993          | 0.7934    | 0.8089 | 0.8010 | 0.9812   |
| 0.0091        | 11.0  | 41382 | 0.1031          | 0.7882    | 0.8123 | 0.8001 | 0.9814   |
| 0.0083        | 12.0  | 45144 | 0.1053          | 0.7911    | 0.8114 | 0.8011 | 0.9815   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1
- Datasets 2.0.0
- Tokenizers 0.10.3

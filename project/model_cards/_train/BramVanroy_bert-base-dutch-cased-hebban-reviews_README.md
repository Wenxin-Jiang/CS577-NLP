---
datasets:
- BramVanroy/hebban-reviews
language:
- nl
license: mit
metrics:
- accuracy
- f1
- precision
- qwk
- recall
model-index:
- name: bert-base-dutch-cased-hebban-reviews
  results:
  - dataset:
      config: filtered_sentiment
      name: BramVanroy/hebban-reviews - filtered_sentiment - 2.0.0
      revision: 2.0.0
      split: test
      type: BramVanroy/hebban-reviews
    metrics:
    - name: Test accuracy
      type: accuracy
      value: 0.8042406311637081
    - name: Test f1
      type: f1
      value: 0.8125977499178383
    - name: Test precision
      type: precision
      value: 0.8283602308368182
    - name: Test qwk
      type: qwk
      value: 0.7301452890386257
    - name: Test recall
      type: recall
      value: 0.8042406311637081
    task:
      name: sentiment analysis
      type: text-classification
tags:
- sentiment-analysis
- dutch
- text
widget:
- text: Wauw, wat een leuk boek! Ik heb me er er goed mee vermaakt.
- text: Nee, deze vond ik niet goed. De auteur doet zijn best om je als lezer mee
    te trekken in het verhaal maar mij overtuigt het alleszins niet.
- text: Ik vind het niet slecht maar de schrijfstijl trekt me ook niet echt aan. Het
    wordt een beetje saai vanaf het vijfde hoofdstuk
---

# bert-base-dutch-cased-hebban-reviews

# Dataset
- dataset_name: BramVanroy/hebban-reviews
- dataset_config: filtered_sentiment
- dataset_revision: 2.0.0
- labelcolumn: review_sentiment
- textcolumn: review_text_without_quotes

# Training
- optim: adamw_hf
- learning_rate: 5e-05
- per_device_train_batch_size: 64
- per_device_eval_batch_size: 64
- gradient_accumulation_steps: 1
- max_steps: 5001
- save_steps: 500
- metric_for_best_model: qwk

# Best checkedpoint based on validation
- best_metric: 0.732569302631819
- best_model_checkpoint: trained/hebban-reviews/bert-base-dutch-cased/checkpoint-3000

# Test results of best checkpoint
- accuracy: 0.8042406311637081
- f1: 0.8125977499178383
- precision: 0.8283602308368182
- qwk: 0.7301452890386257
- recall: 0.8042406311637081

## Confusion matrix

![cfm](fig/test_confusion_matrix.png)

## Normalized confusion matrix

![norm cfm](fig/test_confusion_matrix_norm.png)

# Environment
- cuda_capabilities: 8.0; 8.0
- cuda_device_count: 2
- cuda_devices: NVIDIA A100-SXM4-80GB; NVIDIA A100-SXM4-80GB
- finetuner_commit: 48bb3434fa8bbfc9b2d0061ca6c8feb87f78a7ef
- platform: Linux-4.18.0-305.49.1.el8_4.x86_64-x86_64-with-glibc2.28
- python_version: 3.9.5
- toch_version: 1.10.0
- transformers_version: 4.21.0


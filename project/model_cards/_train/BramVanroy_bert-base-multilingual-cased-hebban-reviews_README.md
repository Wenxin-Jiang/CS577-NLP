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
- name: bert-base-multilingual-cased-hebban-reviews
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
      value: 0.7764792899408284
    - name: Test f1
      type: f1
      value: 0.7821329848271866
    - name: Test precision
      type: precision
      value: 0.7907660190770787
    - name: Test qwk
      type: qwk
      value: 0.6813121109021326
    - name: Test recall
      type: recall
      value: 0.7764792899408284
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

# bert-base-multilingual-cased-hebban-reviews

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
- best_metric: 0.6828581526810108
- best_model_checkpoint: trained/hebban-reviews/bert-base-multilingual-cased/checkpoint-1500

# Test results of best checkpoint
- accuracy: 0.7764792899408284
- f1: 0.7821329848271866
- precision: 0.7907660190770787
- qwk: 0.6813121109021326
- recall: 0.7764792899408284

## Confusion matrix

![cfm](fig/test_confusion_matrix.png)

## Normalized confusion matrix

![norm cfm](fig/test_confusion_matrix_norm.png)

# Environment
- cuda_capabilities: 8.0; 8.0
- cuda_device_count: 2
- cuda_devices: NVIDIA A100-SXM4-80GB; NVIDIA A100-SXM4-80GB
- finetuner_commit: 66294c815326c93682003119534cb72009f558c2
- platform: Linux-4.18.0-305.49.1.el8_4.x86_64-x86_64-with-glibc2.28
- python_version: 3.9.5
- toch_version: 1.10.0
- transformers_version: 4.21.0


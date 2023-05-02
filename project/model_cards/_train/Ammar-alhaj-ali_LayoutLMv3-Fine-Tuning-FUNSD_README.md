---
tags:
- generated_from_trainer
datasets:
- nielsr/funsd-layoutlmv3
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: layoutlmv3-finetuned-funsd
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: nielsr/funsd-layoutlmv3
      type: nielsr/funsd-layoutlmv3
      args: funsd
    metrics:
    - name: Precision
      type: precision
      value: 0.918177	
    - name: Recall
      type: recall
      value: 0.930949
    - name: F1
      type: f1
      value: 0.924519
    - name: Accuracy
      type: accuracy
      value: 0.859979
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-funsd

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the nielsr/funsd-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.038318	
- Precision: 0.918177	
- Recall: 0.930949	
- F1: 0.924519
- Accuracy: 0.859979



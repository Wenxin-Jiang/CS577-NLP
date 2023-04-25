---
tags:
- image-classification
- pytorch
metrics:
- accuracy
model-index:
- name: llama-horse-zebra
  results:
  - task:
      name: Image Classification
      type: image-classification
    metrics:
    - name: Accuracy
      type: accuracy
      value: 1.0
    dataset:
      name: HumanEval
      type: openai_humaneval
  - dataset:
      name: HumanEval
      type: openai_humaneval
    metrics:
    - name: pass@1
      type: code_eval
      value: 4
    task:
      name: Code Generation
      type: code-generation
  - dataset:
      name: HumanEval
      type: openai_differenty_type
    metrics:
    - name: pass@1
      type: code_eval
      value: 4
    task:
      name: Code Generation
      type: code-generation
---

test
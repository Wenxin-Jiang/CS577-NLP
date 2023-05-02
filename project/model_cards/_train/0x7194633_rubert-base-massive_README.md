---
license: apache-2.0
datasets:
- AmazonScience/massive
language:
- ru
library_name: transformers
pipeline_tag: text-classification
train-eval-index:
- config: ru-RU
  task: text-classification
  task_id: multi_class_classification
  splits:
    eval_split: test
  col_mapping:
    utt: text
    intent: target
---
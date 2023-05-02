---
language: 
- en
- ru

datasets:
- glue
- mnli

model_index:
- name: mnli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE MNLI
      type: glue
      args: mnli


tags:
- xlm-roberta
- xlm-roberta-large
- xlm-roberta-large-en-ru
- xlm-roberta-large-en-ru-mnli

widget:
- text: "Люблю тебя. Ненавижу тебя"
- text: "I love you. I hate you"

---


# XLM-RoBERTa-Large-En-Ru-MNLI

xlm-roberta-large-en-ru finetuned on mnli.
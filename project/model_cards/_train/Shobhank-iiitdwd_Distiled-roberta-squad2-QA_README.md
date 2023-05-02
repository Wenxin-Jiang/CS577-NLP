---
language: en
license: cc-by-4.0
datasets:
- squad_v2
model-index:
- name: Distiled-roberta-squad2
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad_v2
      type: squad_v2
      config: squad_v2
      split: validation
    metrics:
    - type: exact_match
      value: 78.8627
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDNlZDU4ODAxMzY5NGFiMTMyZmQ1M2ZhZjMyODA1NmFlOGMxNzYxNTA4OGE5YTBkZWViZjBkNGQ2ZmMxZjVlMCIsInZlcnNpb24iOjF9.Wgu599r6TvgMLTrHlLMVAbUtKD_3b70iJ5QSeDQ-bRfUsVk6Sz9OsJCp47riHJVlmSYzcDj_z_3jTcUjCFFXBg
    - type: f1
      value: 82.0355
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTFkMzEzMWNiZDRhMGZlODhkYzcwZTZiMDFjZDg2YjllZmUzYWM5NTgwNGQ2NGYyMDk2ZGQwN2JmMTE5NTc3YiIsInZlcnNpb24iOjF9.ChgaYpuRHd5WeDFjtiAHUyczxtoOD_M5WR8834jtbf7wXhdGOnZKdZ1KclmhoI5NuAGc1NptX-G0zQ5FTHEcBA
---

# Distiled-roberta-squad2

This is the *distilled* version of the [roberta-base-squad2-QA](https://huggingface.co/Shobhank-iiitdwd/Distiled-roberta-squad2-QA) model. This model has a comparable prediction quality and runs at twice the speed of the base model.

## Overview
**Language model:** Distiled-roberta-squad2-QA  
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD 2.0  

## Hyperparameters

```
batch_size = 96
n_epochs = 4
base_LM_model = "Shobhank-iiitdwd/Distiled-roberta-squad2-QA"
max_seq_len = 384
learning_rate = 3e-5
lr_schedule = LinearWarmup
warmup_proportion = 0.2
doc_stride = 128
max_query_length = 64
distillation_loss_weight = 0.75
temperature = 1.5
teacher = "Shobhank-iiitdwd/Distiled-roberta-squad2-QA"
``` 

## Distillation
This model was distilled using the TinyBERT approach.Firstly, we have performed intermediate layer distillation with roberta-base as the teacher which resulted in Distiles-roberta.
Secondly, we have performed task-specific distillation with [roberta-base-squad2](https://huggingface.co/Shobhank-iiitdwd/roberta-squad2-QA) as the teacher for further intermediate layer distillation on an augmented version of SQuADv2 and then with [roberta-large-squad2](https://huggingface.co/Shobhank-iiitdwd/Distiled-roberta-squad2-QA) as the teacher for prediction layer distillation. 

## Usage

### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "Shobhank-iiitdwd/Distiled-roberta-squad2-QA"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'Why is model conversion important?',
    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res = nlp(QA_input)

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```

## Performance
Evaluated on the SQuAD 2.0 dev set with the [official eval script](https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/).

```
"exact": 78.69114798281817,
"f1": 81.9198998536977,

"total": 11873,
"HasAns_exact": 76.19770580296895,
"HasAns_f1": 82.66446878592329,
"HasAns_total": 5928,
"NoAns_exact": 81.17746005046257,
"NoAns_f1": 81.17746005046257,
"NoAns_total": 5945
```

---
language: en
license: cc-by-4.0
datasets:
- squad_v2
model-index:
- name: Shobhank-iiitdwd/bert-large-uncased-squad2-QA
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
      value: 80.8846
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2E5ZGNkY2ExZWViZGEwNWE3OGRmMWM2ZmE4ZDU4ZDQ1OGM3ZWE0NTVmZjFmYmZjZmJmNjJmYTc3NTM3OTk3OSIsInZlcnNpb24iOjF9.aSblF4ywh1fnHHrN6UGL392R5KLaH3FCKQlpiXo_EdQ4XXEAENUCjYm9HWDiFsgfSENL35GkbSyz_GAhnefsAQ
    - type: f1
      value: 83.8765
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGFlNmEzMTk2NjRkNTI3ZTk3ZTU1NWNlYzIyN2E0ZDFlNDA2ZjYwZWJlNThkMmRmMmE0YzcwYjIyZDM5NmRiMCIsInZlcnNpb24iOjF9.-rc2_Bsp_B26-o12MFYuAU0Ad2Hg9PDx7Preuk27WlhYJDeKeEr32CW8LLANQABR3Mhw2x8uTYkEUrSDMxxLBw
---

# bert-large-uncased-whole-word-masking-squad2

This is a berta-large model, fine-tuned using the SQuAD2.0 dataset for the task of question answering.

## Overview
**Language model:** bert-large  
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD 2.0  
## Usage


### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "Shobhank-iiitdwd/bert-large-uncased-squad2-QA"

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

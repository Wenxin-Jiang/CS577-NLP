---
language: en
tags: question answering
license: apache-2.0
datasets: 
- squad
- batterydata/battery-device-data-qa
metrics: squad
---

# BatteryBERT-uncased for QA 
**Language model:** batterybert-uncased
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD v1
**Eval data:** SQuAD v1
**Code:**  See [example](https://github.com/ShuHuang/batterybert) 
**Infrastructure**: 8x DGX A100
## Hyperparameters
```
batch_size = 32
n_epochs = 3
base_LM_model = "batterybert-uncased"
max_seq_len = 386
learning_rate = 3e-5
doc_stride=128
max_query_length=64
``` 
## Performance
Evaluated on the SQuAD v1.0 dev set.
```
"exact": 81.08,
"f1": 88.41,
```
Evaluated on the battery device dataset.
```
"precision": 68.27,
"recall": 80.88,
```
## Usage
### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "batterydata/batterybert-uncased-squad-v1"
# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'What is the electrolyte?',
    'context': 'The typical non-aqueous electrolyte for commercial Li-ion cells is a solution of LiPF6 in linear and cyclic carbonates.'
}
res = nlp(QA_input)
# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```
## Authors
Shu Huang: `sh2009 [at] cam.ac.uk`

Jacqueline Cole: `jmc61 [at] cam.ac.uk`

## Citation
BatteryBERT: A Pre-trained Language Model for Battery Database Enhancement

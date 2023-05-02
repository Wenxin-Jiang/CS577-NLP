---
language: vi

datasets:
- oscar

---

# NlpHUST/roberta-base-vn

## Model description

This is a Vietnamese RoBERTa base model pretrained on Vietnamese Oscar dataset.

## How to use

You can use this model for masked language modeling as follows:
```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("NlpHUST/roberta-base-vn")
model = AutoModelForMaskedLM.from_pretrained("NlpHUST/roberta-base-vn")

You can fine-tune this model on downstream tasks.

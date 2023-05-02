---
datasets:
- leipzig

language: 
- hr
- sr
- multilingual
tags:
- masked-lm
widget:
- text: "Gde je <mask>."
license: apache-2.0
---
# Transformer language model for Croatian and Serbian
Trained on 0.7GB dataset Croatian and Serbian language for one epoch.
Dataset from Leipzig Corpora.

# Information of dataset
| Model                          | #params                        | Arch. | Training data                     |
|--------------------------------|--------------------------------|-------|-----------------------------------|
| `Andrija/SRoBERTa` | 120M   | First  | Leipzig Corpus (0.7 GB of text)            |


# How to use in code
```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
  
tokenizer = AutoTokenizer.from_pretrained("Andrija/SRoBERTa")

model = AutoModelForMaskedLM.from_pretrained("Andrija/SRoBERTa")
```
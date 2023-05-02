---
datasets:
- oscar
- leipzig

language: 
- hr
- sr
- multilingual

tags:
- masked-lm

widget:
- text: "Ovo je početak <mask>."

license: apache-2.0

---
# Transformer language model for Croatian and Serbian
Trained on 3GB datasets that contain Croatian and Serbian language for two epochs.
Leipzig and OSCAR datasets

# Information of dataset

| Model                          | #params                        | Arch. | Training data                     |
|--------------------------------|--------------------------------|-------|-----------------------------------|
| `Andrija/SRoBERTa-base` | 80M   | Second | Leipzig Corpus and OSCAR (3 GB of text)            |
---
datasets:
- oscar
- srwac
- leipzig
- cc100
- hrwac
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

Trained on 28GB datasets that contain Croatian and Serbian language for one epochs (3 mil. steps).
Leipzig Corpus, OSCAR, srWac, hrWac, cc100-hr and cc100-sr  datasets

| Model                          | #params                        | Arch. | Training data                     |
|--------------------------------|--------------------------------|-------|-----------------------------------|
| `Andrija/SRoBERTa-XL` | 80M   | Forth | Leipzig Corpus, OSCAR, srWac, hrWac, cc100-hr and cc100-sr  (28 GB of text)            |
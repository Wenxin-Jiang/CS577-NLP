---
datasets:
- oscar
- srwac
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
Trained on 6GB datasets that contain Croatian and Serbian language for two epochs (500k steps).
Leipzig, OSCAR and srWac datasets

| Model                          | #params                        | Arch. | Training data                     |
|--------------------------------|--------------------------------|-------|-----------------------------------|
| `Andrija/SRoBERTa-L` | 80M   | Third | Leipzig Corpus, OSCAR and srWac (6 GB of text)            |
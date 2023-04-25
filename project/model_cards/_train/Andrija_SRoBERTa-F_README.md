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
Trained on 43GB datasets that contain Croatian and Serbian language for one epochs (9.6 mil. steps, 3 epochs).
Leipzig Corpus, OSCAR, srWac, hrWac, cc100-hr and cc100-sr  datasets

Validation number of exampels run for perplexity:1620487 sentences
Perplexity:6.02
Start loss: 8.6
Final loss: 2.0
Thoughts: Model could be trained more, the training did not stagnate.

| Model                          | #params                        | Arch. | Training data                     |
|--------------------------------|--------------------------------|-------|-----------------------------------|
| `Andrija/SRoBERTa-F` | 80M   | Fifth | Leipzig Corpus, OSCAR, srWac, hrWac, cc100-hr and cc100-sr  (43 GB of text)             |
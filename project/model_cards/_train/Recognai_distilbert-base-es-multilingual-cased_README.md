---
language: es
license: apache-2.0
datasets:
- wikipedia
widget:
- text: "Mi nombre es Juan y vivo en [MASK]."
---

# DistilBERT base multilingual model Spanish subset (cased)

This model is the Spanish extract of `distilbert-base-multilingual-cased` (https://huggingface.co/distilbert-base-multilingual-cased), a distilled version of the [BERT base multilingual model](bert-base-multilingual-cased). This model is cased: it does make a difference between english and English.

It uses the extraction method proposed by Geotrend described in https://github.com/Geotrend-research/smaller-transformers. 

The resulting model has the same architecture as DistilmBERT: 6 layers, 768 dimension and 12 heads, with a total of **63M parameters** (compared to 134M parameters for DistilmBERT).

The goal of this model is to reduce even further the size of the `distilbert-base-multilingual` multilingual model by selecting only most frequent tokens for Spanish, reducing the size of the embedding layer. For more details visit the paper from the Geotrend team: Load What You Need: Smaller Versions of Multilingual BERT.
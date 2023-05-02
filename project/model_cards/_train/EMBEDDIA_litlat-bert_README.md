---
language: 
- lt
- lv
- en
- multilingual

license: cc-by-sa-4.0
---

# LitLat BERT
LitLat BERT is a trilingual model, using xlm-roberta-base architecture, trained on Lithuanian, Latvian, and English corpora. Focusing on three languages, the model performs better than [multilingual BERT](https://huggingface.co/bert-base-multilingual-cased), while still offering an option for cross-lingual knowledge transfer, which a monolingual model wouldn't. 

### Named entity recognition evaluation

We compare LitLat BERT with multilingual BERT (mBERT), XLM-RoBERTa (XLM-R) and monolingual Latvian BERT (LVBERT) (Znotins and Barzdins, 2020). The report the results as a macro F1 score of 3 named entity classes shared in all three datasets: person, location, organization.

Language | mBERT | XLM-R | LVBERT | LitLat
---|---|---|---|---
Latvian | 0.830 | 0.865 | 0.797 | **0.881**
Lithuanian | 0.797 | 0.817 | / | **0.850**
English | 0.939 | 0.937 | / | **0.943**

---
language: 
- fi
- et
- en
- multilingual

license: cc-by-4.0
---
# FinEst BERT
FinEst BERT is a trilingual model, using bert-base architecture, trained on Finnish, Estonian, and English corpora. Focusing on three languages, the model performs better than [multilingual BERT](https://huggingface.co/bert-base-multilingual-cased), while still offering an option for cross-lingual knowledge transfer, which a monolingual model wouldn't. 

Evaluation is presented in our article:
```
@Inproceedings{ulcar-robnik2020finest,
author = "Ulčar, M. and Robnik-Šikonja, M.",
year = 2020,
title = "{FinEst BERT} and {CroSloEngual BERT}: less is more in multilingual models",
editor = "Sojka, P and Kopeček, I and Pala, K and Horák, A",
booktitle = "Text, Speech, and Dialogue {TSD 2020}",
series = "Lecture Notes in Computer Science",
volume = 12284,
publisher = "Springer",
url = "https://doi.org/10.1007/978-3-030-58323-1_11",
}
```
The preprint is available at [arxiv.org/abs/2006.07890](https://arxiv.org/abs/2006.07890).
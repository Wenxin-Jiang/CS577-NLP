---
license: mit
tags:
- feature-extraction
library_name: generic
datasets:
- ubertext2.0
widget:
- text: "доброго вечора ми з україни"
---

**cbow.uk.300.bin** is pre-trained word vectors for the Ukrainian language, trained with fastText on (yet unreleased) UberText2.0 dataset, collected and processed by the [lang-uk](https://lang.org.ua/en/). This model was trained using cbow in dimension 300, with character n-grams range of 4-6, and 15 negative samples.

The dataset for Ukrainian word analogy is available [here](https://github.com/lang-uk/vecs/).

Extrinsic evaluations were performed on two sequence labeling tasks: NER and POS tagging. [NER-UK dataset](https://github.com/lang-uk/ner-uk) was released by the [lang-uk](https://lang.org.ua/), and [Ukrainian (UD) corpus](https://github.com/brown-uk/corpus) was developed by a [non-profit organization Institute for Ukrainian](https://mova.institute/).

Results:
1) Word analogy task: **0.49**
2) spaCy NER F-score: **0.82**
3) POS Flair Accuracy: **0.82**
4) POS spaCy Accuracy: **0.87**


Usage
```
import fasttext.util
ft = fasttext.load_model('cbow.uk.300.bin')
ft.get_word_vector('привіт')
```

### BibTeX entry and citation info
```bibtex
@inproceedings{romanyshyn-etal-2023-learning,
    title = "Learning Word Embeddings for {U}krainian: A Comparative Study of Fast{T}ext Hyperparameters",
    author = "Romanyshyn, Nataliia  and
      Chaplynskyi, Dmytro  and
      Zakharov, Kyrylo",
    booktitle = "Proceedings of the Second Ukrainian Natural Language Processing Workshop",
    month = may,
    year = "2023",
    address = "Dubrovnik, Croatia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.unlp-1.3",
    pages = "20--31",
}
```

Copyright: [Dmytro Chaplynskyi](https://twitter.com/dchaplinsky), [lang-uk](https://lang.org.ua) project, [Nataliia Romanyshyn](https://github.com/romanyshyn-natalia), [Ukrainian Catholic University](https://ucu.edu.ua/en/), 2022
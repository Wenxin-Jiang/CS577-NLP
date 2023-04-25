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

**skipgram.uk.300.bin** is pre-trained word vectors for the Ukrainian language, trained with fastText on (yet unreleased) UberText2.0 dataset, collected and processed by the [lang-uk](https://lang.org.ua/en/). This model was trained using skipgram in dimension 300, with character n-grams range of 2-5, and 15 negative samples. 

Our model increases Accuracy by 6.3% compared to the [Facebook Ukrainian word vectors](https://fasttext.cc/docs/en/crawl-vectors.html) on the word analogy task. The dataset for Ukrainian word analogy is available [here](https://github.com/lang-uk/vecs/).

Extrinsic evaluations were performed on two sequence labeling tasks: NER and POS tagging. [NER-UK dataset](https://github.com/lang-uk/ner-uk) was released by the [lang-uk](https://lang.org.ua/), and [Ukrainian (UD) corpus](https://github.com/brown-uk/corpus) was developed by a [non-profit organization Institute for Ukrainian](https://mova.institute/).

Results:
1) spaCy NER F-score: **0.818**
2) POS Flair Accuracy: **0.824**
3) POS spaCy Accuracy: **0.911**

Usage
```
import fasttext.util
ft = fasttext.load_model('skipgram.uk.300.bin')
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
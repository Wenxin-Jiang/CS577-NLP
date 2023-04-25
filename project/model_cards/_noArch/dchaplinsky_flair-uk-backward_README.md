---
language:
  - uk
tags:
  - text2text-generation
  - flair
library_name: generic
license: mit
metrics:
  - perplexity
datasets:
- ubertext2.0
widget:
- text: "підсумував він."
- text: "Україна переможе!"
---

# Ukrainian flair embeddings (backward)

Trained for 25+ epochs on the texts from ubertext2.0 (WIP).
The characters dictionary used for training is in `flair_dictionary.pkl` file

For more information on flair embeddings see [the article](https://github.com/flairNLP/flair/blob/master/resources/docs/embeddings/FLAIR_EMBEDDINGS.md) or the paper below:


```bibtex
@inproceedings{akbik2018coling,
  title={Contextual String Embeddings for Sequence Labeling},
  author={Akbik, Alan and Blythe, Duncan and Vollgraf, Roland},
  booktitle = {{COLING} 2018, 27th International Conference on Computational Linguistics},
  pages     = {1638--1649},
  year      = {2018}
}
```

Copyright: [Dmytro Chaplynskyi](https://twitter.com/dchaplinsky), [lang-uk](https://lang.org.ua) project, 2022
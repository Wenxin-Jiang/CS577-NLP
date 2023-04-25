---
language: fr
tags:
- Early Modern French
- Historical
- NER
- flair
license: apache-2.0
datasets:
- freemner
library_name: flair
pipeline_tag: token-classification
---

<a href="https://portizs.eu/publication/2022/lrec/dalembert/">
	<img width="300px" src="https://portizs.eu/publication/2022/lrec/dalembert/featured_hu18bf34d40cdc71c744bdd15e48ff0b23_61788_720x2500_fit_q100_h2_lanczos_3.webp">
</a>

# D'AlemBERT-NER  model

This model is fine-tuned version of a [D'AlemBERT](https://huggingface.co/pjox/DalemBERT) on the [FreEMNER corpus](https://doi.org/10.5281/zenodo.6481135) for Early Modern French. It was
introduced in [this paper](https://aclanthology.org/2022.coling-1.327/).

### BibTeX entry and citation info

```bibtex
@inproceedings{ortiz-suarez-gabay-2022-data,
    title = "A Data-driven Approach to Named Entity Recognition for Early {M}odern {F}rench",
    author = "Ortiz Suarez, Pedro  and
      Gabay, Simon",
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "International Committee on Computational Linguistics",
    url = "https://aclanthology.org/2022.coling-1.327",
    pages = "3722--3730",
    abstract = "Named entity recognition has become an increasingly useful tool for digital humanities research, specially when it comes to historical texts. However, historical texts pose a wide range of challenges to both named entity recognition and natural language processing in general that are still difficult to address even with modern neural methods. In this article we focus in named entity recognition for historical French, and in particular for Early Modern French (16th-18th c.), i.e. Ancien R{\'e}gime French. However, instead of developing a specialised architecture to tackle the particularities of this state of language, we opt for a data-driven approach by developing a new corpus with fine-grained entity annotation, covering three centuries of literature corresponding to the early modern period; we try to annotate as much data as possible producing a corpus that is many times bigger than the most popular NER evaluation corpora for both Contemporary English and French. We then fine-tune existing state-of-the-art architectures for Early Modern and Contemporary French, obtaining results that are on par with those of the current state-of-the-art NER systems for Contemporary English. Both the corpus and the fine-tuned models are released.",
}
```
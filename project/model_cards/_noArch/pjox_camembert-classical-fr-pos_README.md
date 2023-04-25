---
language: fr
tags:
- Early Modern French
- Historical
- POS
- flair
license: apache-2.0
datasets:
  - freemlpm
library_name: flair
pipeline_tag: token-classification
---

<a href="https://portizs.eu/publication/2022/lrec/dalembert/">
	<img width="300px" src="https://portizs.eu/publication/2022/lrec/dalembert/featured_hu18bf34d40cdc71c744bdd15e48ff0b23_61788_720x2500_fit_q100_h2_lanczos_3.webp">
</a>

# CamemBERT Early Modern French POS model

This model is fine-tuned version of a [CamemBERT model](https://huggingface.co/camembert-base) on the [FreEMLPM corpus](https://doi.org/10.5281/zenodo.6481300) for Early Modern French. It was
introduced in [this paper](https://aclanthology.org/2022.lrec-1.359/).

### BibTeX entry and citation info

```bibtex
@inproceedings{gabay-etal-2022-freem,
    title = "From {F}re{EM} to D{'}{A}lem{BERT}: a Large Corpus and a Language Model for Early {M}odern {F}rench",
    author = "Gabay, Simon  and
      Ortiz Suarez, Pedro  and
      Bartz, Alexandre  and
      Chagu{\'e}, Alix  and
      Bawden, Rachel  and
      Gambette, Philippe  and
      Sagot, Beno{\^\i}t",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.359",
    pages = "3367--3374",
    abstract = "anguage models for historical states of language are becoming increasingly important to allow the optimal digitisation and analysis of old textual sources. Because these historical states are at the same time more complex to process and more scarce in the corpora available, this paper presents recent efforts to overcome this difficult situation. These efforts include producing a corpus, creating the model, and evaluating it with an NLP task currently used by scholars in other ongoing projects.",
}
```
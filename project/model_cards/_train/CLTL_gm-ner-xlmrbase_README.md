---
language: nl
license: apache-2.0
tags:
- dighum
pipeline_tag: token-classification
---

# Early-modern Dutch NER (General Letters)

## Description
This is a fine-tuned NER model for early-modern Dutch United East India Company (VOC) letters based on XLM-R_base [(Conneau et al., 2020)](https://aclanthology.org/2020.acl-main.747/). The model identifies *locations*, *persons*, *organisations*, but also *ships* as well as derived forms of locations and religions.

## Intended uses and limitations

This model was fine-tuned (trained, validated and tested) on a single source of data, the General Letters (Generale Missiven). These letters span a large variety of Dutch, as they cover the largest part of the 17th and 18th centuries, and have been extended with editorial notes between 1960 and 2017. As the model was only fine-tuned on this data however, it may perform less well on other texts from the same period.

## How to use

The model can run on raw text through the *token-classification* pipeline:
```
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("CLTL/gm-ner-xlmrbase")
model = AutoModelForTokenClassification.from_pretrained("CLTL/gm-ner-xlmrbase")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Batavia heeft om advies gevraagd."

ner_results = nlp(example)
print(ner_results)
```

This outputs a list of entities with their character offsets in the input text:
```
[{'entity': 'B-LOC', 'score': 0.99739265, 'index': 1, 'word': '▁Bata', 'start': 0, 'end': 4}, {'entity': 'I-LOC', 'score': 0.5373179, 'index': 2, 'word': 'via', 'start': 4, 'end': 7}]
```

## Training data and tagset

The model was fine-tuned on the General Letters [GM-NER](https://github.com/cltl/voc-missives/tree/master/data/ner/datasplit_all_standard) dataset, with the following tagset:

| tag | description | notes |
| --- | ----------- | ----- |
| LOC | locations   | |
| LOCderiv | derived forms of locations | by derivation, e.g. *Bandanezen*, or composition, e.g. *Javakoffie* |
| ORG | organisations | includes forms derived by composition, e.g. *Compagnieszaken*
| PER | persons |
| RELderiv | forms related to religion | merges religion names (*Christendom*), derived forms (*christenen*) and composed forms (*Christen-orangkay*) |
| SHP | ships |

The base text for this dataset is OCR text that has been partially corrected. The text is clean overall but errors remain.

## Training procedure
The model was fine-tuned with [xlm-roberta-base](https://huggingface.co/xlm-roberta-base), using [this  script](https://github.com/huggingface/transformers/blob/master/examples/legacy/token-classification/run_ner.py).

Non-default training parameters are:
* training batch size: 16
* max sequence length: 256
* number of epochs: 4 -- loading the best checkpoint model by loss at the end, with checkpoints every 200 steps
* (seed: 1)


## Evaluation 
### Metric
* entity-level F1

### Results

| overall | 92.7 |
| --- | ----------- | 
| LOC | 95.8   | 
| LOCderiv | 92.7 | 
| ORG | 92.5 |
| PER | 86.2 | 
| RELderiv | 90.7 |
| SHP | 81.6 |


## Reference
The model and fine-tuning data presented here were developed as part of:
```bibtex
@inproceedings{arnoult-etal-2021-batavia,
    title = "Batavia asked for advice. Pretrained language models for Named Entity Recognition in historical texts.",
    author = "Arnoult, Sophie I.  and
      Petram, Lodewijk  and
      Vossen, Piek",
    booktitle = "Proceedings of the 5th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities and Literature",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic (online)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.latechclfl-1.3",
    pages = "21--30"
}
```


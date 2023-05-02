---
language:
- mt
datasets:
- MLRS/korpus_malti
model-index:
- name: mBERTu
  results:
  - task: 
      type: dependency-parsing
      name: Dependency Parsing
    dataset:
      type: universal_dependencies
      args: mt_mudt
      name: Maltese Universal Dependencies Treebank (MUDT)
    metrics:
      - type: uas
        value: 92.10
        name: Unlabelled Attachment Score
      - type: las
        value: 87.87
        name: Labelled Attachment Score
  - task: 
      type: part-of-speech-tagging
      name: Part-of-Speech Tagging
    dataset:
      type: mlrs_pos
      name: MLRS POS dataset
    metrics:
      - type: accuracy
        value: 98.66
        name: UPOS Accuracy
        args: upos
      - type: accuracy
        value: 98.58
        name: XPOS Accuracy
        args: xpos
  - task: 
      type: named-entity-recognition
      name: Named Entity Recognition
    dataset:
      type: wikiann
      name: WikiAnn (Maltese)
      args: mt
    metrics:
      - type: f1
        args: span
        value: 86.60
        name: Span-based F1
  - task: 
      type: sentiment-analysis
      name: Sentiment Analysis
    dataset:
      type: mt-sentiment-analysis
      name: Maltese Sentiment Analysis Dataset
    metrics:
      - type: f1
        args: macro
        value: 76.79
        name: Macro-averaged F1
license: cc-by-nc-sa-4.0
widget:
- text: "Malta huwa pajjiż fl-[MASK]."
---

# mBERTu

A Maltese multilingual model pre-trained on the Korpus Malti v4.0 using multilingual BERT as the initial checkpoint.


## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].
Permissions beyond the scope of this license may be available at [https://mlrs.research.um.edu.mt/](https://mlrs.research.um.edu.mt/).

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png

## Citation

This work was first presented in [Pre-training Data Quality and Quantity for a Low-Resource Language: New Corpus and BERT Models for Maltese](https://aclanthology.org/2022.deeplo-1.10/).
Cite it as follows: 

```bibtex
@inproceedings{BERTu,
    title = "Pre-training Data Quality and Quantity for a Low-Resource Language: New Corpus and {BERT} Models for {M}altese",
    author = "Micallef, Kurt  and
              Gatt, Albert  and
              Tanti, Marc  and
              van der Plas, Lonneke  and
              Borg, Claudia",
    booktitle = "Proceedings of the Third Workshop on Deep Learning for Low-Resource Natural Language Processing",
    month = jul,
    year = "2022",
    address = "Hybrid",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.deeplo-1.10",
    doi = "10.18653/v1/2022.deeplo-1.10",
    pages = "90--101",
}
```

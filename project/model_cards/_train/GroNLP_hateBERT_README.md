---
language: en
tags:
- HateBERT
- text classification
- abusive language
- hate speech
- offensive language
---

# 
[Tommaso Caselli](https://www.semanticscholar.org/author/Tommaso-Caselli/1864635) •
[Valerio Basile](https://www.semanticscholar.org/author/Valerio-Basile/3101511) •
[Jelena Mitrovic](https://www.semanticscholar.org/author/Jelena-Mitrovic/145157863) •
[Michael Granizter](https://www.semanticscholar.org/author/M.-Granitzer/2389675) 

## Model description

HateBERT is an English pre-trained BERT model obtained by further training the English BERT base uncased model with more than 1 million posts from banned communites from Reddit. The model has been developed as a collaboration between the University of Groningen, the university of Turin, and the University of Passau.

For details, check out the paper presented at [WOAH 2021](https://aclanthology.org/2021.woah-1.3/). The code and the fine-tuned models are available on [OSF](https://osf.io/tbd58/?view_onlycb79b3228d4248ddb875eb1803525ad8).


### BibTeX entry and citation info

```bibtex
@inproceedings{caselli-etal-2021-hatebert,
    \ttitle = "{H}ate{BERT}: Retraining {BERT} for Abusive Language Detection in {E}nglish",
    \tauthor = "Caselli, Tommaso  and
      Basile, Valerio  and
      Mitrovi{\'c}, Jelena  and
      Granitzer, Michael",
    \tbooktitle = "Proceedings of the 5th Workshop on Online Abuse and Harms (WOAH 2021)",
    \tmonth = aug,
    \tyear = "2021",
    \taddress = "Online",
    \tpublisher = "Association for Computational Linguistics",
    \tturl = "https://aclanthology.org/2021.woah-1.3",
    \tdoi = "10.18653/v1/2021.woah-1.3",
    \tpages = "17--25",
    \tabstract = "We introduce HateBERT, a re-trained BERT model for abusive language detection in English. The model was trained on RAL-E, a large-scale dataset of Reddit comments in English from communities banned for being offensive, abusive, or hateful that we have curated and made available to the public. We present the results of a detailed comparison between a general pre-trained language model and the retrained version on three English datasets for offensive, abusive language and hate speech detection tasks. In all datasets, HateBERT outperforms the corresponding general BERT model. We also discuss a battery of experiments comparing the portability of the fine-tuned models across the datasets, suggesting that portability is affected by compatibility of the annotated phenomena.",
}
```
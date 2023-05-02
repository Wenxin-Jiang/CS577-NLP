---
language:
- en

datasets:
- winogrande

widget:
- text: "The roof of Rachel's home is old and falling apart, while Betty's is new. The home value of </s> Rachel is lower."
- text: "The wooden doors at my friends work are worse than the wooden desks at my work, because the </s> desks material is cheaper."
- text: "Postal Service were to reduce delivery frequency. </s> The postal service could deliver less frequently."
- text: "I put the cake away in the refrigerator. It has a lot of butter in it. </s> The cake has a lot of butter in it."

---
# RoBERTa Large model fine-tuned on Winogrande

This model was fine-tuned on Winogrande dataset (XL size) in sequence classification task format, meaning that original pairs of sentences
with corresponding options filled in were separated, shuffled and classified independently of each other.

## Model description


## Intended use & limitations


### How to use


## Training data

[WinoGrande-XL](https://huggingface.co/datasets/winogrande) reformatted the following way:
1. Each sentence was split on "`_`" placeholder symbol.
2. Each option was concatenated with the second part of the split, thus transforming each example into two text segment pairs.
3. Text segment pairs corresponding to correct and incorrect options were marked with `True` and `False` labels accordingly.
4. Text segment pairs were shuffled thereafter.

For example,

```json
{
  "answer": "2",
  "option1": "plant",
  "option2": "urn",
  "sentence": "The plant took up too much room in the urn, because the _ was small."
}
```

becomes

```json
{
  "sentence1": "The plant took up too much room in the urn, because the ",
  "sentence2": "plant was small.",
  "label": false
}
```

and

```json
{
  "sentence1": "The plant took up too much room in the urn, because the ",
  "sentence2": "urn was small.",
  "label": true
}
```
These sentence pairs are then treated as independent examples.

### BibTeX entry and citation info

```bibtex
@article{sakaguchi2019winogrande,
    title={WinoGrande: An Adversarial Winograd Schema Challenge at Scale},
    author={Sakaguchi, Keisuke and Bras, Ronan Le and Bhagavatula, Chandra and Choi, Yejin},
    journal={arXiv preprint arXiv:1907.10641},
    year={2019}
}

@article{DBLP:journals/corr/abs-1907-11692,
  author    = {Yinhan Liu and
               Myle Ott and
               Naman Goyal and
               Jingfei Du and
               Mandar Joshi and
               Danqi Chen and
               Omer Levy and
               Mike Lewis and
               Luke Zettlemoyer and
               Veselin Stoyanov},
  title     = {RoBERTa: {A} Robustly Optimized {BERT} Pretraining Approach},
  journal   = {CoRR},
  volume    = {abs/1907.11692},
  year      = {2019},
  url       = {http://arxiv.org/abs/1907.11692},
  archivePrefix = {arXiv},
  eprint    = {1907.11692},
  timestamp = {Thu, 01 Aug 2019 08:59:33 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1907-11692.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
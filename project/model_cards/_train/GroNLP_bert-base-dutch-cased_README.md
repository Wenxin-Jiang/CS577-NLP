---
language: nl
thumbnail: "https://raw.githubusercontent.com/wietsedv/bertje/master/bertje.png"
tags:
- BERTje
---

# BERTje: A Dutch BERT model
[Wietse de Vries](https://www.semanticscholar.org/author/Wietse-de-Vries/144611157) •
[Andreas van Cranenburgh](https://www.semanticscholar.org/author/Andreas-van-Cranenburgh/2791585) •
[Arianna Bisazza](https://www.semanticscholar.org/author/Arianna-Bisazza/3242253) •
[Tommaso Caselli](https://www.semanticscholar.org/author/Tommaso-Caselli/1864635) •
[Gertjan van Noord](https://www.semanticscholar.org/author/Gertjan-van-Noord/143715131) •
[Malvina Nissim](https://www.semanticscholar.org/author/M.-Nissim/2742475)

## Model description

BERTje is a Dutch pre-trained BERT model developed at the University of Groningen.

<img src="https://raw.githubusercontent.com/wietsedv/bertje/master/bertje.png" height="250">

For details, check out our paper on [arXiv](https://arxiv.org/abs/1912.09582), the code on [Github](https://github.com/wietsedv/bertje) and related work on [Semantic Scholar](https://www.semanticscholar.org/paper/BERTje%3A-A-Dutch-BERT-Model-Vries-Cranenburgh/a4d5e425cac0bf84c86c0c9f720b6339d6288ffa).

The paper and Github page mention fine-tuned models that are available [here](https://huggingface.co/wietsedv).

## How to use

```python
from transformers import AutoTokenizer, AutoModel, TFAutoModel

tokenizer = AutoTokenizer.from_pretrained("GroNLP/bert-base-dutch-cased")
model = AutoModel.from_pretrained("GroNLP/bert-base-dutch-cased")  # PyTorch
model = TFAutoModel.from_pretrained("GroNLP/bert-base-dutch-cased")  # Tensorflow
```

**WARNING:** The vocabulary size of BERTje has changed in 2021. If you use an older fine-tuned model and experience problems with the `GroNLP/bert-base-dutch-cased` tokenizer, use use the following tokenizer:

```python
tokenizer = AutoTokenizer.from_pretrained("GroNLP/bert-base-dutch-cased", revision="v1")  # v1 is the old vocabulary
```

## Benchmarks

The arXiv paper lists benchmarks. Here are a couple of comparisons between BERTje, multilingual BERT, BERT-NL and RobBERT that were done after writing the paper. Unlike some other comparisons, the fine-tuning procedures for these benchmarks are identical for each pre-trained model. You may be able to achieve higher scores for individual models by optimizing fine-tuning procedures.

More experimental results will be added to this page when they are finished. Technical details about how a fine-tuned these models will be published later as well as downloadable fine-tuned checkpoints.

All of the tested models are *base* sized (12) layers with cased tokenization.

Headers in the tables below link to original data sources. Scores link to the model pages that corresponds to that specific fine-tuned model. These tables will be updated when more simple fine-tuned models are made available.


### Named Entity Recognition


| Model                                                                        | [CoNLL-2002](https://www.clips.uantwerpen.be/conll2002/ner/)                                  | [SoNaR-1](https://ivdnt.org/downloads/taalmaterialen/tstc-sonar-corpus)                   | spaCy UD LassySmall                                                                             |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **BERTje**                                                                   | [**90.24**](https://huggingface.co/wietsedv/bert-base-dutch-cased-finetuned-conll2002-ner)    | [**84.93**](https://huggingface.co/wietsedv/bert-base-dutch-cased-finetuned-sonar-ner)    | [86.10](https://huggingface.co/wietsedv/bert-base-dutch-cased-finetuned-udlassy-ner)            |
| [mBERT](https://github.com/google-research/bert/blob/master/multilingual.md) | [88.61](https://huggingface.co/wietsedv/bert-base-multilingual-cased-finetuned-conll2002-ner) | [84.19](https://huggingface.co/wietsedv/bert-base-multilingual-cased-finetuned-sonar-ner) | [**86.77**](https://huggingface.co/wietsedv/bert-base-multilingual-cased-finetuned-udlassy-ner) |
| [BERT-NL](http://textdata.nl)                                                | 85.05                                                                                         | 80.45                                                                                     | 81.62                                                                                           |
| [RobBERT](https://github.com/iPieter/RobBERT)                                | 84.72                                                                                         | 81.98                                                                                     | 79.84                                                                                           |

### Part-of-speech tagging

| Model                                                                        | [UDv2.5 LassySmall](https://universaldependencies.org/treebanks/nl_lassysmall/index.html) |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **BERTje**                                                                   | **96.48**                                                                                 |
| [mBERT](https://github.com/google-research/bert/blob/master/multilingual.md) | 96.20                                                                                     |
| [BERT-NL](http://textdata.nl)                                                | 96.10                                                                                     |
| [RobBERT](https://github.com/iPieter/RobBERT)                                | 95.91                                                                                     |



### BibTeX entry and citation info

```bibtex
@misc{devries2019bertje,
\ttitle = {{BERTje}: {A} {Dutch} {BERT} {Model}},
\tshorttitle = {{BERTje}},
\tauthor = {de Vries, Wietse  and  van Cranenburgh, Andreas  and  Bisazza, Arianna  and  Caselli, Tommaso  and  Noord, Gertjan van  and  Nissim, Malvina},
\tyear = {2019},
\tmonth = dec,
\thowpublished = {arXiv:1912.09582},
\turl = {http://arxiv.org/abs/1912.09582},
}
```

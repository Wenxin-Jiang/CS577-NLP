---
language: 
- multilingual
- af
- am
- ar
- as
- az
- be
- bg
- bn
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- no
- om
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sa
- sd
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- th
- tl
- tr
- ug
- uk
- ur
- uz
- vi
- xh
- yi
- zh
tags:
- Dialectal Arabic
- Arabic
- sequence labeling
- Named entity recognition
- Part-of-speech tagging
- Zero-shot transfer learning
- bert
license: "mit"
---

# Dialectal Arabic XLM-R Base

This is a repo of the language model used for "AdaSL: An Unsupervised Domain Adaptation framework for Arabic multi-dialectal Sequence Labeling". The state-of-the-art method for sequence labeling on multi-dialect Arabic.

### About the Dialectal-Arabic-XLM-R-Base model

This model is an trained as a further pre-trained of XLM-RoBERTa base using the Masked-language modeling on a dialectal Arabic corpus.

### About the Dialectal-Arabic-XLM-R-Base model training corpora

We have built a 5 million Tweets corpus from Twitter. The crawled tweets cover the dialects of the four Arabic world regions (EGY, GLF, LEV, and MAG regions), as well as MSA. The collected corpus consists of one million (1M) tweets per Arabic variant. We did not perform any text pre-processing on the tweets, except by removing tweets that have a small length (tweets containing less than four words).

### Usage
The model weights can be loaded using `transformers` library by HuggingFace.

```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("3ebdola/Dialectal-Arabic-XLM-R-Base")
model = AutoModel.from_pretrained("3ebdola/Dialectal-Arabic-XLM-R-Base")
text = "هذا مثال لنص باللغة العربية, يمكنك استعمال اللهجات العربية أيضا"
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

### Citation

```
@article{ELMEKKI2022102964,
title = {AdaSL: An Unsupervised Domain Adaptation framework for Arabic multi-dialectal Sequence Labeling},
journal = {Information Processing & Management},
volume = {59},
number = {4},
pages = {102964},
year = {2022},
issn = {0306-4573},
doi = {https://doi.org/10.1016/j.ipm.2022.102964},
url = {https://www.sciencedirect.com/science/article/pii/S0306457322000814},
author = {Abdellah {El Mekki} and Abdelkader {El Mahdaouy} and Ismail Berrada and Ahmed Khoumsi},
keywords = {Dialectal Arabic, Arabic natural language processing, Domain adaptation, Multi-dialectal sequence labeling, Named entity recognition, Part-of-speech tagging, Zero-shot transfer learning}
}
```

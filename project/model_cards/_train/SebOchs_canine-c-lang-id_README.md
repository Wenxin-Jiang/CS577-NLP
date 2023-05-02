---
language:
- ace
- af
- als
- am
- an
- ang
- ar
- arz
- as
- ast
- av
- ay
- az
- azb
- ba
- bar
- bcl
- be
- bg
- bho
- bjn
- bn
- bo
- bpy
- br
- bs
- bxr
- ca
- cbk
- cdo
- ce
- ceb
- chr
- ckb
- co
- crh
- cs
- csb
- cv
- cy
- da
- de
- diq
- dsb
- dty
- dv
- egl
- el
- en
- eo
- es
- et
- eu
- ext
- fa
- fi
- fo
- fr
- frp
- fur
- fy
- ga
- gag
- gd
- gl
- glk
- gn
- gu
- gv
- ha
- hak
- he
- hi
- hif
- hr
- hsb
- ht
- hu
- hy
- ia
- id
- ie
- ig
- ilo
- io
- is
- it
- ja
- jam
- jbo
- jv
- ka
- kaa
- kab
- kbd
- kk
- km
- kn
- ko
- koi
- kok
- krc
- ksh
- ku
- kv
- kw
- ky
- la
- lad
- lb
- lez
- lg
- li
- lij
- lmo
- ln
- lo
- lrc
- lt
- ltg
- lv
- lzh
- mai
- map
- mdf
- mg
- mhr
- mi
- min
- mk
- ml
- mn
- mr
- mrj
- ms
- mt
- mwl
- my
- myv
- mzn
- nan
- nap
- nb
- nci
- nds
- ne
- new
- nl
- nn
- nrm
- nso
- nv
- oc
- olo
- om
- or
- os
- pa
- pag
- pam
- pap
- pcd
- pdc
- pfl
- pl
- pnb
- ps
- pt
- qu
- rm
- ro
- roa
- ru
- rue
- rup
- rw
- sa
- sah
- sc
- scn
- sco
- sd
- sgs
- sh
- si
- sk
- sl
- sme
- sn
- so
- sq
- sr
- srn
- stq
- su
- sv
- sw
- szl
- ta
- tcy
- te
- tet
- tg
- th
- tk
- tl
- tn
- to
- tr
- tt
- tyv
- udm
- ug
- uk
- ur
- uz
- vec
- vep
- vi
- vls
- vo
- vro
- wa
- war
- wo
- wuu
- xh
- xmf
- yi
- yo
- zea
- zh
- multilingual
license: apache-2.0
tags:
- Language Identification
datasets:
- wili_2018
metrics:
- accuracy
- macro F1-score
language_bcp47:
- be-tarask
- map-bms
- nds-nl
- roa-tara
- zh-yue
---
# Canine for Language Identification
Canine model trained on WiLI-2018 dataset to identify the language of a text.

### Preprocessing
  - 10% of train data stratified sampled as validation set
  - max sequence length: 512

### Hyperparameters
  - epochs: 4
  - learning-rate: 3e-5
  - batch size: 16
  - gradient_accumulation: 4
  - optimizer: AdamW with default settings

### Test Results
  - Accuracy: 94,92%
  - Macro F1-score: 94,91%

### Inference
Dictionary to return English names for a label id:
```python
import datasets
import pycountry
def int_to_lang():
    dataset = datasets.load_dataset('wili_2018')
    # names for languages not in iso-639-3 from wikipedia
    non_iso_languages = {'roa-tara': 'Tarantino', 'zh-yue': 'Cantonese', 'map-bms': 'Banyumasan',
                         'nds-nl': 'Dutch Low Saxon', 'be-tarask': 'Belarusian'}
    # create dictionary from data set labels to language names
    lab_to_lang = {}
    for i, lang in enumerate(dataset['train'].features['label'].names):
        full_lang = pycountry.languages.get(alpha_3=lang)
        if full_lang:
            lab_to_lang[i] = full_lang.name
        else:
            lab_to_lang[i] = non_iso_languages[lang]
    return lab_to_lang
```

### Credit to 
```
@article{clark-etal-2022-canine,
    title = "Canine: Pre-training an Efficient Tokenization-Free Encoder for Language Representation",
    author = "Clark, Jonathan H.  and
      Garrette, Dan  and
      Turc, Iulia  and
      Wieting, John",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "10",
    year = "2022",
    address = "Cambridge, MA",
    publisher = "MIT Press",
    url = "https://aclanthology.org/2022.tacl-1.5",
    doi = "10.1162/tacl_a_00448",
    pages = "73--91",
    abstract = "Pipelined NLP systems have largely been superseded by end-to-end neural modeling, yet nearly all commonly used models still require an explicit tokenization step. While recent tokenization approaches based on data-derived subword lexicons are less brittle than manually engineered tokenizers, these techniques are not equally suited to all languages, and the use of any fixed vocabulary may limit a model{'}s ability to adapt. In this paper, we present Canine, a neural encoder that operates directly on character sequences{---}without explicit tokenization or vocabulary{---}and a pre-training strategy that operates either directly on characters or optionally uses subwords as a soft inductive bias. To use its finer-grained input effectively and efficiently, Canine combines downsampling, which reduces the input sequence length, with a deep transformer stack, which encodes context. Canine outperforms a comparable mBert model by 5.7 F1 on TyDi QA, a challenging multilingual benchmark, despite having fewer model parameters.",
}
@dataset{thoma_martin_2018_841984,
  author       = {Thoma, Martin},
  title        = {{WiLI-2018 - Wikipedia Language Identification 
                   database}},
  month        = jan,
  year         = 2018,
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.841984},
  url          = {https://doi.org/10.5281/zenodo.841984}
}
```


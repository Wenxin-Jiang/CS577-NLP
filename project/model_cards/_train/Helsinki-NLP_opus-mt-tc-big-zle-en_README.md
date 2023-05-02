---
language:
- be
- en
- ru
- uk
- zle
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-zle-en
  results:
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 35.2
  - task:
      name: Translation ukr-eng
      type: translation
      args: ukr-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 39.2
  - task:
      name: Translation bel-eng
      type: translation
      args: bel-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bel-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 48.1
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 57.4
  - task:
      name: Translation ukr-eng
      type: translation
      args: ukr-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 56.9
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: tico19-test
      type: tico19-test
      args: rus-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 33.3
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: rus-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 39.2
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: rus-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 31.3
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: newstest2014
      type: wmt-2014-news
      args: rus-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 40.5
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: newstest2015
      type: wmt-2015-news
      args: rus-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 36.1
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: newstest2016
      type: wmt-2016-news
      args: rus-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 35.7
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: newstest2017
      type: wmt-2017-news
      args: rus-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 40.8
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: newstest2018
      type: wmt-2018-news
      args: rus-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 35.2
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: newstest2019
      type: wmt-2019-news
      args: rus-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 41.6
  - task:
      name: Translation rus-eng
      type: translation
      args: rus-eng
    dataset:
      name: newstest2020
      type: wmt-2020-news
      args: rus-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 36.9
---
# opus-mt-tc-big-zle-en

Neural machine translation model for translating from East Slavic languages (zle) to English (en).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).

* Publications: [OPUS-MT – Building open translation services for the World](https://aclanthology.org/2020.eamt-1.61/) and [The Tatoeba Translation Challenge – Realistic Data Sets for Low Resource and Multilingual MT](https://aclanthology.org/2020.wmt-1.139/) (Please, cite if you use this model.)

```
@inproceedings{tiedemann-thottingal-2020-opus,
    title = "{OPUS}-{MT} {--} Building open translation services for the World",
    author = {Tiedemann, J{\"o}rg  and Thottingal, Santhosh},
    booktitle = "Proceedings of the 22nd Annual Conference of the European Association for Machine Translation",
    month = nov,
    year = "2020",
    address = "Lisboa, Portugal",
    publisher = "European Association for Machine Translation",
    url = "https://aclanthology.org/2020.eamt-1.61",
    pages = "479--480",
}

@inproceedings{tiedemann-2020-tatoeba,
    title = "The Tatoeba Translation Challenge {--} Realistic Data Sets for Low Resource and Multilingual {MT}",
    author = {Tiedemann, J{\"o}rg},
    booktitle = "Proceedings of the Fifth Conference on Machine Translation",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.wmt-1.139",
    pages = "1174--1182",
}
```

## Model info

* Release: 2022-03-17
* source language(s): bel rus ukr
* target language(s): eng
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-eng/opusTCv20210807+bt_transformer-big_2022-03-17.zip)
* more information released models: [OPUS-MT zle-eng README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-eng/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "Скільки мені слід купити пива?",
    "Я клієнтка."
]

model_name = "pytorch-models/opus-mt-tc-big-zle-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     How much beer should I buy?
#     I'm a client.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zle-en")
print(pipe("Скільки мені слід купити пива?"))

# expected output: How much beer should I buy?
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-eng/opusTCv20210807+bt_transformer-big_2022-03-17.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-eng/opusTCv20210807+bt_transformer-big_2022-03-17.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| bel-eng | tatoeba-test-v2021-08-07 | 0.65221 | 48.1 | 2500 | 18571 |
| rus-eng | tatoeba-test-v2021-08-07 | 0.71452 | 57.4 | 19425 | 147872 |
| ukr-eng | tatoeba-test-v2021-08-07 | 0.71162 | 56.9 | 13127 | 88607 |
| bel-eng | flores101-devtest | 0.51689 | 18.1 | 1012 | 24721 |
| rus-eng | flores101-devtest | 0.62581 | 35.2 | 1012 | 24721 |
| ukr-eng | flores101-devtest | 0.65001 | 39.2 | 1012 | 24721 |
| rus-eng | newstest2012 | 0.63724 | 39.2 | 3003 | 72812 |
| rus-eng | newstest2013 | 0.57641 | 31.3 | 3000 | 64505 |
| rus-eng | newstest2014 | 0.65667 | 40.5 | 3003 | 69190 |
| rus-eng | newstest2015 | 0.61747 | 36.1 | 2818 | 64428 |
| rus-eng | newstest2016 | 0.61414 | 35.7 | 2998 | 69278 |
| rus-eng | newstest2017 | 0.65365 | 40.8 | 3001 | 69025 |
| rus-eng | newstest2018 | 0.61386 | 35.2 | 3000 | 71291 |
| rus-eng | newstest2019 | 0.65476 | 41.6 | 2000 | 42642 |
| rus-eng | newstest2020 | 0.64878 | 36.9 | 991 | 20217 |
| rus-eng | newstestB2020 | 0.65685 | 39.3 | 991 | 20423 |
| rus-eng | tico19-test | 0.63280 | 33.3 | 2100 | 56323 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Wed Mar 23 22:17:11 EET 2022
* port machine: LM0-400-22516.local

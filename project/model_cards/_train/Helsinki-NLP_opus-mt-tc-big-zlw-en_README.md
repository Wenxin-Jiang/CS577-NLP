---
language:
- cs
- dsb
- en
- hsb
- pl
- zlw
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-zlw-en
  results:
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ces eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 41.2
  - task:
      name: Translation pol-eng
      type: translation
      args: pol-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: pol eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 29.6
  - task:
      name: Translation slk-eng
      type: translation
      args: slk-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: slk eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 40.0
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: multi30k_test_2016_flickr
      type: multi30k-2016_flickr
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 37.6
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: multi30k_test_2018_flickr
      type: multi30k-2018_flickr
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 37.4
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: news-test2008
      type: news-test2008
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 26.3
  - task:
      name: Translation pol-eng
      type: translation
      args: pol-eng
    dataset:
      name: newsdev2020
      type: newsdev2020
      args: pol-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 32.7
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 57.4
  - task:
      name: Translation pol-eng
      type: translation
      args: pol-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: pol-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 55.7
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 29.5
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: newstest2010
      type: wmt-2010-news
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 30.7
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: newstest2011
      type: wmt-2011-news
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 30.9
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 29.4
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 32.8
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: newstest2014
      type: wmt-2014-news
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 38.7
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: newstest2015
      type: wmt-2015-news
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 33.4
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: newstest2016
      type: wmt-2016-news
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 37.1
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: newstest2017
      type: wmt-2017-news
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 32.5
  - task:
      name: Translation ces-eng
      type: translation
      args: ces-eng
    dataset:
      name: newstest2018
      type: wmt-2018-news
      args: ces-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 33.1
  - task:
      name: Translation pol-eng
      type: translation
      args: pol-eng
    dataset:
      name: newstest2020
      type: wmt-2020-news
      args: pol-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 32.6
---
# opus-mt-tc-big-zlw-en

Neural machine translation model for translating from West Slavic languages (zlw) to English (en).

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
* source language(s): ces dsb hsb pol
* target language(s): eng
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-eng/opusTCv20210807+bt_transformer-big_2022-03-17.zip)
* more information released models: [OPUS-MT zlw-eng README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zlw-eng/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "Aoi'ego hobby to tańczenie.",
    "Myślisz, że Tom planuje to zrobić?"
]

model_name = "pytorch-models/opus-mt-tc-big-zlw-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Aoi's hobby is dancing.
#     You think Tom's planning on doing that?
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zlw-en")
print(pipe("Aoi'ego hobby to tańczenie."))

# expected output: Aoi's hobby is dancing.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-eng/opusTCv20210807+bt_transformer-big_2022-03-17.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-eng/opusTCv20210807+bt_transformer-big_2022-03-17.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| ces-eng | tatoeba-test-v2021-08-07 | 0.71861 | 57.4 | 13824 | 105010 |
| pol-eng | tatoeba-test-v2021-08-07 | 0.70544 | 55.7 | 10099 | 75766 |
| ces-eng | flores101-devtest | 0.66444 | 41.2 | 1012 | 24721 |
| pol-eng | flores101-devtest | 0.58301 | 29.6 | 1012 | 24721 |
| slk-eng | flores101-devtest | 0.66103 | 40.0 | 1012 | 24721 |
| ces-eng | multi30k_test_2016_flickr | 0.61482 | 37.6 | 1000 | 12955 |
| ces-eng | multi30k_test_2018_flickr | 0.61405 | 37.4 | 1071 | 14689 |
| pol-eng | newsdev2020 | 0.60478 | 32.7 | 2000 | 46654 |
| ces-eng | newssyscomb2009 | 0.56495 | 30.2 | 502 | 11818 |
| ces-eng | news-test2008 | 0.54300 | 26.3 | 2051 | 49380 |
| ces-eng | newstest2009 | 0.56309 | 29.5 | 2525 | 65399 |
| ces-eng | newstest2010 | 0.57778 | 30.7 | 2489 | 61711 |
| ces-eng | newstest2011 | 0.57336 | 30.9 | 3003 | 74681 |
| ces-eng | newstest2012 | 0.56761 | 29.4 | 3003 | 72812 |
| ces-eng | newstest2013 | 0.58809 | 32.8 | 3000 | 64505 |
| ces-eng | newstest2014 | 0.64401 | 38.7 | 3003 | 68065 |
| ces-eng | newstest2015 | 0.58607 | 33.4 | 2656 | 53569 |
| ces-eng | newstest2016 | 0.61780 | 37.1 | 2999 | 64670 |
| ces-eng | newstest2017 | 0.58259 | 32.5 | 3005 | 61721 |
| ces-eng | newstest2018 | 0.58677 | 33.1 | 2983 | 63495 |
| pol-eng | newstest2020 | 0.60047 | 32.6 | 1001 | 21755 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 20:19:48 EEST 2022
* port machine: LM0-400-22516.local

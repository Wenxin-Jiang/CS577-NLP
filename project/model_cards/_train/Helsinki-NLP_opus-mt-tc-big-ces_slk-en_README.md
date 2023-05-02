---
language:
- cs
- en
- sk
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-ces_slk-en
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
      value: 40.1
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
      value: 38.6
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
      value: 37.9
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
      value: 26.2
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
      value: 57.7
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
      value: 28.8
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
      value: 30.3
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
      value: 30.3
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
      value: 33.1
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
      value: 38.3
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
      value: 33.6
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
      value: 36.8
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
      value: 32.3
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
      value: 33.0
---
# opus-mt-tc-big-ces_slk-en

Neural machine translation model for translating from Czech and Slovak (ces+slk) to English (en).

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
* source language(s): ces
* target language(s): eng
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ces+slk-eng/opusTCv20210807+bt_transformer-big_2022-03-17.zip)
* more information released models: [OPUS-MT ces+slk-eng README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ces+slk-eng/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "Podívej se na své kalhoty! Zapni si je na zip.",
    "Mrzí mě, že Tom odchází."
]

model_name = "pytorch-models/opus-mt-tc-big-ces_slk-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Look at your pants, zip them up.
#     I'm sorry Tom's leaving.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-ces_slk-en")
print(pipe("Podívej se na své kalhoty! Zapni si je na zip."))

# expected output: Look at your pants, zip them up.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ces+slk-eng/opusTCv20210807+bt_transformer-big_2022-03-17.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ces+slk-eng/opusTCv20210807+bt_transformer-big_2022-03-17.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| ces-eng | tatoeba-test-v2021-08-07 | 0.72120 | 57.7 | 13824 | 105010 |
| ces-eng | flores101-devtest | 0.66511 | 41.2 | 1012 | 24721 |
| slk-eng | flores101-devtest | 0.66084 | 40.1 | 1012 | 24721 |
| ces-eng | multi30k_test_2016_flickr | 0.62216 | 38.6 | 1000 | 12955 |
| ces-eng | multi30k_test_2018_flickr | 0.61838 | 37.9 | 1071 | 14689 |
| ces-eng | newssyscomb2009 | 0.56380 | 29.9 | 502 | 11818 |
| ces-eng | news-test2008 | 0.54071 | 26.2 | 2051 | 49380 |
| ces-eng | newstest2009 | 0.55871 | 28.8 | 2525 | 65399 |
| ces-eng | newstest2010 | 0.57634 | 30.3 | 2489 | 61711 |
| ces-eng | newstest2011 | 0.57002 | 30.3 | 3003 | 74681 |
| ces-eng | newstest2012 | 0.56564 | 29.4 | 3003 | 72812 |
| ces-eng | newstest2013 | 0.58723 | 33.1 | 3000 | 64505 |
| ces-eng | newstest2014 | 0.64192 | 38.3 | 3003 | 68065 |
| ces-eng | newstest2015 | 0.58688 | 33.6 | 2656 | 53569 |
| ces-eng | newstest2016 | 0.61544 | 36.8 | 2999 | 64670 |
| ces-eng | newstest2017 | 0.58085 | 32.3 | 3005 | 61721 |
| ces-eng | newstest2018 | 0.58627 | 33.0 | 2983 | 63495 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 18:42:25 EEST 2022
* port machine: LM0-400-22516.local

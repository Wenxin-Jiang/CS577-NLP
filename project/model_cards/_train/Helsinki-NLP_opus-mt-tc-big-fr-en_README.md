---
language:
- en
- fr
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-fr-en
  results:
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 46.0
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: multi30k_test_2016_flickr
      type: multi30k-2016_flickr
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 49.7
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: multi30k_test_2017_flickr
      type: multi30k-2017_flickr
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 52.0
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: multi30k_test_2017_mscoco
      type: multi30k-2017_mscoco
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 50.6
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: multi30k_test_2018_flickr
      type: multi30k-2018_flickr
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 44.9
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: news-test2008
      type: news-test2008
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 26.5
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: newsdiscussdev2015
      type: newsdiscussdev2015
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 34.4
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: newsdiscusstest2015
      type: newsdiscusstest2015
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 40.2
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 59.8
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: tico19-test
      type: tico19-test
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 41.3
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 30.4
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: newstest2010
      type: wmt-2010-news
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 33.4
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: newstest2011
      type: wmt-2011-news
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 33.8
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 33.6
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 34.8
  - task:
      name: Translation fra-eng
      type: translation
      args: fra-eng
    dataset:
      name: newstest2014
      type: wmt-2014-news
      args: fra-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 39.4
---
# opus-mt-tc-big-fr-en

Neural machine translation model for translating from French (fr) to English (en).

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

* Release: 2022-03-09
* source language(s): fra
* target language(s): eng
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-09.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-eng/opusTCv20210807+bt_transformer-big_2022-03-09.zip)
* more information released models: [OPUS-MT fra-eng README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fra-eng/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "J'ai adoré l'Angleterre.",
    "C'était la seule chose à faire."
]

model_name = "pytorch-models/opus-mt-tc-big-fr-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     I loved England.
#     It was the only thing to do.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-fr-en")
print(pipe("J'ai adoré l'Angleterre."))

# expected output: I loved England.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-09.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-eng/opusTCv20210807+bt_transformer-big_2022-03-09.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-09.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-eng/opusTCv20210807+bt_transformer-big_2022-03-09.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| fra-eng | tatoeba-test-v2021-08-07 | 0.73772 | 59.8 | 12681 | 101754 |
| fra-eng | flores101-devtest | 0.69350 | 46.0 | 1012 | 24721 |
| fra-eng | multi30k_test_2016_flickr | 0.68005 | 49.7 | 1000 | 12955 |
| fra-eng | multi30k_test_2017_flickr | 0.70596 | 52.0 | 1000 | 11374 |
| fra-eng | multi30k_test_2017_mscoco | 0.69356 | 50.6 | 461 | 5231 |
| fra-eng | multi30k_test_2018_flickr | 0.65751 | 44.9 | 1071 | 14689 |
| fra-eng | newsdiscussdev2015 | 0.59008 | 34.4 | 1500 | 27759 |
| fra-eng | newsdiscusstest2015 | 0.62603 | 40.2 | 1500 | 26982 |
| fra-eng | newssyscomb2009 | 0.57488 | 31.1 | 502 | 11818 |
| fra-eng | news-test2008 | 0.54316 | 26.5 | 2051 | 49380 |
| fra-eng | newstest2009 | 0.56959 | 30.4 | 2525 | 65399 |
| fra-eng | newstest2010 | 0.59561 | 33.4 | 2489 | 61711 |
| fra-eng | newstest2011 | 0.60271 | 33.8 | 3003 | 74681 |
| fra-eng | newstest2012 | 0.59507 | 33.6 | 3003 | 72812 |
| fra-eng | newstest2013 | 0.59691 | 34.8 | 3000 | 64505 |
| fra-eng | newstest2014 | 0.64533 | 39.4 | 3003 | 70708 |
| fra-eng | tico19-test | 0.63326 | 41.3 | 2100 | 56323 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 19:02:28 EEST 2022
* port machine: LM0-400-22516.local

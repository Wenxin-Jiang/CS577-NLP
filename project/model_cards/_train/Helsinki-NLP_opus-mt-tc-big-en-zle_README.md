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
- name: opus-mt-tc-big-en-zle
  results:
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 32.7
  - task:
      name: Translation eng-ukr
      type: translation
      args: eng-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 32.1
  - task:
      name: Translation eng-bel
      type: translation
      args: eng-bel
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-bel
    metrics:
    - name: BLEU
      type: bleu
      value: 24.9
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 45.5
  - task:
      name: Translation eng-ukr
      type: translation
      args: eng-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 37.7
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: tico19-test
      type: tico19-test
      args: eng-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 33.7
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: eng-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 36.8
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: eng-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 26.9
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: newstest2014
      type: wmt-2014-news
      args: eng-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 43.5
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: newstest2015
      type: wmt-2015-news
      args: eng-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 34.9
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: newstest2016
      type: wmt-2016-news
      args: eng-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 33.1
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: newstest2017
      type: wmt-2017-news
      args: eng-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 37.3
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: newstest2018
      type: wmt-2018-news
      args: eng-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 32.9
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: newstest2019
      type: wmt-2019-news
      args: eng-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 31.8
  - task:
      name: Translation eng-rus
      type: translation
      args: eng-rus
    dataset:
      name: newstest2020
      type: wmt-2020-news
      args: eng-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 25.5
---
# opus-mt-tc-big-en-zle

Neural machine translation model for translating from English (en) to East Slavic languages (zle).

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

* Release: 2022-03-13
* source language(s): eng
* target language(s): bel rus ukr
* valid target language labels: >>bel<< >>rus<< >>ukr<<
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-13.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zle/opusTCv20210807+bt_transformer-big_2022-03-13.zip)
* more information released models: [OPUS-MT eng-zle README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-zle/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>bel<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>rus<< Are they coming as well?",
    ">>rus<< I didn't let Tom do what he wanted to do."
]

model_name = "pytorch-models/opus-mt-tc-big-en-zle"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Они тоже приедут?
#     Я не позволил Тому сделать то, что он хотел.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-zle")
print(pipe(">>rus<< Are they coming as well?"))

# expected output: Они тоже приедут?
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-13.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zle/opusTCv20210807+bt_transformer-big_2022-03-13.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-13.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zle/opusTCv20210807+bt_transformer-big_2022-03-13.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| eng-bel | tatoeba-test-v2021-08-07 | 0.50345 | 24.9 | 2500 | 16237 |
| eng-rus | tatoeba-test-v2021-08-07 | 0.66182 | 45.5 | 19425 | 134296 |
| eng-ukr | tatoeba-test-v2021-08-07 | 0.60175 | 37.7 | 13127 | 80998 |
| eng-bel | flores101-devtest | 0.42078 | 11.2 | 1012 | 24829 |
| eng-rus | flores101-devtest | 0.59654 | 32.7 | 1012 | 23295 |
| eng-ukr | flores101-devtest | 0.60131 | 32.1 | 1012 | 22810 |
| eng-rus | newstest2012 | 0.62842 | 36.8 | 3003 | 64790 |
| eng-rus | newstest2013 | 0.54627 | 26.9 | 3000 | 58560 |
| eng-rus | newstest2014 | 0.68348 | 43.5 | 3003 | 61603 |
| eng-rus | newstest2015 | 0.62621 | 34.9 | 2818 | 55915 |
| eng-rus | newstest2016 | 0.60595 | 33.1 | 2998 | 62014 |
| eng-rus | newstest2017 | 0.64249 | 37.3 | 3001 | 60253 |
| eng-rus | newstest2018 | 0.61219 | 32.9 | 3000 | 61907 |
| eng-rus | newstest2019 | 0.57902 | 31.8 | 1997 | 48147 |
| eng-rus | newstest2020 | 0.52939 | 25.5 | 2002 | 47083 |
| eng-rus | tico19-test | 0.59314 | 33.7 | 2100 | 55843 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Thu Mar 24 01:58:40 EET 2022
* port machine: LM0-400-22516.local

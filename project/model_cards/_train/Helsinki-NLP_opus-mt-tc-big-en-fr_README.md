---
language:
- en
- fr
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-en-fr
  results:
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng fra devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 52.2
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: multi30k_test_2016_flickr
      type: multi30k-2016_flickr
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 52.4
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: multi30k_test_2017_flickr
      type: multi30k-2017_flickr
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 52.8
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: multi30k_test_2017_mscoco
      type: multi30k-2017_mscoco
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 54.7
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: multi30k_test_2018_flickr
      type: multi30k-2018_flickr
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 43.7
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: news-test2008
      type: news-test2008
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 27.6
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: newsdiscussdev2015
      type: newsdiscussdev2015
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 33.4
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: newsdiscusstest2015
      type: newsdiscusstest2015
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 40.3
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 53.2
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: tico19-test
      type: tico19-test
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 40.6
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 30.0
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: newstest2010
      type: wmt-2010-news
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 33.5
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: newstest2011
      type: wmt-2011-news
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 35.0
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 32.8
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 34.6
  - task:
      name: Translation eng-fra
      type: translation
      args: eng-fra
    dataset:
      name: newstest2014
      type: wmt-2014-news
      args: eng-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 41.9
---
# opus-mt-tc-big-en-fr

Neural machine translation model for translating from English (en) to French (fr).

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
* source language(s): eng
* target language(s): fra
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-09.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-fra/opusTCv20210807+bt_transformer-big_2022-03-09.zip)
* more information released models: [OPUS-MT eng-fra README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-fra/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "The Portuguese teacher is very demanding.",
    "When was your last hearing test?"
]

model_name = "pytorch-models/opus-mt-tc-big-en-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Le professeur de portugais est très exigeant.
#     Quand a eu lieu votre dernier test auditif ?
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-fr")
print(pipe("The Portuguese teacher is very demanding."))

# expected output: Le professeur de portugais est très exigeant.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-09.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-fra/opusTCv20210807+bt_transformer-big_2022-03-09.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-09.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-fra/opusTCv20210807+bt_transformer-big_2022-03-09.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| eng-fra | tatoeba-test-v2021-08-07 | 0.69621 | 53.2 | 12681 | 106378 |
| eng-fra | flores101-devtest | 0.72494 | 52.2 | 1012 | 28343 |
| eng-fra | multi30k_test_2016_flickr | 0.72361 | 52.4 | 1000 | 13505 |
| eng-fra | multi30k_test_2017_flickr | 0.72826 | 52.8 | 1000 | 12118 |
| eng-fra | multi30k_test_2017_mscoco | 0.73547 | 54.7 | 461 | 5484 |
| eng-fra | multi30k_test_2018_flickr | 0.66723 | 43.7 | 1071 | 15867 |
| eng-fra | newsdiscussdev2015 | 0.60471 | 33.4 | 1500 | 27940 |
| eng-fra | newsdiscusstest2015 | 0.64915 | 40.3 | 1500 | 27975 |
| eng-fra | newssyscomb2009 | 0.58903 | 30.7 | 502 | 12331 |
| eng-fra | news-test2008 | 0.55516 | 27.6 | 2051 | 52685 |
| eng-fra | newstest2009 | 0.57907 | 30.0 | 2525 | 69263 |
| eng-fra | newstest2010 | 0.60156 | 33.5 | 2489 | 66022 |
| eng-fra | newstest2011 | 0.61632 | 35.0 | 3003 | 80626 |
| eng-fra | newstest2012 | 0.59736 | 32.8 | 3003 | 78011 |
| eng-fra | newstest2013 | 0.59700 | 34.6 | 3000 | 70037 |
| eng-fra | newstest2014 | 0.66686 | 41.9 | 3003 | 77306 |
| eng-fra | tico19-test | 0.63022 | 40.6 | 2100 | 64661 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 17:07:05 EEST 2022
* port machine: LM0-400-22516.local

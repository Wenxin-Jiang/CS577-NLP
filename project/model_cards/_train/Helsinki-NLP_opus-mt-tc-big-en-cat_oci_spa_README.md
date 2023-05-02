---
language:
- ca
- en
- es
- oc
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-en-cat_oci_spa
  results:
  - task:
      name: Translation eng-cat
      type: translation
      args: eng-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng cat devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 41.5
  - task:
      name: Translation eng-oci
      type: translation
      args: eng-oci
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng oci devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 25.4
  - task:
      name: Translation eng-spa
      type: translation
      args: eng-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng spa devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 28.1
  - task:
      name: Translation eng-spa
      type: translation
      args: eng-spa
    dataset:
      name: news-test2008
      type: news-test2008
      args: eng-spa
    metrics:
    - name: BLEU
      type: bleu
      value: 30.0
  - task:
      name: Translation eng-cat
      type: translation
      args: eng-cat
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-cat
    metrics:
    - name: BLEU
      type: bleu
      value: 47.8
  - task:
      name: Translation eng-spa
      type: translation
      args: eng-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-spa
    metrics:
    - name: BLEU
      type: bleu
      value: 57.0
  - task:
      name: Translation eng-spa
      type: translation
      args: eng-spa
    dataset:
      name: tico19-test
      type: tico19-test
      args: eng-spa
    metrics:
    - name: BLEU
      type: bleu
      value: 52.5
  - task:
      name: Translation eng-spa
      type: translation
      args: eng-spa
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: eng-spa
    metrics:
    - name: BLEU
      type: bleu
      value: 30.5
  - task:
      name: Translation eng-spa
      type: translation
      args: eng-spa
    dataset:
      name: newstest2010
      type: wmt-2010-news
      args: eng-spa
    metrics:
    - name: BLEU
      type: bleu
      value: 37.4
  - task:
      name: Translation eng-spa
      type: translation
      args: eng-spa
    dataset:
      name: newstest2011
      type: wmt-2011-news
      args: eng-spa
    metrics:
    - name: BLEU
      type: bleu
      value: 39.1
  - task:
      name: Translation eng-spa
      type: translation
      args: eng-spa
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: eng-spa
    metrics:
    - name: BLEU
      type: bleu
      value: 39.6
  - task:
      name: Translation eng-spa
      type: translation
      args: eng-spa
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: eng-spa
    metrics:
    - name: BLEU
      type: bleu
      value: 35.8
---
# opus-mt-tc-big-en-cat_oci_spa

Neural machine translation model for translating from English (en) to Catalan, Occitan and Spanish (cat+oci+spa).

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
* target language(s): cat spa
* valid target language labels: >>cat<< >>spa<<
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-13.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cat+oci+spa/opusTCv20210807+bt_transformer-big_2022-03-13.zip)
* more information released models: [OPUS-MT eng-cat+oci+spa README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-cat+oci+spa/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>cat<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>spa<< Why do you want Tom to go there with me?",
    ">>spa<< She forced him to eat spinach."
]

model_name = "pytorch-models/opus-mt-tc-big-en-cat_oci_spa"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     ¿Por qué quieres que Tom vaya conmigo?
#     Ella lo obligó a comer espinacas.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-cat_oci_spa")
print(pipe(">>spa<< Why do you want Tom to go there with me?"))

# expected output: ¿Por qué quieres que Tom vaya conmigo?
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-13.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cat+oci+spa/opusTCv20210807+bt_transformer-big_2022-03-13.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-13.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cat+oci+spa/opusTCv20210807+bt_transformer-big_2022-03-13.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| eng-cat | tatoeba-test-v2021-08-07 | 0.66414 | 47.8 | 1631 | 12344 |
| eng-spa | tatoeba-test-v2021-08-07 | 0.73725 | 57.0 | 16583 | 134710 |
| eng-cat | flores101-devtest | 0.66071 | 41.5 | 1012 | 27304 |
| eng-oci | flores101-devtest | 0.56192 | 25.4 | 1012 | 27305 |
| eng-spa | flores101-devtest | 0.56288 | 28.1 | 1012 | 29199 |
| eng-spa | newssyscomb2009 | 0.58431 | 31.4 | 502 | 12503 |
| eng-spa | news-test2008 | 0.56622 | 30.0 | 2051 | 52586 |
| eng-spa | newstest2009 | 0.57988 | 30.5 | 2525 | 68111 |
| eng-spa | newstest2010 | 0.62343 | 37.4 | 2489 | 65480 |
| eng-spa | newstest2011 | 0.62424 | 39.1 | 3003 | 79476 |
| eng-spa | newstest2012 | 0.63006 | 39.6 | 3003 | 79006 |
| eng-spa | newstest2013 | 0.60291 | 35.8 | 3000 | 70528 |
| eng-spa | tico19-test | 0.73224 | 52.5 | 2100 | 66563 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 16:40:45 EEST 2022
* port machine: LM0-400-22516.local

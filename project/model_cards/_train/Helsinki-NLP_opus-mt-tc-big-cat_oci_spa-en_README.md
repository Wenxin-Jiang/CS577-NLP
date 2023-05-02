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
- name: opus-mt-tc-big-cat_oci_spa-en
  results:
  - task:
      name: Translation cat-eng
      type: translation
      args: cat-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 45.4
  - task:
      name: Translation oci-eng
      type: translation
      args: oci-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: oci eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 37.5
  - task:
      name: Translation spa-eng
      type: translation
      args: spa-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 29.9
  - task:
      name: Translation spa-eng
      type: translation
      args: spa-eng
    dataset:
      name: news-test2008
      type: news-test2008
      args: spa-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 27.9
  - task:
      name: Translation cat-eng
      type: translation
      args: cat-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: cat-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 57.3
  - task:
      name: Translation spa-eng
      type: translation
      args: spa-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: spa-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 62.3
  - task:
      name: Translation spa-eng
      type: translation
      args: spa-eng
    dataset:
      name: tico19-test
      type: tico19-test
      args: spa-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 51.8
  - task:
      name: Translation spa-eng
      type: translation
      args: spa-eng
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: spa-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 30.2
  - task:
      name: Translation spa-eng
      type: translation
      args: spa-eng
    dataset:
      name: newstest2010
      type: wmt-2010-news
      args: spa-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 36.8
  - task:
      name: Translation spa-eng
      type: translation
      args: spa-eng
    dataset:
      name: newstest2011
      type: wmt-2011-news
      args: spa-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 34.7
  - task:
      name: Translation spa-eng
      type: translation
      args: spa-eng
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: spa-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 38.6
  - task:
      name: Translation spa-eng
      type: translation
      args: spa-eng
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: spa-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 35.3
---
# opus-mt-tc-big-cat_oci_spa-en

Neural machine translation model for translating from Catalan, Occitan and Spanish (cat+oci+spa) to English (en).

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
* source language(s): cat spa
* target language(s): eng
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-13.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cat+oci+spa-eng/opusTCv20210807+bt_transformer-big_2022-03-13.zip)
* more information released models: [OPUS-MT cat+oci+spa-eng README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cat+oci+spa-eng/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "¿Puedo hacerte una pregunta?",
    "Toca algo de música."
]

model_name = "pytorch-models/opus-mt-tc-big-cat_oci_spa-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Can I ask you a question?
#     He plays some music.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-cat_oci_spa-en")
print(pipe("¿Puedo hacerte una pregunta?"))

# expected output: Can I ask you a question?
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-13.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat+oci+spa-eng/opusTCv20210807+bt_transformer-big_2022-03-13.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-13.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat+oci+spa-eng/opusTCv20210807+bt_transformer-big_2022-03-13.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| cat-eng | tatoeba-test-v2021-08-07 | 0.72019 | 57.3 | 1631 | 12627 |
| spa-eng | tatoeba-test-v2021-08-07 | 0.76017 | 62.3 | 16583 | 138123 |
| cat-eng | flores101-devtest | 0.69572 | 45.4 | 1012 | 24721 |
| oci-eng | flores101-devtest | 0.63347 | 37.5 | 1012 | 24721 |
| spa-eng | flores101-devtest | 0.59696 | 29.9 | 1012 | 24721 |
| spa-eng | newssyscomb2009 | 0.57104 | 30.8 | 502 | 11818 |
| spa-eng | news-test2008 | 0.55440 | 27.9 | 2051 | 49380 |
| spa-eng | newstest2009 | 0.57153 | 30.2 | 2525 | 65399 |
| spa-eng | newstest2010 | 0.61890 | 36.8 | 2489 | 61711 |
| spa-eng | newstest2011 | 0.60278 | 34.7 | 3003 | 74681 |
| spa-eng | newstest2012 | 0.62760 | 38.6 | 3003 | 72812 |
| spa-eng | newstest2013 | 0.60994 | 35.3 | 3000 | 64505 |
| spa-eng | tico19-test | 0.74033 | 51.8 | 2100 | 56315 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 18:30:38 EEST 2022
* port machine: LM0-400-22516.local

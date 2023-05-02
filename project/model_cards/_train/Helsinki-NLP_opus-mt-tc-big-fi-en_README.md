---
language:
- en
- fi
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-fi-en
  results:
  - task:
      name: Translation fin-eng
      type: translation
      args: fin-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fin eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 35.4
  - task:
      name: Translation fin-eng
      type: translation
      args: fin-eng
    dataset:
      name: newsdev2015
      type: newsdev2015
      args: fin-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 28.6
  - task:
      name: Translation fin-eng
      type: translation
      args: fin-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fin-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 57.4
  - task:
      name: Translation fin-eng
      type: translation
      args: fin-eng
    dataset:
      name: newstest2015
      type: wmt-2015-news
      args: fin-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 29.9
  - task:
      name: Translation fin-eng
      type: translation
      args: fin-eng
    dataset:
      name: newstest2016
      type: wmt-2016-news
      args: fin-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 34.3
  - task:
      name: Translation fin-eng
      type: translation
      args: fin-eng
    dataset:
      name: newstest2017
      type: wmt-2017-news
      args: fin-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 37.3
  - task:
      name: Translation fin-eng
      type: translation
      args: fin-eng
    dataset:
      name: newstest2018
      type: wmt-2018-news
      args: fin-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 27.1
  - task:
      name: Translation fin-eng
      type: translation
      args: fin-eng
    dataset:
      name: newstest2019
      type: wmt-2019-news
      args: fin-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 32.7
---
# opus-mt-tc-big-fi-en

Neural machine translation model for translating from Finnish (fi) to English (en).

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

* Release: 2021-12-08
* source language(s): fin
* target language(s): eng
* model: transformer (big)
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt-2021-12-08.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opusTCv20210807+bt-2021-12-08.zip)
* more information released models: [OPUS-MT fin-eng README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fin-eng/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "Kolme kolmanteen on kaksikymmentäseitsemän.",
    "Heille syntyi poikavauva."
]

model_name = "pytorch-models/opus-mt-tc-big-fi-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-fi-en")
print(pipe("Kolme kolmanteen on kaksikymmentäseitsemän."))
```

## Benchmarks

* test set translations: [opusTCv20210807+bt-2021-12-08.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opusTCv20210807+bt-2021-12-08.test.txt)
* test set scores: [opusTCv20210807+bt-2021-12-08.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opusTCv20210807+bt-2021-12-08.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| fin-eng | tatoeba-test-v2021-08-07 | 0.72298 | 57.4 | 10690 | 80552 |
| fin-eng | flores101-devtest | 0.62521 | 35.4 | 1012 | 24721 |
| fin-eng | newsdev2015 | 0.56232 | 28.6 | 1500 | 32012 |
| fin-eng | newstest2015 | 0.57469 | 29.9 | 1370 | 27270 |
| fin-eng | newstest2016 | 0.60715 | 34.3 | 3000 | 62945 |
| fin-eng | newstest2017 | 0.63050 | 37.3 | 3002 | 61846 |
| fin-eng | newstest2018 | 0.54199 | 27.1 | 3000 | 62325 |
| fin-eng | newstest2019 | 0.59620 | 32.7 | 1996 | 36215 |
| fin-eng | newstestB2016 | 0.55472 | 27.9 | 3000 | 62945 |
| fin-eng | newstestB2017 | 0.58847 | 31.1 | 3002 | 61846 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: f084bad
* port time: Tue Mar 22 14:52:19 EET 2022
* port machine: LM0-400-22516.local

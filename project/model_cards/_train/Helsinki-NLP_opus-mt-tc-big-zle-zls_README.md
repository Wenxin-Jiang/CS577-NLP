---
language:
- be
- bg
- hr
- ru
- sh
- sl
- sr_Cyrl
- sr_Latn
- uk
- zle
- zls
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-zle-zls
  results:
  - task:
      name: Translation rus-bul
      type: translation
      args: rus-bul
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus bul devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 28.9
  - task:
      name: Translation rus-hrv
      type: translation
      args: rus-hrv
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus hrv devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 23.2
  - task:
      name: Translation rus-mkd
      type: translation
      args: rus-mkd
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus mkd devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 24.3
  - task:
      name: Translation rus-slv
      type: translation
      args: rus-slv
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus slv devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 23.1
  - task:
      name: Translation rus-srp_Cyrl
      type: translation
      args: rus-srp_Cyrl
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus srp_Cyrl devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 24.1
  - task:
      name: Translation ukr-bul
      type: translation
      args: ukr-bul
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr bul devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 30.8
  - task:
      name: Translation ukr-hrv
      type: translation
      args: ukr-hrv
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr hrv devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 24.6
  - task:
      name: Translation ukr-mkd
      type: translation
      args: ukr-mkd
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr mkd devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 26.2
  - task:
      name: Translation ukr-slv
      type: translation
      args: ukr-slv
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr slv devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 24.2
  - task:
      name: Translation ukr-srp_Cyrl
      type: translation
      args: ukr-srp_Cyrl
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr srp_Cyrl devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 26.2
  - task:
      name: Translation rus-bul
      type: translation
      args: rus-bul
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-bul
    metrics:
    - name: BLEU
      type: bleu
      value: 53.7
  - task:
      name: Translation rus-hbs
      type: translation
      args: rus-hbs
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-hbs
    metrics:
    - name: BLEU
      type: bleu
      value: 49.4
  - task:
      name: Translation rus-slv
      type: translation
      args: rus-slv
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-slv
    metrics:
    - name: BLEU
      type: bleu
      value: 21.5
  - task:
      name: Translation rus-srp_Cyrl
      type: translation
      args: rus-srp_Cyrl
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-srp_Cyrl
    metrics:
    - name: BLEU
      type: bleu
      value: 46.1
  - task:
      name: Translation rus-srp_Latn
      type: translation
      args: rus-srp_Latn
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-srp_Latn
    metrics:
    - name: BLEU
      type: bleu
      value: 51.7
  - task:
      name: Translation ukr-bul
      type: translation
      args: ukr-bul
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-bul
    metrics:
    - name: BLEU
      type: bleu
      value: 61.3
  - task:
      name: Translation ukr-hbs
      type: translation
      args: ukr-hbs
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-hbs
    metrics:
    - name: BLEU
      type: bleu
      value: 52.1
  - task:
      name: Translation ukr-hrv
      type: translation
      args: ukr-hrv
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-hrv
    metrics:
    - name: BLEU
      type: bleu
      value: 50.1
  - task:
      name: Translation ukr-srp_Cyrl
      type: translation
      args: ukr-srp_Cyrl
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-srp_Cyrl
    metrics:
    - name: BLEU
      type: bleu
      value: 54.7
  - task:
      name: Translation ukr-srp_Latn
      type: translation
      args: ukr-srp_Latn
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-srp_Latn
    metrics:
    - name: BLEU
      type: bleu
      value: 53.4
---
# opus-mt-tc-big-zle-zls

Neural machine translation model for translating from East Slavic languages (zle) to South Slavic languages (zls).

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

* Release: 2022-03-23
* source language(s): bel rus ukr
* target language(s): bul hbs hrv slv srp_Cyrl srp_Latn
* valid target language labels: >>bul<< >>hbs<< >>hrv<< >>slv<< >>srp_Cyrl<< >>srp_Latn<<
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-zls/opusTCv20210807+bt_transformer-big_2022-03-23.zip)
* more information released models: [OPUS-MT zle-zls README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-zls/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>bul<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>bul<< Новы каранавірус вельмі заразны.",
    ">>srp_Latn<< Моє ім'я — Саллі."
]

model_name = "pytorch-models/opus-mt-tc-big-zle-zls"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Короната е силно заразна.
#     Zovem se Sali.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zle-zls")
print(pipe(">>bul<< Новы каранавірус вельмі заразны."))

# expected output: Короната е силно заразна.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-23.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-zls/opusTCv20210807+bt_transformer-big_2022-03-23.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-23.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-zls/opusTCv20210807+bt_transformer-big_2022-03-23.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| rus-bul | tatoeba-test-v2021-08-07 | 0.71515 | 53.7 | 1247 | 8272 |
| rus-hbs | tatoeba-test-v2021-08-07 | 0.69192 | 49.4 | 2500 | 14736 |
| rus-slv | tatoeba-test-v2021-08-07 | 0.38051 | 21.5 | 657 | 3969 |
| rus-srp_Cyrl | tatoeba-test-v2021-08-07 | 0.66622 | 46.1 | 881 | 5407 |
| rus-srp_Latn | tatoeba-test-v2021-08-07 | 0.70990 | 51.7 | 1483 | 8552 |
| ukr-bul | tatoeba-test-v2021-08-07 | 0.77283 | 61.3 | 1020 | 5181 |
| ukr-hbs | tatoeba-test-v2021-08-07 | 0.69401 | 52.1 | 942 | 5130 |
| ukr-hrv | tatoeba-test-v2021-08-07 | 0.67202 | 50.1 | 389 | 2302 |
| ukr-srp_Cyrl | tatoeba-test-v2021-08-07 | 0.70064 | 54.7 | 205 | 1112 |
| ukr-srp_Latn | tatoeba-test-v2021-08-07 | 0.72405 | 53.4 | 348 | 1716 |
| bel-bul | flores101-devtest | 0.49528 | 16.1 | 1012 | 24700 |
| bel-hrv | flores101-devtest | 0.46308 | 12.4 | 1012 | 22423 |
| bel-mkd | flores101-devtest | 0.48608 | 13.5 | 1012 | 24314 |
| bel-slv | flores101-devtest | 0.44452 | 12.2 | 1012 | 23425 |
| bel-srp_Cyrl | flores101-devtest | 0.44424 | 12.6 | 1012 | 23456 |
| rus-bul | flores101-devtest | 0.58653 | 28.9 | 1012 | 24700 |
| rus-hrv | flores101-devtest | 0.53494 | 23.2 | 1012 | 22423 |
| rus-mkd | flores101-devtest | 0.55184 | 24.3 | 1012 | 24314 |
| rus-slv | flores101-devtest | 0.52201 | 23.1 | 1012 | 23425 |
| rus-srp_Cyrl | flores101-devtest | 0.53038 | 24.1 | 1012 | 23456 |
| ukr-bul | flores101-devtest | 0.59625 | 30.8 | 1012 | 24700 |
| ukr-hrv | flores101-devtest | 0.54530 | 24.6 | 1012 | 22423 |
| ukr-mkd | flores101-devtest | 0.56822 | 26.2 | 1012 | 24314 |
| ukr-slv | flores101-devtest | 0.53092 | 24.2 | 1012 | 23425 |
| ukr-srp_Cyrl | flores101-devtest | 0.54618 | 26.2 | 1012 | 23456 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Thu Mar 24 00:46:26 EET 2022
* port machine: LM0-400-22516.local

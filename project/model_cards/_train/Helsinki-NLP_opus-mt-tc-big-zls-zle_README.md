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
- name: opus-mt-tc-big-zls-zle
  results:
  - task:
      name: Translation bul-rus
      type: translation
      args: bul-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bul rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 24.6
  - task:
      name: Translation bul-ukr
      type: translation
      args: bul-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bul ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 22.9
  - task:
      name: Translation hrv-rus
      type: translation
      args: hrv-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: hrv rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 23.5
  - task:
      name: Translation hrv-ukr
      type: translation
      args: hrv-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: hrv ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 21.9
  - task:
      name: Translation mkd-rus
      type: translation
      args: mkd-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: mkd rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 24.3
  - task:
      name: Translation mkd-ukr
      type: translation
      args: mkd-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: mkd ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 22.5
  - task:
      name: Translation slv-rus
      type: translation
      args: slv-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: slv rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 22.0
  - task:
      name: Translation slv-ukr
      type: translation
      args: slv-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: slv ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 20.2
  - task:
      name: Translation srp_Cyrl-rus
      type: translation
      args: srp_Cyrl-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: srp_Cyrl rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 25.7
  - task:
      name: Translation srp_Cyrl-ukr
      type: translation
      args: srp_Cyrl-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: srp_Cyrl ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 24.4
  - task:
      name: Translation bul-rus
      type: translation
      args: bul-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bul-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 52.6
  - task:
      name: Translation bul-ukr
      type: translation
      args: bul-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bul-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 53.3
  - task:
      name: Translation hbs-rus
      type: translation
      args: hbs-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hbs-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 58.5
  - task:
      name: Translation hbs-ukr
      type: translation
      args: hbs-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hbs-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 52.3
  - task:
      name: Translation hrv-ukr
      type: translation
      args: hrv-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hrv-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 50.0
  - task:
      name: Translation slv-rus
      type: translation
      args: slv-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: slv-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 27.3
  - task:
      name: Translation srp_Cyrl-rus
      type: translation
      args: srp_Cyrl-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: srp_Cyrl-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 56.2
  - task:
      name: Translation srp_Cyrl-ukr
      type: translation
      args: srp_Cyrl-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: srp_Cyrl-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 51.8
  - task:
      name: Translation srp_Latn-rus
      type: translation
      args: srp_Latn-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: srp_Latn-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 60.1
  - task:
      name: Translation srp_Latn-ukr
      type: translation
      args: srp_Latn-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: srp_Latn-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 55.8
---
# opus-mt-tc-big-zls-zle

Neural machine translation model for translating from South Slavic languages (zls) to East Slavic languages (zle).

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
* source language(s): bul hbs hrv slv srp_Cyrl srp_Latn
* target language(s): bel rus ukr
* valid target language labels: >>bel<< >>rus<< >>ukr<<
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-zle/opusTCv20210807+bt_transformer-big_2022-03-23.zip)
* more information released models: [OPUS-MT zls-zle README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zls-zle/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>bel<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>rus<< Gdje je brigadir?",
    ">>ukr<< Zovem se Seli."
]

model_name = "pytorch-models/opus-mt-tc-big-zls-zle"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Где бригадир?
#     Мене звати Саллі.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zls-zle")
print(pipe(">>rus<< Gdje je brigadir?"))

# expected output: Где бригадир?
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-23.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-zle/opusTCv20210807+bt_transformer-big_2022-03-23.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-23.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-zle/opusTCv20210807+bt_transformer-big_2022-03-23.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| bul-rus | tatoeba-test-v2021-08-07 | 0.71467 | 52.6 | 1247 | 7870 |
| bul-ukr | tatoeba-test-v2021-08-07 | 0.71757 | 53.3 | 1020 | 4932 |
| hbs-rus | tatoeba-test-v2021-08-07 | 0.74593 | 58.5 | 2500 | 14213 |
| hbs-ukr | tatoeba-test-v2021-08-07 | 0.70244 | 52.3 | 942 | 4961 |
| hrv-ukr | tatoeba-test-v2021-08-07 | 0.68931 | 50.0 | 389 | 2232 |
| slv-rus | tatoeba-test-v2021-08-07 | 0.42255 | 27.3 | 657 | 4056 |
| srp_Cyrl-rus | tatoeba-test-v2021-08-07 | 0.74112 | 56.2 | 881 | 5117 |
| srp_Cyrl-ukr | tatoeba-test-v2021-08-07 | 0.68915 | 51.8 | 205 | 1061 |
| srp_Latn-rus | tatoeba-test-v2021-08-07 | 0.75340 | 60.1 | 1483 | 8311 |
| srp_Latn-ukr | tatoeba-test-v2021-08-07 | 0.73106 | 55.8 | 348 | 1668 |
| bul-rus | flores101-devtest | 0.54226 | 24.6 | 1012 | 23295 |
| bul-ukr | flores101-devtest | 0.53382 | 22.9 | 1012 | 22810 |
| hrv-rus | flores101-devtest | 0.51726 | 23.5 | 1012 | 23295 |
| hrv-ukr | flores101-devtest | 0.51011 | 21.9 | 1012 | 22810 |
| mkd-bel | flores101-devtest | 0.40885 | 10.7 | 1012 | 24829 |
| mkd-rus | flores101-devtest | 0.52509 | 24.3 | 1012 | 23295 |
| mkd-ukr | flores101-devtest | 0.52021 | 22.5 | 1012 | 22810 |
| slv-rus | flores101-devtest | 0.50349 | 22.0 | 1012 | 23295 |
| slv-ukr | flores101-devtest | 0.49156 | 20.2 | 1012 | 22810 |
| srp_Cyrl-rus | flores101-devtest | 0.53656 | 25.7 | 1012 | 23295 |
| srp_Cyrl-ukr | flores101-devtest | 0.53623 | 24.4 | 1012 | 22810 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Thu Mar 24 04:08:51 EET 2022
* port machine: LM0-400-22516.local

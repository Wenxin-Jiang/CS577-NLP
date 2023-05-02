---
language:
- bg
- bs
- en
- hr
- mk
- sh
- sl
- sr
- zls
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-zls-en
  results:
  - task:
      name: Translation bul-eng
      type: translation
      args: bul-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bul eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 42.0
  - task:
      name: Translation hrv-eng
      type: translation
      args: hrv-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: hrv eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 37.1
  - task:
      name: Translation mkd-eng
      type: translation
      args: mkd-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: mkd eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 43.2
  - task:
      name: Translation slv-eng
      type: translation
      args: slv-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: slv eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 35.2
  - task:
      name: Translation srp_Cyrl-eng
      type: translation
      args: srp_Cyrl-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: srp_Cyrl eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 36.8
  - task:
      name: Translation bos_Latn-eng
      type: translation
      args: bos_Latn-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bos_Latn-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 66.5
  - task:
      name: Translation bul-eng
      type: translation
      args: bul-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bul-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 59.3
  - task:
      name: Translation hbs-eng
      type: translation
      args: hbs-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hbs-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 57.3
  - task:
      name: Translation hrv-eng
      type: translation
      args: hrv-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hrv-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 59.2
  - task:
      name: Translation mkd-eng
      type: translation
      args: mkd-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: mkd-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 57.4
  - task:
      name: Translation slv-eng
      type: translation
      args: slv-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: slv-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 23.5
  - task:
      name: Translation srp_Cyrl-eng
      type: translation
      args: srp_Cyrl-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: srp_Cyrl-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 47.0
  - task:
      name: Translation srp_Latn-eng
      type: translation
      args: srp_Latn-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: srp_Latn-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 58.5
---
# opus-mt-tc-big-zls-en

Neural machine translation model for translating from South Slavic languages (zls) to English (en).

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
* source language(s): bos_Latn bul hbs hrv mkd slv srp_Cyrl srp_Latn
* target language(s): eng
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-eng/opusTCv20210807+bt_transformer-big_2022-03-17.zip)
* more information released models: [OPUS-MT zls-eng README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zls-eng/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "Да не би случайно Том да остави Мери да кара колата?",
    "Какво е времето днес?"
]

model_name = "pytorch-models/opus-mt-tc-big-zls-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Did Tom just let Mary drive the car?
#     What's the weather like today?
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zls-en")
print(pipe("Да не би случайно Том да остави Мери да кара колата?"))

# expected output: Did Tom just let Mary drive the car?
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-eng/opusTCv20210807+bt_transformer-big_2022-03-17.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-eng/opusTCv20210807+bt_transformer-big_2022-03-17.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| bos_Latn-eng | tatoeba-test-v2021-08-07 | 0.79339 | 66.5 | 301 | 1826 |
| bul-eng | tatoeba-test-v2021-08-07 | 0.72656 | 59.3 | 10000 | 71872 |
| hbs-eng | tatoeba-test-v2021-08-07 | 0.71783 | 57.3 | 10017 | 68934 |
| hrv-eng | tatoeba-test-v2021-08-07 | 0.74066 | 59.2 | 1480 | 10620 |
| mkd-eng | tatoeba-test-v2021-08-07 | 0.70043 | 57.4 | 10010 | 65667 |
| slv-eng | tatoeba-test-v2021-08-07 | 0.39534 | 23.5 | 2495 | 16940 |
| srp_Cyrl-eng | tatoeba-test-v2021-08-07 | 0.67628 | 47.0 | 1580 | 10181 |
| srp_Latn-eng | tatoeba-test-v2021-08-07 | 0.71878 | 58.5 | 6656 | 46307 |
| bul-eng | flores101-devtest | 0.67375 | 42.0 | 1012 | 24721 |
| hrv-eng | flores101-devtest | 0.63914 | 37.1 | 1012 | 24721 |
| mkd-eng | flores101-devtest | 0.67444 | 43.2 | 1012 | 24721 |
| slv-eng | flores101-devtest | 0.62087 | 35.2 | 1012 | 24721 |
| srp_Cyrl-eng | flores101-devtest | 0.67810 | 36.8 | 1012 | 24721 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 20:12:26 EEST 2022
* port machine: LM0-400-22516.local

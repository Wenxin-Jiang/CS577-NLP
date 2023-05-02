---
language:
- bs_Latn
- en
- hr
- sh
- sr_Cyrl
- sr_Latn
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-sh-en
  results:
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
      value: 56.4
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
      value: 58.8
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
      value: 44.7
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
      value: 58.4
---
# opus-mt-tc-big-sh-en

Neural machine translation model for translating from Serbo-Croatian (sh) to English (en).

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

* Release: 2022-02-25
* source language(s): bos_Latn hrv srp_Cyrl srp_Latn
* target language(s): eng
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-02-25.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/hbs-eng/opusTCv20210807+bt_transformer-big_2022-02-25.zip)
* more information released models: [OPUS-MT hbs-eng README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/hbs-eng/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "Ispostavilo se da je istina.",
    "Ovaj vikend imamo besplatne pozive."
]

model_name = "pytorch-models/opus-mt-tc-big-sh-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Turns out it's true.
#     We got free calls this weekend.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-sh-en")
print(pipe("Ispostavilo se da je istina."))

# expected output: Turns out it's true.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-02-25.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/hbs-eng/opusTCv20210807+bt_transformer-big_2022-02-25.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-02-25.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/hbs-eng/opusTCv20210807+bt_transformer-big_2022-02-25.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| bos_Latn-eng | tatoeba-test-v2021-08-07 | 0.80010 | 66.5 | 301 | 1826 |
| hbs-eng | tatoeba-test-v2021-08-07 | 0.71744 | 56.4 | 10017 | 68934 |
| hrv-eng | tatoeba-test-v2021-08-07 | 0.73563 | 58.8 | 1480 | 10620 |
| srp_Cyrl-eng | tatoeba-test-v2021-08-07 | 0.68248 | 44.7 | 1580 | 10181 |
| srp_Latn-eng | tatoeba-test-v2021-08-07 | 0.71781 | 58.4 | 6656 | 46307 |
| hrv-eng | flores101-devtest | 0.63948 | 37.1 | 1012 | 24721 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 19:21:10 EEST 2022
* port machine: LM0-400-22516.local

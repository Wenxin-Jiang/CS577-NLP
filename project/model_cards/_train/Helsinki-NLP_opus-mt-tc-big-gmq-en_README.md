---
language:
- da
- en
- fo
- gmq
- is
- nb
- nn
- false
- sv
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-gmq-en
  results:
  - task:
      name: Translation dan-eng
      type: translation
      args: dan-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 49.3
  - task:
      name: Translation isl-eng
      type: translation
      args: isl-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: isl eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 34.2
  - task:
      name: Translation nob-eng
      type: translation
      args: nob-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 44.2
  - task:
      name: Translation swe-eng
      type: translation
      args: swe-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe eng devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 49.8
  - task:
      name: Translation isl-eng
      type: translation
      args: isl-eng
    dataset:
      name: newsdev2021.is-en
      type: newsdev2021.is-en
      args: isl-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 30.4
  - task:
      name: Translation dan-eng
      type: translation
      args: dan-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: dan-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 65.9
  - task:
      name: Translation fao-eng
      type: translation
      args: fao-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fao-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 30.1
  - task:
      name: Translation isl-eng
      type: translation
      args: isl-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: isl-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 53.3
  - task:
      name: Translation nno-eng
      type: translation
      args: nno-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nno-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 56.1
  - task:
      name: Translation nob-eng
      type: translation
      args: nob-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nob-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 60.2
  - task:
      name: Translation swe-eng
      type: translation
      args: swe-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: swe-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 66.4
  - task:
      name: Translation isl-eng
      type: translation
      args: isl-eng
    dataset:
      name: newstest2021.is-en
      type: wmt-2021-news
      args: isl-eng
    metrics:
    - name: BLEU
      type: bleu
      value: 34.4
---
# opus-mt-tc-big-gmq-en

Neural machine translation model for translating from North Germanic languages (gmq) to English (en).

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
* source language(s): dan fao isl nno nob nor swe
* target language(s): eng
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-09.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-eng/opusTCv20210807+bt_transformer-big_2022-03-09.zip)
* more information released models: [OPUS-MT gmq-eng README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmq-eng/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "Han var synligt nervøs.",
    "Inte ens Tom själv var övertygad."
]

model_name = "pytorch-models/opus-mt-tc-big-gmq-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     He was visibly nervous.
#     Even Tom was not convinced.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-gmq-en")
print(pipe("Han var synligt nervøs."))

# expected output: He was visibly nervous.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-09.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-eng/opusTCv20210807+bt_transformer-big_2022-03-09.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-09.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-eng/opusTCv20210807+bt_transformer-big_2022-03-09.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| dan-eng | tatoeba-test-v2021-08-07 | 0.78292 | 65.9 | 10795 | 79684 |
| fao-eng | tatoeba-test-v2021-08-07 | 0.47467 | 30.1 | 294 | 1984 |
| isl-eng | tatoeba-test-v2021-08-07 | 0.68346 | 53.3 | 2503 | 19788 |
| nno-eng | tatoeba-test-v2021-08-07 | 0.69788 | 56.1 | 460 | 3524 |
| nob-eng | tatoeba-test-v2021-08-07 | 0.73524 | 60.2 | 4539 | 36823 |
| swe-eng | tatoeba-test-v2021-08-07 | 0.77665 | 66.4 | 10362 | 68513 |
| dan-eng | flores101-devtest | 0.72322 | 49.3 | 1012 | 24721 |
| isl-eng | flores101-devtest | 0.59616 | 34.2 | 1012 | 24721 |
| nob-eng | flores101-devtest | 0.68224 | 44.2 | 1012 | 24721 |
| swe-eng | flores101-devtest | 0.72042 | 49.8 | 1012 | 24721 |
| isl-eng | newsdev2021.is-en | 0.56709 | 30.4 | 2004 | 46383 |
| isl-eng | newstest2021.is-en | 0.57756 | 34.4 | 1000 | 22529 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 19:13:11 EEST 2022
* port machine: LM0-400-22516.local

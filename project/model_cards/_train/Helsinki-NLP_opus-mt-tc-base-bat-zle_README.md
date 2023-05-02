---
language:
- bat
- lt
- lv
- ru
- zle
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-base-bat-zle
  results:
  - task:
      name: Translation lav-rus
      type: translation
      args: lav-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: lav rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 21.1
  - task:
      name: Translation lit-rus
      type: translation
      args: lit-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: lit rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 21.3
  - task:
      name: Translation lav-rus
      type: translation
      args: lav-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: lav-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 60.5
  - task:
      name: Translation lit-rus
      type: translation
      args: lit-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: lit-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 54.9
---
# opus-mt-tc-base-bat-zle

Neural machine translation model for translating from Baltic languages (bat) to East Slavic languages (zle).

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
* source language(s): lav lit
* target language(s): rus
* model: transformer-align
* data: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807_transformer-align_2022-03-13.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/bat-zle/opusTCv20210807_transformer-align_2022-03-13.zip)
* more information released models: [OPUS-MT bat-zle README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bat-zle/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>rus<< Āfrika ir cilvēces šūpulis.",
    ">>ukr<< Tomas yra mūsų kapitonas."
]

model_name = "pytorch-models/opus-mt-tc-base-bat-zle"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Африка - это колыбель человечества.
#     Томас - наш капітан.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-base-bat-zle")
print(pipe(">>rus<< Āfrika ir cilvēces šūpulis."))

# expected output: Африка - это колыбель человечества.
```

## Benchmarks

* test set translations: [opusTCv20210807_transformer-align_2022-03-13.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bat-zle/opusTCv20210807_transformer-align_2022-03-13.test.txt)
* test set scores: [opusTCv20210807_transformer-align_2022-03-13.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bat-zle/opusTCv20210807_transformer-align_2022-03-13.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| lav-rus | tatoeba-test-v2021-08-07 | 0.75918 | 60.5 | 274 | 1541 |
| lit-rus | tatoeba-test-v2021-08-07 | 0.72796 | 54.9 | 3598 | 21908 |
| lav-rus | flores101-devtest | 0.49210 | 21.1 | 1012 | 23295 |
| lav-ukr | flores101-devtest | 0.48185 | 19.2 | 1012 | 22810 |
| lit-rus | flores101-devtest | 0.49850 | 21.3 | 1012 | 23295 |
| lit-ukr | flores101-devtest | 0.49114 | 19.5 | 1012 | 22810 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Thu Mar 24 00:51:59 EET 2022
* port machine: LM0-400-22516.local

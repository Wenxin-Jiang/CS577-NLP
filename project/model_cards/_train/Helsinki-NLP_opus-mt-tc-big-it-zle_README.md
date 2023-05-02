---
language:
- be
- it
- ru
- uk
- zle
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-it-zle
  results:
  - task:
      name: Translation ita-rus
      type: translation
      args: ita-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 21.3
  - task:
      name: Translation ita-bel
      type: translation
      args: ita-bel
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ita-bel
    metrics:
    - name: BLEU
      type: bleu
      value: 33.3
  - task:
      name: Translation ita-rus
      type: translation
      args: ita-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ita-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 46.7
  - task:
      name: Translation ita-ukr
      type: translation
      args: ita-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ita-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 48.4
---
# opus-mt-tc-big-it-zle

Neural machine translation model for translating from Italian (it) to East Slavic languages (zle).

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
* source language(s): ita
* target language(s): bel rus ukr
* valid target language labels: >>bel<< >>rus<< >>ukr<<
* model: transformer-big
* data: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807_transformer-big_2022-03-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-zle/opusTCv20210807_transformer-big_2022-03-23.zip)
* more information released models: [OPUS-MT ita-zle README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-zle/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>bel<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>ukr<< Alcune cose non cambiano mai.",
    ">>rus<< Puoi sederti."
]

model_name = "pytorch-models/opus-mt-tc-big-it-zle"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Деякі речі ніколи не змінюються.
#     Можешь присесть.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-it-zle")
print(pipe(">>ukr<< Alcune cose non cambiano mai."))

# expected output: Деякі речі ніколи не змінюються.
```

## Benchmarks

* test set translations: [opusTCv20210807_transformer-big_2022-03-23.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-zle/opusTCv20210807_transformer-big_2022-03-23.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-03-23.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-zle/opusTCv20210807_transformer-big_2022-03-23.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| ita-bel | tatoeba-test-v2021-08-07 | 0.55727 | 33.3 | 264 | 1513 |
| ita-rus | tatoeba-test-v2021-08-07 | 0.66083 | 46.7 | 10045 | 65968 |
| ita-ukr | tatoeba-test-v2021-08-07 | 0.67674 | 48.4 | 5000 | 25353 |
| ita-rus | flores101-devtest | 0.50323 | 21.3 | 1012 | 23295 |
| ita-ukr | flores101-devtest | 0.47658 | 18.3 | 1012 | 22810 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Thu Mar 24 02:49:36 EET 2022
* port machine: LM0-400-22516.local

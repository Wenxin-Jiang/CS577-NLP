---
language:
- cs
- sk
- uk
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-base-uk-ces_slk
  results:
  - task:
      name: Translation ukr-ces
      type: translation
      args: ukr-ces
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr ces devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 23.0
  - task:
      name: Translation ukr-slk
      type: translation
      args: ukr-slk
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr slk devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 22.1
  - task:
      name: Translation ukr-ces
      type: translation
      args: ukr-ces
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 54.2
---
# opus-mt-tc-base-uk-ces_slk

Neural machine translation model for translating from Ukrainian (uk) to Czech and Slovak (cs+sk).

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
* source language(s): ukr
* target language(s): ces
* valid target language labels: >>ces<< >>slk<<
* model: transformer-align
* data: opusTCv20210807+pft ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+pft_transformer-align_2022-03-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ces+slk/opusTCv20210807+pft_transformer-align_2022-03-17.zip)
* more information released models: [OPUS-MT ukr-ces+slk README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-ces+slk/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>ces<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>ces<< А чого так?",
    ">>ces<< Я загубив свої окуляри."
]

model_name = "pytorch-models/opus-mt-tc-base-uk-ces_slk"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Proč to tak je?
#     Ztratil jsem brýle.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-base-uk-ces_slk")
print(pipe(">>ces<< А чого так?"))

# expected output: Proč to tak je?
```

## Benchmarks

* test set translations: [opusTCv20210807+pft_transformer-align_2022-03-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ces+slk/opusTCv20210807+pft_transformer-align_2022-03-17.test.txt)
* test set scores: [opusTCv20210807+pft_transformer-align_2022-03-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ces+slk/opusTCv20210807+pft_transformer-align_2022-03-17.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| ukr-ces | tatoeba-test-v2021-08-07 | 0.70661 | 54.2 | 1787 | 8550 |
| ukr-ces | flores101-devtest | 0.51283 | 23.0 | 1012 | 22101 |
| ukr-slk | flores101-devtest | 0.51043 | 22.1 | 1012 | 22543 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: f084bad
* port time: Wed Mar 23 21:54:02 EET 2022
* port machine: LM0-400-22516.local

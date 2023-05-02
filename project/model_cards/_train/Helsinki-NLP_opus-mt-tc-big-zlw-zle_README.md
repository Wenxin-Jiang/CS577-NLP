---
language:
- be
- cs
- dsb
- hsb
- pl
- ru
- uk
- zle
- zlw
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-zlw-zle
  results:
  - task:
      name: Translation ces-rus
      type: translation
      args: ces-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ces rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 24.2
  - task:
      name: Translation ces-ukr
      type: translation
      args: ces-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ces ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 22.9
  - task:
      name: Translation pol-rus
      type: translation
      args: pol-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: pol rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 20.1
  - task:
      name: Translation ces-rus
      type: translation
      args: ces-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ces-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 56.4
  - task:
      name: Translation ces-ukr
      type: translation
      args: ces-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ces-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 53.0
  - task:
      name: Translation pol-bel
      type: translation
      args: pol-bel
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: pol-bel
    metrics:
    - name: BLEU
      type: bleu
      value: 29.4
  - task:
      name: Translation pol-rus
      type: translation
      args: pol-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: pol-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 55.3
  - task:
      name: Translation pol-ukr
      type: translation
      args: pol-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: pol-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 48.6
  - task:
      name: Translation ces-rus
      type: translation
      args: ces-rus
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: ces-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 21.0
  - task:
      name: Translation ces-rus
      type: translation
      args: ces-rus
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: ces-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 27.2
---
# opus-mt-tc-big-zlw-zle

Neural machine translation model for translating from West Slavic languages (zlw) to East Slavic languages (zle).

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

* Release: 2022-03-19
* source language(s): ces dsb hsb pol
* target language(s): bel rus ukr
* valid target language labels: >>bel<< >>rus<< >>ukr<<
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-19.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-zle/opusTCv20210807+bt_transformer-big_2022-03-19.zip)
* more information released models: [OPUS-MT zlw-zle README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zlw-zle/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>bel<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>rus<< Je vystudovaný právník.",
    ">>rus<< Gdzie jest moja książka ?"
]

model_name = "pytorch-models/opus-mt-tc-big-zlw-zle"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Он дипломированный юрист.
#     Где моя книга?
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zlw-zle")
print(pipe(">>rus<< Je vystudovaný právník."))

# expected output: Он дипломированный юрист.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-19.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-zle/opusTCv20210807+bt_transformer-big_2022-03-19.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-19.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-zle/opusTCv20210807+bt_transformer-big_2022-03-19.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| ces-rus | tatoeba-test-v2021-08-07 | 0.73154 | 56.4 | 2934 | 17790 |
| ces-ukr | tatoeba-test-v2021-08-07 | 0.69934 | 53.0 | 1787 | 8891 |
| pol-bel | tatoeba-test-v2021-08-07 | 0.51039 | 29.4 | 287 | 1730 |
| pol-rus | tatoeba-test-v2021-08-07 | 0.73156 | 55.3 | 3543 | 22067 |
| pol-ukr | tatoeba-test-v2021-08-07 | 0.68247 | 48.6 | 2519 | 13535 |
| ces-rus | flores101-devtest | 0.52316 | 24.2 | 1012 | 23295 |
| ces-ukr | flores101-devtest | 0.52261 | 22.9 | 1012 | 22810 |
| pol-rus | flores101-devtest | 0.49414 | 20.1 | 1012 | 23295 |
| pol-ukr | flores101-devtest | 0.48250 | 18.3 | 1012 | 22810 |
| ces-rus | newstest2012 | 0.49469 | 21.0 | 3003 | 64790 |
| ces-rus | newstest2013 | 0.54197 | 27.2 | 3000 | 58560 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Thu Mar 24 04:13:23 EET 2022
* port machine: LM0-400-22516.local

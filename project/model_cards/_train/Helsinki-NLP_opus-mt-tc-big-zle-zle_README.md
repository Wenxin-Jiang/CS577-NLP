---
language:
- be
- ru
- uk
- zle
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-zle-zle
  results:
  - task:
      name: Translation rus-ukr
      type: translation
      args: rus-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 25.5
  - task:
      name: Translation ukr-rus
      type: translation
      args: ukr-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 28.3
  - task:
      name: Translation bel-rus
      type: translation
      args: bel-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bel-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 68.6
  - task:
      name: Translation bel-ukr
      type: translation
      args: bel-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bel-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 65.5
  - task:
      name: Translation rus-bel
      type: translation
      args: rus-bel
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-bel
    metrics:
    - name: BLEU
      type: bleu
      value: 50.3
  - task:
      name: Translation rus-ukr
      type: translation
      args: rus-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 70.1
  - task:
      name: Translation ukr-bel
      type: translation
      args: ukr-bel
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-bel
    metrics:
    - name: BLEU
      type: bleu
      value: 58.9
  - task:
      name: Translation ukr-rus
      type: translation
      args: ukr-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 75.7
---
# opus-mt-tc-big-zle-zle

Neural machine translation model for translating from East Slavic languages (zle) to East Slavic languages (zle).

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

* Release: 2022-03-07
* source language(s): bel rus ukr
* target language(s): bel rus ukr
* valid target language labels: >>bel<< >>rus<< >>ukr<<
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-07.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-zle/opusTCv20210807+bt_transformer-big_2022-03-07.zip)
* more information released models: [OPUS-MT zle-zle README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-zle/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>bel<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>ukr<< Кот мёртвый.",
    ">>bel<< Джон живе в Нью-Йорку."
]

model_name = "pytorch-models/opus-mt-tc-big-zle-zle"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Кіт мертвий.
#     Джон жыве ў Нью-Йорку.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zle-zle")
print(pipe(">>ukr<< Кот мёртвый."))

# expected output: Кіт мертвий.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-07.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-zle/opusTCv20210807+bt_transformer-big_2022-03-07.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-07.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-zle/opusTCv20210807+bt_transformer-big_2022-03-07.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| bel-rus | tatoeba-test-v2021-08-07 | 0.82526 | 68.6 | 2500 | 18895 |
| bel-ukr | tatoeba-test-v2021-08-07 | 0.81036 | 65.5 | 2355 | 15179 |
| rus-bel | tatoeba-test-v2021-08-07 | 0.66943 | 50.3 | 2500 | 18756 |
| rus-ukr | tatoeba-test-v2021-08-07 | 0.83639 | 70.1 | 10000 | 60212 |
| ukr-bel | tatoeba-test-v2021-08-07 | 0.75368 | 58.9 | 2355 | 15175 |
| ukr-rus | tatoeba-test-v2021-08-07 | 0.86806 | 75.7 | 10000 | 60387 |
| bel-rus | flores101-devtest | 0.47960 | 14.5 | 1012 | 23295 |
| bel-ukr | flores101-devtest | 0.47335 | 12.8 | 1012 | 22810 |
| rus-ukr | flores101-devtest | 0.55287 | 25.5 | 1012 | 22810 |
| ukr-rus | flores101-devtest | 0.56224 | 28.3 | 1012 | 23295 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Thu Mar 24 00:15:39 EET 2022
* port machine: LM0-400-22516.local

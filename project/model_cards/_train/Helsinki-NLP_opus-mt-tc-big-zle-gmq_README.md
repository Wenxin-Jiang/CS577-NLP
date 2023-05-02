---
language:
- da
- gmq
- nb
- false
- ru
- sv
- uk
- zle
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-zle-gmq
  results:
  - task:
      name: Translation rus-dan
      type: translation
      args: rus-dan
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus dan devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 28.0
  - task:
      name: Translation rus-nob
      type: translation
      args: rus-nob
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus nob devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 20.6
  - task:
      name: Translation rus-swe
      type: translation
      args: rus-swe
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus swe devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 26.4
  - task:
      name: Translation ukr-dan
      type: translation
      args: ukr-dan
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr dan devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 30.3
  - task:
      name: Translation ukr-nob
      type: translation
      args: ukr-nob
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr nob devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 21.1
  - task:
      name: Translation ukr-swe
      type: translation
      args: ukr-swe
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr swe devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 28.8
  - task:
      name: Translation rus-dan
      type: translation
      args: rus-dan
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-dan
    metrics:
    - name: BLEU
      type: bleu
      value: 59.6
  - task:
      name: Translation rus-nob
      type: translation
      args: rus-nob
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-nob
    metrics:
    - name: BLEU
      type: bleu
      value: 46.1
  - task:
      name: Translation rus-swe
      type: translation
      args: rus-swe
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-swe
    metrics:
    - name: BLEU
      type: bleu
      value: 53.3
---
# opus-mt-tc-big-zle-gmq

Neural machine translation model for translating from East Slavic languages (zle) to North Germanic languages (gmq).

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

* Release: 2022-03-14
* source language(s): rus ukr
* target language(s): dan nob nor swe
* valid target language labels: >>dan<< >>nob<< >>nor<< >>swe<<
* model: transformer-big
* data: opusTCv20210807+pft ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+pft_transformer-big_2022-03-14.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-gmq/opusTCv20210807+pft_transformer-big_2022-03-14.zip)
* more information released models: [OPUS-MT zle-gmq README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-gmq/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>dan<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>dan<< Заўтра ўжо чацвер.",
    ">>swe<< Том грав з Мері в кішки-мишки."
]

model_name = "pytorch-models/opus-mt-tc-big-zle-gmq"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     I morgen er det torsdag.
#     Tom lekte med Mary i katt-möss.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zle-gmq")
print(pipe(">>dan<< Заўтра ўжо чацвер."))

# expected output: I morgen er det torsdag.
```

## Benchmarks

* test set translations: [opusTCv20210807+pft_transformer-big_2022-03-14.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-gmq/opusTCv20210807+pft_transformer-big_2022-03-14.test.txt)
* test set scores: [opusTCv20210807+pft_transformer-big_2022-03-14.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-gmq/opusTCv20210807+pft_transformer-big_2022-03-14.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| rus-dan | tatoeba-test-v2021-08-07 | 0.74307 | 59.6 | 1713 | 11746 |
| rus-nob | tatoeba-test-v2021-08-07 | 0.66376 | 46.1 | 1277 | 11672 |
| rus-swe | tatoeba-test-v2021-08-07 | 0.69608 | 53.3 | 1282 | 8449 |
| bel-dan | flores101-devtest | 0.47621 | 13.9 | 1012 | 24638 |
| bel-nob | flores101-devtest | 0.44966 | 10.8 | 1012 | 23873 |
| bel-swe | flores101-devtest | 0.47274 | 13.2 | 1012 | 23121 |
| rus-dan | flores101-devtest | 0.55917 | 28.0 | 1012 | 24638 |
| rus-nob | flores101-devtest | 0.50724 | 20.6 | 1012 | 23873 |
| rus-swe | flores101-devtest | 0.55812 | 26.4 | 1012 | 23121 |
| ukr-dan | flores101-devtest | 0.57829 | 30.3 | 1012 | 24638 |
| ukr-nob | flores101-devtest | 0.52271 | 21.1 | 1012 | 23873 |
| ukr-swe | flores101-devtest | 0.57499 | 28.8 | 1012 | 23121 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Wed Mar 23 23:13:54 EET 2022
* port machine: LM0-400-22516.local

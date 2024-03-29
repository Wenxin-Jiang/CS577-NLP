---
language:
- da
- gmq
- is
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
- name: opus-mt-tc-big-gmq-zle
  results:
  - task:
      name: Translation dan-rus
      type: translation
      args: dan-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 25.6
  - task:
      name: Translation dan-ukr
      type: translation
      args: dan-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 25.5
  - task:
      name: Translation nob-rus
      type: translation
      args: nob-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 22.1
  - task:
      name: Translation nob-ukr
      type: translation
      args: nob-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 21.6
  - task:
      name: Translation swe-rus
      type: translation
      args: swe-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 25.8
  - task:
      name: Translation swe-ukr
      type: translation
      args: swe-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 25.7
  - task:
      name: Translation dan-rus
      type: translation
      args: dan-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: dan-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 53.9
  - task:
      name: Translation nob-rus
      type: translation
      args: nob-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nob-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 45.8
  - task:
      name: Translation swe-rus
      type: translation
      args: swe-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: swe-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 45.9
---
# opus-mt-tc-big-gmq-zle

Neural machine translation model for translating from North Germanic languages (gmq) to East Slavic languages (zle).

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
* source language(s): dan isl nob nor swe
* target language(s): rus ukr
* valid target language labels: >>rus<< >>ukr<<
* model: transformer-big
* data: opusTCv20210807+pbt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+pbt_transformer-big_2022-03-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-zle/opusTCv20210807+pbt_transformer-big_2022-03-23.zip)
* more information released models: [OPUS-MT gmq-zle README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmq-zle/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>rus<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>bel<< Det er allerede torsdag i morgen.",
    ">>ukr<< Tom lekte katt och råtta med Mary."
]

model_name = "pytorch-models/opus-mt-tc-big-gmq-zle"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Гэта ўжо чацвер заўтра.
#     Том грав кішку і щура з Марією.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-gmq-zle")
print(pipe(">>bel<< Det er allerede torsdag i morgen."))

# expected output: Гэта ўжо чацвер заўтра.
```

## Benchmarks

* test set translations: [opusTCv20210807+pbt_transformer-big_2022-03-23.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-zle/opusTCv20210807+pbt_transformer-big_2022-03-23.test.txt)
* test set scores: [opusTCv20210807+pbt_transformer-big_2022-03-23.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-zle/opusTCv20210807+pbt_transformer-big_2022-03-23.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| dan-rus | tatoeba-test-v2021-08-07 | 0.72627 | 53.9 | 1713 | 10480 |
| nob-rus | tatoeba-test-v2021-08-07 | 0.66881 | 45.8 | 1277 | 10659 |
| swe-rus | tatoeba-test-v2021-08-07 | 0.66248 | 45.9 | 1282 | 7659 |
| dan-rus | flores101-devtest | 0.53271 | 25.6 | 1012 | 23295 |
| dan-ukr | flores101-devtest | 0.54273 | 25.5 | 1012 | 22810 |
| nob-rus | flores101-devtest | 0.50426 | 22.1 | 1012 | 23295 |
| nob-ukr | flores101-devtest | 0.51156 | 21.6 | 1012 | 22810 |
| swe-rus | flores101-devtest | 0.53226 | 25.8 | 1012 | 23295 |
| swe-ukr | flores101-devtest | 0.54257 | 25.7 | 1012 | 22810 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Thu Mar 24 02:08:53 EET 2022
* port machine: LM0-400-22516.local

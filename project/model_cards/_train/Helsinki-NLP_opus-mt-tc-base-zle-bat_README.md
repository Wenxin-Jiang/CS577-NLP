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
- name: opus-mt-tc-base-zle-bat
  results:
  - task:
      name: Translation rus-lav
      type: translation
      args: rus-lav
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus lav devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 20.0
  - task:
      name: Translation rus-lit
      type: translation
      args: rus-lit
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus lit devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 20.6
  - task:
      name: Translation ukr-lav
      type: translation
      args: ukr-lav
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr lav devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 21.4
  - task:
      name: Translation ukr-lit
      type: translation
      args: ukr-lit
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr lit devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 20.5
  - task:
      name: Translation rus-lav
      type: translation
      args: rus-lav
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-lav
    metrics:
    - name: BLEU
      type: bleu
      value: 55.3
  - task:
      name: Translation rus-lit
      type: translation
      args: rus-lit
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-lit
    metrics:
    - name: BLEU
      type: bleu
      value: 47.2
---
# opus-mt-tc-base-zle-bat

Neural machine translation model for translating from East Slavic languages (zle) to Baltic languages (bat).

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
* source language(s): rus
* target language(s): lav lit
* valid target language labels: >>lav<< >>lit<<
* model: transformer-align
* data: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807_transformer-align_2022-03-14.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-bat/opusTCv20210807_transformer-align_2022-03-14.zip)
* more information released models: [OPUS-MT zle-bat README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-bat/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>lav<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>lav<< Африка - колыбель человечества.",
    ">>lit<< Том — наш капітан."
]

model_name = "pytorch-models/opus-mt-tc-base-zle-bat"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Āfrika ir cilvēces šūpulis.
#     Tomas yra mūsų kapitonas.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-base-zle-bat")
print(pipe(">>lav<< Африка - колыбель человечества."))

# expected output: Āfrika ir cilvēces šūpulis.
```

## Benchmarks

* test set translations: [opusTCv20210807_transformer-align_2022-03-14.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-bat/opusTCv20210807_transformer-align_2022-03-14.test.txt)
* test set scores: [opusTCv20210807_transformer-align_2022-03-14.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-bat/opusTCv20210807_transformer-align_2022-03-14.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| rus-lav | tatoeba-test-v2021-08-07 | 0.74223 | 55.3 | 274 | 1518 |
| rus-lit | tatoeba-test-v2021-08-07 | 0.70795 | 47.2 | 3598 | 20662 |
| rus-lav | flores101-devtest | 0.50134 | 20.0 | 1012 | 22092 |
| rus-lit | flores101-devtest | 0.53732 | 20.6 | 1012 | 20695 |
| ukr-lav | flores101-devtest | 0.51379 | 21.4 | 1012 | 22092 |
| ukr-lit | flores101-devtest | 0.54085 | 20.5 | 1012 | 20695 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Wed Mar 23 22:11:57 EET 2022
* port machine: LM0-400-22516.local

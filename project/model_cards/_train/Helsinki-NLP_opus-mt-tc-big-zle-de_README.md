---
language:
- be
- de
- ru
- uk
- zle
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-zle-de
  results:
  - task:
      name: Translation rus-deu
      type: translation
      args: rus-deu
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus deu devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 26.1
  - task:
      name: Translation ukr-deu
      type: translation
      args: ukr-deu
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr deu devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 28.1
  - task:
      name: Translation bel-deu
      type: translation
      args: bel-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bel-deu
    metrics:
    - name: BLEU
      type: bleu
      value: 44.8
  - task:
      name: Translation rus-deu
      type: translation
      args: rus-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-deu
    metrics:
    - name: BLEU
      type: bleu
      value: 51.8
  - task:
      name: Translation ukr-deu
      type: translation
      args: ukr-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-deu
    metrics:
    - name: BLEU
      type: bleu
      value: 54.7
  - task:
      name: Translation rus-deu
      type: translation
      args: rus-deu
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: rus-deu
    metrics:
    - name: BLEU
      type: bleu
      value: 25.2
---
# opus-mt-tc-big-zle-de

Neural machine translation model for translating from East Slavic languages (zle) to German (de).

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
* source language(s): bel rus ukr
* target language(s): deu
* model: transformer-big
* data: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807_transformer-big_2022-03-19.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-deu/opusTCv20210807_transformer-big_2022-03-19.zip)
* more information released models: [OPUS-MT zle-deu README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-deu/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "Это был по-настоящему прекрасный день.",
    "Дождь кончился?"
]

model_name = "pytorch-models/opus-mt-tc-big-zle-de"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Es war ein wirklich schöner Tag.
#     Ist der Regen vorbei?
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zle-de")
print(pipe("Это был по-настоящему прекрасный день."))

# expected output: Es war ein wirklich schöner Tag.
```

## Benchmarks

* test set translations: [opusTCv20210807_transformer-big_2022-03-19.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-deu/opusTCv20210807_transformer-big_2022-03-19.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-03-19.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-deu/opusTCv20210807_transformer-big_2022-03-19.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| bel-deu | tatoeba-test-v2021-08-07 | 0.63720 | 44.8 | 551 | 4182 |
| rus-deu | tatoeba-test-v2021-08-07 | 0.69768 | 51.8 | 12800 | 98842 |
| ukr-deu | tatoeba-test-v2021-08-07 | 0.70860 | 54.7 | 10319 | 64646 |
| bel-deu | flores101-devtest | 0.47052 | 12.9 | 1012 | 25094 |
| rus-deu | flores101-devtest | 0.56159 | 26.1 | 1012 | 25094 |
| ukr-deu | flores101-devtest | 0.57251 | 28.1 | 1012 | 25094 |
| rus-deu | newstest2012 | 0.49257 | 19.8 | 3003 | 72886 |
| rus-deu | newstest2013 | 0.54015 | 25.2 | 3000 | 63737 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Wed Mar 23 22:16:45 EET 2022
* port machine: LM0-400-22516.local

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
- name: opus-mt-tc-big-de-zle
  results:
  - task:
      name: Translation deu-rus
      type: translation
      args: deu-rus
    dataset:
      name: flores101-devtest
      type: flores_101
      args: deu rus devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 26.3
  - task:
      name: Translation deu-ukr
      type: translation
      args: deu-ukr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: deu ukr devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 24.2
  - task:
      name: Translation deu-bel
      type: translation
      args: deu-bel
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: deu-bel
    metrics:
    - name: BLEU
      type: bleu
      value: 29.5
  - task:
      name: Translation deu-rus
      type: translation
      args: deu-rus
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: deu-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 46.1
  - task:
      name: Translation deu-ukr
      type: translation
      args: deu-ukr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: deu-ukr
    metrics:
    - name: BLEU
      type: bleu
      value: 40.7
  - task:
      name: Translation deu-rus
      type: translation
      args: deu-rus
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: deu-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 20.8
  - task:
      name: Translation deu-rus
      type: translation
      args: deu-rus
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: deu-rus
    metrics:
    - name: BLEU
      type: bleu
      value: 24.9
---
# opus-mt-tc-big-de-zle

Neural machine translation model for translating from German (de) to East Slavic languages (zle).

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
* source language(s): deu
* target language(s): bel rus ukr
* valid target language labels: >>bel<< >>rus<< >>ukr<<
* model: transformer-big
* data: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807_transformer-big_2022-03-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-zle/opusTCv20210807_transformer-big_2022-03-23.zip)
* more information released models: [OPUS-MT deu-zle README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-zle/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>bel<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>ukr<< Der Soldat hat mir Wasser gegeben.",
    ">>ukr<< Ich will hier nicht essen."
]

model_name = "pytorch-models/opus-mt-tc-big-de-zle"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Солдат дав мені воду.
#     Я не хочу тут їсти.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-de-zle")
print(pipe(">>ukr<< Der Soldat hat mir Wasser gegeben."))

# expected output: Солдат дав мені воду.
```

## Benchmarks

* test set translations: [opusTCv20210807_transformer-big_2022-03-23.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-zle/opusTCv20210807_transformer-big_2022-03-23.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-03-23.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-zle/opusTCv20210807_transformer-big_2022-03-23.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| deu-bel | tatoeba-test-v2021-08-07 | 0.53128 | 29.5 | 551 | 3601 |
| deu-rus | tatoeba-test-v2021-08-07 | 0.67143 | 46.1 | 12800 | 87296 |
| deu-ukr | tatoeba-test-v2021-08-07 | 0.62737 | 40.7 | 10319 | 56287 |
| deu-rus | flores101-devtest | 0.54152 | 26.3 | 1012 | 23295 |
| deu-ukr | flores101-devtest | 0.53286 | 24.2 | 1012 | 22810 |
| deu-rus | newstest2012 | 0.49409 | 20.8 | 3003 | 64790 |
| deu-rus | newstest2013 | 0.52631 | 24.9 | 3000 | 58560 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Thu Mar 24 01:29:09 EET 2022
* port machine: LM0-400-22516.local

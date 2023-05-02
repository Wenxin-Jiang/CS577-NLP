---
language:
- be
- fr
- ru
- uk
- zle
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-zle-fr
  results:
  - task:
      name: Translation bel-fra
      type: translation
      args: bel-fra
    dataset:
      name: tatoeba-test-v2020-07-28-v2021-08-07
      type: tatoeba_mt
      args: bel-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 46.4
  - task:
      name: Translation multi-fra
      type: translation
      args: multi-fra
    dataset:
      name: tatoeba-test-v2020-07-28-v2021-08-07
      type: tatoeba_mt
      args: multi-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 52.4
  - task:
      name: Translation rus-fra
      type: translation
      args: rus-fra
    dataset:
      name: tatoeba-test-v2020-07-28-v2021-08-07
      type: tatoeba_mt
      args: rus-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 51.8
  - task:
      name: Translation ukr-fra
      type: translation
      args: ukr-fra
    dataset:
      name: tatoeba-test-v2020-07-28-v2021-08-07
      type: tatoeba_mt
      args: ukr-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 50.7
  - task:
      name: Translation rus-fra
      type: translation
      args: rus-fra
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: rus-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 25.3
  - task:
      name: Translation rus-fra
      type: translation
      args: rus-fra
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: rus-fra
    metrics:
    - name: BLEU
      type: bleu
      value: 29.7
---
# opus-mt-tc-big-zle-fr

Neural machine translation model for translating from East Slavic languages (zle) to French (fr).

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
* source language(s): bel rus ukr
* target language(s): fra
* model: transformer-big
* data: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807_transformer-big_2022-03-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-fra/opusTCv20210807_transformer-big_2022-03-23.zip)
* more information released models: [OPUS-MT zle-fra README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-fra/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "Подавай блюдо на тарелке.",
    "Операція не може чекати."
]

model_name = "pytorch-models/opus-mt-tc-big-zle-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Servez le plat dans l'assiette.
#     L'opération ne peut pas attendre.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zle-fr")
print(pipe("Подавай блюдо на тарелке."))

# expected output: Servez le plat dans l'assiette.
```

## Benchmarks

* test set translations: [opusTCv20210807_transformer-big_2022-03-23.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-fra/opusTCv20210807_transformer-big_2022-03-23.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-03-23.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-fra/opusTCv20210807_transformer-big_2022-03-23.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| bel-fra | tatoeba-test-v2020-07-28-v2021-08-07 | 0.65415 | 46.4 | 283 | 2005 |
| multi-fra | tatoeba-test-v2020-07-28-v2021-08-07 | 0.68422 | 52.4 | 10000 | 66671 |
| rus-fra | tatoeba-test-v2020-07-28-v2021-08-07 | 0.68699 | 51.8 | 11490 | 80573 |
| ukr-fra | tatoeba-test-v2020-07-28-v2021-08-07 | 0.67887 | 50.7 | 10035 | 63222 |
| rus-fra | newstest2012 | 0.53679 | 25.3 | 3003 | 78011 |
| rus-fra | newstest2013 | 0.56211 | 29.7 | 3000 | 70037 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 1bdabf7
* port time: Wed Mar 23 22:45:20 EET 2022
* port machine: LM0-400-22516.local

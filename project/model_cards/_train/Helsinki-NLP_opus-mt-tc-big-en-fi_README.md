---
language:
- en
- fi
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-en-fi
  results:
  - task:
      name: Translation eng-fin
      type: translation
      args: eng-fin
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng fin devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 27.6
  - task:
      name: Translation eng-fin
      type: translation
      args: eng-fin
    dataset:
      name: newsdev2015
      type: newsdev2015
      args: eng-fin
    metrics:
    - name: BLEU
      type: bleu
      value: 24.2
  - task:
      name: Translation eng-fin
      type: translation
      args: eng-fin
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-fin
    metrics:
    - name: BLEU
      type: bleu
      value: 39.3
  - task:
      name: Translation eng-fin
      type: translation
      args: eng-fin
    dataset:
      name: newstest2015
      type: wmt-2015-news
      args: eng-fin
    metrics:
    - name: BLEU
      type: bleu
      value: 26.4
  - task:
      name: Translation eng-fin
      type: translation
      args: eng-fin
    dataset:
      name: newstest2016
      type: wmt-2016-news
      args: eng-fin
    metrics:
    - name: BLEU
      type: bleu
      value: 28.8
  - task:
      name: Translation eng-fin
      type: translation
      args: eng-fin
    dataset:
      name: newstest2017
      type: wmt-2017-news
      args: eng-fin
    metrics:
    - name: BLEU
      type: bleu
      value: 31.3
  - task:
      name: Translation eng-fin
      type: translation
      args: eng-fin
    dataset:
      name: newstest2019
      type: wmt-2019-news
      args: eng-fin
    metrics:
    - name: BLEU
      type: bleu
      value: 26.4
---
# opus-mt-tc-big-en-fi

Neural machine translation model for translating from English (en) to Finnish (fi).

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

* Release: 2022-03-09
* source language(s): eng
* target language(s): fin
* valid target language labels: >>fin<<
* model: transformer (big)
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-09.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-fin/opusTCv20210807+bt_transformer-big_2022-03-09.zip)
* more information released models: [OPUS-MT eng-fin README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-fin/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>fin<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "Russia is big.",
    "Touch wood!"
]

model_name = "pytorch-models/opus-mt-tc-big-en-fi"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Venäjä on suuri.
#     Kosketa puuta!
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-fi")
print(pipe("Russia is big."))

# expected output: Venäjä on suuri.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-09.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-fin/opusTCv20210807+bt_transformer-big_2022-03-09.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-09.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-fin/opusTCv20210807+bt_transformer-big_2022-03-09.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| eng-fin | tatoeba-test-v2021-08-07 | 0.64352 | 39.3 | 10690 | 65122 |
| eng-fin | flores101-devtest | 0.61334 | 27.6 | 1012 | 18781 |
| eng-fin | newsdev2015 | 0.58367 | 24.2 | 1500 | 23091 |
| eng-fin | newstest2015 | 0.60080 | 26.4 | 1370 | 19735 |
| eng-fin | newstest2016 | 0.61636 | 28.8 | 3000 | 47678 |
| eng-fin | newstest2017 | 0.64381 | 31.3 | 3002 | 45269 |
| eng-fin | newstest2018 | 0.55626 | 19.7 | 3000 | 44836 |
| eng-fin | newstest2019 | 0.58420 | 26.4 | 1997 | 38369 |
| eng-fin | newstestB2016 | 0.57554 | 23.3 | 3000 | 45766 |
| eng-fin | newstestB2017 | 0.60212 | 26.8 | 3002 | 45506 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: f084bad
* port time: Tue Mar 22 14:42:32 EET 2022
* port machine: LM0-400-22516.local

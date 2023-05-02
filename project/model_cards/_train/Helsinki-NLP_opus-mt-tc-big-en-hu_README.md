---
language:
- en
- hu
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-en-hu
  results:
  - task:
      name: Translation eng-hun
      type: translation
      args: eng-hun
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng hun devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 29.6
  - task:
      name: Translation eng-hun
      type: translation
      args: eng-hun
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-hun
    metrics:
    - name: BLEU
      type: bleu
      value: 38.7
  - task:
      name: Translation eng-hun
      type: translation
      args: eng-hun
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: eng-hun
    metrics:
    - name: BLEU
      type: bleu
      value: 20.3
---
# opus-mt-tc-big-en-hu

Neural machine translation model for translating from English (en) to Hungarian (hu).

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

* Release: 2022-02-25
* source language(s): eng
* target language(s): hun
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-02-25.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hun/opusTCv20210807+bt_transformer-big_2022-02-25.zip)
* more information released models: [OPUS-MT eng-hun README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-hun/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "I wish I hadn't seen such a horrible film.",
    "She's at school."
]

model_name = "pytorch-models/opus-mt-tc-big-en-hu"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Bárcsak ne láttam volna ilyen szörnyű filmet.
#     Iskolában van.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-hu")
print(pipe("I wish I hadn't seen such a horrible film."))

# expected output: Bárcsak ne láttam volna ilyen szörnyű filmet.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-02-25.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hun/opusTCv20210807+bt_transformer-big_2022-02-25.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-02-25.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hun/opusTCv20210807+bt_transformer-big_2022-02-25.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| eng-hun | tatoeba-test-v2021-08-07 | 0.62096 | 38.7 | 13037 | 79562 |
| eng-hun | flores101-devtest | 0.60159 | 29.6 | 1012 | 22183 |
| eng-hun | newssyscomb2009 | 0.51918 | 20.6 | 502 | 9733 |
| eng-hun | newstest2009 | 0.50973 | 20.3 | 2525 | 54965 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 17:21:20 EEST 2022
* port machine: LM0-400-22516.local

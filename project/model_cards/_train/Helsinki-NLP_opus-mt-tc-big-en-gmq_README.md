---
language:
- da
- en
- fo
- gmq
- is
- nb
- nn
- false
- sv
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-en-gmq
  results:
  - task:
      name: Translation eng-dan
      type: translation
      args: eng-dan
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng dan devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 47.7
  - task:
      name: Translation eng-isl
      type: translation
      args: eng-isl
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng isl devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 24.1
  - task:
      name: Translation eng-nob
      type: translation
      args: eng-nob
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng nob devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 34.5
  - task:
      name: Translation eng-swe
      type: translation
      args: eng-swe
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng swe devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 46.9
  - task:
      name: Translation eng-isl
      type: translation
      args: eng-isl
    dataset:
      name: newsdev2021.en-is
      type: newsdev2021.en-is
      args: eng-isl
    metrics:
    - name: BLEU
      type: bleu
      value: 22.6
  - task:
      name: Translation eng-dan
      type: translation
      args: eng-dan
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-dan
    metrics:
    - name: BLEU
      type: bleu
      value: 61.6
  - task:
      name: Translation eng-isl
      type: translation
      args: eng-isl
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-isl
    metrics:
    - name: BLEU
      type: bleu
      value: 39.9
  - task:
      name: Translation eng-nno
      type: translation
      args: eng-nno
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-nno
    metrics:
    - name: BLEU
      type: bleu
      value: 40.1
  - task:
      name: Translation eng-nob
      type: translation
      args: eng-nob
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-nob
    metrics:
    - name: BLEU
      type: bleu
      value: 57.3
  - task:
      name: Translation eng-swe
      type: translation
      args: eng-swe
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-swe
    metrics:
    - name: BLEU
      type: bleu
      value: 60.9
  - task:
      name: Translation eng-isl
      type: translation
      args: eng-isl
    dataset:
      name: newstest2021.en-is
      type: wmt-2021-news
      args: eng-isl
    metrics:
    - name: BLEU
      type: bleu
      value: 21.5
---
# opus-mt-tc-big-en-gmq

Neural machine translation model for translating from English (en) to North Germanic languages (gmq).

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

* Release: 2022-03-17
* source language(s): eng
* target language(s): dan fao isl nno nob nor swe
* valid target language labels: >>dan<< >>fao<< >>isl<< >>nno<< >>nob<< >>nor<< >>swe<<
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmq/opusTCv20210807+bt_transformer-big_2022-03-17.zip)
* more information released models: [OPUS-MT eng-gmq README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-gmq/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>dan<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>nno<< The United States borders Canada.",
    ">>nob<< This is the biggest hotel in this city."
]

model_name = "pytorch-models/opus-mt-tc-big-en-gmq"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     USA grensar til Canada.
#     Dette er det største hotellet i denne byen.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-gmq")
print(pipe(">>nno<< The United States borders Canada."))

# expected output: USA grensar til Canada.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmq/opusTCv20210807+bt_transformer-big_2022-03-17.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmq/opusTCv20210807+bt_transformer-big_2022-03-17.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| eng-dan | tatoeba-test-v2021-08-07 | 0.75165 | 61.6 | 10795 | 79385 |
| eng-fao | tatoeba-test-v2021-08-07 | 0.40395 | 18.3 | 294 | 1933 |
| eng-isl | tatoeba-test-v2021-08-07 | 0.59731 | 39.9 | 2503 | 19023 |
| eng-nno | tatoeba-test-v2021-08-07 | 0.61271 | 40.1 | 460 | 3428 |
| eng-nob | tatoeba-test-v2021-08-07 | 0.72380 | 57.3 | 4539 | 36119 |
| eng-swe | tatoeba-test-v2021-08-07 | 0.74197 | 60.9 | 10362 | 68067 |
| eng-dan | flores101-devtest | 0.70810 | 47.7 | 1012 | 24638 |
| eng-isl | flores101-devtest | 0.52076 | 24.1 | 1012 | 22834 |
| eng-nob | flores101-devtest | 0.62760 | 34.5 | 1012 | 23873 |
| eng-swe | flores101-devtest | 0.70129 | 46.9 | 1012 | 23121 |
| eng-isl | newsdev2021.en-is | 0.50376 | 22.6 | 2004 | 43721 |
| eng-isl | newstest2021.en-is | 0.50516 | 21.5 | 1000 | 25233 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 17:14:46 EEST 2022
* port machine: LM0-400-22516.local

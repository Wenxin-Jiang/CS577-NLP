---
language:
- da
- is
- nb
- nn
- sv

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-gmq-gmq
  results:
  - task:
      name: Translation isl-swe
      type: translation
      args: isl-swe
    dataset:
      name: europeana2021
      type: europeana2021
      args: isl-swe
    metrics:
       - name: BLEU
         type: bleu
         value: 22.2
       - name: chr-F
         type: chrf
         value: 0.45562
  - task:
      name: Translation nob-isl
      type: translation
      args: nob-isl
    dataset:
      name: europeana2021
      type: europeana2021
      args: nob-isl
    metrics:
       - name: BLEU
         type: bleu
         value: 29.7
       - name: chr-F
         type: chrf
         value: 0.54171
  - task:
      name: Translation nob-swe
      type: translation
      args: nob-swe
    dataset:
      name: europeana2021
      type: europeana2021
      args: nob-swe
    metrics:
       - name: BLEU
         type: bleu
         value: 54.0
       - name: chr-F
         type: chrf
         value: 0.73891
  - task:
      name: Translation dan-isl
      type: translation
      args: dan-isl
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan isl devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.2
       - name: chr-F
         type: chrf
         value: 0.50227
  - task:
      name: Translation dan-nob
      type: translation
      args: dan-nob
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan nob devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.6
       - name: chr-F
         type: chrf
         value: 0.58445
  - task:
      name: Translation dan-swe
      type: translation
      args: dan-swe
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan swe devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 38.5
       - name: chr-F
         type: chrf
         value: 0.65000
  - task:
      name: Translation isl-dan
      type: translation
      args: isl-dan
    dataset:
      name: flores101-devtest
      type: flores_101
      args: isl dan devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 27.2
       - name: chr-F
         type: chrf
         value: 0.53630
  - task:
      name: Translation isl-nob
      type: translation
      args: isl-nob
    dataset:
      name: flores101-devtest
      type: flores_101
      args: isl nob devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 20.5
       - name: chr-F
         type: chrf
         value: 0.49434
  - task:
      name: Translation isl-swe
      type: translation
      args: isl-swe
    dataset:
      name: flores101-devtest
      type: flores_101
      args: isl swe devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 26.0
       - name: chr-F
         type: chrf
         value: 0.53373
  - task:
      name: Translation nob-dan
      type: translation
      args: nob-dan
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob dan devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.7
       - name: chr-F
         type: chrf
         value: 0.59657
  - task:
      name: Translation nob-isl
      type: translation
      args: nob-isl
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob isl devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 18.9
       - name: chr-F
         type: chrf
         value: 0.47432
  - task:
      name: Translation nob-swe
      type: translation
      args: nob-swe
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob swe devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.3
       - name: chr-F
         type: chrf
         value: 0.60030
  - task:
      name: Translation swe-dan
      type: translation
      args: swe-dan
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe dan devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 39.0
       - name: chr-F
         type: chrf
         value: 0.64340
  - task:
      name: Translation swe-isl
      type: translation
      args: swe-isl
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe isl devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.7
       - name: chr-F
         type: chrf
         value: 0.49590
  - task:
      name: Translation swe-nob
      type: translation
      args: swe-nob
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe nob devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.9
       - name: chr-F
         type: chrf
         value: 0.58336
  - task:
      name: Translation dan-nob
      type: translation
      args: dan-nob
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: dan-nob
    metrics:
       - name: BLEU
         type: bleu
         value: 78.2
       - name: chr-F
         type: chrf
         value: 0.87556
  - task:
      name: Translation dan-swe
      type: translation
      args: dan-swe
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: dan-swe
    metrics:
       - name: BLEU
         type: bleu
         value: 72.5
       - name: chr-F
         type: chrf
         value: 0.83556
  - task:
      name: Translation nno-nob
      type: translation
      args: nno-nob
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nno-nob
    metrics:
       - name: BLEU
         type: bleu
         value: 78.9
       - name: chr-F
         type: chrf
         value: 0.88349
  - task:
      name: Translation nob-dan
      type: translation
      args: nob-dan
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nob-dan
    metrics:
       - name: BLEU
         type: bleu
         value: 73.9
       - name: chr-F
         type: chrf
         value: 0.85345
  - task:
      name: Translation nob-nno
      type: translation
      args: nob-nno
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nob-nno
    metrics:
       - name: BLEU
         type: bleu
         value: 55.2
       - name: chr-F
         type: chrf
         value: 0.74571
  - task:
      name: Translation nob-swe
      type: translation
      args: nob-swe
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nob-swe
    metrics:
       - name: BLEU
         type: bleu
         value: 73.9
       - name: chr-F
         type: chrf
         value: 0.84747
  - task:
      name: Translation swe-dan
      type: translation
      args: swe-dan
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: swe-dan
    metrics:
       - name: BLEU
         type: bleu
         value: 72.6
       - name: chr-F
         type: chrf
         value: 0.83392
  - task:
      name: Translation swe-nob
      type: translation
      args: swe-nob
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: swe-nob
    metrics:
       - name: BLEU
         type: bleu
         value: 76.3
       - name: chr-F
         type: chrf
         value: 0.85815
---
# opus-mt-tc-big-gmq-gmq

## Table of Contents
- [Model Details](#model-details)
- [Uses](#uses)
- [Risks, Limitations and Biases](#risks-limitations-and-biases)
- [How to Get Started With the Model](#how-to-get-started-with-the-model)
- [Training](#training)
- [Evaluation](#evaluation)
- [Citation Information](#citation-information)
- [Acknowledgements](#acknowledgements)

## Model Details

Neural machine translation model for translating from North Germanic languages (gmq) to North Germanic languages (gmq).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-07-29
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): dan fao isl nno nob nor swe
  - Target Language(s): dan isl nno nob nor swe
  - Language Pair(s): dan-isl dan-nob dan-swe isl-dan isl-nob isl-swe nno-nob nob-dan nob-isl nob-nno nob-swe swe-dan swe-isl swe-nob
  - Valid Target Language Labels: >>dan<< >>fao<< >>isl<< >>jut<< >>nno<< >>nob<< >>non<< >>nrn<< >>ovd<< >>qer<< >>rmg<< >>swe<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-07-29.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-gmq/opusTCv20210807_transformer-big_2022-07-29.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT gmq-gmq README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmq-gmq/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>dan<<`

## Uses

This model can be used for translation and text-to-text generation.

## Risks, Limitations and Biases

**CONTENT WARNING: Readers should be aware that the model is trained on various public data sets that may contain content that is disturbing, offensive, and can propagate historical and current stereotypes.**

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).

## How to Get Started With the Model

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>fao<< Jeg er bange for kakerlakker.",
    ">>nob<< Vladivostok är en stad i Ryssland."
]

model_name = "pytorch-models/opus-mt-tc-big-gmq-gmq"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Tað eru uml.
#     Vladivostok er en by i Russland.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-gmq-gmq")
print(pipe(">>fao<< Jeg er bange for kakerlakker."))

# expected output: Tað eru uml.
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-07-29.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-gmq/opusTCv20210807_transformer-big_2022-07-29.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-07-29.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-gmq/opusTCv20210807_transformer-big_2022-07-29.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-07-29.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-gmq/opusTCv20210807_transformer-big_2022-07-29.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| dan-nob | tatoeba-test-v2021-08-07 | 0.87556 | 78.2 | 1299 | 9620 |
| dan-swe | tatoeba-test-v2021-08-07 | 0.83556 | 72.5 | 1549 | 10060 |
| nno-nob | tatoeba-test-v2021-08-07 | 0.88349 | 78.9 | 467 | 3129 |
| nob-dan | tatoeba-test-v2021-08-07 | 0.85345 | 73.9 | 1299 | 9794 |
| nob-nno | tatoeba-test-v2021-08-07 | 0.74571 | 55.2 | 466 | 3141 |
| nob-swe | tatoeba-test-v2021-08-07 | 0.84747 | 73.9 | 563 | 3698 |
| swe-dan | tatoeba-test-v2021-08-07 | 0.83392 | 72.6 | 1549 | 10239 |
| swe-nob | tatoeba-test-v2021-08-07 | 0.85815 | 76.3 | 563 | 3708 |
| isl-swe | europeana2021 | 0.45562 | 22.2 | 563 | 10293 |
| nob-isl | europeana2021 | 0.54171 | 29.7 | 538 | 9932 |
| nob-swe | europeana2021 | 0.73891 | 54.0 | 538 | 9885 |
| dan-isl | flores101-devtest | 0.50227 | 22.2 | 1012 | 22834 |
| dan-nob | flores101-devtest | 0.58445 | 28.6 | 1012 | 23873 |
| dan-swe | flores101-devtest | 0.65000 | 38.5 | 1012 | 23121 |
| isl-dan | flores101-devtest | 0.53630 | 27.2 | 1012 | 24638 |
| isl-nob | flores101-devtest | 0.49434 | 20.5 | 1012 | 23873 |
| isl-swe | flores101-devtest | 0.53373 | 26.0 | 1012 | 23121 |
| nob-dan | flores101-devtest | 0.59657 | 31.7 | 1012 | 24638 |
| nob-isl | flores101-devtest | 0.47432 | 18.9 | 1012 | 22834 |
| nob-swe | flores101-devtest | 0.60030 | 31.3 | 1012 | 23121 |
| swe-dan | flores101-devtest | 0.64340 | 39.0 | 1012 | 24638 |
| swe-isl | flores101-devtest | 0.49590 | 21.7 | 1012 | 22834 |
| swe-nob | flores101-devtest | 0.58336 | 28.9 | 1012 | 23873 |

## Citation Information

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

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 8b9f0b0
* port time: Fri Aug 12 23:59:02 EEST 2022
* port machine: LM0-400-22516.local

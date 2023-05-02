---
language:
- ca
- es
- fr
- gl
- it
- lt
- lv
- pt

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-itc-bat
  results:
  - task:
      name: Translation cat-lav
      type: translation
      args: cat-lav
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat lav devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.9
       - name: chr-F
         type: chrf
         value: 0.52215
  - task:
      name: Translation cat-lit
      type: translation
      args: cat-lit
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat lit devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 20.2
       - name: chr-F
         type: chrf
         value: 0.52380
  - task:
      name: Translation fra-lav
      type: translation
      args: fra-lav
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra lav devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.0
       - name: chr-F
         type: chrf
         value: 0.53390
  - task:
      name: Translation fra-lit
      type: translation
      args: fra-lit
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra lit devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.1
       - name: chr-F
         type: chrf
         value: 0.53595
  - task:
      name: Translation glg-lav
      type: translation
      args: glg-lav
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg lav devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 20.7
       - name: chr-F
         type: chrf
         value: 0.51043
  - task:
      name: Translation glg-lit
      type: translation
      args: glg-lit
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg lit devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 19.9
       - name: chr-F
         type: chrf
         value: 0.51854
  - task:
      name: Translation ita-lav
      type: translation
      args: ita-lav
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita lav devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 19.6
       - name: chr-F
         type: chrf
         value: 0.51065
  - task:
      name: Translation ita-lit
      type: translation
      args: ita-lit
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita lit devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 17.4
       - name: chr-F
         type: chrf
         value: 0.51309
  - task:
      name: Translation por-lav
      type: translation
      args: por-lav
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por lav devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.9
       - name: chr-F
         type: chrf
         value: 0.53493
  - task:
      name: Translation por-lit
      type: translation
      args: por-lit
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por lit devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.8
       - name: chr-F
         type: chrf
         value: 0.53821
  - task:
      name: Translation spa-lav
      type: translation
      args: spa-lav
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa lav devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 17.4
       - name: chr-F
         type: chrf
         value: 0.49290
  - task:
      name: Translation spa-lit
      type: translation
      args: spa-lit
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa lit devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 16.2
       - name: chr-F
         type: chrf
         value: 0.49836
  - task:
      name: Translation ita-lit
      type: translation
      args: ita-lit
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ita-lit
    metrics:
       - name: BLEU
         type: bleu
         value: 40.9
       - name: chr-F
         type: chrf
         value: 0.67640
  - task:
      name: Translation spa-lit
      type: translation
      args: spa-lit
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: spa-lit
    metrics:
       - name: BLEU
         type: bleu
         value: 45.9
       - name: chr-F
         type: chrf
         value: 0.68805
---
# opus-mt-tc-big-itc-bat

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

Neural machine translation model for translating from Italic languages (itc) to Baltic languages (bat).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-07-27
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): cat fra glg ita por spa
  - Target Language(s): lav lit prg
  - Language Pair(s): cat-lav cat-lit fra-lav fra-lit glg-lav glg-lit ita-lav ita-lit por-lav por-lit spa-lit
  - Valid Target Language Labels: >>lav<< >>lit<< >>ltg<< >>ndf<< >>olt<< >>prg<< >>prg_Latn<< >>sgs<< >>svx<< >>sxl<< >>xcu<< >>xgl<< >>xsv<< >>xzm<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-bat/opusTCv20210807_transformer-big_2022-07-27.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT itc-bat README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/itc-bat/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>lav<<`

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
    ">>lit<< Els gats són complexos individus.",
    ">>sgs<< No."
]

model_name = "pytorch-models/opus-mt-tc-big-itc-bat"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Katės yra sudėtingi individai.
#     no no no no no no no no no no no no no no no no no no no no no
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-itc-bat")
print(pipe(">>lit<< Els gats són complexos individus."))

# expected output: Katės yra sudėtingi individai.
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-bat/opusTCv20210807_transformer-big_2022-07-27.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-bat/opusTCv20210807_transformer-big_2022-07-27.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-bat/opusTCv20210807_transformer-big_2022-07-27.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| ita-lit | tatoeba-test-v2021-08-07 | 0.67640 | 40.9 | 224 | 1321 |
| spa-lit | tatoeba-test-v2021-08-07 | 0.68805 | 45.9 | 454 | 2352 |
| cat-lav | flores101-devtest | 0.52215 | 21.9 | 1012 | 22092 |
| cat-lit | flores101-devtest | 0.52380 | 20.2 | 1012 | 20695 |
| fra-lav | flores101-devtest | 0.53390 | 23.0 | 1012 | 22092 |
| fra-lit | flores101-devtest | 0.53595 | 21.1 | 1012 | 20695 |
| glg-lav | flores101-devtest | 0.51043 | 20.7 | 1012 | 22092 |
| glg-lit | flores101-devtest | 0.51854 | 19.9 | 1012 | 20695 |
| ita-lav | flores101-devtest | 0.51065 | 19.6 | 1012 | 22092 |
| ita-lit | flores101-devtest | 0.51309 | 17.4 | 1012 | 20695 |
| por-lav | flores101-devtest | 0.53493 | 22.9 | 1012 | 22092 |
| por-lit | flores101-devtest | 0.53821 | 21.8 | 1012 | 20695 |
| spa-lav | flores101-devtest | 0.49290 | 17.4 | 1012 | 22092 |
| spa-lit | flores101-devtest | 0.49836 | 16.2 | 1012 | 20695 |

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
* port time: Sat Aug 13 00:04:44 EEST 2022
* port machine: LM0-400-22516.local

---
language:
- bg
- fi
- hr
- sl
- sr
language_bcp47:
- sr_Cyrl

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-fi-zls
  results:
  - task:
      name: Translation fin-bul
      type: translation
      args: fin-bul
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fin bul devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 26.2
       - name: chr-F
         type: chrf
         value: 0.54912
  - task:
      name: Translation fin-hrv
      type: translation
      args: fin-hrv
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fin hrv devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.3
       - name: chr-F
         type: chrf
         value: 0.51468
  - task:
      name: Translation fin-slv
      type: translation
      args: fin-slv
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fin slv devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.3
       - name: chr-F
         type: chrf
         value: 0.51226
  - task:
      name: Translation fin-srp_Cyrl
      type: translation
      args: fin-srp_Cyrl
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fin srp_Cyrl devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.8
       - name: chr-F
         type: chrf
         value: 0.50774
---
# opus-mt-tc-big-fi-zls

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

Neural machine translation model for translating from Finnish (fi) to South Slavic languages (zls).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-07-23
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): fin
  - Target Language(s): bul hrv slv srp_Cyrl
  - Language Pair(s): fin-bul fin-hrv fin-slv fin-srp_Cyrl
  - Valid Target Language Labels: >>bos<< >>bos_Cyrl<< >>bos_Latn<< >>bul<< >>chu<< >>hbs<< >>hbs_Cyrl<< >>hrv<< >>kjv<< >>mkd<< >>slv<< >>srp<< >>srp_Cyrl<< >>srp_Latn<< >>svm<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-07-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-zls/opusTCv20210807_transformer-big_2022-07-23.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT fin-zls README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fin-zls/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>slv<<`

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
    ">>bul<< Ajattelen vain sinua.",
    ">>slv<< Virtahevot rakastavat vettä."
]

model_name = "pytorch-models/opus-mt-tc-big-fi-zls"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Мисля само за теб.
#     Povodni konji obožujejo vodo.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-fi-zls")
print(pipe(">>bul<< Ajattelen vain sinua."))

# expected output: Мисля само за теб.
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-07-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-zls/opusTCv20210807_transformer-big_2022-07-23.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-07-23.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-zls/opusTCv20210807_transformer-big_2022-07-23.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-07-23.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-zls/opusTCv20210807_transformer-big_2022-07-23.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| fin-bul | flores101-devtest | 0.54912 | 26.2 | 1012 | 24700 |
| fin-hrv | flores101-devtest | 0.51468 | 21.3 | 1012 | 22423 |
| fin-slv | flores101-devtest | 0.51226 | 22.3 | 1012 | 23425 |
| fin-srp_Cyrl | flores101-devtest | 0.50774 | 21.8 | 1012 | 23456 |

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
* port time: Sat Aug 13 00:08:29 EEST 2022
* port machine: LM0-400-22516.local

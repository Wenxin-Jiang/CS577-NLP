---
language:
- bs
- en
- hr
- sh
- sr
language_bcp47:
- bs_Latn
- sr_Cyrl
- sr_Latn

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-base-en-sh
  results:
  - task:
      name: Translation eng-hrv
      type: translation
      args: eng-hrv
    dataset:
      name: flores200-dev
      type: flores200-dev
      args: eng-hrv
    metrics:
       - name: BLEU
         type: bleu
         value: 28.1
       - name: chr-F
         type: chrf
         value: 0.57963
  - task:
      name: Translation eng-srp_Cyrl
      type: translation
      args: eng-srp_Cyrl
    dataset:
      name: flores200-dev
      type: flores200-dev
      args: eng-srp_Cyrl
    metrics:
       - name: BLEU
         type: bleu
         value: 32.2
       - name: chr-F
         type: chrf
         value: 0.60096
  - task:
      name: Translation eng-hrv
      type: translation
      args: eng-hrv
    dataset:
      name: flores200-devtest
      type: flores200-devtest
      args: eng-hrv
    metrics:
       - name: BLEU
         type: bleu
         value: 28.9
       - name: chr-F
         type: chrf
         value: 0.58652
  - task:
      name: Translation eng-srp_Cyrl
      type: translation
      args: eng-srp_Cyrl
    dataset:
      name: flores200-devtest
      type: flores200-devtest
      args: eng-srp_Cyrl
    metrics:
       - name: BLEU
         type: bleu
         value: 31.7
       - name: chr-F
         type: chrf
         value: 0.59874
  - task:
      name: Translation eng-hrv
      type: translation
      args: eng-hrv
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng hrv devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.7
       - name: chr-F
         type: chrf
         value: 0.586
  - task:
      name: Translation eng-srp_Cyrl
      type: translation
      args: eng-srp_Cyrl
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng srp_Cyrl devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.7
       - name: chr-F
         type: chrf
         value: 0.59874
  - task:
      name: Translation eng-bos_Latn
      type: translation
      args: eng-bos_Latn
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-bos_Latn
    metrics:
       - name: BLEU
         type: bleu
         value: 46.3
       - name: chr-F
         type: chrf
         value: 0.666
  - task:
      name: Translation eng-hbs
      type: translation
      args: eng-hbs
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-hbs
    metrics:
       - name: BLEU
         type: bleu
         value: 42.1
       - name: chr-F
         type: chrf
         value: 0.631
  - task:
      name: Translation eng-hrv
      type: translation
      args: eng-hrv
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-hrv
    metrics:
       - name: BLEU
         type: bleu
         value: 49.7
       - name: chr-F
         type: chrf
         value: 0.691
  - task:
      name: Translation eng-srp_Cyrl
      type: translation
      args: eng-srp_Cyrl
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-srp_Cyrl
    metrics:
       - name: BLEU
         type: bleu
         value: 45.1
       - name: chr-F
         type: chrf
         value: 0.645
  - task:
      name: Translation eng-srp_Latn
      type: translation
      args: eng-srp_Latn
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-srp_Latn
    metrics:
       - name: BLEU
         type: bleu
         value: 39.8
       - name: chr-F
         type: chrf
         value: 0.613
---
# opus-mt-tc-base-en-sh

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

Neural machine translation model for translating from English (en) to Serbo-Croatian (sh).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-align)
- **Release**: 2021-04-20
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): eng
  - Target Language(s): bos_Latn hbs hrv srp_Cyrl srp_Latn
  - Language Pair(s): eng-bos_Latn eng-hbs eng-hrv eng-srp_Cyrl eng-srp_Latn
  - Valid Target Language Labels: >>bos_Cyrl<< >>bos_Latn<< >>cnr<< >>cnr_Latn<< >>hbs<< >>hbs_Cyrl<< >>hrv<< >>srp_Cyrl<< >>srp_Latn<<
- **Original Model**: [opus+bt-2021-04-20.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hbs/opus+bt-2021-04-20.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT eng-hbs README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-hbs/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>bos_Latn<<`

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
    ">>hrv<< You're about to make a very serious mistake.",
    ">>hbs<< I've just been too busy."
]

model_name = "pytorch-models/opus-mt-tc-base-en-sh"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Ti si o tome napraviti vrlo ozbiljnu pogrešku.
#     [4]
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-base-en-sh")
print(pipe(">>hrv<< You're about to make a very serious mistake."))

# expected output: Ti si o tome napraviti vrlo ozbiljnu pogrešku.
```

## Training

- **Data**: opus+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-align
- **Original MarianNMT Model**: [opus+bt-2021-04-20.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hbs/opus+bt-2021-04-20.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opus+bt-2021-04-20.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hbs/opus+bt-2021-04-20.test.txt)
* test set scores: [opus+bt-2021-04-20.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hbs/opus+bt-2021-04-20.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| eng-bos_Latn | tatoeba-test-v2021-08-07 | 0.666 | 46.3 | 301 | 1650 |
| eng-hbs | tatoeba-test-v2021-08-07 | 0.631 | 42.1 | 10017 | 63927 |
| eng-hrv | tatoeba-test-v2021-08-07 | 0.691 | 49.7 | 1480 | 9396 |
| eng-srp_Cyrl | tatoeba-test-v2021-08-07 | 0.645 | 45.1 | 1580 | 9152 |
| eng-srp_Latn | tatoeba-test-v2021-08-07 | 0.613 | 39.8 | 6656 | 43729 |
| eng-hrv | flores101-devtest | 0.586 | 28.7 | 1012 | 22423 |
| eng-hrv | flores200-dev | 0.57963 | 28.1 | 997 | 21567 |
| eng-hrv | flores200-devtest | 0.58652 | 28.9 | 1012 | 22423 |
| eng-srp_Cyrl | flores101-devtest | 0.59874 | 31.7 | 1012 | 23456 |
| eng-srp_Cyrl | flores200-dev | 0.60096 | 32.2 | 997 | 22384 |
| eng-srp_Cyrl | flores200-devtest | 0.59874 | 31.7 | 1012 | 23456 |

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
* OPUS-MT git hash: e2a6299
* port time: Tue Oct 11 10:14:32 CEST 2022
* port machine: LM0-400-22516.local

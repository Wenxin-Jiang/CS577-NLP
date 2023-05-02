---
language:
- ar
- da
- sv

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-gmq-ar
  results:
  - task:
      name: Translation dan-ara
      type: translation
      args: dan-ara
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan ara devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 19.9
       - name: chr-F
         type: chrf
         value: 0.52841
  - task:
      name: Translation nob-ara
      type: translation
      args: nob-ara
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob ara devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 16.8
       - name: chr-F
         type: chrf
         value: 0.49670
  - task:
      name: Translation swe-ara
      type: translation
      args: swe-ara
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe ara devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 19.3
       - name: chr-F
         type: chrf
         value: 0.51882
---
# opus-mt-tc-big-gmq-ar

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

Neural machine translation model for translating from North Germanic languages (gmq) to Arabic (ar).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-07-27
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): dan swe
  - Target Language(s): ara
  - Language Pair(s): dan-ara swe-ara
  - Valid Target Language Labels: >>apc<< >>ara<< >>arq<< >>arz<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-ara/opusTCv20210807_transformer-big_2022-07-27.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT gmq-ara README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmq-ara/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>><<`

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
    ">>ara<< Jeg elsker semitiske sprog.",
    ">>ara<< Vad handlar boken om?"
]

model_name = "pytorch-models/opus-mt-tc-big-gmq-ar"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     أحبّ اللغات الساميّة.
#     عن ماذا يتحدث الكتاب؟
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-gmq-ar")
print(pipe(">>ara<< Jeg elsker semitiske sprog."))

# expected output: أحبّ اللغات الساميّة.
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-ara/opusTCv20210807_transformer-big_2022-07-27.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-ara/opusTCv20210807_transformer-big_2022-07-27.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-ara/opusTCv20210807_transformer-big_2022-07-27.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| dan-ara | flores101-devtest | 0.52841 | 19.9 | 1012 | 21357 |
| nob-ara | flores101-devtest | 0.49670 | 16.8 | 1012 | 21357 |
| swe-ara | flores101-devtest | 0.51882 | 19.3 | 1012 | 21357 |

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
* port time: Sat Aug 13 00:05:06 EEST 2022
* port machine: LM0-400-22516.local

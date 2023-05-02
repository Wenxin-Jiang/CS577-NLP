---
language:
- ar
- ca
- es
- fr
- gl
- it
- pt
- ro

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-itc-ar
  results:
  - task:
      name: Translation cat-ara
      type: translation
      args: cat-ara
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat ara devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 18.9
       - name: chr-F
         type: chrf
         value: 0.52029
  - task:
      name: Translation fra-ara
      type: translation
      args: fra-ara
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra ara devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 19.5
       - name: chr-F
         type: chrf
         value: 0.52573
  - task:
      name: Translation glg-ara
      type: translation
      args: glg-ara
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg ara devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 19.2
       - name: chr-F
         type: chrf
         value: 0.51181
  - task:
      name: Translation ita-ara
      type: translation
      args: ita-ara
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita ara devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 15.0
       - name: chr-F
         type: chrf
         value: 0.49401
  - task:
      name: Translation por-ara
      type: translation
      args: por-ara
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por ara devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 20.2
       - name: chr-F
         type: chrf
         value: 0.53356
  - task:
      name: Translation ron-ara
      type: translation
      args: ron-ara
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ron ara devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 18.4
       - name: chr-F
         type: chrf
         value: 0.51849
  - task:
      name: Translation spa-ara
      type: translation
      args: spa-ara
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa ara devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 14.3
       - name: chr-F
         type: chrf
         value: 0.47872
  - task:
      name: Translation ita-ara
      type: translation
      args: ita-ara
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ita-ara
    metrics:
       - name: BLEU
         type: bleu
         value: 25.7
       - name: chr-F
         type: chrf
         value: 0.53797
  - task:
      name: Translation spa-ara
      type: translation
      args: spa-ara
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: spa-ara
    metrics:
       - name: BLEU
         type: bleu
         value: 26.6
       - name: chr-F
         type: chrf
         value: 0.55520
---
# opus-mt-tc-big-itc-ar

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

Neural machine translation model for translating from Italic languages (itc) to Arabic (ar).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-08-09
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): cat fra glg ita lat_Latn por ron spa
  - Target Language(s): ara
  - Language Pair(s): cat-ara fra-ara glg-ara ita-ara por-ara ron-ara spa-ara
  - Valid Target Language Labels: >>ajp<< >>apc<< >>ara<< >>arq<< >>ary<< >>arz<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-08-09.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-ara/opusTCv20210807_transformer-big_2022-08-09.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT itc-ara README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/itc-ara/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>ara<<`

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
    ">>ary<< Entiendo.",
    ">>arq<< Por favor entiende mi posición."
]

model_name = "pytorch-models/opus-mt-tc-big-itc-ar"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     فهمتك
#     من فضلك افهم موقفي.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-itc-ar")
print(pipe(">>ary<< Entiendo."))

# expected output: فهمتك
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-08-09.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-ara/opusTCv20210807_transformer-big_2022-08-09.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-08-09.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-ara/opusTCv20210807_transformer-big_2022-08-09.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-08-09.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-ara/opusTCv20210807_transformer-big_2022-08-09.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| fra-ara | tatoeba-test-v2021-08-07 | 0.46463 | 18.9 | 1569 | 7956 |
| ita-ara | tatoeba-test-v2021-08-07 | 0.53797 | 25.7 | 235 | 1161 |
| spa-ara | tatoeba-test-v2021-08-07 | 0.55520 | 26.6 | 1511 | 7547 |
| cat-ara | flores101-devtest | 0.52029 | 18.9 | 1012 | 21357 |
| fra-ara | flores101-devtest | 0.52573 | 19.5 | 1012 | 21357 |
| glg-ara | flores101-devtest | 0.51181 | 19.2 | 1012 | 21357 |
| ita-ara | flores101-devtest | 0.49401 | 15.0 | 1012 | 21357 |
| por-ara | flores101-devtest | 0.53356 | 20.2 | 1012 | 21357 |
| ron-ara | flores101-devtest | 0.51849 | 18.4 | 1012 | 21357 |
| spa-ara | flores101-devtest | 0.47872 | 14.3 | 1012 | 21357 |

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
* port time: Sat Aug 13 00:00:31 EEST 2022
* port machine: LM0-400-22516.local

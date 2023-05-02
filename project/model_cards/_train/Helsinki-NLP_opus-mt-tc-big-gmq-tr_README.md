---
language:
- da
- nb
- sv
- tr

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-gmq-tr
  results:
  - task:
      name: Translation dan-tur
      type: translation
      args: dan-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan tur devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.4
       - name: chr-F
         type: chrf
         value: 0.56363
  - task:
      name: Translation nob-tur
      type: translation
      args: nob-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob tur devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 19.0
       - name: chr-F
         type: chrf
         value: 0.52696
  - task:
      name: Translation swe-tur
      type: translation
      args: swe-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe tur devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.2
       - name: chr-F
         type: chrf
         value: 0.54996
  - task:
      name: Translation dan-tur
      type: translation
      args: dan-tur
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: dan-tur
    metrics:
       - name: BLEU
         type: bleu
         value: 43.0
       - name: chr-F
         type: chrf
         value: 0.67830
  - task:
      name: Translation swe-tur
      type: translation
      args: swe-tur
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: swe-tur
    metrics:
       - name: BLEU
         type: bleu
         value: 34.2
       - name: chr-F
         type: chrf
         value: 0.63653
---
# opus-mt-tc-big-gmq-tr

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

Neural machine translation model for translating from North Germanic languages (gmq) to Turkish (tr).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-07-26
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): dan nno nob nor swe
  - Target Language(s): tur
  - Language Pair(s): dan-tur nob-tur swe-tur
  - Valid Target Language Labels: 
- **Original Model**: [opusTCv20210807_transformer-big_2022-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-tur/opusTCv20210807_transformer-big_2022-07-26.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT gmq-tur README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmq-tur/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

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
    "Aftensmaden dufter lækkert.",
    "Vi ser vad som händer tillsammans."
]

model_name = "pytorch-models/opus-mt-tc-big-gmq-tr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Akşam yemeği çok güzel kokuyor.
#     Birlikte bakalım neler olacak.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-gmq-tr")
print(pipe("Aftensmaden dufter lækkert."))

# expected output: Akşam yemeği çok güzel kokuyor.
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-tur/opusTCv20210807_transformer-big_2022-07-26.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-tur/opusTCv20210807_transformer-big_2022-07-26.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-tur/opusTCv20210807_transformer-big_2022-07-26.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| dan-tur | tatoeba-test-v2021-08-07 | 0.67830 | 43.0 | 758 | 3436 |
| swe-tur | tatoeba-test-v2021-08-07 | 0.63653 | 34.2 | 203 | 1008 |
| dan-tur | flores101-devtest | 0.56363 | 23.4 | 1012 | 20253 |
| nob-tur | flores101-devtest | 0.52696 | 19.0 | 1012 | 20253 |
| swe-tur | flores101-devtest | 0.54996 | 22.2 | 1012 | 20253 |

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
* port time: Sat Aug 13 00:05:52 EEST 2022
* port machine: LM0-400-22516.local

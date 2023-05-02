---
language:
- ca
- es
- fr
- gl
- it
- oc
- pt
- ro
- tr

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-itc-tr
  results:
  - task:
      name: Translation cat-tur
      type: translation
      args: cat-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat tur devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.7
       - name: chr-F
         type: chrf
         value: 0.54892
  - task:
      name: Translation fra-tur
      type: translation
      args: fra-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra tur devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.7
       - name: chr-F
         type: chrf
         value: 0.55342
  - task:
      name: Translation glg-tur
      type: translation
      args: glg-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg tur devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 20.6
       - name: chr-F
         type: chrf
         value: 0.53936
  - task:
      name: Translation ita-tur
      type: translation
      args: ita-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita tur devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 18.4
       - name: chr-F
         type: chrf
         value: 0.52842
  - task:
      name: Translation oci-tur
      type: translation
      args: oci-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: oci tur devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 17.6
       - name: chr-F
         type: chrf
         value: 0.50618
  - task:
      name: Translation por-tur
      type: translation
      args: por-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por tur devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.5
       - name: chr-F
         type: chrf
         value: 0.56396
  - task:
      name: Translation ron-tur
      type: translation
      args: ron-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ron tur devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.5
       - name: chr-F
         type: chrf
         value: 0.55409
  - task:
      name: Translation spa-tur
      type: translation
      args: spa-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa tur devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 16.5
       - name: chr-F
         type: chrf
         value: 0.51066
  - task:
      name: Translation fra-tur
      type: translation
      args: fra-tur
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fra-tur
    metrics:
       - name: BLEU
         type: bleu
         value: 34.8
       - name: chr-F
         type: chrf
         value: 0.63006
  - task:
      name: Translation ita-tur
      type: translation
      args: ita-tur
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ita-tur
    metrics:
       - name: BLEU
         type: bleu
         value: 34.9
       - name: chr-F
         type: chrf
         value: 0.59991
  - task:
      name: Translation por-tur
      type: translation
      args: por-tur
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: por-tur
    metrics:
       - name: BLEU
         type: bleu
         value: 40.1
       - name: chr-F
         type: chrf
         value: 0.67836
  - task:
      name: Translation ron-tur
      type: translation
      args: ron-tur
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ron-tur
    metrics:
       - name: BLEU
         type: bleu
         value: 35.5
       - name: chr-F
         type: chrf
         value: 0.64031
  - task:
      name: Translation spa-tur
      type: translation
      args: spa-tur
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: spa-tur
    metrics:
       - name: BLEU
         type: bleu
         value: 45.2
       - name: chr-F
         type: chrf
         value: 0.71524
---
# opus-mt-tc-big-itc-tr

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

Neural machine translation model for translating from Italic languages (itc) to Turkish (tr).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-07-28
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): cat fra glg ita lad lad_Latn oci por ron spa
  - Target Language(s): tur
  - Language Pair(s): cat-tur fra-tur glg-tur ita-tur oci-tur por-tur ron-tur spa-tur
  - Valid Target Language Labels: 
- **Original Model**: [opusTCv20210807_transformer-big_2022-07-28.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-tur/opusTCv20210807_transformer-big_2022-07-28.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT itc-tur README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/itc-tur/README.md)
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
    ""Di che nazionalità sono le tue dottoresse?" "Malese."",
    ""Di che nazionalità sono i nostri amici?" "Maltese.""
]

model_name = "pytorch-models/opus-mt-tc-big-itc-tr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     "Doktorların hangi milletten?" "Malezyalı."
#     "Arkadaşlarımız hangi milletten?" "Maltalı."
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-itc-tr")
print(pipe(""Di che nazionalità sono le tue dottoresse?" "Malese.""))

# expected output: "Doktorların hangi milletten?" "Malezyalı."
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-07-28.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-tur/opusTCv20210807_transformer-big_2022-07-28.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-07-28.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-tur/opusTCv20210807_transformer-big_2022-07-28.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-07-28.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-tur/opusTCv20210807_transformer-big_2022-07-28.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| fra-tur | tatoeba-test-v2021-08-07 | 0.63006 | 34.8 | 2582 | 14307 |
| ita-tur | tatoeba-test-v2021-08-07 | 0.59991 | 34.9 | 10000 | 75807 |
| por-tur | tatoeba-test-v2021-08-07 | 0.67836 | 40.1 | 1794 | 9312 |
| ron-tur | tatoeba-test-v2021-08-07 | 0.64031 | 35.5 | 2460 | 13788 |
| spa-tur | tatoeba-test-v2021-08-07 | 0.71524 | 45.2 | 10615 | 56099 |
| cat-tur | flores101-devtest | 0.54892 | 21.7 | 1012 | 20253 |
| fra-tur | flores101-devtest | 0.55342 | 21.7 | 1012 | 20253 |
| glg-tur | flores101-devtest | 0.53936 | 20.6 | 1012 | 20253 |
| ita-tur | flores101-devtest | 0.52842 | 18.4 | 1012 | 20253 |
| oci-tur | flores101-devtest | 0.50618 | 17.6 | 1012 | 20253 |
| por-tur | flores101-devtest | 0.56396 | 23.5 | 1012 | 20253 |
| ron-tur | flores101-devtest | 0.55409 | 21.5 | 1012 | 20253 |
| spa-tur | flores101-devtest | 0.51066 | 16.5 | 1012 | 20253 |

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
* port time: Sat Aug 13 00:03:26 EEST 2022
* port machine: LM0-400-22516.local

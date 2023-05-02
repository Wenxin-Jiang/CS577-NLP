---
language:
- bg
- de
- hr
- mk
- sh
- sl
- sr
language_bcp47:
- sr_Cyrl
- sr_Latn

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-zls-de
  results:
  - task:
      name: Translation bul-deu
      type: translation
      args: bul-deu
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bul deu devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.4
       - name: chr-F
         type: chrf
         value: 0.57688
  - task:
      name: Translation hrv-deu
      type: translation
      args: hrv-deu
    dataset:
      name: flores101-devtest
      type: flores_101
      args: hrv deu devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 27.4
       - name: chr-F
         type: chrf
         value: 0.56674
  - task:
      name: Translation mkd-deu
      type: translation
      args: mkd-deu
    dataset:
      name: flores101-devtest
      type: flores_101
      args: mkd deu devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 29.3
       - name: chr-F
         type: chrf
         value: 0.57688
  - task:
      name: Translation slv-deu
      type: translation
      args: slv-deu
    dataset:
      name: flores101-devtest
      type: flores_101
      args: slv deu devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 26.7
       - name: chr-F
         type: chrf
         value: 0.56258
  - task:
      name: Translation srp_Cyrl-deu
      type: translation
      args: srp_Cyrl-deu
    dataset:
      name: flores101-devtest
      type: flores_101
      args: srp_Cyrl deu devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 30.7
       - name: chr-F
         type: chrf
         value: 0.59271
  - task:
      name: Translation bul-deu
      type: translation
      args: bul-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bul-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 54.5
       - name: chr-F
         type: chrf
         value: 0.71220
  - task:
      name: Translation hbs-deu
      type: translation
      args: hbs-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hbs-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 54.8
       - name: chr-F
         type: chrf
         value: 0.71283
  - task:
      name: Translation hrv-deu
      type: translation
      args: hrv-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hrv-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 53.1
       - name: chr-F
         type: chrf
         value: 0.69448
  - task:
      name: Translation slv-deu
      type: translation
      args: slv-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: slv-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 21.1
       - name: chr-F
         type: chrf
         value: 0.36339
  - task:
      name: Translation srp_Latn-deu
      type: translation
      args: srp_Latn-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: srp_Latn-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 56.0
       - name: chr-F
         type: chrf
         value: 0.72489
---
# opus-mt-tc-big-zls-de

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

Neural machine translation model for translating from South Slavic languages (zls) to German (de).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-07-26
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): bos_Latn bul hbs hrv mkd slv srp_Cyrl srp_Latn
  - Target Language(s): deu
  - Language Pair(s): bul-deu hbs-deu hrv-deu mkd-deu slv-deu srp_Cyrl-deu srp_Latn-deu
  - Valid Target Language Labels: 
- **Original Model**: [opusTCv20210807_transformer-big_2022-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-deu/opusTCv20210807_transformer-big_2022-07-26.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT zls-deu README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zls-deu/README.md)
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
    "Jesi li ti student?",
    "Dve stvari deca treba da dobiju od svojih roditelja: korene i krila."
]

model_name = "pytorch-models/opus-mt-tc-big-zls-de"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Sind Sie Student?
#     Zwei Dinge sollten Kinder von ihren Eltern bekommen: Wurzeln und Flügel.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zls-de")
print(pipe("Jesi li ti student?"))

# expected output: Sind Sie Student?
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-deu/opusTCv20210807_transformer-big_2022-07-26.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-deu/opusTCv20210807_transformer-big_2022-07-26.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-deu/opusTCv20210807_transformer-big_2022-07-26.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| bul-deu | tatoeba-test-v2021-08-07 | 0.71220 | 54.5 | 314 | 2224 |
| hbs-deu | tatoeba-test-v2021-08-07 | 0.71283 | 54.8 | 1959 | 15559 |
| hrv-deu | tatoeba-test-v2021-08-07 | 0.69448 | 53.1 | 782 | 5734 |
| slv-deu | tatoeba-test-v2021-08-07 | 0.36339 | 21.1 | 492 | 3003 |
| srp_Latn-deu | tatoeba-test-v2021-08-07 | 0.72489 | 56.0 | 986 | 8500 |
| bul-deu | flores101-devtest | 0.57688 | 28.4 | 1012 | 25094 |
| hrv-deu | flores101-devtest | 0.56674 | 27.4 | 1012 | 25094 |
| mkd-deu | flores101-devtest | 0.57688 | 29.3 | 1012 | 25094 |
| slv-deu | flores101-devtest | 0.56258 | 26.7 | 1012 | 25094 |
| srp_Cyrl-deu | flores101-devtest | 0.59271 | 30.7 | 1012 | 25094 |

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
* port time: Sat Aug 13 00:05:30 EEST 2022
* port machine: LM0-400-22516.local

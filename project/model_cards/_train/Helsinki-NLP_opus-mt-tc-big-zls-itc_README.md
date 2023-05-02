---
language:
- bg
- es
- fr
- hr
- it
- mk
- pt
- ro
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
- name: opus-mt-tc-big-zls-itc
  results:
  - task:
      name: Translation bul-fra
      type: translation
      args: bul-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bul fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 34.4
       - name: chr-F
         type: chrf
         value: 0.60640
  - task:
      name: Translation bul-ita
      type: translation
      args: bul-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bul ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.0
       - name: chr-F
         type: chrf
         value: 0.54135
  - task:
      name: Translation bul-por
      type: translation
      args: bul-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bul por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 32.4
       - name: chr-F
         type: chrf
         value: 0.59322
  - task:
      name: Translation bul-ron
      type: translation
      args: bul-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bul ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 27.1
       - name: chr-F
         type: chrf
         value: 0.55558
  - task:
      name: Translation bul-spa
      type: translation
      args: bul-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bul spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.4
       - name: chr-F
         type: chrf
         value: 0.50962
  - task:
      name: Translation hrv-fra
      type: translation
      args: hrv-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: hrv fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 33.1
       - name: chr-F
         type: chrf
         value: 0.59349
  - task:
      name: Translation hrv-ita
      type: translation
      args: hrv-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: hrv ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.5
       - name: chr-F
         type: chrf
         value: 0.52980
  - task:
      name: Translation hrv-por
      type: translation
      args: hrv-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: hrv por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 30.2
       - name: chr-F
         type: chrf
         value: 0.57402
  - task:
      name: Translation hrv-ron
      type: translation
      args: hrv-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: hrv ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 25.9
       - name: chr-F
         type: chrf
         value: 0.53650
  - task:
      name: Translation hrv-spa
      type: translation
      args: hrv-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: hrv spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.5
       - name: chr-F
         type: chrf
         value: 0.50161
  - task:
      name: Translation mkd-fra
      type: translation
      args: mkd-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: mkd fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 35.2
       - name: chr-F
         type: chrf
         value: 0.60801
  - task:
      name: Translation mkd-ita
      type: translation
      args: mkd-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: mkd ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.9
       - name: chr-F
         type: chrf
         value: 0.53543
  - task:
      name: Translation mkd-por
      type: translation
      args: mkd-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: mkd por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 33.9
       - name: chr-F
         type: chrf
         value: 0.59648
  - task:
      name: Translation mkd-ron
      type: translation
      args: mkd-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: mkd ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.0
       - name: chr-F
         type: chrf
         value: 0.54998
  - task:
      name: Translation mkd-spa
      type: translation
      args: mkd-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: mkd spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.8
       - name: chr-F
         type: chrf
         value: 0.51079
  - task:
      name: Translation slv-fra
      type: translation
      args: slv-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: slv fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.5
       - name: chr-F
         type: chrf
         value: 0.58233
  - task:
      name: Translation slv-ita
      type: translation
      args: slv-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: slv ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.4
       - name: chr-F
         type: chrf
         value: 0.52390
  - task:
      name: Translation slv-por
      type: translation
      args: slv-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: slv por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 29.0
       - name: chr-F
         type: chrf
         value: 0.56436
  - task:
      name: Translation slv-ron
      type: translation
      args: slv-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: slv ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 25.0
       - name: chr-F
         type: chrf
         value: 0.53116
  - task:
      name: Translation slv-spa
      type: translation
      args: slv-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: slv spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.1
       - name: chr-F
         type: chrf
         value: 0.49621
  - task:
      name: Translation srp_Cyrl-fra
      type: translation
      args: srp_Cyrl-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: srp_Cyrl fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 36.0
       - name: chr-F
         type: chrf
         value: 0.62110
  - task:
      name: Translation srp_Cyrl-ita
      type: translation
      args: srp_Cyrl-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: srp_Cyrl ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.9
       - name: chr-F
         type: chrf
         value: 0.54083
  - task:
      name: Translation srp_Cyrl-por
      type: translation
      args: srp_Cyrl-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: srp_Cyrl por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 34.9
       - name: chr-F
         type: chrf
         value: 0.61248
  - task:
      name: Translation srp_Cyrl-ron
      type: translation
      args: srp_Cyrl-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: srp_Cyrl ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.8
       - name: chr-F
         type: chrf
         value: 0.56235
  - task:
      name: Translation srp_Cyrl-spa
      type: translation
      args: srp_Cyrl-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: srp_Cyrl spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.8
       - name: chr-F
         type: chrf
         value: 0.51698
  - task:
      name: Translation bul-fra
      type: translation
      args: bul-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bul-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 52.9
       - name: chr-F
         type: chrf
         value: 0.68971
  - task:
      name: Translation bul-ita
      type: translation
      args: bul-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bul-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 45.1
       - name: chr-F
         type: chrf
         value: 0.66412
  - task:
      name: Translation bul-spa
      type: translation
      args: bul-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bul-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 49.7
       - name: chr-F
         type: chrf
         value: 0.66672
  - task:
      name: Translation hbs-fra
      type: translation
      args: hbs-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hbs-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 48.1
       - name: chr-F
         type: chrf
         value: 0.66434
  - task:
      name: Translation hbs-ita
      type: translation
      args: hbs-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hbs-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 53.5
       - name: chr-F
         type: chrf
         value: 0.72381
  - task:
      name: Translation hbs-spa
      type: translation
      args: hbs-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hbs-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 58.0
       - name: chr-F
         type: chrf
         value: 0.73105
  - task:
      name: Translation hrv-fra
      type: translation
      args: hrv-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hrv-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 44.3
       - name: chr-F
         type: chrf
         value: 0.62800
  - task:
      name: Translation hrv-spa
      type: translation
      args: hrv-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: hrv-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 57.5
       - name: chr-F
         type: chrf
         value: 0.71370
  - task:
      name: Translation mkd-spa
      type: translation
      args: mkd-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: mkd-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 62.1
       - name: chr-F
         type: chrf
         value: 0.75366
  - task:
      name: Translation srp_Latn-ita
      type: translation
      args: srp_Latn-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: srp_Latn-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 59.6
       - name: chr-F
         type: chrf
         value: 0.76045
---
# opus-mt-tc-big-zls-itc

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

Neural machine translation model for translating from South Slavic languages (zls) to Italic languages (itc).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-08-10
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): bos_Latn bul hbs hrv mkd slv srp_Cyrl srp_Latn
  - Target Language(s): fra ita por ron spa
  - Language Pair(s): bul-fra bul-ita bul-por bul-ron bul-spa hbs-fra hbs-ita hbs-spa hrv-fra hrv-ita hrv-por hrv-ron hrv-spa mkd-fra mkd-ita mkd-por mkd-ron mkd-spa slv-fra slv-ita slv-por slv-ron slv-spa srp_Cyrl-fra srp_Cyrl-ita srp_Cyrl-por srp_Cyrl-ron srp_Cyrl-spa srp_Latn-ita
  - Valid Target Language Labels: >>acf<< >>aoa<< >>arg<< >>ast<< >>cat<< >>cbk<< >>ccd<< >>cks<< >>cos<< >>cri<< >>crs<< >>dlm<< >>drc<< >>egl<< >>ext<< >>fab<< >>fax<< >>fra<< >>frc<< >>frm<< >>fro<< >>frp<< >>fur<< >>gcf<< >>gcr<< >>glg<< >>hat<< >>idb<< >>ist<< >>ita<< >>itk<< >>kea<< >>kmv<< >>lad<< >>lad_Latn<< >>lat<< >>lat_Latn<< >>lij<< >>lld<< >>lmo<< >>lou<< >>mcm<< >>mfe<< >>mol<< >>mwl<< >>mxi<< >>mzs<< >>nap<< >>nrf<< >>oci<< >>osc<< >>osp<< >>pap<< >>pcd<< >>pln<< >>pms<< >>pob<< >>por<< >>pov<< >>pre<< >>pro<< >>qbb<< >>qhr<< >>rcf<< >>rgn<< >>roh<< >>ron<< >>ruo<< >>rup<< >>ruq<< >>scf<< >>scn<< >>sdc<< >>sdn<< >>spa<< >>spq<< >>spx<< >>src<< >>srd<< >>sro<< >>tmg<< >>tvy<< >>vec<< >>vkp<< >>wln<< >>xfa<< >>xum<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-08-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-itc/opusTCv20210807_transformer-big_2022-08-10.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT zls-itc README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zls-itc/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>fra<<`

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
    ">>fra<< Dobar dan, kako si?",
    ">>spa<< Znam da je ovo čudno."
]

model_name = "pytorch-models/opus-mt-tc-big-zls-itc"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Bonjour, comment allez-vous ?
#     Sé que esto es raro.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zls-itc")
print(pipe(">>fra<< Dobar dan, kako si?"))

# expected output: Bonjour, comment allez-vous ?
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-08-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-itc/opusTCv20210807_transformer-big_2022-08-10.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-08-10.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-itc/opusTCv20210807_transformer-big_2022-08-10.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-08-10.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-itc/opusTCv20210807_transformer-big_2022-08-10.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| bul-fra | tatoeba-test-v2021-08-07 | 0.68971 | 52.9 | 446 | 3669 |
| bul-ita | tatoeba-test-v2021-08-07 | 0.66412 | 45.1 | 2500 | 16951 |
| bul-spa | tatoeba-test-v2021-08-07 | 0.66672 | 49.7 | 286 | 1783 |
| hbs-fra | tatoeba-test-v2021-08-07 | 0.66434 | 48.1 | 474 | 3370 |
| hbs-ita | tatoeba-test-v2021-08-07 | 0.72381 | 53.5 | 534 | 3208 |
| hbs-spa | tatoeba-test-v2021-08-07 | 0.73105 | 58.0 | 607 | 3766 |
| hrv-fra | tatoeba-test-v2021-08-07 | 0.62800 | 44.3 | 258 | 1943 |
| hrv-spa | tatoeba-test-v2021-08-07 | 0.71370 | 57.5 | 254 | 1702 |
| mkd-spa | tatoeba-test-v2021-08-07 | 0.75366 | 62.1 | 217 | 1121 |
| srp_Latn-ita | tatoeba-test-v2021-08-07 | 0.76045 | 59.6 | 212 | 1292 |
| bul-fra | flores101-devtest | 0.60640 | 34.4 | 1012 | 28343 |
| bul-ita | flores101-devtest | 0.54135 | 24.0 | 1012 | 27306 |
| bul-por | flores101-devtest | 0.59322 | 32.4 | 1012 | 26519 |
| bul-ron | flores101-devtest | 0.55558 | 27.1 | 1012 | 26799 |
| bul-spa | flores101-devtest | 0.50962 | 22.4 | 1012 | 29199 |
| hrv-fra | flores101-devtest | 0.59349 | 33.1 | 1012 | 28343 |
| hrv-ita | flores101-devtest | 0.52980 | 23.5 | 1012 | 27306 |
| hrv-por | flores101-devtest | 0.57402 | 30.2 | 1012 | 26519 |
| hrv-ron | flores101-devtest | 0.53650 | 25.9 | 1012 | 26799 |
| hrv-spa | flores101-devtest | 0.50161 | 21.5 | 1012 | 29199 |
| mkd-fra | flores101-devtest | 0.60801 | 35.2 | 1012 | 28343 |
| mkd-ita | flores101-devtest | 0.53543 | 23.9 | 1012 | 27306 |
| mkd-por | flores101-devtest | 0.59648 | 33.9 | 1012 | 26519 |
| mkd-ron | flores101-devtest | 0.54998 | 28.0 | 1012 | 26799 |
| mkd-spa | flores101-devtest | 0.51079 | 22.8 | 1012 | 29199 |
| slv-fra | flores101-devtest | 0.58233 | 31.5 | 1012 | 28343 |
| slv-ita | flores101-devtest | 0.52390 | 22.4 | 1012 | 27306 |
| slv-por | flores101-devtest | 0.56436 | 29.0 | 1012 | 26519 |
| slv-ron | flores101-devtest | 0.53116 | 25.0 | 1012 | 26799 |
| slv-spa | flores101-devtest | 0.49621 | 21.1 | 1012 | 29199 |
| srp_Cyrl-fra | flores101-devtest | 0.62110 | 36.0 | 1012 | 28343 |
| srp_Cyrl-ita | flores101-devtest | 0.54083 | 23.9 | 1012 | 27306 |
| srp_Cyrl-por | flores101-devtest | 0.61248 | 34.9 | 1012 | 26519 |
| srp_Cyrl-ron | flores101-devtest | 0.56235 | 28.8 | 1012 | 26799 |
| srp_Cyrl-spa | flores101-devtest | 0.51698 | 22.8 | 1012 | 29199 |

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
* port time: Fri Aug 12 23:59:29 EEST 2022
* port machine: LM0-400-22516.local

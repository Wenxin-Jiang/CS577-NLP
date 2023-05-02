---
language:
- ca
- da
- es
- fr
- gl
- is
- it
- nb
- pt
- ro
- sv

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-gmq-itc
  results:
  - task:
      name: Translation dan-cat
      type: translation
      args: dan-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 33.4
       - name: chr-F
         type: chrf
         value: 0.59224
  - task:
      name: Translation dan-fra
      type: translation
      args: dan-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 38.3
       - name: chr-F
         type: chrf
         value: 0.63387
  - task:
      name: Translation dan-glg
      type: translation
      args: dan-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 26.4
       - name: chr-F
         type: chrf
         value: 0.54446
  - task:
      name: Translation dan-ita
      type: translation
      args: dan-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 25.7
       - name: chr-F
         type: chrf
         value: 0.55237
  - task:
      name: Translation dan-por
      type: translation
      args: dan-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 36.9
       - name: chr-F
         type: chrf
         value: 0.62233
  - task:
      name: Translation dan-ron
      type: translation
      args: dan-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.8
       - name: chr-F
         type: chrf
         value: 0.58235
  - task:
      name: Translation dan-spa
      type: translation
      args: dan-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: dan spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.3
       - name: chr-F
         type: chrf
         value: 0.52453
  - task:
      name: Translation isl-cat
      type: translation
      args: isl-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: isl cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.7
       - name: chr-F
         type: chrf
         value: 0.48930
  - task:
      name: Translation isl-fra
      type: translation
      args: isl-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: isl fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 26.2
       - name: chr-F
         type: chrf
         value: 0.52704
  - task:
      name: Translation isl-glg
      type: translation
      args: isl-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: isl glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 18.0
       - name: chr-F
         type: chrf
         value: 0.45387
  - task:
      name: Translation isl-ita
      type: translation
      args: isl-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: isl ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 18.6
       - name: chr-F
         type: chrf
         value: 0.47303
  - task:
      name: Translation isl-por
      type: translation
      args: isl-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: isl por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.9
       - name: chr-F
         type: chrf
         value: 0.51381
  - task:
      name: Translation isl-ron
      type: translation
      args: isl-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: isl ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.6
       - name: chr-F
         type: chrf
         value: 0.48224
  - task:
      name: Translation isl-spa
      type: translation
      args: isl-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: isl spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 18.1
       - name: chr-F
         type: chrf
         value: 0.45786
  - task:
      name: Translation nob-cat
      type: translation
      args: nob-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.9
       - name: chr-F
         type: chrf
         value: 0.55984
  - task:
      name: Translation nob-fra
      type: translation
      args: nob-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 33.8
       - name: chr-F
         type: chrf
         value: 0.60102
  - task:
      name: Translation nob-glg
      type: translation
      args: nob-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.4
       - name: chr-F
         type: chrf
         value: 0.52145
  - task:
      name: Translation nob-ita
      type: translation
      args: nob-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.2
       - name: chr-F
         type: chrf
         value: 0.52619
  - task:
      name: Translation nob-por
      type: translation
      args: nob-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 32.2
       - name: chr-F
         type: chrf
         value: 0.58836
  - task:
      name: Translation nob-ron
      type: translation
      args: nob-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 27.6
       - name: chr-F
         type: chrf
         value: 0.54845
  - task:
      name: Translation nob-spa
      type: translation
      args: nob-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nob spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.8
       - name: chr-F
         type: chrf
         value: 0.50661
  - task:
      name: Translation swe-cat
      type: translation
      args: swe-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 32.4
       - name: chr-F
         type: chrf
         value: 0.58542
  - task:
      name: Translation swe-fra
      type: translation
      args: swe-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 39.3
       - name: chr-F
         type: chrf
         value: 0.63688
  - task:
      name: Translation swe-glg
      type: translation
      args: swe-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 26.0
       - name: chr-F
         type: chrf
         value: 0.53989
  - task:
      name: Translation swe-ita
      type: translation
      args: swe-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 25.9
       - name: chr-F
         type: chrf
         value: 0.55232
  - task:
      name: Translation swe-por
      type: translation
      args: swe-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 36.5
       - name: chr-F
         type: chrf
         value: 0.61882
  - task:
      name: Translation swe-ron
      type: translation
      args: swe-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.0
       - name: chr-F
         type: chrf
         value: 0.57419
  - task:
      name: Translation swe-spa
      type: translation
      args: swe-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: swe spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.8
       - name: chr-F
         type: chrf
         value: 0.52175
  - task:
      name: Translation dan-fra
      type: translation
      args: dan-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: dan-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 63.8
       - name: chr-F
         type: chrf
         value: 0.76671
  - task:
      name: Translation dan-ita
      type: translation
      args: dan-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: dan-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 56.2
       - name: chr-F
         type: chrf
         value: 0.74658
  - task:
      name: Translation dan-por
      type: translation
      args: dan-por
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: dan-por
    metrics:
       - name: BLEU
         type: bleu
         value: 57.8
       - name: chr-F
         type: chrf
         value: 0.74944
  - task:
      name: Translation dan-spa
      type: translation
      args: dan-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: dan-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 54.8
       - name: chr-F
         type: chrf
         value: 0.72328
  - task:
      name: Translation isl-ita
      type: translation
      args: isl-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: isl-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 51.0
       - name: chr-F
         type: chrf
         value: 0.69354
  - task:
      name: Translation isl-spa
      type: translation
      args: isl-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: isl-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 49.2
       - name: chr-F
         type: chrf
         value: 0.66008
  - task:
      name: Translation nob-fra
      type: translation
      args: nob-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nob-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 54.4
       - name: chr-F
         type: chrf
         value: 0.70854
  - task:
      name: Translation nob-spa
      type: translation
      args: nob-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nob-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 55.9
       - name: chr-F
         type: chrf
         value: 0.73672
  - task:
      name: Translation swe-fra
      type: translation
      args: swe-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: swe-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 59.2
       - name: chr-F
         type: chrf
         value: 0.73014
  - task:
      name: Translation swe-ita
      type: translation
      args: swe-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: swe-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 56.6
       - name: chr-F
         type: chrf
         value: 0.73211
  - task:
      name: Translation swe-por
      type: translation
      args: swe-por
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: swe-por
    metrics:
       - name: BLEU
         type: bleu
         value: 48.7
       - name: chr-F
         type: chrf
         value: 0.68146
  - task:
      name: Translation swe-spa
      type: translation
      args: swe-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: swe-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 55.3
       - name: chr-F
         type: chrf
         value: 0.71373
---
# opus-mt-tc-big-gmq-itc

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

Neural machine translation model for translating from North Germanic languages (gmq) to Italic languages (itc).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-08-09
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): dan isl nno nob nor swe
  - Target Language(s): cat fra glg ita lat por ron spa
  - Language Pair(s): dan-cat dan-fra dan-glg dan-ita dan-por dan-ron dan-spa isl-cat isl-fra isl-ita isl-por isl-ron isl-spa nob-cat nob-fra nob-glg nob-ita nob-por nob-ron nob-spa swe-cat swe-fra swe-glg swe-ita swe-por swe-ron swe-spa
  - Valid Target Language Labels: >>acf<< >>aoa<< >>arg<< >>ast<< >>cat<< >>cbk<< >>ccd<< >>cks<< >>cos<< >>cri<< >>crs<< >>dlm<< >>drc<< >>egl<< >>ext<< >>fab<< >>fax<< >>fra<< >>frc<< >>frm<< >>fro<< >>frp<< >>fur<< >>gcf<< >>gcr<< >>glg<< >>hat<< >>idb<< >>ist<< >>ita<< >>itk<< >>kea<< >>kmv<< >>lad<< >>lad_Latn<< >>lat<< >>lat_Latn<< >>lij<< >>lld<< >>lmo<< >>lou<< >>mcm<< >>mfe<< >>mol<< >>mwl<< >>mxi<< >>mzs<< >>nap<< >>nrf<< >>oci<< >>osc<< >>osp<< >>osp_Latn<< >>pap<< >>pcd<< >>pln<< >>pms<< >>pob<< >>por<< >>pov<< >>pre<< >>pro<< >>qbb<< >>qhr<< >>rcf<< >>rgn<< >>roh<< >>ron<< >>ruo<< >>rup<< >>ruq<< >>scf<< >>scn<< >>sdc<< >>sdn<< >>spa<< >>spq<< >>spx<< >>src<< >>srd<< >>sro<< >>tmg<< >>tvy<< >>vec<< >>vkp<< >>wln<< >>xfa<< >>xum<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-08-09.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-itc/opusTCv20210807_transformer-big_2022-08-09.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT gmq-itc README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmq-itc/README.md)
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
    ">>spa<< Jag är inte religiös.",
    ">>por<< Livet er for kort til å lære seg tysk."
]

model_name = "pytorch-models/opus-mt-tc-big-gmq-itc"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     No soy religioso.
#     A vida é muito curta para aprender alemão.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-gmq-itc")
print(pipe(">>spa<< Jag är inte religiös."))

# expected output: No soy religioso.
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-08-09.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-itc/opusTCv20210807_transformer-big_2022-08-09.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-08-09.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-itc/opusTCv20210807_transformer-big_2022-08-09.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-08-09.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-itc/opusTCv20210807_transformer-big_2022-08-09.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| dan-fra | tatoeba-test-v2021-08-07 | 0.76671 | 63.8 | 1731 | 11882 |
| dan-ita | tatoeba-test-v2021-08-07 | 0.74658 | 56.2 | 284 | 2226 |
| dan-por | tatoeba-test-v2021-08-07 | 0.74944 | 57.8 | 873 | 5360 |
| dan-spa | tatoeba-test-v2021-08-07 | 0.72328 | 54.8 | 5000 | 35528 |
| isl-ita | tatoeba-test-v2021-08-07 | 0.69354 | 51.0 | 236 | 1450 |
| isl-spa | tatoeba-test-v2021-08-07 | 0.66008 | 49.2 | 238 | 1229 |
| nob-fra | tatoeba-test-v2021-08-07 | 0.70854 | 54.4 | 323 | 2269 |
| nob-spa | tatoeba-test-v2021-08-07 | 0.73672 | 55.9 | 885 | 6866 |
| swe-fra | tatoeba-test-v2021-08-07 | 0.73014 | 59.2 | 1407 | 9580 |
| swe-ita | tatoeba-test-v2021-08-07 | 0.73211 | 56.6 | 715 | 4711 |
| swe-por | tatoeba-test-v2021-08-07 | 0.68146 | 48.7 | 320 | 2032 |
| swe-spa | tatoeba-test-v2021-08-07 | 0.71373 | 55.3 | 1351 | 8235 |
| dan-cat | flores101-devtest | 0.59224 | 33.4 | 1012 | 27304 |
| dan-fra | flores101-devtest | 0.63387 | 38.3 | 1012 | 28343 |
| dan-glg | flores101-devtest | 0.54446 | 26.4 | 1012 | 26582 |
| dan-ita | flores101-devtest | 0.55237 | 25.7 | 1012 | 27306 |
| dan-por | flores101-devtest | 0.62233 | 36.9 | 1012 | 26519 |
| dan-ron | flores101-devtest | 0.58235 | 31.8 | 1012 | 26799 |
| dan-spa | flores101-devtest | 0.52453 | 24.3 | 1012 | 29199 |
| isl-cat | flores101-devtest | 0.48930 | 22.7 | 1012 | 27304 |
| isl-fra | flores101-devtest | 0.52704 | 26.2 | 1012 | 28343 |
| isl-glg | flores101-devtest | 0.45387 | 18.0 | 1012 | 26582 |
| isl-ita | flores101-devtest | 0.47303 | 18.6 | 1012 | 27306 |
| isl-por | flores101-devtest | 0.51381 | 24.9 | 1012 | 26519 |
| isl-ron | flores101-devtest | 0.48224 | 21.6 | 1012 | 26799 |
| isl-spa | flores101-devtest | 0.45786 | 18.1 | 1012 | 29199 |
| nob-cat | flores101-devtest | 0.55984 | 28.9 | 1012 | 27304 |
| nob-fra | flores101-devtest | 0.60102 | 33.8 | 1012 | 28343 |
| nob-glg | flores101-devtest | 0.52145 | 23.4 | 1012 | 26582 |
| nob-ita | flores101-devtest | 0.52619 | 22.2 | 1012 | 27306 |
| nob-por | flores101-devtest | 0.58836 | 32.2 | 1012 | 26519 |
| nob-ron | flores101-devtest | 0.54845 | 27.6 | 1012 | 26799 |
| nob-spa | flores101-devtest | 0.50661 | 21.8 | 1012 | 29199 |
| swe-cat | flores101-devtest | 0.58542 | 32.4 | 1012 | 27304 |
| swe-fra | flores101-devtest | 0.63688 | 39.3 | 1012 | 28343 |
| swe-glg | flores101-devtest | 0.53989 | 26.0 | 1012 | 26582 |
| swe-ita | flores101-devtest | 0.55232 | 25.9 | 1012 | 27306 |
| swe-por | flores101-devtest | 0.61882 | 36.5 | 1012 | 26519 |
| swe-ron | flores101-devtest | 0.57419 | 31.0 | 1012 | 26799 |
| swe-spa | flores101-devtest | 0.52175 | 23.8 | 1012 | 29199 |

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
* port time: Sat Aug 13 00:00:00 EEST 2022
* port machine: LM0-400-22516.local

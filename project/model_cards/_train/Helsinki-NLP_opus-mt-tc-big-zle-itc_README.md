---
language:
- be
- ca
- es
- fr
- gl
- it
- pt
- ro
- ru
- uk

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-zle-itc
  results:
  - task:
      name: Translation bel-cat
      type: translation
      args: bel-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bel cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 16.8
       - name: chr-F
         type: chrf
         value: 0.48374
  - task:
      name: Translation bel-fra
      type: translation
      args: bel-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bel fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 19.4
       - name: chr-F
         type: chrf
         value: 0.51278
  - task:
      name: Translation bel-glg
      type: translation
      args: bel-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bel glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 15.3
       - name: chr-F
         type: chrf
         value: 0.45665
  - task:
      name: Translation bel-ita
      type: translation
      args: bel-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bel ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 14.6
       - name: chr-F
         type: chrf
         value: 0.47204
  - task:
      name: Translation bel-por
      type: translation
      args: bel-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bel por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 17.3
       - name: chr-F
         type: chrf
         value: 0.49561
  - task:
      name: Translation bel-ron
      type: translation
      args: bel-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bel ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 14.9
       - name: chr-F
         type: chrf
         value: 0.46315
  - task:
      name: Translation bel-spa
      type: translation
      args: bel-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: bel spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 15.3
       - name: chr-F
         type: chrf
         value: 0.46011
  - task:
      name: Translation rus-ast
      type: translation
      args: rus-ast
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus ast devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 13.6
       - name: chr-F
         type: chrf
         value: 0.45411
  - task:
      name: Translation rus-cat
      type: translation
      args: rus-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.3
       - name: chr-F
         type: chrf
         value: 0.55262
  - task:
      name: Translation rus-fra
      type: translation
      args: rus-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 32.9
       - name: chr-F
         type: chrf
         value: 0.59498
  - task:
      name: Translation rus-glg
      type: translation
      args: rus-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.5
       - name: chr-F
         type: chrf
         value: 0.51668
  - task:
      name: Translation rus-ita
      type: translation
      args: rus-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.7
       - name: chr-F
         type: chrf
         value: 0.52402
  - task:
      name: Translation rus-oci
      type: translation
      args: rus-oci
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus oci devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 12.9
       - name: chr-F
         type: chrf
         value: 0.42301
  - task:
      name: Translation rus-por
      type: translation
      args: rus-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.4
       - name: chr-F
         type: chrf
         value: 0.58045
  - task:
      name: Translation rus-ron
      type: translation
      args: rus-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.7
       - name: chr-F
         type: chrf
         value: 0.52560
  - task:
      name: Translation rus-spa
      type: translation
      args: rus-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: rus spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.8
       - name: chr-F
         type: chrf
         value: 0.50622
  - task:
      name: Translation ukr-ast
      type: translation
      args: ukr-ast
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr ast devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 14.1
       - name: chr-F
         type: chrf
         value: 0.45629
  - task:
      name: Translation ukr-cat
      type: translation
      args: ukr-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 29.5
       - name: chr-F
         type: chrf
         value: 0.56383
  - task:
      name: Translation ukr-fra
      type: translation
      args: ukr-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 34.5
       - name: chr-F
         type: chrf
         value: 0.60596
  - task:
      name: Translation ukr-glg
      type: translation
      args: ukr-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.2
       - name: chr-F
         type: chrf
         value: 0.52217
  - task:
      name: Translation ukr-ita
      type: translation
      args: ukr-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.0
       - name: chr-F
         type: chrf
         value: 0.52610
  - task:
      name: Translation ukr-oci
      type: translation
      args: ukr-oci
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr oci devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 13.7
       - name: chr-F
         type: chrf
         value: 0.42937
  - task:
      name: Translation ukr-por
      type: translation
      args: ukr-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 32.5
       - name: chr-F
         type: chrf
         value: 0.59036
  - task:
      name: Translation ukr-ron
      type: translation
      args: ukr-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 26.0
       - name: chr-F
         type: chrf
         value: 0.53883
  - task:
      name: Translation ukr-spa
      type: translation
      args: ukr-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ukr spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.5
       - name: chr-F
         type: chrf
         value: 0.51018
  - task:
      name: Translation bel-fra
      type: translation
      args: bel-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bel-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 49.1
       - name: chr-F
         type: chrf
         value: 0.66784
  - task:
      name: Translation bel-ita
      type: translation
      args: bel-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bel-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 47.6
       - name: chr-F
         type: chrf
         value: 0.64145
  - task:
      name: Translation bel-spa
      type: translation
      args: bel-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: bel-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 46.9
       - name: chr-F
         type: chrf
         value: 0.65485
  - task:
      name: Translation rus-fra
      type: translation
      args: rus-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 52.1
       - name: chr-F
         type: chrf
         value: 0.68174
  - task:
      name: Translation rus-ita
      type: translation
      args: rus-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 42.7
       - name: chr-F
         type: chrf
         value: 0.63277
  - task:
      name: Translation rus-por
      type: translation
      args: rus-por
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-por
    metrics:
       - name: BLEU
         type: bleu
         value: 42.6
       - name: chr-F
         type: chrf
         value: 0.63606
  - task:
      name: Translation rus-ron
      type: translation
      args: rus-ron
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-ron
    metrics:
       - name: BLEU
         type: bleu
         value: 37.5
       - name: chr-F
         type: chrf
         value: 0.60796
  - task:
      name: Translation rus-spa
      type: translation
      args: rus-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: rus-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 51.3
       - name: chr-F
         type: chrf
         value: 0.69108
  - task:
      name: Translation ukr-cat
      type: translation
      args: ukr-cat
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-cat
    metrics:
       - name: BLEU
         type: bleu
         value: 52.9
       - name: chr-F
         type: chrf
         value: 0.69275
  - task:
      name: Translation ukr-fra
      type: translation
      args: ukr-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 51.3
       - name: chr-F
         type: chrf
         value: 0.67392
  - task:
      name: Translation ukr-ita
      type: translation
      args: ukr-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 49.6
       - name: chr-F
         type: chrf
         value: 0.69157
  - task:
      name: Translation ukr-por
      type: translation
      args: ukr-por
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-por
    metrics:
       - name: BLEU
         type: bleu
         value: 45.0
       - name: chr-F
         type: chrf
         value: 0.64722
  - task:
      name: Translation ukr-spa
      type: translation
      args: ukr-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ukr-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 50.7
       - name: chr-F
         type: chrf
         value: 0.68409
  - task:
      name: Translation rus-fra
      type: translation
      args: rus-fra
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: rus-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 25.0
       - name: chr-F
         type: chrf
         value: 0.53481
  - task:
      name: Translation rus-spa
      type: translation
      args: rus-spa
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: rus-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 28.7
       - name: chr-F
         type: chrf
         value: 0.54814
  - task:
      name: Translation rus-fra
      type: translation
      args: rus-fra
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: rus-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 29.0
       - name: chr-F
         type: chrf
         value: 0.55745
  - task:
      name: Translation rus-spa
      type: translation
      args: rus-spa
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: rus-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 31.5
       - name: chr-F
         type: chrf
         value: 0.56582
---
# opus-mt-tc-big-zle-itc

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

Neural machine translation model for translating from East Slavic languages (zle) to Italic languages (itc).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-08-03
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): bel rue rus ukr
  - Target Language(s): cat fra glg ita lad_Latn por ron spa
  - Language Pair(s): bel-fra bel-ita bel-spa rus-cat rus-fra rus-glg rus-ita rus-por rus-ron rus-spa ukr-cat ukr-fra ukr-glg ukr-ita ukr-por ukr-ron ukr-spa
  - Valid Target Language Labels: >>acf<< >>aoa<< >>arg<< >>ast<< >>cat<< >>cbk<< >>ccd<< >>cks<< >>cos<< >>cri<< >>crs<< >>dlm<< >>drc<< >>egl<< >>ext<< >>fab<< >>fax<< >>fra<< >>frc<< >>frm<< >>fro<< >>frp<< >>fur<< >>gcf<< >>gcf_Latn<< >>gcr<< >>glg<< >>hat<< >>idb<< >>ist<< >>ita<< >>itk<< >>kea<< >>kmv<< >>lad<< >>lad_Latn<< >>lat<< >>lat_Latn<< >>lij<< >>lld<< >>lmo<< >>lou<< >>mcm<< >>mfe<< >>mol<< >>mwl<< >>mxi<< >>mzs<< >>nap<< >>nrf<< >>oci<< >>osc<< >>osp<< >>osp_Latn<< >>pap<< >>pcd<< >>pln<< >>pms<< >>pob<< >>por<< >>pov<< >>pre<< >>pro<< >>qbb<< >>qhr<< >>rcf<< >>rgn<< >>roh<< >>ron<< >>ruo<< >>rup<< >>ruq<< >>scf<< >>scn<< >>sdc<< >>sdn<< >>spa<< >>spq<< >>spx<< >>src<< >>srd<< >>sro<< >>tmg<< >>tvy<< >>vec<< >>vkp<< >>wln<< >>xfa<< >>xum<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-08-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-itc/opusTCv20210807_transformer-big_2022-08-03.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT zle-itc README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-itc/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>cat<<`

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
    ">>fra<< Вони не мої справжні батьки.",
    ">>por<< Мне нужно в школу."
]

model_name = "pytorch-models/opus-mt-tc-big-zle-itc"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Ce ne sont pas mes vrais parents.
#     Tenho de ir para a escola.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-zle-itc")
print(pipe(">>fra<< Вони не мої справжні батьки."))

# expected output: Ce ne sont pas mes vrais parents.
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-08-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-itc/opusTCv20210807_transformer-big_2022-08-03.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-08-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-itc/opusTCv20210807_transformer-big_2022-08-03.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-08-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-itc/opusTCv20210807_transformer-big_2022-08-03.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| bel-fra | tatoeba-test-v2021-08-07 | 0.66784 | 49.1 | 283 | 2005 |
| bel-ita | tatoeba-test-v2021-08-07 | 0.64145 | 47.6 | 264 | 1681 |
| bel-spa | tatoeba-test-v2021-08-07 | 0.65485 | 46.9 | 205 | 1412 |
| rus-fra | tatoeba-test-v2021-08-07 | 0.68174 | 52.1 | 11490 | 80579 |
| rus-ita | tatoeba-test-v2021-08-07 | 0.63277 | 42.7 | 10045 | 71584 |
| rus-por | tatoeba-test-v2021-08-07 | 0.63606 | 42.6 | 10000 | 74713 |
| rus-ron | tatoeba-test-v2021-08-07 | 0.60796 | 37.5 | 782 | 4772 |
| rus-spa | tatoeba-test-v2021-08-07 | 0.69108 | 51.3 | 10506 | 75246 |
| ukr-cat | tatoeba-test-v2021-08-07 | 0.69275 | 52.9 | 456 | 2675 |
| ukr-fra | tatoeba-test-v2021-08-07 | 0.67392 | 51.3 | 10035 | 63227 |
| ukr-ita | tatoeba-test-v2021-08-07 | 0.69157 | 49.6 | 5000 | 27846 |
| ukr-por | tatoeba-test-v2021-08-07 | 0.64722 | 45.0 | 3372 | 21315 |
| ukr-spa | tatoeba-test-v2021-08-07 | 0.68409 | 50.7 | 10115 | 59284 |
| bel-ast | flores101-devtest | 0.40942 | 8.7 | 1012 | 24572 |
| bel-cat | flores101-devtest | 0.48374 | 16.8 | 1012 | 27304 |
| bel-fra | flores101-devtest | 0.51278 | 19.4 | 1012 | 28343 |
| bel-glg | flores101-devtest | 0.45665 | 15.3 | 1012 | 26582 |
| bel-ita | flores101-devtest | 0.47204 | 14.6 | 1012 | 27306 |
| bel-por | flores101-devtest | 0.49561 | 17.3 | 1012 | 26519 |
| bel-ron | flores101-devtest | 0.46315 | 14.9 | 1012 | 26799 |
| bel-spa | flores101-devtest | 0.46011 | 15.3 | 1012 | 29199 |
| rus-ast | flores101-devtest | 0.45411 | 13.6 | 1012 | 24572 |
| rus-cat | flores101-devtest | 0.55262 | 28.3 | 1012 | 27304 |
| rus-fra | flores101-devtest | 0.59498 | 32.9 | 1012 | 28343 |
| rus-glg | flores101-devtest | 0.51668 | 23.5 | 1012 | 26582 |
| rus-ita | flores101-devtest | 0.52402 | 22.7 | 1012 | 27306 |
| rus-oci | flores101-devtest | 0.42301 | 12.9 | 1012 | 27305 |
| rus-por | flores101-devtest | 0.58045 | 31.4 | 1012 | 26519 |
| rus-ron | flores101-devtest | 0.52560 | 24.7 | 1012 | 26799 |
| rus-spa | flores101-devtest | 0.50622 | 21.8 | 1012 | 29199 |
| ukr-ast | flores101-devtest | 0.45629 | 14.1 | 1012 | 24572 |
| ukr-cat | flores101-devtest | 0.56383 | 29.5 | 1012 | 27304 |
| ukr-fra | flores101-devtest | 0.60596 | 34.5 | 1012 | 28343 |
| ukr-glg | flores101-devtest | 0.52217 | 24.2 | 1012 | 26582 |
| ukr-ita | flores101-devtest | 0.52610 | 23.0 | 1012 | 27306 |
| ukr-oci | flores101-devtest | 0.42937 | 13.7 | 1012 | 27305 |
| ukr-por | flores101-devtest | 0.59036 | 32.5 | 1012 | 26519 |
| ukr-ron | flores101-devtest | 0.53883 | 26.0 | 1012 | 26799 |
| ukr-spa | flores101-devtest | 0.51018 | 22.5 | 1012 | 29199 |
| rus-fra | newstest2012 | 0.53481 | 25.0 | 3003 | 78011 |
| rus-spa | newstest2012 | 0.54814 | 28.7 | 3003 | 79006 |
| rus-fra | newstest2013 | 0.55745 | 29.0 | 3000 | 70037 |
| rus-spa | newstest2013 | 0.56582 | 31.5 | 3000 | 70528 |

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
* port time: Sat Aug 13 00:01:33 EEST 2022
* port machine: LM0-400-22516.local

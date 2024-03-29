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
- name: opus-mt-tc-big-ar-itc
  results:
  - task:
      name: Translation ara-cat
      type: translation
      args: ara-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ara cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.7
       - name: chr-F
         type: chrf
         value: 0.55670
  - task:
      name: Translation ara-fra
      type: translation
      args: ara-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ara fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 33.4
       - name: chr-F
         type: chrf
         value: 0.59715
  - task:
      name: Translation ara-glg
      type: translation
      args: ara-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ara glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.5
       - name: chr-F
         type: chrf
         value: 0.51898
  - task:
      name: Translation ara-ita
      type: translation
      args: ara-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ara ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.3
       - name: chr-F
         type: chrf
         value: 0.52523
  - task:
      name: Translation ara-por
      type: translation
      args: ara-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ara por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.6
       - name: chr-F
         type: chrf
         value: 0.58260
  - task:
      name: Translation ara-ron
      type: translation
      args: ara-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ara ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.4
       - name: chr-F
         type: chrf
         value: 0.51425
  - task:
      name: Translation ara-spa
      type: translation
      args: ara-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ara spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.8
       - name: chr-F
         type: chrf
         value: 0.50203
  - task:
      name: Translation ara-fra
      type: translation
      args: ara-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ara-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 41.5
       - name: chr-F
         type: chrf
         value: 0.57876
  - task:
      name: Translation ara-ita
      type: translation
      args: ara-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ara-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 46.5
       - name: chr-F
         type: chrf
         value: 0.66888
  - task:
      name: Translation ara-spa
      type: translation
      args: ara-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ara-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 47.2
       - name: chr-F
         type: chrf
         value: 0.64686
---
# opus-mt-tc-big-ar-itc

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

Neural machine translation model for translating from Arabic (ar) to Italic languages (itc).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-07-28
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): ara
  - Target Language(s): cat fra glg ita por ron spa
  - Language Pair(s): ara-cat ara-fra ara-glg ara-ita ara-por ara-ron ara-spa
  - Valid Target Language Labels: >>acf<< >>aoa<< >>arg<< >>ast<< >>cat<< >>cbk<< >>ccd<< >>cks<< >>cos<< >>cri<< >>crs<< >>dlm<< >>drc<< >>egl<< >>ext<< >>fab<< >>fax<< >>fra<< >>frc<< >>frm<< >>fro<< >>frp<< >>fur<< >>gcf<< >>gcr<< >>glg<< >>hat<< >>idb<< >>ist<< >>ita<< >>itk<< >>kea<< >>kmv<< >>lad<< >>lad_Latn<< >>lat<< >>lat_Latn<< >>lij<< >>lld<< >>lmo<< >>lou<< >>mcm<< >>mfe<< >>mol<< >>mwl<< >>mxi<< >>mzs<< >>nap<< >>nrf<< >>oci<< >>osc<< >>osp<< >>osp_Latn<< >>pap<< >>pcd<< >>pln<< >>pms<< >>pob<< >>por<< >>pov<< >>pre<< >>pro<< >>qbb<< >>qhr<< >>rcf<< >>rgn<< >>roh<< >>ron<< >>ruo<< >>rup<< >>ruq<< >>scf<< >>scn<< >>sdc<< >>sdn<< >>spa<< >>spq<< >>spx<< >>src<< >>srd<< >>sro<< >>tmg<< >>tvy<< >>vec<< >>vkp<< >>wln<< >>xfa<< >>xum<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-07-28.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-itc/opusTCv20210807_transformer-big_2022-07-28.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT ara-itc README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-itc/README.md)
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
    ">>lat_Latn<< إيش إسمك؟",
    ">>por<< اليونان جميلة."
]

model_name = "pytorch-models/opus-mt-tc-big-ar-itc"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Iulia: Tu nombre es?
#     A Grécia é linda.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-ar-itc")
print(pipe(">>lat_Latn<< إيش إسمك؟"))

# expected output: Iulia: Tu nombre es?
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-07-28.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-itc/opusTCv20210807_transformer-big_2022-07-28.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-07-28.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-itc/opusTCv20210807_transformer-big_2022-07-28.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-07-28.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-itc/opusTCv20210807_transformer-big_2022-07-28.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| ara-fra | tatoeba-test-v2021-08-07 | 0.57876 | 41.5 | 1569 | 11066 |
| ara-ita | tatoeba-test-v2021-08-07 | 0.66888 | 46.5 | 235 | 1495 |
| ara-spa | tatoeba-test-v2021-08-07 | 0.64686 | 47.2 | 1511 | 9708 |
| ara-cat | flores101-devtest | 0.55670 | 28.7 | 1012 | 27304 |
| ara-fra | flores101-devtest | 0.59715 | 33.4 | 1012 | 28343 |
| ara-glg | flores101-devtest | 0.51898 | 23.5 | 1012 | 26582 |
| ara-ita | flores101-devtest | 0.52523 | 22.3 | 1012 | 27306 |
| ara-por | flores101-devtest | 0.58260 | 31.6 | 1012 | 26519 |
| ara-ron | flores101-devtest | 0.51425 | 22.4 | 1012 | 26799 |
| ara-spa | flores101-devtest | 0.50203 | 21.8 | 1012 | 29199 |

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
* port time: Sat Aug 13 00:04:20 EEST 2022
* port machine: LM0-400-22516.local

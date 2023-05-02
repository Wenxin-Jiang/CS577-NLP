---
language:
- fa
- fr
- pt
- ro

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-fa-itc
  results:
  - task:
      name: Translation fas-fra
      type: translation
      args: fas-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fas fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.9
       - name: chr-F
         type: chrf
         value: 0.55883
  - task:
      name: Translation fas-ita
      type: translation
      args: fas-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fas ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 19.7
       - name: chr-F
         type: chrf
         value: 0.49512
  - task:
      name: Translation fas-por
      type: translation
      args: fas-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fas por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 27.6
       - name: chr-F
         type: chrf
         value: 0.54829
  - task:
      name: Translation fas-ron
      type: translation
      args: fas-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fas ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 19.7
       - name: chr-F
         type: chrf
         value: 0.48821
  - task:
      name: Translation fas-spa
      type: translation
      args: fas-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fas spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 19.4
       - name: chr-F
         type: chrf
         value: 0.47722
  - task:
      name: Translation fas-fra
      type: translation
      args: fas-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fas-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 37.5
       - name: chr-F
         type: chrf
         value: 0.57949
---
# opus-mt-tc-big-fa-itc

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

Neural machine translation model for translating from Persian (fa) to Italic languages (itc).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-07-23
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): fas
  - Target Language(s): fra ita por ron spa
  - Language Pair(s): fas-fra fas-por fas-ron
  - Valid Target Language Labels: >>acf<< >>aoa<< >>arg<< >>ast<< >>cat<< >>cbk<< >>ccd<< >>cks<< >>cos<< >>cri<< >>crs<< >>dlm<< >>drc<< >>egl<< >>ext<< >>fab<< >>fax<< >>fra<< >>frc<< >>frm<< >>fro<< >>frp<< >>fur<< >>gcf<< >>gcr<< >>glg<< >>hat<< >>idb<< >>ist<< >>ita<< >>itk<< >>kea<< >>kmv<< >>lad<< >>lad_Latn<< >>lat<< >>lat_Latn<< >>lij<< >>lld<< >>lmo<< >>lou<< >>mcm<< >>mfe<< >>mol<< >>mwl<< >>mxi<< >>mzs<< >>nap<< >>nrf<< >>oci<< >>osc<< >>osp<< >>pap<< >>pcd<< >>pln<< >>pms<< >>pob<< >>por<< >>pov<< >>pre<< >>pro<< >>qbb<< >>qhr<< >>rcf<< >>rgn<< >>roh<< >>ron<< >>ruo<< >>rup<< >>ruq<< >>scf<< >>scn<< >>sdc<< >>sdn<< >>spa<< >>spq<< >>spx<< >>src<< >>srd<< >>sro<< >>tmg<< >>tvy<< >>vec<< >>vkp<< >>wln<< >>xfa<< >>xum<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-07-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fas-itc/opusTCv20210807_transformer-big_2022-07-23.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT fas-itc README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fas-itc/README.md)
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
    ">>lad<< اسلام زیباست.",
    ">>spa<< ورود به کتابخانه رایگان است."
]

model_name = "pytorch-models/opus-mt-tc-big-fa-itc"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     O Islam é lindo.
#     La entrada a la biblioteca es gratuita.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-fa-itc")
print(pipe(">>lad<< اسلام زیباست."))

# expected output: O Islam é lindo.
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-07-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fas-itc/opusTCv20210807_transformer-big_2022-07-23.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-07-23.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fas-itc/opusTCv20210807_transformer-big_2022-07-23.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-07-23.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fas-itc/opusTCv20210807_transformer-big_2022-07-23.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| fas-fra | tatoeba-test-v2021-08-07 | 0.57949 | 37.5 | 376 | 3377 |
| fas-fra | flores101-devtest | 0.55883 | 28.9 | 1012 | 28343 |
| fas-ita | flores101-devtest | 0.49512 | 19.7 | 1012 | 27306 |
| fas-por | flores101-devtest | 0.54829 | 27.6 | 1012 | 26519 |
| fas-ron | flores101-devtest | 0.48821 | 19.7 | 1012 | 26799 |
| fas-spa | flores101-devtest | 0.47722 | 19.4 | 1012 | 29199 |

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
* port time: Sat Aug 13 00:08:53 EEST 2022
* port machine: LM0-400-22516.local

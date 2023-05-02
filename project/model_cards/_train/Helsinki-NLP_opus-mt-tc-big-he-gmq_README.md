---
language:
- da
- he
- nb
- sv

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-he-gmq
  results:
  - task:
      name: Translation heb-dan
      type: translation
      args: heb-dan
    dataset:
      name: flores101-devtest
      type: flores_101
      args: heb dan devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.4
       - name: chr-F
         type: chrf
         value: 0.58023
  - task:
      name: Translation heb-isl
      type: translation
      args: heb-isl
    dataset:
      name: flores101-devtest
      type: flores_101
      args: heb isl devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 14.0
       - name: chr-F
         type: chrf
         value: 0.41998
  - task:
      name: Translation heb-nob
      type: translation
      args: heb-nob
    dataset:
      name: flores101-devtest
      type: flores_101
      args: heb nob devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.7
       - name: chr-F
         type: chrf
         value: 0.53086
  - task:
      name: Translation heb-swe
      type: translation
      args: heb-swe
    dataset:
      name: flores101-devtest
      type: flores_101
      args: heb swe devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 29.6
       - name: chr-F
         type: chrf
         value: 0.56881
---
# opus-mt-tc-big-he-gmq

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

Neural machine translation model for translating from Hebrew (he) to North Germanic languages (gmq).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-07-23
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): heb
  - Target Language(s): dan nob nor swe
  - Language Pair(s): heb-dan heb-nob heb-swe
  - Valid Target Language Labels: >>dan<< >>fao<< >>isl<< >>jut<< >>nno<< >>nob<< >>non<< >>nrn<< >>ovd<< >>qer<< >>rmg<< >>swe<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-07-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-gmq/opusTCv20210807_transformer-big_2022-07-23.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT heb-gmq README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-gmq/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>dan<<`

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
    ">>dan<< כל שלושת הילדים של אליעזר לודוויג זמנהוף נרצחו בשואה.",
    ">>swe<< הסתבר שטום היה מרגל."
]

model_name = "pytorch-models/opus-mt-tc-big-he-gmq"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Alle tre børn af Eliezer Ludwig Zamenhof blev dræbt i Holocaust.
#     Det visade sig att Tom var en spion.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-he-gmq")
print(pipe(">>dan<< כל שלושת הילדים של אליעזר לודוויג זמנהוף נרצחו בשואה."))

# expected output: Alle tre børn af Eliezer Ludwig Zamenhof blev dræbt i Holocaust.
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-07-23.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-gmq/opusTCv20210807_transformer-big_2022-07-23.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-07-23.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-gmq/opusTCv20210807_transformer-big_2022-07-23.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-07-23.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-gmq/opusTCv20210807_transformer-big_2022-07-23.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| heb-dan | flores101-devtest | 0.58023 | 31.4 | 1012 | 24638 |
| heb-isl | flores101-devtest | 0.41998 | 14.0 | 1012 | 22834 |
| heb-nob | flores101-devtest | 0.53086 | 23.7 | 1012 | 23873 |
| heb-swe | flores101-devtest | 0.56881 | 29.6 | 1012 | 23121 |

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
* port time: Sat Aug 13 00:07:45 EEST 2022
* port machine: LM0-400-22516.local

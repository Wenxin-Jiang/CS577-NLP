---
language:
- de
- es

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-de-es
  results:
  - task:
      name: Translation deu-spa
      type: translation
      args: deu-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: deu spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.9
       - name: chr-F
         type: chrf
         value: 0.53208
  - task:
      name: Translation deu-spa
      type: translation
      args: deu-spa
    dataset:
      name: news-test2008
      type: news-test2008
      args: deu-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 26.6
       - name: chr-F
         type: chrf
         value: 0.54400
  - task:
      name: Translation deu-spa
      type: translation
      args: deu-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: deu-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 50.8
       - name: chr-F
         type: chrf
         value: 0.69105
  - task:
      name: Translation deu-spa
      type: translation
      args: deu-spa
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: deu-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 25.9
       - name: chr-F
         type: chrf
         value: 0.53934
  - task:
      name: Translation deu-spa
      type: translation
      args: deu-spa
    dataset:
      name: newstest2010
      type: wmt-2010-news
      args: deu-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 33.8
       - name: chr-F
         type: chrf
         value: 0.60102
  - task:
      name: Translation deu-spa
      type: translation
      args: deu-spa
    dataset:
      name: newstest2011
      type: wmt-2011-news
      args: deu-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 31.3
       - name: chr-F
         type: chrf
         value: 0.57133
  - task:
      name: Translation deu-spa
      type: translation
      args: deu-spa
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: deu-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 32.6
       - name: chr-F
         type: chrf
         value: 0.58119
  - task:
      name: Translation deu-spa
      type: translation
      args: deu-spa
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: deu-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 32.4
       - name: chr-F
         type: chrf
         value: 0.57559
---
# opus-mt-tc-big-de-es

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

Neural machine translation model for translating from German (de) to Spanish (es).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-07-26
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): deu
  - Target Language(s): spa
  - Language Pair(s): deu-spa
  - Valid Target Language Labels: 
- **Original Model**: [opusTCv20210807_transformer-big_2022-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-spa/opusTCv20210807_transformer-big_2022-07-26.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT deu-spa README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-spa/README.md)
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
    "Ich verstehe nicht, worüber ihr redet.",
    "Die Vögel singen in den Bäumen."
]

model_name = "pytorch-models/opus-mt-tc-big-de-es"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     No entiendo de qué están hablando.
#     Los pájaros cantan en los árboles.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-de-es")
print(pipe("Ich verstehe nicht, worüber ihr redet."))

# expected output: No entiendo de qué están hablando.
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-spa/opusTCv20210807_transformer-big_2022-07-26.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-spa/opusTCv20210807_transformer-big_2022-07-26.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-spa/opusTCv20210807_transformer-big_2022-07-26.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| deu-spa | tatoeba-test-v2021-08-07 | 0.69105 | 50.8 | 10521 | 82570 |
| deu-spa | flores101-devtest | 0.53208 | 24.9 | 1012 | 29199 |
| deu-spa | newssyscomb2009 | 0.55547 | 28.3 | 502 | 12503 |
| deu-spa | news-test2008 | 0.54400 | 26.6 | 2051 | 52586 |
| deu-spa | newstest2009 | 0.53934 | 25.9 | 2525 | 68111 |
| deu-spa | newstest2010 | 0.60102 | 33.8 | 2489 | 65480 |
| deu-spa | newstest2011 | 0.57133 | 31.3 | 3003 | 79476 |
| deu-spa | newstest2012 | 0.58119 | 32.6 | 3003 | 79006 |
| deu-spa | newstest2013 | 0.57559 | 32.4 | 3000 | 70528 |

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
* port time: Sat Aug 13 00:06:19 EEST 2022
* port machine: LM0-400-22516.local

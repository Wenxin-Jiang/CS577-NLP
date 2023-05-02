---
language:
- ar
- en
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-en-ar
  results:
  - task:
      name: Translation eng-ara
      type: translation
      args: eng-ara
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng ara devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 29.4
  - task:
      name: Translation eng-ara
      type: translation
      args: eng-ara
    dataset:
      name: tatoeba-test-v2020-07-28
      type: tatoeba_mt
      args: eng-ara
    metrics:
    - name: BLEU
      type: bleu
      value: 20.0
  - task:
      name: Translation eng-ara
      type: translation
      args: eng-ara
    dataset:
      name: tico19-test
      type: tico19-test
      args: eng-ara
    metrics:
    - name: BLEU
      type: bleu
      value: 30.0
---
# opus-mt-tc-big-en-ar

Neural machine translation model for translating from English (en) to Arabic (ar).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).

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

## Model info

* Release: 2022-02-25
* source language(s): eng
* target language(s): afb ara
* valid target language labels: >>afb<< >>ara<<
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-02-25.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ara/opusTCv20210807+bt_transformer-big_2022-02-25.zip)
* more information released models: [OPUS-MT eng-ara README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-ara/README.md)
* more information about the model: [MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>afb<<`

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>ara<< I can't help you because I'm busy.",
    ">>ara<< I have to write a letter. Do you have some paper?"
]

model_name = "pytorch-models/opus-mt-tc-big-en-ar"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     لا أستطيع مساعدتك لأنني مشغول.
#     يجب أن أكتب رسالة هل لديك بعض الأوراق؟
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-ar")
print(pipe(">>ara<< I can't help you because I'm busy."))

# expected output: لا أستطيع مساعدتك لأنني مشغول.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-02-25.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ara/opusTCv20210807+bt_transformer-big_2022-02-25.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-02-25.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ara/opusTCv20210807+bt_transformer-big_2022-02-25.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| eng-ara | tatoeba-test-v2021-08-07 | 0.48813 | 19.8 | 10305 | 61356 |
| eng-ara | flores101-devtest | 0.61154 | 29.4 | 1012 | 21357 |
| eng-ara | tico19-test | 0.60075 | 30.0 | 2100 | 51339 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 16:37:31 EEST 2022
* port machine: LM0-400-22516.local

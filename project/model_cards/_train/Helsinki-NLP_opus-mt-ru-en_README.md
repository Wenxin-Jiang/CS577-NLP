---
tags:
- translation
license: cc-by-4.0
---

### opus-mt-ru-en

## Table of Contents
- [Model Details](#model-details)
- [Uses](#uses)
- [Risks, Limitations and Biases](#risks-limitations-and-biases)
- [Training](#training)
- [Evaluation](#evaluation)
- [Citation Information](#citation-information)
- [How to Get Started With the Model](#how-to-get-started-with-the-model)

## Model Details
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Transformer-align
- **Language(s):**  
  - Source Language: Russian
  - Target Language: English
- **License:** CC-BY-4.0
- **Resources for more information:**
  - [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)



## Uses

#### Direct Use

This model can be used for translation and text-to-text generation.


## Risks, Limitations and Biases

**CONTENT WARNING: Readers should be aware this section contains content that is disturbing, offensive, and can propagate historical and current stereotypes.**

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).

Further details about the dataset for this model can be found in the OPUS readme: [ru-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/ru-en/README.md)

## Training
#### Training Data
##### Preprocessing
* Pre-processing: Normalization + SentencePiece
* Dataset: [opus](https://github.com/Helsinki-NLP/Opus-MT)
* Download original weights: [opus-2020-02-26.zip](https://object.pouta.csc.fi/OPUS-MT-models/ru-en/opus-2020-02-26.zip)

* Test set translations: [opus-2020-02-26.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/ru-en/opus-2020-02-26.test.txt)


## Evaluation

#### Results

* test set scores: [opus-2020-02-26.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/ru-en/opus-2020-02-26.eval.txt)

#### Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newstest2012.ru.en 	| 34.8 	| 0.603 |
| newstest2013.ru.en 	| 27.9 	| 0.545 |
| newstest2014-ruen.ru.en 	| 31.9 	| 0.591 |
| newstest2015-enru.ru.en 	| 30.4 	| 0.568 |
| newstest2016-enru.ru.en 	| 30.1 	| 0.565 |
| newstest2017-enru.ru.en 	| 33.4 	| 0.593 |
| newstest2018-enru.ru.en 	| 29.6 	| 0.565 |
| newstest2019-ruen.ru.en 	| 31.4 	| 0.576 |
| Tatoeba.ru.en 	| 61.1 	| 0.736 |

## Citation Information

```bibtex
@InProceedings{TiedemannThottingal:EAMT2020,
  author = {J{\"o}rg Tiedemann and Santhosh Thottingal},
  title = {{OPUS-MT} — {B}uilding open translation services for the {W}orld},
  booktitle = {Proceedings of the 22nd Annual Conferenec of the European Association for Machine Translation (EAMT)},
  year = {2020},
  address = {Lisbon, Portugal}
 }
```

## How to Get Started With the Model

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
```

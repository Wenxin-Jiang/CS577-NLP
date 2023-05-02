---
tags:
- translation
license: cc-by-4.0
---

### opus-mt-en-de


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
- **Model Type:** Translation
- **Language(s):**  
  - Source Language: English
  - Target Language: German 
- **License:** CC-BY-4.0
- **Resources for more information:**
  - [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  

## Uses

#### Direct Use

This model can be used for translation and text-to-text generation.


## Risks, Limitations and Biases



**CONTENT WARNING: Readers should be aware this section contains content that is disturbing, offensive, and can propagate historical and current stereotypes.**

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).

Further details about the dataset for this model can be found in the OPUS readme: [en-de](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-de/README.md)


#### Training Data
##### Preprocessing
* pre-processing: normalization + SentencePiece

* dataset: [opus](https://github.com/Helsinki-NLP/Opus-MT)
* download original weights: [opus-2020-02-26.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-de/opus-2020-02-26.zip)

* test set translations: [opus-2020-02-26.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-de/opus-2020-02-26.test.txt)

## Evaluation

#### Results

* test set scores: [opus-2020-02-26.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-de/opus-2020-02-26.eval.txt)


#### Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009.en.de 	| 23.5 	| 0.540 |
| news-test2008.en.de 	| 23.5 	| 0.529 |
| newstest2009.en.de 	| 22.3 	| 0.530 |
| newstest2010.en.de 	| 24.9 	| 0.544 |
| newstest2011.en.de 	| 22.5 	| 0.524 |
| newstest2012.en.de 	| 23.0 	| 0.525 |
| newstest2013.en.de 	| 26.9 	| 0.553 |
| newstest2015-ende.en.de 	| 31.1 	| 0.594 |
| newstest2016-ende.en.de 	| 37.0 	| 0.636 |
| newstest2017-ende.en.de 	| 29.9 	| 0.586 |
| newstest2018-ende.en.de 	| 45.2 	| 0.690 |
| newstest2019-ende.en.de 	| 40.9 	| 0.654 |
| Tatoeba.en.de 	| 47.3 	| 0.664 |



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

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")

model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-de")

```





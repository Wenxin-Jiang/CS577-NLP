---
language: "nl"
thumbnail: "https://github.com/iPieter/RobBERT/raw/master/res/robbert_2022_logo.png"
tags:
- Dutch
- Flemish
- RoBERTa
- RobBERT
license: mit
datasets:
- oscar
- dbrd
- lassy-ud
- europarl-mono
- conll2002
widget:
- text: "Hallo, ik ben RobBERT-2022, het nieuwe <mask> taalmodel van de KU Leuven."
---

<p align="center"> 
    <img src="https://github.com/iPieter/RobBERT/raw/master/res/robbert_2022_logo_with_name.png" alt="RobBERT-2022: Updating a Dutch Language Model to Account for Evolving Language Use" width="75%">
 </p>

# RobBERT-2022: Updating a Dutch Language Model to Account for Evolving Language Use.

RobBERT-2022 is the latest release of the [Dutch RobBERT model](https://pieter.ai/robbert/).
It further pretrained the original [pdelobelle/robbert-v2-dutch-base](https://huggingface.co/pdelobelle/robbert-v2-dutch-base) model on the 2022 version of the OSCAR version.
Thanks to this more recent dataset, this [DTAI-KULeuven/robbert-2022-dutch-base](https://huggingface.co/DTAI-KULeuven/robbert-2022-dutch-base) model shows increased performance on several tasks related to recent events, e.g. COVID-19-related tasks.
We also found that for some tasks that do not contain more recent information than 2019, the original [pdelobelle/robbert-v2-dutch-base](https://huggingface.co/pdelobelle/robbert-v2-dutch-base) RobBERT model can still outperform this newer one.

The original RobBERT model was released in January 2020. Dutch has evolved a lot since then, for example the COVID-19 pandemic introduced a wide range of new words that were suddenly used daily. Also, many other world facts that the original model considered true have also changed. To account for this and other changes in usage, we release a new Dutch BERT model trained on data from 2022: RobBERT 2022.
More in-depth information about RobBERT-2022 can be found in our [blog post](https://pieter.ai/robbert-2022/), [our paper](http://arxiv.org/abs/2211.08192), [the original RobBERT paper](https://arxiv.org/abs/2001.06286) and [the RobBERT Github repository](https://github.com/iPieter/RobBERT).



## How to use

RobBERT-2022 and RobBERT both use the [RoBERTa](https://arxiv.org/abs/1907.11692) architecture and pre-training but with a Dutch tokenizer and training data. RoBERTa is the robustly optimized English BERT model, making it even more powerful than the original BERT model. Given this same architecture, RobBERT can easily be finetuned and inferenced using [code to finetune RoBERTa](https://huggingface.co/transformers/model_doc/roberta.html) models and most code used for BERT models, e.g. as provided by [HuggingFace Transformers](https://huggingface.co/transformers/) library.

By default, RobBERT-2022 has the masked language model head used in training. This can be used as a zero-shot way to fill masks in sentences. It can be tested out for free on [RobBERT's Hosted infererence API of Huggingface](https://huggingface.co/pdelobelle/robbert-v2-dutch-base?text=De+hoofdstad+van+Belgi%C3%AB+is+%3Cmask%3E.). You can also create a new prediction head for your own task by using any of HuggingFace's [RoBERTa-runners](https://huggingface.co/transformers/v2.7.0/examples.html#language-model-training), [their fine-tuning notebooks](https://huggingface.co/transformers/v4.1.1/notebooks.html) by changing the model name to `DTAI-KULeuven/robbert-2022-dutch-base`.


```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("DTAI-KULeuven/robbert-2022-dutch-base")
model = AutoModelForSequenceClassification.from_pretrained("DTAI-KULeuven/robbert-2022-dutch-base")
```

You can then use most of [HuggingFace's BERT-based notebooks](https://huggingface.co/transformers/v4.1.1/notebooks.html) for finetuning RobBERT-2022 on your type of Dutch language dataset.


## Comparison of Available Dutch BERT models

There is a wide variety of Dutch BERT-based models available for fine-tuning on your tasks.
Here's a quick summary to find the one that suits your need:

- [pdelobelle/robbert-v2-dutch-base](https://huggingface.co/pdelobelle/robbert-v2-dutch-base): The RobBERT model has for years been the best performing BERT-like model for most language tasks. It is trained on a large Dutch webcrawled dataset (OSCAR) and uses the superior [RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta) architecture, which robustly optimized the original [BERT model](https://huggingface.co/docs/transformers/model_doc/bert).
- [DTAI-KULeuven/robbertje-1-gb-merged](https://huggingface.co/DTAI-KULeuven/robbertje-1-gb-mergedRobBERTje): The RobBERTje model is a distilled version of RobBERT and about half the size and four times faster to perform inference on. This can help deploy more scalable language models for your language task 
- [DTAI-KULeuven/robbert-2022-dutch-base](https://huggingface.co/DTAI-KULeuven/robbert-2022-dutch-base): The RobBERT-2022 is a further pre-trained RobBERT model on the OSCAR2022 dataset. It is helpful for tasks that rely on words and/or information about more recent events.

There's also the [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) "BERTje" model. This model uses the outdated basic BERT model, and is trained on a smaller corpus of clean Dutch texts.
Thanks to RobBERT's more recent architecture as well as its larger and more real-world-like training corpus, most researchers and practitioners seem to achieve higher performance on their language tasks with the RobBERT model. 



## Technical Details From The Paper


### Our Performance Evaluation Results

All experiments are described in more detail in our [paper](https://arxiv.org/abs/2001.06286), with the code in [our GitHub repository](https://github.com/iPieter/RobBERT).

### Sentiment analysis
Predicting whether a review is positive or negative using the [Dutch Book Reviews Dataset](https://github.com/benjaminvdb/110kDBRD).

|   Model           | Accuracy [%]             |
|-------------------|--------------------------|
| ULMFiT            | 93.8                     |
| BERTje            | 93.0                     |
| RobBERT v2        | 94.4                     |
| RobBERT 2022      | **95.1**                 |

### Die/Dat (coreference resolution)

We measured how well the models are able to do coreference resolution by predicting whether "die" or "dat" should be filled into a sentence.
For this, we used the [EuroParl corpus](https://www.statmt.org/europarl/).

#### Finetuning on whole dataset

|   Model           | Accuracy [%]             |  F1 [%]    |
|-------------------|--------------------------|--------------|
| [Baseline](https://arxiv.org/abs/2001.02943) (LSTM)   |                          | 75.03        |
| mBERT             | 98.285                   | 98.033       |
| BERTje            | 98.268                   | 98.014       |
| RobBERT v2        | **99.232**               | **99.121**   |
| RobBERT 2022      | 97.8                     |    |

#### Finetuning on 10K examples

We also measured the performance using only 10K training examples.
This experiment clearly illustrates that RobBERT outperforms other models when there is little data available.

|   Model           | Accuracy [%]             |  F1 [%]      |
|-------------------|--------------------------|--------------|
| mBERT             | 92.157                   | 90.898       |
| BERTje            | 93.096                   | 91.279       |
| RobBERT v2        | **97.816**               | **97.514**   |

#### Using zero-shot word masking task

Since BERT models are pre-trained using the word masking task, we can use this to predict whether "die" or "dat" is more likely.
This experiment shows that RobBERT has internalised more information about Dutch than other models.

|   Model           | Accuracy [%]             |
|-------------------|--------------------------|
| ZeroR             | 66.70                    |
| mBERT             | 90.21                    |
| BERTje            | 94.94                    |
| RobBERT v2        | **98.75**                |

### Part-of-Speech Tagging.

Using the [Lassy UD dataset](https://universaldependencies.org/treebanks/nl_lassysmall/index.html).


|   Model           | Accuracy [%]             |
|-------------------|--------------------------|
| Frog              | 91.7                     |
| mBERT             | **96.5**                 |
| BERTje            | 96.3                     |
| RobBERT v2        | 96.4                     |
| RobBERT 2022      | 96.1                     |


## Credits and citation

This project is created by [Pieter Delobelle](https://people.cs.kuleuven.be/~pieter.delobelle), [Thomas Winters](https://thomaswinters.be) and [Bettina Berendt](https://people.cs.kuleuven.be/~bettina.berendt/).
If you would like to cite our paper or model, you can use the following BibTeX:

```
@inproceedings{delobelle2022robbert2022,
  doi = {10.48550/ARXIV.2211.08192},
  url = {https://arxiv.org/abs/2211.08192},
  author = {Delobelle, Pieter and Winters, Thomas and Berendt, Bettina},
  keywords = {Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {RobBERT-2022: Updating a Dutch Language Model to Account for Evolving Language Use},
  venue = {arXiv},
  year = {2022},
}

@inproceedings{delobelle2020robbert,
    title = "{R}ob{BERT}: a {D}utch {R}o{BERT}a-based {L}anguage {M}odel",
    author = "Delobelle, Pieter  and
      Winters, Thomas  and
      Berendt, Bettina",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.findings-emnlp.292",
    doi = "10.18653/v1/2020.findings-emnlp.292",
    pages = "3255--3265"
}
```
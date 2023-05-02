---
license: cc0-1.0
language:
- tr
tags:
- MaCoCu
---

# Model description

**XLMR-MaCoCu-tr** is a large pre-trained language model trained on **Turkish** texts. It was created by continuing training from the [XLM-RoBERTa-large](https://huggingface.co/xlm-roberta-large) model. It was developed as part of the [MaCoCu](https://macocu.eu/) project and only uses data that was crawled during the project. The main developer is [Rik van Noord](https://www.rikvannoord.nl/) from the University of Groningen.

XLMR-MaCoCu-tr was trained on 35GB of Turkish text, which is equal to 4.4B tokens. It was trained for 70,000 steps with a batch size of 1,024. It uses the same vocabulary as the original XLMR-large model.

The training and fine-tuning procedures are described in detail on our [Github repo](https://github.com/macocu/LanguageModels).

# How to use

```python
from transformers import AutoTokenizer, AutoModel, TFAutoModel

tokenizer = AutoTokenizer.from_pretrained("RVN/XLMR-MaCoCu-tr")
model = AutoModel.from_pretrained("RVN/XLMR-MaCoCu-tr") # PyTorch
model = TFAutoModel.from_pretrained("RVN/XLMR-MaCoCu-tr") # Tensorflow
```

# Data

For training, we used all Turkish data that was present in the monolingual Turkish [MaCoCu](https://macocu.eu/) corpus. After de-duplicating the data, we were left with a total of 35 GB of text, which equals 4.4 billion tokens.

# Benchmark performance

We tested the performance of **XLMR-MaCoCu-tr** on benchmarks of XPOS, UPOS and NER from the [Universal Dependencies](https://universaldependencies.org/) project. For COPA, we train on a machine translated (MT) set of the data (for details see our [Github repo](https://github.com/RikVN/COPA)), and evaluate on a similar MT set, but also on the human-translated (HT) test set from the [XCOPA](https://github.com/cambridgeltl/xcopa) project. We compare performance to the strong multi-lingual models XLMR-base and XLMR-large, but also to the monolingual [BERTurk](https://huggingface.co/dbmdz/bert-base-turkish-cased) model. For details regarding the fine-tuning procedure you can checkout our [Github](https://github.com/macocu/LanguageModels).

Scores are averages of three runs, except for COPA, for which we use 10 runs. We use the same hyperparameter settings for all models for POS/NER, for COPA we optimized each learning rate on the dev set.

|                    | **UPOS** | **UPOS** | **XPOS** | **XPOS** | **NER** | **NER**  | **COPA** | **COPA** |
|--------------------|:--------:|:--------:|:--------:|:--------:|---------|----------| ----------| ----------|
|                    |  **Dev** | **Test** |  **Dev** | **Test** | **Dev** | **Test** |  **Test (MT)** | **Test (HT)** |
| **XLM-R-base**     |   89.0   |   89.0   |   90.4   |   90.6   |   92.8  |   92.6   | 56.0 |   53.2  |
| **XLM-R-large**    |   89.4   |   89.3   |   90.8   |   90.7   |   94.1  |   94.1   | 52.1 |   50.5  |
| **BERTurk**        |   88.2   |   88.4   |   89.7   |   89.6   |   92.6  |   92.6   | 57.0 |  56.4   |
| **XLMR-MaCoCu-tr** |   89.1   |   89.4   |   90.7   |   90.5   |   94.4  |   94.4   | 60.7 |   58.5  |

# Acknowledgements

Research supported with Cloud TPUs from Google's TPU Research Cloud (TRC). The authors received funding from the European Union’s Connecting Europe Facility 2014-
2020 - CEF Telecom, under Grant Agreement No.INEA/CEF/ICT/A2020/2278341 (MaCoCu).

# Citation

If you use this model, please cite the following paper:

```bibtex
@inproceedings{non-etal-2022-macocu,
    title = "{M}a{C}o{C}u: Massive collection and curation of monolingual and bilingual data: focus on under-resourced languages",
    author = "Ba{\~n}{\'o}n, Marta  and
      Espl{\`a}-Gomis, Miquel  and
      Forcada, Mikel L.  and
      Garc{\'\i}a-Romero, Cristian  and
      Kuzman, Taja  and
      Ljube{\v{s}}i{\'c}, Nikola  and
      van Noord, Rik  and
      Sempere, Leopoldo Pla  and
      Ram{\'\i}rez-S{\'a}nchez, Gema  and
      Rupnik, Peter  and
      Suchomel, V{\'\i}t  and
      Toral, Antonio  and
      van der Werff, Tobias  and
      Zaragoza, Jaume",
    booktitle = "Proceedings of the 23rd Annual Conference of the European Association for Machine Translation",
    month = jun,
    year = "2022",
    address = "Ghent, Belgium",
    publisher = "European Association for Machine Translation",
    url = "https://aclanthology.org/2022.eamt-1.41",
    pages = "303--304"
}
```
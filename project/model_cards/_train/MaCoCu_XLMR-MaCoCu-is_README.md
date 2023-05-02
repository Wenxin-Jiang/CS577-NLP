---
license: cc0-1.0
language:
- is
tags:
- MaCoCu
---

# Model description

**XLMR-MaCoCu-is** is a large pre-trained language model trained on **Icelandic** texts. It was created by continuing training from the [XLM-RoBERTa-large](https://huggingface.co/xlm-roberta-large) model. It was developed as part of the [MaCoCu](https://macocu.eu/) project and only uses data that was crawled during the project. The main developer is [Rik van Noord](https://www.rikvannoord.nl/) from the University of Groningen.

XLMR-MaCoCu-is was trained on 4.4GB of Icelandic text, which is equal to 688M tokens. It was trained for 75,000 steps with a batch size of 1,024. It uses the same vocabulary as the original XLMR-large model.

The training and fine-tuning procedures are described in detail on our [Github repo](https://github.com/macocu/LanguageModels).

# How to use

```python
from transformers import AutoTokenizer, AutoModel, TFAutoModel

tokenizer = AutoTokenizer.from_pretrained("RVN/XLMR-MaCoCu-is")
model = AutoModel.from_pretrained("RVN/XLMR-MaCoCu-is") # PyTorch
model = TFAutoModel.from_pretrained("RVN/XLMR-MaCoCu-is") # Tensorflow
```

# Data

For training, we used all Icelandic data that was present in the monolingual Icelandic [MaCoCu](https://macocu.eu/) corpus. After de-duplicating the data, we were left with a total of 4.4 GB of text, which equals 688M tokens.

# Benchmark performance

We tested the performance of **XLMR-MaCoCu-is** on benchmarks of XPOS, UPOS, NER and COPA. For UPOS and XPOS, we used the data from the [Universal Dependencies](https://universaldependencies.org/) project. For NER, we used the data from the MIM-GOLD-NER data set. For COPA, we automatically translated the English data set by using Google Translate. For details please see our [Github repo](https://github.com/RikVN/COPA). We compare performance to the strong multi-lingual models XLMR-base and XLMR-large, but also the monolingual [IceBERT](https://huggingface.co/vesteinn/IceBERT) model. For details regarding the XPOS/UPOS/NER fine-tuning procedure you can checkout our [Github](https://github.com/macocu/LanguageModels).

Scores are averages of three runs, except for COPA, for which we use 10 runs. We use the same hyperparameter settings for all models.

|                    | **UPOS** | **UPOS** | **XPOS** | **XPOS** | **NER** | **NER**  | **COPA**  |
|--------------------|:--------:|:--------:|:--------:|:--------:|---------|----------| ----------|
|                    |  **Dev** | **Test** |  **Dev** | **Test** | **Dev** | **Test** | **Test** |
| **XLM-R-base**     |   96.8   |   96.5   |   94.6   |   94.3   |   85.3  |   89.7   | 55.2 |
| **XLM-R-large**    |   97.0   |   96.7   |   94.9   |   94.7   |   88.5  |   91.7   | 54.3 |
| **IceBERT**        |   96.4   |   96.0   |   94.0   |   93.7   |   83.8  |   89.7   | 54.6 | 
| **XLMR-MaCoCu-is** |   **97.3**   |    **97.0**    |   **95.4**   |   **95.1**  |   **90.8**  |   **93.2**   | **59.6** |

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
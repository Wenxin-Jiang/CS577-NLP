---
license: cc0-1.0
language:
- mt
tags:
- MaltBERTa
- MaCoCu
---

# Model description

**MaltBERTa** is a large pre-trained language model trained on Maltese texts. It was trained from scratch using the RoBERTa architecture. It was developed as part of the [MaCoCu](https://macocu.eu/) project. The main developer is [Rik van Noord](https://www.rikvannoord.nl/) from the University of Groningen.

MaltBERTa was trained on 3.2GB of text, which is equal to 439M tokens. It was trained for 100,000 steps with a batch size of 1,024.

The training and fine-tuning procedures are described in detail on our [Github repo](https://github.com/macocu/LanguageModels).
# How to use

```python
from transformers import AutoTokenizer, AutoModel, TFAutoModel

tokenizer = AutoTokenizer.from_pretrained("RVN/MaltBERTa")
model = AutoModel.from_pretrained("RVN/MaltBERTa") # PyTorch
model = TFAutoModel.from_pretrained("RVN/MaltBERTa") # Tensorflow
```

# Data

For training, we used all Maltese data that was present in the [MaCoCu](https://macocu.eu/), Oscar and mc4 corpora. After de-duplicating the data, we were left with a total of 3.2GB of text. We ran experiments with only training on data that came from the .mt domain in Oscar and mc4, but got better performance by incorporating all data.

# Benchmark performance

We tested the performance of MaltBERTa on the UPOS and XPOS benchmark of the [Universal Dependencies](https://universaldependencies.org/) project. Moreover, we test on a Google Translated version of the COPA data set (see our [Github repo](https://github.com/RikVN/COPA) for details). We compare performance to the strong multi-lingual models XLMR-base and XLMR-large, though note that Maltese was not one of the training languages for those models. We also compare to the recently introduced Maltese language models [BERTu](https://huggingface.co/MLRS/BERTu), [mBERTu](https://huggingface.co/MLRS/mBERTu) and our own [MaltBERTa](https://huggingface.co/RVN/MaltBERTa). For details regarding the fine-tuning procedure you can checkout our [Github](https://github.com/macocu/LanguageModels).

Scores are averages of three runs for UPOS/XPOS and 10 runs for COPA. We use the same hyperparameter settings for all models for UPOS/XPOS, while for COPA we optimize on the dev set.

|                 | **UPOS** | **UPOS** | **XPOS** | **XPOS** | **COPA** |
|-----------------|:--------:|:--------:|:--------:|:--------:| :--------:|
|                 |  **Dev** | **Test** |  **Dev** | **Test** | **Test** |
| **XLM-R-base**  |   93.6   |   93.2   |   93.4   |   93.2   |  52.2 |
| **XLM-R-large** |   94.9   |   94.4   |   95.1   |   94.7   |  54.0 |
| **BERTu**       |   97.5   |   97.6   |   95.7   |   95.8   |  **55.6** |
| **mBERTu**      |   **97.7**   |   **97.8**   |   **97.9**   |   **98.1** |  52.6  |
| **MaltBERTa**   |   95.7   |   95.8   |   96.1   |   96.0   | 53.7 |

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
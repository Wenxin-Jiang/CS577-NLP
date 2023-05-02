---
language:
- bg
- mk
- multilingual
license: cc0-1.0
tags:
- BERTovski
- MaCoCu
---

# Model description

**XLMR-BERTovski** is a large pre-trained language model trained on Bulgarian and Macedonian texts. It was created by continuing training from the [XLM-RoBERTa-large](https://huggingface.co/xlm-roberta-large) model. It was developed as part of the [MaCoCu](https://macocu.eu/) project. The main developer is [Rik van Noord](https://www.rikvannoord.nl/) from the University of Groningen.

XLMR-BERTovski was trained on 74GB of Bulgarian and Macedonian text, which is equal to just over 7 billion tokens. It was trained for 67,500 steps with a batch size of 1,024, which was approximately 2.5 epochs. It uses the same vocabulary as the original XLMR-large model. The model is trained on the same data as [BERTovski](https://huggingface.co/RVN/BERTovski), but this model was trained from scratch using the RoBERTa architecture.

The training and fine-tuning procedures are described in detail on our [Github repo](https://github.com/macocu/LanguageModels).

# How to use

```python
from transformers import AutoTokenizer, AutoModel, TFAutoModel

tokenizer = AutoTokenizer.from_pretrained("RVN/XLMR-BERTovski")
model = AutoModel.from_pretrained("RVN/XLMR-BERTovski") # PyTorch
model = TFAutoModel.from_pretrained("RVN/XLMR-BERTovski") # Tensorflow
```

# Data

For training, we used all Bulgarian and Macedonian data that was present in the [MaCoCu](https://macocu.eu/), Oscar, mc4 and Wikipedia corpora. In a manual analysis we found that for Oscar and mc4, if the data did not come from the corresponding domain (.bg or .mk), it was often (badly) machine translated. Therefore, we opted to only use data that originally came from a .bg or .mk domain. 

After de-duplicating the data, we were left with a total of 54.5 GB of Bulgarian and 9 GB of Macedonian text. Since there was quite a bit more Bulgarian data, we simply doubled the Macedonian data during training.

# Benchmark performance

We tested performance of XLMR-BERTovski on benchmarks of XPOS, UPOS and NER. For Bulgarian, we used the data from the [Universal Dependencies](https://universaldependencies.org/) project. For Macedonian, we used the data sets created in the [babushka-bench](https://github.com/clarinsi/babushka-bench/) project. We also tested on a Google (Bulgarian) and human (Macedonian) translated version of the COPA data set (for details see our [Github repo](https://github.com/RikVN/COPA)). We compare performance to [BERTovski](https://huggingface.co/RVN/BERTovski) and the strong multi-lingual models XLMR-base and XLMR-large. For details regarding the fine-tuning procedure you can checkout our [Github](https://github.com/macocu/LanguageModels).

Scores are averages of three runs, except for COPA, for which we use 10 runs. We use the same hyperparameter settings for all models for UPOS/XPOS/NER, for COPA we optimized the learning rate on the dev set.

## Bulgarian

|                 | **UPOS** | **UPOS** | **XPOS** | **XPOS** | **NER** |  **NER** | **COPA** |
|-----------------|:--------:|:--------:|:--------:|:--------:|:-------:|:--------:|:--------:|
|                 |  **Dev** | **Test** |  **Dev** | **Test** | **Dev** | **Test** | **Test** |
| **XLM-R-base**  |   99.2   |   99.4   |   98.0   |   98.3   |   93.2  |   92.9   |   56.9   |
| **XLM-R-large** |   99.3   |   99.4   |   97.4   |   97.7   |   93.7  |   93.5   |   53.1   |
| **BERTovski**   |   98.8   |   99.1   |   97.6   |   97.8   |   93.5  |   93.3   |   51.7   |
| **XLMR-BERTovski**   |  99.3    |   99.5   |    98.5  |   98.8  |  94.4   |  94.3    | 54.6 |

## Macedonian

|                 | **UPOS** | **UPOS** | **XPOS** | **XPOS** | **NER** |  **NER** |  **COPA** |
|-----------------|:--------:|:--------:|:--------:|:--------:|:-------:|:--------:|:--------:|
|                 |  **Dev** | **Test** |  **Dev** | **Test** | **Dev** | **Test** |  **Test** |
| **XLM-R-base**  |   98.3   |   98.6   |   97.3   |   97.1   |   92.8  |   94.8   | 55.3 |
| **XLM-R-large** |   98.3   |   98.7   |   97.7   |   97.5   |   93.3  |   95.1   | 52.5 |
| **BERTovski**   |   97.8   |   98.1   |   96.4   |   96.0   |   92.8  |   94.6   | 51.8 |
| **XLMR-BERTovski**   |  98.6    | 98.8    |    98.0 |    97.7  |   94.4 |    96.3  | 55.6|

# Acknowledgements

Research supported with Cloud TPUs from Google's TPU Research Cloud (TRC). The authors received funding from the European Union's Connecting Europe Facility 2014-
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
---

language:

- en

- pt

datasets:

- EMEA

- ParaCrawl 99k

- CAPES

- Scielo

- JRC-Acquis

- Biomedical Domain Corpora

tags:

- translation

metrics:

- bleu

---


# Introduction

This repository brings an implementation of T5 for translation in EN-PT tasks using a modest hardware setup. We propose some changes in tokenizator and post-processing that improves the result and used a Portuguese pretrained model for the translation. You can collect more informations in [our repository](https://github.com/unicamp-dl/Lite-T5-Translation). Also, check [our paper](https://aclanthology.org/2020.wmt-1.90.pdf)!

# Usage

Just follow "Use in Transformers" instructions. It is necessary to add a few words before to define the task to T5. 

You can also create a pipeline for it. An example with the phrase "I like to eat rice" is:

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
  
tokenizer = AutoTokenizer.from_pretrained("unicamp-dl/translation-en-pt-t5")

model = AutoModelForSeq2SeqLM.from_pretrained("unicamp-dl/translation-en-pt-t5")

enpt_pipeline = pipeline('text2text-generation', model=model, tokenizer=tokenizer)

enpt_pipeline("translate English to Portuguese: I like to eat rice.")

```

# Citation

```bibtex
@inproceedings{lopes-etal-2020-lite,
    title = "Lite Training Strategies for {P}ortuguese-{E}nglish and {E}nglish-{P}ortuguese Translation",
    author = "Lopes, Alexandre  and
      Nogueira, Rodrigo  and
      Lotufo, Roberto  and
      Pedrini, Helio",
    booktitle = "Proceedings of the Fifth Conference on Machine Translation",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.wmt-1.90",
    pages = "833--840",
}
```
---
license: apache-2.0
---

# Model description

This is an [t5-base](https://huggingface.co/t5-base) model, finetuned to generate questions given a table using [WikiSQL](https://huggingface.co/datasets/wikisql) dataset. It was trained to take the SQL, answer and column header of a table as input to generate questions. For more information check our T3QA [paper](https://aclanthology.org/2021.emnlp-main.342/) from EMNLP 2021.

# Overview

*Language model*: t5-base \
*Language*: English \
*Task*: Table Question Generation \
*Data*: WikiSQL

# Intented use and limitations
One can use this model to generate questions given a table. Biases associated with pre-training of T5 and WikiSQL dataset may be present.

## Usage
One can use this model directly in the [PrimeQA](https://github.com/primeqa/primeqa) framework as in this example [notebook](https://github.com/primeqa/primeqa/blob/tableqg/notebooks/qg/tableqg_inference.ipynb).

## Citation
```bibtex
@inproceedings{chemmengath2021topic,
  title={Topic Transferable Table Question Answering},
  author={Chemmengath, Saneem and Kumar, Vishwajeet and
          Bharadwaj, Samarth and Sen, Jaydeep and
          Canim, Mustafa and Chakrabarti, Soumen and
          Gliozzo, Alfio and Sankaranarayanan, Karthik},
  booktitle={Proceedings of the 2021 Conference on 
      Empirical Methods in Natural Language Processing},
  pages={4159--4172},
  year={2021}
}
```


---
license: apache-2.0
---

# Model description

This is an [tapas-base](https://huggingface.co/google/tapas-base) model, trained on the lookup queries of [wikisql](https://huggingface.co/datasets/wikisql) dataset. It was trained to take tables and questions as input to extract answers from the table.

# Overview

*Language model*: tapas-base \
*Language*: English\
*Task*: Table Question Answering \
*Data*: WikiSQL

# Intented use and limitations
One can use this model to predict answers for natural language queries given a table. Biases associated with pre-training of tapas-base and wikisql dataset may be present.

## Usage
One can use this model directly in the [PrimeQA](https://github.com/primeqa/primeqa) framework as in this example [notebook](https://github.com/primeqa/primeqa/blob/tableqa_tapas/notebooks/tableqa/tableqa_inference.ipynb).


## Citation
```bibtex
@misc{herzig2020tapas,
      title={TAPAS: Weakly Supervised Table Parsing via Pre-training}, 
      author={Jonathan Herzig and Paweł Krzysztof Nowak and Thomas Müller and Francesco Piccinno and Julian Martin Eisenschlos},
      year={2020},
      eprint={2004.02349},
      archivePrefix={arXiv},
      primaryClass={cs.IR}
}

```
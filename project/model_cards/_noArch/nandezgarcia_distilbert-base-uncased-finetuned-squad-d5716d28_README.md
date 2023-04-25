---
language: 
- en
thumbnail: https://github.com/karanchahal/distiller/blob/master/distiller.jpg
tags:
- question-answering
license: apache-2.0
datasets:
- squad
metrics:
- squad
---

# DistilBERT with a second step of distillation

## Model description

This model replicates the "DistilBERT (D)" model from Table 2 of the [DistilBERT paper](https://arxiv.org/pdf/1910.01108.pdf). In this approach, a DistilBERT student is fine-tuned on SQuAD v1.1, but with a BERT model (also fine-tuned on SQuAD v1.1) acting as a teacher for a second step of task-specific distillation.

In this version, the following pre-trained models were used:

* Student: `distilbert-base-uncased`
* Teacher: `lewtun/bert-base-uncased-finetuned-squad-v1`

## Training data

This model was trained on the SQuAD v1.1 dataset which can be obtained from the `datasets` library as follows:

```python
from datasets import load_dataset
squad = load_dataset('squad')
```

## Training procedure

## Eval results

|                  | Exact Match | F1   |
|------------------|-------------|------|
| DistilBERT paper | 79.1        | 86.9 |
| Ours             | 78.4        | 86.5 |

The scores were calculated using the `squad` metric from `datasets`.

### BibTeX entry and citation info

```bibtex
@misc{sanh2020distilbert,
      title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter}, 
      author={Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},
      year={2020},
      eprint={1910.01108},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
---
language:
- en
tags:
- text reranking
license: apache-2.0
datasets:
- MS MARCO document ranking
---

# BERT Reranker for MS-MARCO Document Ranking

## Model description

A text reranker trained for HDCT retriever on MS MARCO document dataset.

## Intended uses & limitations
It is possible to work with other retrievers like BM25 but using aligned HDCT works the best.

#### How to use
See our [project repo page](https://github.com/luyug/Reranker).

## Eval results
MRR @10: 0.434 on Dev.
MRR @10: 0.382 on Eval.

### BibTeX entry and citation info

```bibtex
@inproceedings{gao2021lce,
               title={Rethink Training of BERT Rerankers in Multi-Stage Retrieval Pipeline}, 
               author={Luyu Gao and Zhuyun Dai and Jamie Callan},
               year={2021},
               booktitle={The 43rd European Conference On Information Retrieval (ECIR)},
      
}
```
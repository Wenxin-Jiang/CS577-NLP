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

A text reranker trained for BM25 retriever on MS MARCO document dataset.

## Intended uses & limitations
It is possible to work with other retrievers like but using aligned BM25 works the best.

We used anserini toolkit's BM25 implementation and indexed with tuned parameters (k1=3.8, b=0.87) following [this instruction](https://github.com/castorini/anserini/blob/master/docs/experiments-msmarco-doc.md).

#### How to use
See our [project repo page](https://github.com/luyug/Reranker).

## Eval results
MRR @10: 0.423 on Dev.

### BibTeX entry and citation info

```bibtex
@inproceedings{gao2021lce,
               title={Rethink Training of BERT Rerankers in Multi-Stage Retrieval Pipeline}, 
               author={Luyu Gao and Zhuyun Dai and Jamie Callan},
               year={2021},
               booktitle={The 43rd European Conference On Information Retrieval (ECIR)},
      
}
```
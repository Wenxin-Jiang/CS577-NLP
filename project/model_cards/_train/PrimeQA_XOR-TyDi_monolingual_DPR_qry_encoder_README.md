---
license: cc-by-sa-4.0
---

# Model Description

Query encoder, trained on monolingual (English queries) version of the XOR-TyDi training data, as described in the XOR-TyDi task description https://nlp.cs.washington.edu/xorqa/.

## Usage 

The model is compatible with the PrimeQA DPR engine, or the Hugging Face DPR engine as shown this example https://huggingface.co/docs/datasets/faiss_es.  
The model uses the tokenizer from `facebook/dpr-question_encoder-multiset-base`.

## Performance comparison

| R@5kt | R@2kt | model |
|-------|-------|-------|
| 69.6 | 62.2 | DPR, En, XOR-TyDi paper (https://arxiv.org/pdf/2010.11856.pdf, table 13) |
| 70.22 | 64.34 | DPR, En, trained on En (human) version of XOR |


## BibTeX entry and citation info
```bibtex
@inproceedings{asai-etal-2021-xor,
    title = "{XOR} {QA}: Cross-lingual Open-Retrieval Question Answering",
    author = "Asai, Akari  and
      Kasai, Jungo  and
      Clark, Jonathan  and
      Lee, Kenton  and
      Choi, Eunsol  and
      Hajishirzi, Hannaneh",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.46",
    doi = "10.18653/v1/2021.naacl-main.46",
    pages = "547--564",
}
```

```bibtex
@inproceedings{karpukhin-etal-2020-dense,
    title = "Dense Passage Retrieval for Open-Domain Question Answering",
    author = "Karpukhin, Vladimir  and
      Oguz, Barlas  and
      Min, Sewon  and
      Lewis, Patrick  and
      Wu, Ledell  and
      Edunov, Sergey  and
      Chen, Danqi  and
      Yih, Wen-tau",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.emnlp-main.550",
    doi = "10.18653/v1/2020.emnlp-main.550",
    pages = "6769--6781",
}
```

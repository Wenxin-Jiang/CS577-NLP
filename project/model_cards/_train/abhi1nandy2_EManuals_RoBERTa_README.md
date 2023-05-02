---
language: 
  - English
tags:
- EManuals
- customer support
- QA
- roberta

---

Refer to https://aclanthology.org/2021.findings-emnlp.392/ for the paper and https://sites.google.com/view/emanualqa/home for the project website

## Citation

Please cite the work if you would like to use it.

```
@inproceedings{nandy-etal-2021-question-answering,
    title = "Question Answering over Electronic Devices: A New Benchmark Dataset and a Multi-Task Learning based {QA} Framework",
    author = "Nandy, Abhilash  and
      Sharma, Soumya  and
      Maddhashiya, Shubham  and
      Sachdeva, Kapil  and
      Goyal, Pawan  and
      Ganguly, NIloy",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-emnlp.392",
    doi = "10.18653/v1/2021.findings-emnlp.392",
    pages = "4600--4609",
    abstract = "Answering questions asked from instructional corpora such as E-manuals, recipe books, etc., has been far less studied than open-domain factoid context-based question answering. This can be primarily attributed to the absence of standard benchmark datasets. In this paper, we meticulously create a large amount of data connected with E-manuals and develop a suitable algorithm to exploit it. We collect E-Manual Corpus, a huge corpus of 307,957 E-manuals, and pretrain RoBERTa on this large corpus. We create various benchmark QA datasets which include question answer pairs curated by experts based upon two E-manuals, real user questions from Community Question Answering Forum pertaining to E-manuals etc. We introduce EMQAP (E-Manual Question Answering Pipeline) that answers questions pertaining to electronics devices. Built upon the pretrained RoBERTa, it harbors a supervised multi-task learning framework which efficiently performs the dual tasks of identifying the section in the E-manual where the answer can be found and the exact answer span within that section. For E-Manual annotated question-answer pairs, we show an improvement of about 40{\%} in ROUGE-L F1 scores over most competitive baseline. We perform a detailed ablation study and establish the versatility of EMQAP across different circumstances. The code and datasets are shared at https://github.com/abhi1nandy2/EMNLP-2021-Findings, and the corresponding project website is https://sites.google.com/view/emanualqa/home.",
}
```
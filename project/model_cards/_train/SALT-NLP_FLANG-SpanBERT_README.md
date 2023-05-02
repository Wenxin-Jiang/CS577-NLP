
---
language: "en"
tags:
- Financial Language Modelling
widget:
- text: "Stocks rallied and the British pound [MASK]."
---
## Dataset Summary
- **Homepage:** https://salt-nlp.github.io/FLANG/
- **Models:** https://huggingface.co/SALT-NLP/FLANG-BERT
- **Repository:** https://github.com/SALT-NLP/FLANG

## FLANG
FLANG is a set of large language models for Financial LANGuage tasks. These models use domain specific pre-training with preferential masking to build more robust representations for the domain. The models in the set are:\
[FLANG-BERT](https://huggingface.co/SALT-NLP/FLANG-BERT)\
[FLANG-SpanBERT](https://huggingface.co/SALT-NLP/FLANG-SpanBERT)\
[FLANG-DistilBERT](https://huggingface.co/SALT-NLP/FLANG-DistilBERT)\
[FLANG-Roberta](https://huggingface.co/SALT-NLP/FLANG-Roberta)\
[FLANG-ELECTRA](https://huggingface.co/SALT-NLP/FLANG-ELECTRA)

## FLANG-SpanBERT
FLANG-SpanBERT is a pre-trained language model which uses financial keywords and phrases for preferential masking of domain specific terms. It is built by further training the SpanBERT language model in the finance domain with improved performance over previous models due to the use of domain knowledge and vocabulary.

## FLUE
FLUE (Financial Language Understanding Evaluation) is a comprehensive and heterogeneous benchmark that has been built from 5 diverse financial domain specific datasets.

Sentiment Classification: [Financial PhraseBank](https://huggingface.co/datasets/financial_phrasebank)\
Sentiment Analysis, Question Answering: [FiQA 2018](https://huggingface.co/datasets/SALT-NLP/FLUE-FiQA)\
New Headlines Classification: [Headlines](https://www.kaggle.com/datasets/daittan/gold-commodity-news-and-dimensions)\
Named Entity Recognition: [NER](https://paperswithcode.com/dataset/fin)\
Structure Boundary Detection: [FinSBD3](https://sites.google.com/nlg.csie.ntu.edu.tw/finweb2021/shared-task-finsbd-3)

## Citation
Please cite the model with the following citation:
```bibtex
@INPROCEEDINGS{shah-etal-2022-flang,
    author = {Shah, Raj Sanjay  and
      Chawla, Kunal and
      Eidnani, Dheeraj and
      Shah, Agam and
      Du, Wendi and
      Chava, Sudheer and
      Raman, Natraj and
      Smiley, Charese and
      Chen, Jiaao and
      Yang, Diyi },
    title = {When FLUE Meets FLANG: Benchmarks and Large Pretrained Language Model for Financial Domain},
    booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
    year = {2022},
    publisher = {Association for Computational Linguistics}
}
```

## Contact information

Please contact Raj Sanjay Shah (rajsanjayshah[at]gatech[dot]edu) or Sudheer Chava (schava6[at]gatech[dot]edu) or Diyi Yang (diyiy[at]stanford[dot]edu) about any FLANG-SpanBERT related issues and questions.


---
license: afl-3.0
---
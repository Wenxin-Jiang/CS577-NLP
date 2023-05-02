---
language: 
  - "en"
license: mit
tags:
- fill-mask
---


# MedBERT Model

**MedBERT** is a newly pre-trained transformer-based language model for biomedical named entity recognition: initialized with [Bio_ClinicalBERT](https://arxiv.org/abs/1904.03323) & pre-trained on N2C2, BioNLP, and CRAFT community datasets.

## Pretraining

### Data
The `MedBERT` model was trained on N2C2, BioNLP, and CRAFT community datasets.

| Dataset | Description |
| ------------- | ------------- | 
| [NLP Clinical Challenges (N2C2)](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/) | A collection of clinical notes released in N2C2 2018 and N2C2 2022 challenges| 
| [BioNLP](http://bionlp.sourceforge.net/index.shtml) | It contains the articles released under the BioNLP project. The articles cover multiple biomedical disciplines such as molecular biology, IE for protein and DNA modifications, biomolecular mechanisms of infectious diseases, habitats of bacteria mentioned, and bacterial molecular interactions and regulations |
| [CRAFT](https://www.researchgate.net/publication/318175988_The_Colorado_Richly_Annotated_Full_Text_CRAFT_Corpus_Multi-Model_Annotation_in_the_Biomedical_Domain) | It consists of 67 full-text open-access biomedical journal articles from PubMed Central that covers a wide range of biomedical domains including biochemistry and molecular biology, genetics, developmental biology, and computational biology |
| Wikipedia | Crawled medical-related articles |


### Procedures
The model was trained using code from [Google's BERT repository](https://github.com/google-research/bert). Model parameters were initialized with Bio_ClinicalBERT.

### Hyperparameters
We used a batch size of 32, a maximum sequence length of 256, and a learning rate of 1·10−4 for pre-training our models. The models trained for 200,000 steps. The dup factor for duplicating input data with different masks was set to 5. All other default parameters were used (specifically, masked language model probability = 0.15
and max predictions per sequence = 22).

## How to use

```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("Charangan/MedBERT")
model = AutoModel.from_pretrained("Charangan/MedBERT")
```

## More Information

Refer to the original paper, [MedBERT: A Pre-trained Language Model for Biomedical Named Entity Recognition](https://ieeexplore.ieee.org/abstract/document/9980157) (APSIPA Conference 2022) for additional details and performance of biomedical NER tasks.

## Citation
```
@INPROCEEDINGS{9980157,
    author={Vasantharajan, Charangan and Tun, Kyaw Zin and Thi-Nga, Ho and Jain, Sparsh and Rong, Tong and Siong, Chng Eng},
    booktitle={2022 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC)},
    title={MedBERT: A Pre-trained Language Model for Biomedical Named Entity Recognition},
    year={2022},
    volume={},
    number={},
    pages={1482-1488},
    doi={10.23919/APSIPAASC55919.2022.9980157}
}
```
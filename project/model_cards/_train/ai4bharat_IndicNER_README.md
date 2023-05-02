---
language:
- as 
- bn
- gu 
- hi 
- kn 
- ml 
- mr 
- or 
- pa 
- ta 
- te 
license: mit
datasets:
- Samanantar
tags:
- ner
- Pytorch
- transformer
- multilingual
- nlp
- indicnlp
---

# IndicNER
IndicNER is a model trained to complete the task of identifying named entities from sentences in Indian languages. Our model is specifically fine-tuned to the 11 Indian languages mentioned above over millions of sentences. The model is then benchmarked over a human annotated testset and multiple other publicly available Indian NER datasets.
The 11 languages covered by IndicNER are: Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu.

## Training Corpus
Our model was trained on a [dataset](https://huggingface.co/datasets/ai4bharat/naamapadam) which we mined from the existing [Samanantar Corpus](https://huggingface.co/datasets/ai4bharat/samanantar). We used a bert-base-multilingual-uncased model as the starting point and then fine-tuned it to the NER dataset mentioned previously.

## Downloads
Download from this same Huggingface repo.

Update 20 Dec 2022: We released a new paper documenting IndicNER and Naamapadam. We have a different model reported in the paper. We will update the repo here soon with this model.

## Usage

You can use [this Colab notebook](https://colab.research.google.com/drive/1sYa-PDdZQ_c9SzUgnhyb3Fl7j96QBCS8?usp=sharing) for samples on using IndicNER or for finetuning a pre-trained model on Naampadam dataset to build your own NER models.

<!-- citing information -->
## Citing

If you are using IndicNER, please cite the following article:
```
@misc{mhaske2022naamapadam,
  doi = {10.48550/ARXIV.2212.10168},
  url = {https://arxiv.org/abs/2212.10168},
  author = {Mhaske, Arnav and Kedia, Harshit and Doddapaneni, Sumanth and Khapra, Mitesh M. and Kumar, Pratyush and Murthy, Rudra and Kunchukuttan, Anoop},
  title = {Naamapadam: A Large-Scale Named Entity Annotated Data for Indic Languages}
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}

```
We would like to hear from you if:

- You are using our resources. Please let us know how you are putting these resources to use.
- You have any feedback on these resources.


<!-- License -->
## License

The IndicNER code (and models) are released under the MIT License.

<!-- Contributors -->
## Contributors
 - Arnav Mhaske <sub> ([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in)) </sub>
 - Harshit Kedia <sub> ([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in)) </sub>
 - Sumanth Doddapaneni <sub> ([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in)) </sub>
 - Mitesh M. Khapra <sub> ([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in)) </sub>
 - Pratyush Kumar <sub> ([AI4Bharat](https://ai4bharat.org), [Microsoft](https://www.microsoft.com/en-in/), [IITM](https://www.iitm.ac.in)) </sub> 
 - Rudra Murthy <sub> ([AI4Bharat](https://ai4bharat.org), [IBM](https://www.ibm.com))</sub>
 - Anoop Kunchukuttan <sub> ([AI4Bharat](https://ai4bharat.org), [Microsoft](https://www.microsoft.com/en-in/), [IITM](https://www.iitm.ac.in)) </sub> 

This work is the outcome of a volunteer effort as part of the [AI4Bharat initiative](https://ai4bharat.iitm.ac.in).


<!-- Contact -->
## Contact
- Anoop Kunchukuttan ([anoop.kunchukuttan@gmail.com](mailto:anoop.kunchukuttan@gmail.com))
- Rudra Murthy V ([rmurthyv@in.ibm.com](mailto:rmurthyv@in.ibm.com))
  
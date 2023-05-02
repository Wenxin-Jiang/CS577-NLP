---
language: 
  - es
tags:
- biomedical
- clinical
- spanish
license: apache-2.0
metrics:
- ppl
widget:
- text: "El único antecedente personal a reseñar era la <mask> arterial."
- text: "Las radiologías óseas de cuerpo entero no detectan alteraciones <mask>, ni alteraciones vertebrales."
- text: "En el <mask> toraco-abdómino-pélvico no se encontraron hallazgos patológicos de interés."
---

# Biomedical language model for Spanish

## Table of contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-use)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
  - [Tokenization and model pretraining](#Tokenization-modelpretraining)
  - [Training corpora and preprocessing](#Trainingcorpora-preprocessing)
- [Evaluation](#evaluation)
- [Additional information](#additional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Copyright](#copyright)
  - [Licensing information](#licensing-information)
  - [Funding](#funding)
  - [Citation information](#citation-information)
  - [Disclaimer](#disclaimer)
  
</details>


## Model description
Biomedical pretrained language model for Spanish. For more details about the corpus, the pretraining and the evaluation, check the official [repository](https://github.com/PlanTL-GOB-ES/lm-biomedical-clinical-es).

## Intended uses and limitations

The model is ready-to-use only for masked language modelling to perform the Fill Mask task (try the inference API or read the next section). However, it is intended to be fine-tuned on downstream tasks such as Named Entity Recognition or Text Classification.

## How to use


## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training

### Tokenization and model pretraining

This model is a [RoBERTa-based](https://github.com/pytorch/fairseq/tree/master/examples/roberta) model trained on a
**biomedical** corpus in Spanish collected from several sources (see next section). 
The training corpus has been tokenized using a byte version of [Byte-Pair Encoding (BPE)](https://github.com/openai/gpt-2)
used in the original [RoBERTA](https://github.com/pytorch/fairseq/tree/master/examples/roberta) model with a vocabulary size of 52,000 tokens. The pretraining consists of a masked language model training at the subword level following the approach employed for the RoBERTa base model with the same hyperparameters as in the original work. The training lasted a total of 48 hours with 16 NVIDIA V100 GPUs of 16GB DDRAM, using Adam optimizer with a peak learning rate of 0.0005 and an effective batch size of 2,048 sentences.


### Training corpora and preprocessing

The training corpus is composed of several biomedical corpora in Spanish, collected from publicly available corpora and crawlers.
To obtain a high-quality training corpus, a cleaning pipeline with the following operations has been applied:

- data parsing in different formats
  - sentence splitting
  - language detection
  - filtering of ill-formed sentences 
  - deduplication of repetitive contents
  - keep the original document boundaries

Finally, the corpora are concatenated and further global deduplication among the corpora has been applied.
The result is a medium-size biomedical corpus for Spanish composed of about 963M tokens. The table below shows some basic statistics of the individual cleaned corpora:

    
| Name                                                                                    | No. tokens  | Description                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Medical crawler](https://zenodo.org/record/4561970)                                    | 903,558,136 | Crawler of more than 3,000 URLs belonging to Spanish biomedical and health domains.                                                                                                                                                                                 |
| Clinical cases misc.                                                                    | 102,855,267 | A miscellany of medical content, essentially clinical cases. Note that a clinical case report is a scientific publication where medical practitioners share patient cases and it is different from a clinical note or document.                                                                                                                                                                                 |
| [Scielo](https://zenodo.org/record/2541681#.YlP1DshBwio)                        | 60,007,289  | Publications written in Spanish crawled from the Spanish SciELO server in 2017.                                                                                                                                       |
| [BARR2_background](https://temu.bsc.es/BARR2/downloads/background_set.raw_text.tar.bz2) | 24,516,442  | Biomedical Abbreviation Recognition and Resolution (BARR2) containing Spanish clinical case study sections from a variety of clinical disciplines.                                                                                       |
| Wikipedia_life_sciences                                                                 | 13,890,501  | Wikipedia articles crawled 04/01/2021 with the [Wikipedia API python library](https://pypi.org/project/Wikipedia-API/) starting from the "Ciencias\_de\_la\_vida" category up to a maximum of 5 subcategories. Multiple links to the same articles are then discarded to avoid repeating content.                                                                                                                                                                    |
| Patents                                                                                 | 13,463,387  | Google Patent in Medical Domain for Spain (Spanish). The accepted codes (Medical Domain) for Json files of patents are: "A61B", "A61C","A61F", "A61H", "A61K", "A61L","A61M", "A61B", "A61P".                                                        |
| [EMEA](http://opus.nlpl.eu/download.php?f=EMEA/v3/moses/en-es.txt.zip)                  | 5,377,448   | Spanish-side documents extracted from parallel corpora made out of PDF documents from the European Medicines Agency.                                                                                                                            |
| [mespen_Medline](https://zenodo.org/record/3562536#.YTt1fH2xXbR)                        | 4,166,077   | Spanish-side articles extracted from a collection of Spanish-English parallel corpus consisting of biomedical scientific literature.  The collection of parallel resources is aggregated from the MedlinePlus source. |
| PubMed                                                                                  | 1,858,966   | Open-access articles from the PubMed repository crawled in 2017.                                                                                                                                              |


## Evaluation 

The model has been fine-tuned on three Named Entity Recognition (NER) tasks using three clinical NER datasets:

 - [PharmaCoNER](https://zenodo.org/record/4270158): is a track on chemical and drug mention recognition from Spanish medical texts (for more info see: https://temu.bsc.es/pharmaconer/).

 - [CANTEMIST](https://zenodo.org/record/3978041#.YTt5qH2xXbQ): is a shared task specifically focusing on named entity recognition of tumour morphology, in Spanish (for more info see: https://zenodo.org/record/3978041#.YTt5qH2xXbQ). 

 - ICTUSnet: consists of 1,006 hospital discharge reports of patients admitted for stroke from 18 different Spanish hospitals. It contains more than 79,000 annotations for 51 different kinds of variables.
 
We addressed the NER task as a token classification problem using a standard linear layer along with the BIO tagging schema. We compared our models with the general-domain Spanish [roberta-base-bne](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne), the general-domain multilingual model that supports Spanish [mBERT](https://huggingface.co/bert-base-multilingual-cased), the domain-specific English model [BioBERT](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2), and three domain-specific models based on continual pre-training, [mBERT-Galén](https://ieeexplore.ieee.org/document/9430499), [XLM-R-Galén](https://ieeexplore.ieee.org/document/9430499) and [BETO-Galén](https://ieeexplore.ieee.org/document/9430499).

The table below shows the F1 scores obtained:

| Tasks/Models | bsc-bio-es  | XLM-R-Galén        | BETO-Galén   | mBERT-Galén  | mBERT        | BioBERT      | roberta-base-bne |
|--------------|----------------|--------------------|--------------|--------------|--------------|--------------|------------------|
| PharmaCoNER  | **0.8907** | 0.8754       | 0.8537 | 0.8594 | 0.8671 | 0.8545 | 0.8474     |
| CANTEMIST    | **0.8220**  | 0.8078 | 0.8153 | 0.8168 | 0.8116 | 0.8070  | 0.7875     |
| ICTUSnet     | **0.8727**  | 0.8716       | 0.8498 | 0.8509 | 0.8631 | 0.8521 | 0.8677 |

The fine-tuning scripts can be found in the official GitHub [repository](https://github.com/PlanTL-GOB-ES/lm-biomedical-clinical-es).


## Additional information

### Author
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

### Contact information
For further information, send an email to <plantl-gob-es@bsc.es>

### Copyright
Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022)

### Licensing information
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Funding
This work was funded by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) within the framework of the Plan-TL.

### Citation information
If you use these models, please cite our work:

```bibtext
@inproceedings{carrino-etal-2022-pretrained,
    title = "Pretrained Biomedical Language Models for Clinical {NLP} in {S}panish",
    author = "Carrino, Casimiro Pio  and
      Llop, Joan  and
      P{\`a}mies, Marc  and
      Guti{\'e}rrez-Fandi{\~n}o, Asier  and
      Armengol-Estap{\'e}, Jordi  and
      Silveira-Ocampo, Joaqu{\'\i}n  and
      Valencia, Alfonso  and
      Gonzalez-Agirre, Aitor  and
      Villegas, Marta",
    booktitle = "Proceedings of the 21st Workshop on Biomedical Language Processing",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.bionlp-1.19",
    doi = "10.18653/v1/2022.bionlp-1.19",
    pages = "193--199",
    abstract = "This work presents the first large-scale biomedical Spanish language models trained from scratch, using large biomedical corpora consisting of a total of 1.1B tokens and an EHR corpus of 95M tokens. We compared them against general-domain and other domain-specific models for Spanish on three clinical NER tasks. As main results, our models are superior across the NER tasks, rendering them more convenient for clinical NLP applications. Furthermore, our findings indicate that when enough data is available, pre-training from scratch is better than continual pre-training when tested on clinical tasks, raising an exciting research question about which approach is optimal. Our models and fine-tuning scripts are publicly available at HuggingFace and GitHub.",
}
```

### Disclaimer

<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner of the models (SEDIA – State Secretariat for Digitalization and Artificial Intelligence) nor the creator (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.

En ningún caso el propietario de los modelos (SEDIA – Secretaría de Estado de Digitalización e Inteligencia Artificial) ni el creador (BSC – Barcelona Supercomputing Center) serán responsables de los resultados derivados del uso que hagan terceros de estos modelos.
</details>

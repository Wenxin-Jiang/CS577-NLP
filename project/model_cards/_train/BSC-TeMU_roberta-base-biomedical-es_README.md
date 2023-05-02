---
language: 
  - es
tags:
- biomedical
- spanish
license: apache-2.0
metrics:
- ppl
widget:
- text: "El único antecedente personal a reseñar era la <mask> arterial."
- text: "Las radiologías óseas de cuerpo entero no detectan alteraciones <mask>, ni alteraciones vertebrales."
- text: "En el <mask> toraco-abdómino-pélvico no se encontraron hallazgos patológicos de interés."
---

**⚠️NOTICE⚠️: THIS MODEL HAS BEEN MOVED TO THE FOLLOWING URL AND WILL SOON BE REMOVED:** https://huggingface.co/PlanTL-GOB-ES/roberta-base-biomedical-es

# Biomedical language model for Spanish
Biomedical pretrained language model for Spanish. For more details about the corpus, the pretraining and the evaluation, check the official [repository](https://github.com/PlanTL-SANIDAD/lm-biomedical-clinical-es) and read our [preprint](https://arxiv.org/abs/2109.03570) "_Carrino, C. P., Armengol-Estapé, J., Gutiérrez-Fandiño, A., Llop-Palao, J., Pàmies, M., Gonzalez-Agirre, A., & Villegas, M. (2021). Biomedical and Clinical Language Models for Spanish: On the Benefits of Domain-Specific Pretraining in a Mid-Resource Scenario._".


## Tokenization and model pretraining

This model is a [RoBERTa-based](https://github.com/pytorch/fairseq/tree/master/examples/roberta) model trained on a
**biomedical** corpus in Spanish collected from several sources (see next section). 
The training corpus has been tokenized using a byte version of [Byte-Pair Encoding (BPE)](https://github.com/openai/gpt-2)
used in the original [RoBERTA](https://github.com/pytorch/fairseq/tree/master/examples/roberta) model with a vocabulary size of 52,000 tokens. The pretraining consists of a masked language model training at the subword level following the approach employed for the RoBERTa base model with the same hyperparameters as in the original work. The training lasted a total of 48 hours with 16 NVIDIA V100 GPUs of 16GB DDRAM, using Adam optimizer with a peak learning rate of 0.0005 and an effective batch size of 2,048 sentences.


## Training corpora and preprocessing

The training corpus is composed of several biomedical corpora in Spanish, collected from publicly available corpora and crawlers.
To obtain a high-quality training corpus, a cleaning pipeline with the following operations has been applied:

- data parsing in different formats
  - sentence splitting
  - language detection
  - filtering of ill-formed sentences 
  - deduplication of repetitive contents
  - keep the original document boundaries

Finally, the corpora are concatenated and further global deduplication among the corpora have been applied.
The result is a medium-size biomedical corpus for Spanish composed of about 963M tokens. The table below shows some basic statistics of the individual cleaned corpora:

    
| Name                                                                                    | No. tokens  | Description                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Medical crawler](https://zenodo.org/record/4561970)                                    | 745,705,946 | Crawler of more than 3,000 URLs belonging to Spanish biomedical and health domains.                                                                                                                                                                                 |
| Clinical cases misc.                                                                    | 102,855,267 | A miscellany of medical content, essentially clinical cases. Note that a clinical case report is a scientific publication where medical practitioners share patient cases and it is different from a clinical note or document.                                                                                                                                                                                 |
| [Scielo](https://github.com/PlanTL-SANIDAD/SciELO-Spain-Crawler)                        | 60,007,289  | Publications written in Spanish crawled from the Spanish SciELO server in 2017.                                                                                                                                       |
| [BARR2_background](https://temu.bsc.es/BARR2/downloads/background_set.raw_text.tar.bz2) | 24,516,442  | Biomedical Abbreviation Recognition and Resolution (BARR2) containing Spanish clinical case study sections from a variety of clinical disciplines.                                                                                       |
| Wikipedia_life_sciences                                                                 | 13,890,501  | Wikipedia articles crawled 04/01/2021 with the [Wikipedia API python library](https://pypi.org/project/Wikipedia-API/) starting from the "Ciencias\_de\_la\_vida" category up to a maximum of 5 subcategories. Multiple links to the same articles are then discarded to avoid repeating content.                                                                                                                                                                    |
| Patents                                                                                 | 13,463,387  | Google Patent in Medical Domain for Spain (Spanish). The accepted codes (Medical Domain) for Json files of patents are: "A61B", "A61C","A61F", "A61H", "A61K", "A61L","A61M", "A61B", "A61P".                                                        |
| [EMEA](http://opus.nlpl.eu/download.php?f=EMEA/v3/moses/en-es.txt.zip)                  | 5,377,448   | Spanish-side documents extracted from parallel corpora made out of PDF documents from the European Medicines Agency.                                                                                                                            |
| [mespen_Medline](https://zenodo.org/record/3562536#.YTt1fH2xXbR)                        | 4,166,077   | Spanish-side articles extracted from a collection of Spanish-English parallel corpus consisting of biomedical scientific literature.  The collection of parallel resources are aggregated from the MedlinePlus source. |
| PubMed                                                                                  | 1,858,966   | Open-access articles from the PubMed repository crawled in 2017.                                                                                                                                              |



## Evaluation and results

The model has been evaluated on the Named Entity Recognition (NER) using the following datasets:

 - [PharmaCoNER](https://zenodo.org/record/4270158): is a track on chemical and drug mention recognition from Spanish medical texts (for more info see: https://temu.bsc.es/pharmaconer/).

 - [CANTEMIST](https://zenodo.org/record/3978041#.YTt5qH2xXbQ): is a shared task specifically focusing on named entity recognition of tumor morphology, in Spanish (for more info see: https://zenodo.org/record/3978041#.YTt5qH2xXbQ). 

 - ICTUSnet: consists of 1,006 hospital discharge reports of patients admitted for stroke from 18 different Spanish hospitals. It contains more than 79,000 annotations for 51 different kinds of variables.

The evaluation results are compared against the [mBERT](https://huggingface.co/bert-base-multilingual-cased) and [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) models:

| F1 - Precision - Recall | roberta-base-biomedical-es | mBERT                   | BETO                    |
|---------------------------|----------------------------|-------------------------------|-------------------------|
| PharmaCoNER               | **89.48** - **87.85** - **91.18**    | 87.46 - 86.50 - 88.46 | 88.18 - 87.12 - 89.28 |
| CANTEMIST                 | **83.87** - **81.70** - **86.17**    | 82.61 - 81.12 - 84.15 | 82.42 - 80.91 - 84.00 |
| ICTUSnet                  | **88.12** - **85.56** - **90.83**    | 86.75 - 83.53 - 90.23 | 85.95 - 83.10 - 89.02 |


## Intended uses & limitations

The model is ready-to-use only for masked language modelling to perform the Fill Mask task (try the inference API or read the next section)

However, the is intended to be fine-tuned on downstream tasks such as Named Entity Recognition or Text Classification.

## Cite
If you use our models, please cite our latest preprint:

```bibtex

@misc{carrino2021biomedical,
      title={Biomedical and Clinical Language Models for Spanish: On the Benefits of Domain-Specific Pretraining in a Mid-Resource Scenario}, 
      author={Casimiro Pio Carrino and Jordi Armengol-Estapé and Asier Gutiérrez-Fandiño and Joan Llop-Palao and Marc Pàmies and Aitor Gonzalez-Agirre and Marta Villegas},
      year={2021},
      eprint={2109.03570},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

```

If you use our Medical Crawler corpus, please cite the preprint:

```bibtex

@misc{carrino2021spanish,
      title={Spanish Biomedical Crawled Corpus: A Large, Diverse Dataset for Spanish Biomedical Language Models}, 
      author={Casimiro Pio Carrino and Jordi Armengol-Estapé and Ona de Gibert Bonet and Asier Gutiérrez-Fandiño and Aitor Gonzalez-Agirre and Martin Krallinger and Marta Villegas},
      year={2021},
      eprint={2109.07765},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

```

---

## How to use

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("BSC-TeMU/roberta-base-biomedical-es")

model = AutoModelForMaskedLM.from_pretrained("BSC-TeMU/roberta-base-biomedical-es")

from transformers import pipeline

unmasker = pipeline('fill-mask', model="BSC-TeMU/roberta-base-biomedical-es")

unmasker("El único antecedente personal a reseñar era la <mask> arterial.")
```
```
# Output
[
  {
    "sequence": " El único antecedente personal a reseñar era la hipertensión arterial.",
    "score": 0.9855039715766907,
    "token": 3529,
    "token_str": " hipertensión"
  },
  {
    "sequence": " El único antecedente personal a reseñar era la diabetes arterial.",
    "score": 0.0039140828885138035,
    "token": 1945,
    "token_str": " diabetes"
  },
  {
    "sequence": " El único antecedente personal a reseñar era la hipotensión arterial.",
    "score": 0.002484665485098958,
    "token": 11483,
    "token_str": " hipotensión"
  },
  {
    "sequence": " El único antecedente personal a reseñar era la Hipertensión arterial.",
    "score": 0.0023484621196985245,
    "token": 12238,
    "token_str": " Hipertensión"
  },
  {
    "sequence": " El único antecedente personal a reseñar era la presión arterial.",
    "score": 0.0008009297889657319,
    "token": 2267,
    "token_str": " presión"
  }
]
```
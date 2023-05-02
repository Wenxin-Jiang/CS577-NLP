---
language:
- es
license: apache-2.0
tags:
- "national library of spain"
- "spanish"
- "bne"
datasets:
- "bne"  
metrics:
- "ppl"
widget:
- text: "Este año las campanadas de La Sexta las presentará <mask>." 
- text: "David Broncano es un presentador de La <mask>."
- text: "Gracias a los datos de la BNE se ha podido <mask> este modelo del lenguaje."
- text: "Hay base legal dentro del marco <mask> actual."

---

**⚠️NOTICE⚠️: THIS MODEL HAS BEEN MOVED TO THE FOLLOWING URL AND WILL SOON BE REMOVED:** https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne

# RoBERTa base trained with data from National Library of Spain (BNE)

## Model Description
RoBERTa-base-bne is a transformer-based masked language model for the Spanish language. It is based on the [RoBERTa](https://arxiv.org/abs/1907.11692) base model and has been pre-trained using the largest Spanish corpus known to date, with a total of 570GB of clean and deduplicated text processed for this work, compiled from the web crawlings performed by the  [National Library of Spain (Biblioteca Nacional de España)](http://www.bne.es/en/Inicio/index.html) from 2009 to 2019.

## Training corpora and preprocessing 
The [National Library of Spain (Biblioteca Nacional de España)](http://www.bne.es/en/Inicio/index.html) crawls all .es domains once a year. The training corpus consists of 59TB of WARC files from these crawls, carried out from 2009 to 2019.

To obtain a high-quality training corpus, the corpus has been preprocessed with a pipeline of operations, including among the others, sentence splitting, language detection, filtering of bad-formed sentences and deduplication of repetitive contents. During the process document boundaries are kept. This resulted into 2TB of Spanish clean corpus. Further global deduplication among the corpus is applied, resulting into 570GB of text.

Some of the statistics of the corpus:

| Corpora | Number of documents | Number of tokens | Size (GB) |
|---------|---------------------|------------------|-----------|
| BNE     |         201,080,084 |  135,733,450,668 |     570GB |

## Tokenization and pre-training 
The training corpus has been tokenized using a byte version of Byte-Pair Encoding (BPE) used in the original [RoBERTA](https://arxiv.org/abs/1907.11692) model with a vocabulary size of 50,262 tokens. The RoBERTa-base-bne pre-training consists of a masked language model training that follows the approach employed for the RoBERTa base. The training lasted a total of 48 hours with 16 computing nodes each one with 4 NVIDIA V100 GPUs of 16GB VRAM.

## Evaluation and results
For evaluation details visit our [GitHub repository](https://github.com/PlanTL-SANIDAD/lm-spanish).

## Citing 
Check out our paper for all the details: https://arxiv.org/abs/2107.07253

```
@misc{gutierrezfandino2021spanish,
      title={Spanish Language Models}, 
      author={Asier Gutiérrez-Fandiño and Jordi Armengol-Estapé and Marc Pàmies and Joan Llop-Palao and Joaquín Silveira-Ocampo and Casimiro Pio Carrino and Aitor Gonzalez-Agirre and Carme Armentano-Oller and Carlos Rodriguez-Penagos and Marta Villegas},
      year={2021},
      eprint={2107.07253},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
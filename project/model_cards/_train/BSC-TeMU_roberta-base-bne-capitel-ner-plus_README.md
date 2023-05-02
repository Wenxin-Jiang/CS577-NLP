---
language:
- es
license: apache-2.0
tags:
- "national library of spain"
- "spanish"
- "bne"
- "capitel"
- "ner"
datasets:
- "bne"
- "capitel"  
metrics:
- "f1"
inference:
  parameters:
    aggregation_strategy: "first"

---

**⚠️NOTICE⚠️: THIS MODEL HAS BEEN MOVED TO THE FOLLOWING URL AND WILL SOON BE REMOVED:** https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne-capitel-ner-plus

# Spanish RoBERTa-base trained on BNE finetuned for CAPITEL Named Entity Recognition (NER) dataset.
RoBERTa-base-bne is a transformer-based masked language model for the Spanish language. It is based on the [RoBERTa](https://arxiv.org/abs/1907.11692) base model and has been pre-trained using the largest Spanish corpus known to date, with a total of 570GB of clean and deduplicated text processed for this work, compiled from the web crawlings performed by the  [National Library of Spain (Biblioteca Nacional de España)](http://www.bne.es/en/Inicio/index.html) from 2009 to 2019.

Original pre-trained model can be found here: https://huggingface.co/BSC-TeMU/roberta-base-bne

## Dataset
The dataset used is the one from the [CAPITEL competition at IberLEF 2020](https://sites.google.com/view/capitel2020) (sub-task 1).

**IMPORTANT ABOUT THIS MODEL:** We modified the dataset to make this model more robust to general Spanish input. In the Spanish language all the name entities are capitalized, as this dataset has been elaborated by experts, it is totally correct in terms of Spanish language. We randomly took some entities and we lower-cased some of them for the model to learn not only that the named entities are capitalized, but also the structure of a sentence that should contain a named entity. For instance: "My name is [placeholder]", this [placeholder] should be a named entity even though it is not written capitalized. The model trained on the original capitel dataset can be found here: https://huggingface.co/BSC-TeMU/roberta-base-bne-capitel-ner

Examples:

This model:
- "Me llamo asier y vivo en barcelona todo el año." → "Me llamo {as:S-PER}{ier:S-PER} y vivo en {barcelona:S-LOC} todo el año."
- "Hoy voy a visitar el parc güell tras salir del barcelona supercomputing center." → "Hoy voy a visitar el {par:B-LOC}{k:I-LOC} {gü:E-LOC}{ell:E-LOC} tras salir del {barcelona:B-ORG} {super:I-ORG}{com:I-ORG}{pu:I-ORG}{ting:I-ORG} {cen:E-ORG}{ter:E-ORG}."

Model trained on original data:
- "Me llamo asier y vivo en barcelona todo el año." → "Me llamo asier y vivo en barcelona todo el año." (nothing)
- "Hoy voy a visitar el parc güell tras salir del barcelona supercomputing center." → "Hoy voy a visitar el parc güell tras salir del barcelona supercomputing center." (nothing)

## Evaluation and results
F1 Score: 0.8867

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
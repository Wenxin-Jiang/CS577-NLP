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

---

**⚠️NOTICE⚠️: THIS MODEL HAS BEEN MOVED TO THE FOLLOWING URL AND WILL SOON BE REMOVED:** https://huggingface.co/PlanTL-GOB-ES/roberta-large-bne-capitel-ner

# Spanish RoBERTa-large trained on BNE finetuned for CAPITEL Named Entity Recognition (NER) dataset.
RoBERTa-large-bne is a transformer-based masked language model for the Spanish language. It is based on the [RoBERTa](https://arxiv.org/abs/1907.11692) large model and has been pre-trained using the largest Spanish corpus known to date, with a total of 570GB of clean and deduplicated text processed for this work, compiled from the web crawlings performed by the  [National Library of Spain (Biblioteca Nacional de España)](http://www.bne.es/en/Inicio/index.html) from 2009 to 2019.

Original pre-trained model can be found here: https://huggingface.co/BSC-TeMU/roberta-large-bne

## Dataset
The dataset used is the one from the [CAPITEL competition at IberLEF 2020](https://sites.google.com/view/capitel2020) (sub-task 1).

## Evaluation and results
F1 Score: 0.8998

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
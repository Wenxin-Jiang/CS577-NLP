---
language:
- es
license: apache-2.0
tags:
- legal
- spanish
datasets:
- legal_ES
- temu_legal  
metrics:
- ppl
widget:
- text: "La ley fue <mask> finalmente." 
- text: "El Tribunal <mask> desestimó el recurso de amparo."
- text: "Hay base legal dentro del marco <mask> actual."

---

**⚠️NOTICE⚠️: THIS MODEL HAS BEEN MOVED TO THE FOLLOWING URL AND WILL SOON BE REMOVED:** https://huggingface.co/PlanTL-GOB-ES/RoBERTalex

# Spanish Legal-domain RoBERTa

There are few models trained for the Spanish language. Some of the models have been trained with a low resource, unclean corpora. The ones derived from the Spanish National Plan for Language Technologies are proficient solving several tasks and have been trained using large scale clean corpora. However, the Spanish Legal domain language could be think of an independent language on its own. We therefore created a Spanish Legal model from scratch trained exclusively on legal corpora.

## Citing 
```
@misc{gutierrezfandino2021legal,
      title={Spanish Legalese Language Model and Corpora}, 
      author={Asier Gutiérrez-Fandiño and Jordi Armengol-Estapé and Aitor Gonzalez-Agirre and Marta Villegas},
      year={2021},
      eprint={2110.12201},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

For more information visit our [GitHub repository](https://github.com/PlanTL-GOB-ES/lm-legal-es)

## Funding
This work was funded by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) within the framework of the Plan-TL.
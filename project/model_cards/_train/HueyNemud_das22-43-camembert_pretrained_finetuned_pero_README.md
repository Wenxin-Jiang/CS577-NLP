---
tags:
- generated_from_trainer
model-index:
- name: CamemBERT pretrained on french trade directories from the XIXth century
  results: []
---

# CamemBERT trained and fine-tuned for NER on french trade directories from the XIXth century [PERO-OCR training set]

This mdoel is part of the material of the paper
> Abadie, N., Carlinet, E., Chazalon, J., Duménieu, B. (2022). A
> Benchmark of Named Entity Recognition Approaches in Historical
> Documents Application to 19𝑡ℎ Century French Directories. In: Uchida,
> S., Barney, E., Eglin, V. (eds) Document Analysis Systems. DAS 2022.
> Lecture Notes in Computer Science, vol 13237. Springer, Cham.
> https://doi.org/10.1007/978-3-031-06555-2_30

The source code to train this model is available on the  [GitHub repository](https://github.com/soduco/paper-ner-bench-das22) of the paper as a Jupyter notebook in  `src/ner/40_experiment_2.ipynb`.


## Model description
This model adapts the model [Jean-Baptiste/camembert-ner](https://huggingface.co/Jean-Baptiste/camembert-ner) for NER on 6004 manually annotated directory entries referred as the "reference dataset" in the paper.

Trade directory entries are short and strongly structured texts that giving the name, activity and location of a person or business, e.g: 
```
Peynaud, R. de la Vieille Bouclerie, 18. Richard, Joullain et comp., (commission- —Phéâtre Français. naire, (entrepôt), au port de la Rapée-
```

## Intended uses & limitations
This model is intended for reproducibility of the NER evaluation published in the DAS2022 paper.
Several derived models trained for NER on trade directories are available on HuggingFace, each trained on a different dataset :
- [das22-10-camembert_pretrained_finetuned_ref](): trained for NER on ~6000 directory entries manually corrected.
- [das22-10-camembert_pretrained_finetuned_pero](): trained for NER on ~6000 directory entries extracted with PERO-OCR.
- [das22-10-camembert_pretrained_finetuned_tess](): trained for NER on ~6000 directory entries extracted with Tesseract.



### Training hyperparameters

### Training results

### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.0
- Tokenizers 0.10.3


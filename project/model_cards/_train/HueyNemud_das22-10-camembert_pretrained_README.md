---
tags:
- generated_from_trainer
model-index:
- name: CamemBERT pretrained on french trade directories from the XIXth century
  results: []
---

# CamemBERT pretrained on french trade directories from the XIXth century

This mdoel is part of the material of the paper
> Abadie, N., Carlinet, E., Chazalon, J., Duménieu, B. (2022). A
> Benchmark of Named Entity Recognition Approaches in Historical
> Documents Application to 19𝑡ℎ Century French Directories. In: Uchida,
> S., Barney, E., Eglin, V. (eds) Document Analysis Systems. DAS 2022.
> Lecture Notes in Computer Science, vol 13237. Springer, Cham.
> https://doi.org/10.1007/978-3-031-06555-2_30

The source code to train this model is available on the  [GitHub repository](https://github.com/soduco/paper-ner-bench-das22) of the paper as a Jupyter notebook in  `src/ner/10-camembert_pretraining.ipynb`.


## Model description
This model pre-train the model [Jean-Baptiste/camembert-ner](https://huggingface.co/Jean-Baptiste/camembert-ner) on a set of ~845k entries from Paris trade directories from the XIXth century extracted with OCR.
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

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 1.9603        | 1.0   | 100346 | 1.8005          |
| 1.7032        | 2.0   | 200692 | 1.6460          |
| 1.5879        | 3.0   | 301038 | 1.5570          |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.0
- Tokenizers 0.10.3


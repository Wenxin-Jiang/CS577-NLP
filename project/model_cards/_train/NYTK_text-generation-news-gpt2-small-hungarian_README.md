---
language:
- hu
tags:
- text-generation
license: mit
widget:
- text: Szeptember végén zárul a balatoni szezon
---

# Hungarian GPT-2 news generator

For further models, scripts and details, see [our repository](https://github.com/nytud/neural-models) or [our demo site](https://juniper.nytud.hu/demo/nlp).

- Pretrained on Hungarian Wikipedia
- Finetuned on hin corpus (hvg.hu, index.hu, nol.hu)


## Results

| Model | Perplexity |
| ------------- | ------------- |
| GPT-2 poem  | 47.46 | 
| **GPT-2 news** | **22.06** | 


## Citation
If you use this model, please cite the following paper:
```
@inproceedings {yang-gpt2,
    title = {{"Az invazív medvék nem tolerálják a suzukis agressziót" - Magyar GPT-2 kísérleti modell}},
	booktitle = {XVIII. Magyar Számítógépes Nyelvészeti Konferencia},
	year = {2022},
	publisher = {Szegedi Tudományegyetem, Informatikai Intézet},
	address = {Szeged, Magyarország},
	author = {Yang, Zijian Győző},
	pages = {463--476}
}

```
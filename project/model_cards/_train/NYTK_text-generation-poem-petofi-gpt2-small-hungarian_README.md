---
language:
- hu
tags:
- text-generation
license: mit
widget:
- text: Szegeden, január végén,
---

# Hungarian GPT-2 poem generator in Petőfi style

For further models, scripts and details, see [our repository](https://github.com/nytud/neural-models) or [our demo site](https://juniper.nytud.hu/demo/nlp).

- Pretrained on Hungarian Wikipedia
- Finetuned on Petőfi Sándor összes költeményei


## Results

| Model | Perplexity |
| ------------- | ------------- |
| **GPT-2 poem**  | **47.46** | 
| GPT-2 news | 22.06 | 


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
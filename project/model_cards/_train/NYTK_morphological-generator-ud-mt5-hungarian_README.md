---
license: apache-2.0
language:
- hu
tags:
- text2text-generation
metrics:
- accuracy
widget:
- text: 'morph: munka NOUN Case=Acc|Number=Sin'
---

# Hungarian morphological generator model with mT5

For further models, scripts and details, see [our demo site](https://juniper.nytud.hu/demo/nlp).

  - Pretrained model used: mT5
  - Prefix: "morph: "
  - UD-based generation
  	
## Limitations

- max_source_length = 64
- max_target_length = 32

## Results

| Model | emMorph | UD |
| ------------- | ------------- | ------------- | 
| mT5 | 95.53 | 94.66 |

## Usage with pipeline

```python
from transformers import pipeline

text2text_generator = pipeline(task="text2text-generation", model="NYTK/morphological-generator-ud-mt5-hungarian")

print(text2text_generator("morph: munka NOUN Case=Acc|Number=Sin")[0]["generated_text"])
```

## Citation
If you use this model, please cite the following paper:

```
@inproceedings {morph-generator,
    title = {Neural Morphological Generators for Hungarian},
	booktitle = {XIX. Magyar Számítógépes Nyelvészeti Konferencia (MSZNY 2023)},
	year = {2023},
	publisher = {Szegedi Tudományegyetem, Informatikai Intézet},
	address = {Szeged, Hungary},
	author = {Laki, László János and Ligeti-Nagy, Noémi and Vadász, Noémi and Yang, Zijian Győző},
	pages = {331--340}
}
```
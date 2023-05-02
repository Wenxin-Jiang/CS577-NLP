---
license: apache-2.0
tags:
- text2text-generation
- reading-comprehension
datasets:
- NYTK/HuRC
widget:
- text: "question: 'Nem ismerek olyan embert, aki <mask> haragudott volna. Életét úgy fejezte be, ahogyan élt: utolsó fellépésére, amely talán egy hónappal ezelőtt lehetett, már nagyon nehezen tudott csak elmenni, de nem mondta le, mert Pécsett egy jótékonysági koncerten játszott beteg gyerekeknek' - mondta Presser Gábor. context: A kedd hajnalban elhunyt Somló Tamásról emlékezett meg zenésztársa, Presser Gábor. Somló Tamás nagyszerű egyénisége, énekhangja és éneklési stílusa egészen egyedülálló volt' – fogalmazott. '1968 lehetett, amikor először találkoztunk, gyakorlatilag váltottuk egymást az Omega együttesben. Tamás akkor indult el az artista pályán, miközben zenélt is. Az Omegában csak néhányszor játszottunk együtt, miután én beléptem, ő éveket töltött külföldön artistaként, aztán összefutottunk az LGT-ben, ennek már 43 éve' - idézte fel Presser Gábor. Somló Tamás színpadi jelenléte nagy húzóerőt jelentett a zenekar számára és zenészi képességeit mutatta az is, hogy amikor Frenreisz Károly helyett belépett az LGT-be, néhány hét alatt megtanult basszusgitározni."
  example_title: Somló Tamás
- text: "question: 'Nem ismerek olyan embert, aki Tamásra haragudott volna. Életét úgy fejezte be, ahogyan élt: utolsó fellépésére, amely talán egy hónappal ezelőtt lehetett, már nagyon nehezen tudott csak elmenni, de nem mondta le, mert Pécsett egy jótékonysági koncerten játszott beteg gyerekeknek' - mondta <mask>. context: A kedd hajnalban elhunyt Somló Tamásról emlékezett meg zenésztársa, Presser Gábor. Somló Tamás nagyszerű egyénisége, énekhangja és éneklési stílusa egészen egyedülálló volt' – fogalmazott. '1968 lehetett, amikor először találkoztunk, gyakorlatilag váltottuk egymást az Omega együttesben. Tamás akkor indult el az artista pályán, miközben zenélt is. Az Omegában csak néhányszor játszottunk együtt, miután én beléptem, ő éveket töltött külföldön artistaként, aztán összefutottunk az LGT-ben, ennek már 43 éve' - idézte fel Presser Gábor. Somló Tamás színpadi jelenléte nagy húzóerőt jelentett a zenekar számára és zenészi képességeit mutatta az is, hogy amikor Frenreisz Károly helyett belépett az LGT-be, néhány hét alatt megtanult basszusgitározni."
  example_title: Presser Gábor
language:
- hu
---

# Hungarian Reading Comprehension with finetuned mT5 base model

For further details, see [our demo site](https://juniper.nytud.hu/demo/nlp).

## Results

| Model | Exact Match | F1 |
| ------------- | ------------- | ------------- |
| huBERT | 64.50 | 69.03  |
| mT5 | 69.51 | 76.26 |

## Usage with pipeline

```python
from transformers import pipeline

context = "A kedd hajnalban elhunyt Somló Tamásról emlékezett meg zenésztársa, Presser Gábor. Somló Tamás nagyszerű egyénisége, énekhangja és éneklési stílusa egészen egyedülálló volt' – fogalmazott. '1968 lehetett, amikor először találkoztunk, gyakorlatilag váltottuk egymást az Omega együttesben. Tamás akkor indult el az artista pályán, miközben zenélt is. Az Omegában csak néhányszor játszottunk együtt, miután én beléptem, ő éveket töltött külföldön artistaként, aztán összefutottunk az LGT-ben, ennek már 43 éve' - idézte fel Presser Gábor. Somló Tamás színpadi jelenléte nagy húzóerőt jelentett a zenekar számára és zenészi képességeit mutatta az is, hogy amikor Frenreisz Károly helyett belépett az LGT-be, néhány hét alatt megtanult basszusgitározni."
question = "'Nem ismerek olyan embert, aki <mask> haragudott volna. Életét úgy fejezte be, ahogyan élt: utolsó fellépésére, amely talán egy hónappal ezelőtt lehetett, már nagyon nehezen tudott csak elmenni, de nem mondta le, mert Pécsett egy jótékonysági koncerten játszott beteg gyerekeknek' - mondta Presser Gábor."

text2text_generator = pipeline(task="text2text-generation", model="NYTK/reading-comprehension-hurc-mt5-hungarian")

print(text2text_generator(f"question: {question} context: {context}")[0]["generated_text"])
```

## Citation
If you use this model, please cite the following paper:

```
@article {yang-ligeti-rc,
    title = {Building machine reading comprehension model from scratch},
	journal = {Annales Mathematicae et Informaticae},
	year = {2023},
	author = {Yang, Zijian Győző and Ligeti-Nagy, Noémi},
	pages = {accetped}
}

```
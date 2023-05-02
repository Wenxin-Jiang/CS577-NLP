---
language: lt
tags:
- byt5
- Lithuanian
- grammatical error correction
widget:
- text: 'Sveiki pardodu tvarkyngą "Audi" firmos automobylį. Kątik iš Amerikės. Viena savininka prižiurietas ir mylietas Automobylis. Dar turu patobulintą „Mersedes“ su automatinia greičių pavara už 4000 evrų (iš Amerikės). Taippat tvarkingas.'

license: apache-2.0
---
This is *google/byt5-small* transformer model trained on Lithuanian text for ~100 hours.
It was created during the work [**Towards Lithuanian Grammatical Error Correction**](https://link.springer.com/chapter/10.1007/978-3-031-09076-9_44), which was presented at [11th Computer Science On-line Conference 2022](https://csoc.openpublish.eu/).

The model is yet in its infancy (we are planning to train 100x longer in the future). Nevertheless, it clearly shows the possibilities and capabilities.

## Usage
Given the following corrupted text obtained from [https://www.diktantas.lt/pasitikrink-lietuviu-kalbos-zinias]:
```
text = 'Sveiki pardodu tvarkyngą "Audi" firmos automobylį. Kątik iš Amerikės. Viena savininka prižiurietas ir mylietas Automobylis. Dar turu patobulintą „Mersedes“ su automatinia greičių pavara už 4000 evrų (iš Amerikės). Taippat tvarkingas.'
```
The correction can be obtained by:
```python
from transformers import pipeline
name= "LukasStankevicius/ByT5-Lithuanian-gec-100h"
my_pipeline = pipeline(task="text2text-generation", model=name, framework="pt")
corrected_text = my_pipeline(text)[0]["generated_text"]
print(corrected_text)
```
Output from the above would be:

Sveiki parduodu tvarkingą „Audi“ firmos automobilį. Ką tik iš Amerikės. Viena savininkas prižiūrintas ir mylimas automobilis. Dar turiu patobulintą „Mersedes“ su automatine greičių pavara už 4000 eurų (iš Amerikės). Taip pat tvarkingas.

More information can be found in the accompanying [GitHub repository](https://github.com/LukasStankevicius/Towards-Lithuanian-Grammatical-Error-Correction)

If you find our work useful, please cite the following paper:

``` latex
@InProceedings{10.1007/978-3-031-09076-9_44,
author="Stankevi{\v{c}}ius, Lukas
and Luko{\v{s}}evi{\v{c}}ius, Mantas",
editor="Silhavy, Radek",
title="Towards Lithuanian Grammatical Error Correction",
booktitle="Artificial Intelligence Trends in Systems",
year="2022",
publisher="Springer International Publishing",
address="Cham",
pages="490--503",
abstract="Everyone wants to write beautiful and correct text, yet the lack of language skills, experience, or hasty typing can result in errors. By employing the recent advances in transformer architectures, we construct a grammatical error correction model for Lithuanian, the language rich in archaic features. We compare subword and byte-level approaches and share our best trained model, achieving F{\$}{\$}{\_}{\{}0.5{\}}=0.92{\$}{\$}0.5=0.92, and accompanying code, in an online open-source repository.",
isbn="978-3-031-09076-9"
}
```
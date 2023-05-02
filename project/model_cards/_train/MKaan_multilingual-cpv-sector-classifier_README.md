---
license: apache-2.0
tags:
- eu
- public procurement
- cpv
- sector
- multilingual
- transformers
- text-classification
widget:
- text: "Oppegård municipality, hereafter called the contracting authority, intends to enter into a framework agreement with one supplier for the procurement of fresh bread and bakery products for Oppegård municipality.  The contract is estimated to NOK 1 400 000 per annum excluding VAT  The total for the entire period including options is NOK 5 600 000 excluding VAT"
---

# multilingual-cpv-sector-classifier
This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on [the Tenders Economic Daily Public Procurement Data](https://simap.ted.europa.eu/en).
It achieves the following results on the evaluation set:
- F1 Score: 0.686

## Model description
The model takes procurement descriptions written in any of [104 languages](https://github.com/google-research/bert/blob/master/multilingual.md#list-of-languages) and classifies them into 45 sector classes represented by [CPV(Common Procurement Vocabulary)](https://simap.ted.europa.eu/en_GB/web/simap/cpv) code descriptions as listed below.

 | Common Procurement Vocabulary |
 |:-----------------------------|
 | Administration, defence and social security services. 👮‍♀️ |
 | Agricultural machinery. 🚜 |
 | Agricultural, farming, fishing, forestry and related products. 🌾 |
 | Agricultural, forestry, horticultural, aquacultural and apicultural services. 👨🏿‍🌾 |
 | Architectural, construction, engineering and inspection services. 👷‍♂️ |
 | Business services: law, marketing, consulting, recruitment, printing and security. 👩‍💼 |
 | Chemical products. 🧪 |
 | Clothing, footwear, luggage articles and accessories. 👖 |
 | Collected and purified water. 🌊 |
 | Construction structures and materials; auxiliary products to construction (excepts electric apparatus). 🧱 |
 | Construction work. 🏗️ |
 | Education and training services. 👩🏿‍🏫 |
 | Electrical machinery, apparatus, equipment and consumables; Lighting. ⚡ |
 | Financial and insurance services. 👨‍💼 |
 | Food, beverages, tobacco and related products. 🍽️ |
 | Furniture (incl. office furniture), furnishings, domestic appliances (excl. lighting) and cleaning products. 🗄️ |
 | Health and social work services. 👨🏽‍⚕️ |
 | Hotel, restaurant and retail trade services. 🏨 |
 | IT services: consulting, software development, Internet and support. 🖥️ |
 | Industrial machinery. 🏭 |
 | Installation services (except software). 🛠️ |
 | Laboratory, optical and precision equipments (excl. glasses). 🔬 |
 | Leather and textile fabrics, plastic and rubber materials. 🧵 |
 | Machinery for mining, quarrying, construction equipment. ⛏️ |
 | Medical equipments, pharmaceuticals and personal care products. 💉 |
 | Mining, basic metals and related products. ⚙️ |
 | Musical instruments, sport goods, games, toys, handicraft, art materials and accessories. 🎸 |
 | Office and computing machinery, equipment and supplies except furniture and software packages. 🖨️ |
 | Other community, social and personal services. 🧑🏽‍🤝‍🧑🏽 |
 | Petroleum products, fuel, electricity and other sources of energy. 🔋 |
 | Postal and telecommunications services. 📶 |
 | Printed matter and related products. 📰 |
 | Public utilities. ⛲ |
 | Radio, television, communication, telecommunication and related equipment. 📡 |
 | Real estate services. 🏠 |
 | Recreational, cultural and sporting services. 🚴 |
 | Repair and maintenance services. 🔧 |
 | Research and development services and related consultancy services. 👩‍🔬 |
 | Security, fire-fighting, police and defence equipment. 🧯 |
 | Services related to the oil and gas industry. ⛽ |
 | Sewage-, refuse-, cleaning-, and environmental services. 🧹 |
 | Software package and information systems. 🔣 |
 | Supporting and auxiliary transport services; travel agencies services. 🚃 |
 | Transport equipment and auxiliary products to transportation. 🚌 |
 | Transport services (excl. Waste transport). 💺

## Intended uses & limitations
- Input description should be written in any of [the 104 languages](https://github.com/google-research/bert/blob/master/multilingual.md#list-of-languages) that MBERT supports.
- The model is just evaluated in 22 languages. Thus there is no information about the performances in other languages.
- The domain is also restricted by the awarded procurement notice descriptions in European Union. Evaluating on whole document texts might change the performance.

## Training and evaluation data
- The whole data consists of 744,360 rows. Shuffled and split into train and validation sets by using 80%/20% manner.
- Each description represents a unique contract notice description awarded between 2011 and 2018.
- Both training and validation data have contract notice descriptions written in 22 European Languages. (Malta and Irish are extracted due to scarcity compared to whole data)

## Training procedure
The training procedure has been completed on Google Cloud V3-8 TPUs. Thanks [Google](https://sites.research.google/trc/about/) for giving the access to Cloud TPUs

### Training hyperparameters
The following hyperparameters were used during training:
- learning_rate: 2e-05
- num_epochs: 3
- gradient_accumulation_steps: 8
- batch_size_per_device: 4
- total_train_batch_size: 32

### Training results
| Epoch |  Step  | F1 Score|
|:-----:|:------:|:------:|
| 1   | 18,609 | 0.630    |
| 2   | 37,218 | 0.674    |
| 3   | 55,827 | 0.686    |

| Language| F1 Score| Test Size|
|:-----:|:-----:|:-----:|
| PL| 0.759| 13950|
| RO| 0.736| 3522|
| SK| 0.719| 1122|
| LT| 0.687| 2424|
| HU| 0.681| 1879|
| BG| 0.675| 2459|
| CS| 0.668| 2694|
| LV| 0.664| 836|
| DE| 0.645| 35354|
| FI| 0.644| 1898|
| ES| 0.643| 7483|
| PT| 0.631| 874|
| EN| 0.631| 16615|
| HR| 0.626| 865|
| IT| 0.626| 8035|
| NL| 0.624| 5640|
| EL| 0.623| 1724|
| SL| 0.615| 482|
| SV| 0.607| 3326|
| DA| 0.603| 1925|
| FR| 0.601| 33113|
| ET| 0.572| 458||
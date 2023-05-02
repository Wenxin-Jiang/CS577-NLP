---
license: mit
tag: text-classification
widget:
- text: "Inde dit salt du dun degelikes bit innechlicheme herzen so hilfet did dat vuizes uuerliche du salt lesen di paternoster inde euuangleno miner vroaen scene marie"
- text: "Mihály zágrábi püspök előtt Vaguth (dict.) László c. a püspöki várnépek (castrenses) Csázma comitatus-beli volt földjének egy részét, amelyet szolgálataiért predialis jogon tőle kapott, 1 szőlővel együtt (a Zuynar föld azon része kivételével, amelyet a püspök László c.-től elvett és a megvakított Kokosnak adományozott"
- text: "Rath und Gemeinde der Stadt Wismar beschweren sich über die von den Hauptleuten, Beamten und Vasallen des Grafen Johann von Holstein und Stormarn ihren Bürgern seit Jahren zugefügten Unbilden, indem sie ein Verzeichniss der erlittenen einzelnen Verluste beibringen."
- text: "Diplomă de înnobilare emisă de împăratul romano-german Rudolf al II-lea de Habsburg la în favoarea familiei Szőke de Galgóc. Aussteller: Rudolf al II-lea de Habsburg, împărat romano-german Empfänger: Szőke de Galgóc, familie"
- text: "бѣ жє болѧ єтєръ лазаръ отъ виѳаньѧ градьца марьина и марѳꙑ сєстрꙑ єѧ | бѣ жє марьꙗ помазавъшиꙗ господа мѵромъ и отьръши ноѕѣ єго власꙑ своими єѧжє братъ лазаръ болѣашє"
- text: "μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος οὐλομένην, ἣ μυρί᾽ Ἀχαιοῖς ἄλγε᾽ ἔθηκε, πολλὰς δ᾽ ἰφθίμους ψυχὰς Ἄϊδι προΐαψεν ἡρώων, αὐτοὺς δὲ ἑλώρια τεῦχε κύνεσσιν οἰωνοῖσί"
---

#  XLM-RoBERTa (base) language-detection model (modern and medieval)

This model is a fine-tuned version of xlm-roberta-base on the [monasterium.net](https://www.icar-us.eu/en/cooperation/online-portals/monasterium-net/) dataset.

## Model description
On the top of this XLM-RoBERTa transformer model is a classification head. Please refer this model together with to the [XLM-RoBERTa (base-sized model)](https://huggingface.co/xlm-roberta-base) card or the paper [Unsupervised Cross-lingual Representation Learning at Scale by Conneau et al.](https://arxiv.org/abs/1911.02116) for additional information.

## Intended uses & limitations
You can directly use this model as a language detector, i.e. for sequence classification tasks. Currently, it supports the following 41 languages, modern and medieval:

Modern: Bulgarian (bg), Croatian (hr), Czech (cs), Danish (da), Dutch (nl), English (en), Estonian (et), Finnish (fi), French (fr), German (de), Greek (el), Hungarian (hu), Irish (ga), Italian (it), Latvian (lv), Lithuanian (lt), Maltese (mt), Polish (pl), Portuguese (pt), Romanian (ro), Slovak (sk), Slovenian (sl), Spanish (es), Swedish (sv),  Russian (ru), Turkish (tr), Basque (eu), Catalan (ca), Albanian (sq), Serbian (se), Ukrainian (uk), Norwegian (no), Arabic (ar), Chinese (zh), Hebrew (he)

Medieval: Middle High German (mhd), Latin (la), Middle Low German (gml), Old French (fro), Old Church Slavonic (chu), Early New High German (fnhd), Ancient and Medieval Greek (grc)

## Training and evaluation data
The model was fine-tuned using the Monasterium and Wikipedia datasets, which consist of text sequences in 41 languages. The training set contains 80k samples, while the validation and test sets contain 16k. The average accuracy on the test set is 99.59% (this matches the average macro/weighted F1-score, the test set being perfectly balanced).

## Training procedure
Fine-tuning was done via the Trainer API with WeightedLossTrainer.

## Training hyperparameters
The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 20
- eval_batch_size: 20
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

mixed_precision_training: Native AMP

## Training results

| Training Loss     | Validation Loss      | F1   
| ------------- | ------------- | --------    |
| 0.000300        | 0.048985         | 0.991585   |
| 0.000100         | 0.033340         | 0.994663   |
| 0.000000         | 0.032938         | 0.995979   |


## Using example

```
#Install packages
!pip install transformers --quiet

#Import libraries
import torch
from transformers import pipeline

#Define pipeline
classificator = pipeline("text-classification", model="ERCDiDip/langdetect")

#Use pipeline
classificator("clemens etc dilecto filio scolastico ecclesie wetflari ensi treveren dioc salutem etc significarunt nobis dilecti filii commendator et fratres hospitalis beate marie theotonicorum")
```

## Updates
- 25th November 2022: Adding Ancient and Medieval Greek (grc)

## Framework versions
- Transformers 4.24.0
- Pytorch 1.13.0
- Datasets 2.6.1
- Tokenizers 0.13.3

## Citation
Please cite the following papers when using this model.

```
@misc{ercdidip2022,
  title={langdetect (Revision 0215f72)},
  author={Kovács, Tamás, Atzenhofer-Baumgartner, Florian, Aoun, Sandy, Nicolaou, Anguelos, Luger, Daniel, Decker, Franziska, Lamminger, Florian and Vogeler, Georg},
  year         = { 2022 },
  url          = { https://huggingface.co/ERCDiDip/40_langdetect_v01 },
  doi          = { 10.57967/hf/0135 },
  publisher    = { Hugging Face }
}
```

This model is part of the [From Digital to Distant Diplomatics (DiDip) ERC project](https://cordis.europa.eu/project/id/101019327) funded by the European Research Council.
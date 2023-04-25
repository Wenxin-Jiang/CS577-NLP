---
tags:
- Transformers
- text-classification
- multi-class-classification
languages:
- af-ZA
- am-ET
- ar-SA
- az-AZ
- bn-BD
- cy-GB
- da-DK
- de-DE
- el-GR
- en-US
- es-ES
- fa-IR
- fi-FI
- fr-FR
- he-IL
- hi-IN
- hu-HU
- hy-AM
- id-ID
- is-IS
- it-IT
- ja-JP
- jv-ID
- ka-GE
- km-KH
- kn-IN
- ko-KR
- lv-LV
- ml-IN
- mn-MN
- ms-MY
- my-MM
- nb-NO
- nl-NL
- pl-PL
- pt-PT
- ro-RO
- ru-RU
- sl-SL
- sq-AL
- sv-SE
- sw-KE
- ta-IN
- te-IN
- th-TH
- tl-PH
- tr-TR
- ur-PK
- vi-VN
- zh-CN
- zh-TW
multilinguality:
- af-ZA
- am-ET
- ar-SA
- az-AZ
- bn-BD
- cy-GB
- da-DK
- de-DE
- el-GR
- en-US
- es-ES
- fa-IR
- fi-FI
- fr-FR
- he-IL
- hi-IN
- hu-HU
- hy-AM
- id-ID
- is-IS
- it-IT
- ja-JP
- jv-ID
- ka-GE
- km-KH
- kn-IN
- ko-KR
- lv-LV
- ml-IN
- mn-MN
- ms-MY
- my-MM
- nb-NO
- nl-NL
- pl-PL
- pt-PT
- ro-RO
- ru-RU
- sl-SL
- sq-AL
- sv-SE
- sw-KE
- ta-IN
- te-IN
- th-TH
- tl-PH
- tr-TR
- ur-PK
- vi-VN
- zh-CN
- zh-TW
datasets:
- qanastek/MASSIVE
widget:
- text: "wake me up at five am this week"
- text: "je veux écouter la chanson de jacques brel encore une fois"
- text: "quiero escuchar la canción de arijit singh una vez más"
- text: "olly onde é que á um parque por perto onde eu possa correr"
- text: "פרק הבא בפודקאסט בבקשה"
- text: "亚马逊股价"
- text: "найди билет на поезд в санкт-петербург"
license: cc-by-4.0
---

**People Involved**

* [LABRAK Yanis](https://www.linkedin.com/in/yanis-labrak-8a7412145/) (1)

**Affiliations**

1. [LIA, NLP team](https://lia.univ-avignon.fr/), Avignon University, Avignon, France.

## Model

XLM-Roberta : [https://huggingface.co/xlm-roberta-base](https://huggingface.co/xlm-roberta-base)

Paper : [Unsupervised Cross-lingual Representation Learning at Scale](https://arxiv.org/pdf/1911.02116.pdf)

## Demo: How to use in HuggingFace Transformers Pipeline

Requires [transformers](https://pypi.org/project/transformers/): ```pip install transformers```

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
model_name = 'qanastek/51-languages-classifier'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = TextClassificationPipeline(model=model, tokenizer=tokenizer)
res = classifier("פרק הבא בפודקאסט בבקשה")
print(res)
```

Outputs:

```python
[{'label': 'he-IL', 'score': 0.9998375177383423}]
```

## Training data

[MASSIVE](https://huggingface.co/datasets/qanastek/MASSIVE) is a parallel dataset of > 1M utterances across 51 languages with annotations for the Natural Language Understanding tasks of intent prediction and slot annotation. Utterances span 60 intents and include 55 slot types. MASSIVE was created by localizing the SLURP dataset, composed of general Intelligent Voice Assistant single-shot interactions.

### Languages

Thee model is capable of distinguish 51 languages :

- `Afrikaans - South Africa (af-ZA)`
- `Amharic - Ethiopia (am-ET)`
- `Arabic - Saudi Arabia (ar-SA)`
- `Azeri - Azerbaijan (az-AZ)`
- `Bengali - Bangladesh (bn-BD)`
- `Chinese - China (zh-CN)`
- `Chinese - Taiwan (zh-TW)`
- `Danish - Denmark (da-DK)`
- `German - Germany (de-DE)`
- `Greek - Greece (el-GR)`
- `English - United States (en-US)`
- `Spanish - Spain (es-ES)`
- `Farsi - Iran (fa-IR)`
- `Finnish - Finland (fi-FI)`
- `French - France (fr-FR)`
- `Hebrew - Israel (he-IL)`
- `Hungarian - Hungary (hu-HU)`
- `Armenian - Armenia (hy-AM)`
- `Indonesian - Indonesia (id-ID)`
- `Icelandic - Iceland (is-IS)`
- `Italian - Italy (it-IT)`
- `Japanese - Japan (ja-JP)`
- `Javanese - Indonesia (jv-ID)`
- `Georgian - Georgia (ka-GE)`
- `Khmer - Cambodia (km-KH)`
- `Korean - Korea (ko-KR)`
- `Latvian - Latvia (lv-LV)`
- `Mongolian - Mongolia (mn-MN)`
- `Malay - Malaysia (ms-MY)`
- `Burmese - Myanmar (my-MM)`
- `Norwegian - Norway (nb-NO)`
- `Dutch - Netherlands (nl-NL)`
- `Polish - Poland (pl-PL)`
- `Portuguese - Portugal (pt-PT)`
- `Romanian - Romania (ro-RO)`
- `Russian - Russia (ru-RU)`
- `Slovanian - Slovania (sl-SL)`
- `Albanian - Albania (sq-AL)`
- `Swedish - Sweden (sv-SE)`
- `Swahili - Kenya (sw-KE)`
- `Hindi - India (hi-IN)`
- `Kannada - India (kn-IN)`
- `Malayalam - India (ml-IN)`
- `Tamil - India (ta-IN)`
- `Telugu - India (te-IN)`
- `Thai - Thailand (th-TH)`
- `Tagalog - Philippines (tl-PH)`
- `Turkish - Turkey (tr-TR)`
- `Urdu - Pakistan (ur-PK)`
- `Vietnamese - Vietnam (vi-VN)`
- `Welsh - United Kingdom (cy-GB)`

## Evaluation results

```plain
              precision    recall  f1-score   support

       af-ZA     0.9821    0.9805    0.9813      2974
       am-ET     1.0000    1.0000    1.0000      2974
       ar-SA     0.9809    0.9822    0.9815      2974
       az-AZ     0.9946    0.9845    0.9895      2974
       bn-BD     0.9997    0.9990    0.9993      2974
       cy-GB     0.9970    0.9929    0.9949      2974
       da-DK     0.9575    0.9617    0.9596      2974
       de-DE     0.9906    0.9909    0.9908      2974
       el-GR     0.9997    0.9973    0.9985      2974
       en-US     0.9712    0.9866    0.9788      2974
       es-ES     0.9825    0.9842    0.9834      2974
       fa-IR     0.9940    0.9973    0.9956      2974
       fi-FI     0.9943    0.9946    0.9945      2974
       fr-FR     0.9963    0.9923    0.9943      2974
       he-IL     1.0000    0.9997    0.9998      2974
       hi-IN     1.0000    0.9980    0.9990      2974
       hu-HU     0.9983    0.9950    0.9966      2974
       hy-AM     1.0000    0.9993    0.9997      2974
       id-ID     0.9319    0.9291    0.9305      2974
       is-IS     0.9966    0.9943    0.9955      2974
       it-IT     0.9698    0.9926    0.9811      2974
       ja-JP     0.9987    0.9963    0.9975      2974
       jv-ID     0.9628    0.9744    0.9686      2974
       ka-GE     0.9993    0.9997    0.9995      2974
       km-KH     0.9867    0.9963    0.9915      2974
       kn-IN     1.0000    0.9993    0.9997      2974
       ko-KR     0.9917    0.9997    0.9956      2974
       lv-LV     0.9990    0.9950    0.9970      2974
       ml-IN     0.9997    0.9997    0.9997      2974
       mn-MN     0.9987    0.9966    0.9976      2974
       ms-MY     0.9359    0.9418    0.9388      2974
       my-MM     1.0000    0.9993    0.9997      2974
       nb-NO     0.9600    0.9533    0.9566      2974
       nl-NL     0.9850    0.9748    0.9799      2974
       pl-PL     0.9946    0.9923    0.9934      2974
       pt-PT     0.9885    0.9798    0.9841      2974
       ro-RO     0.9919    0.9916    0.9918      2974
       ru-RU     0.9976    0.9983    0.9980      2974
       sl-SL     0.9956    0.9939    0.9948      2974
       sq-AL     0.9936    0.9896    0.9916      2974
       sv-SE     0.9902    0.9842    0.9872      2974
       sw-KE     0.9867    0.9953    0.9910      2974
       ta-IN     1.0000    1.0000    1.0000      2974
       te-IN     1.0000    0.9997    0.9998      2974
       th-TH     1.0000    0.9983    0.9992      2974
       tl-PH     0.9929    0.9899    0.9914      2974
       tr-TR     0.9869    0.9872    0.9871      2974
       ur-PK     0.9983    0.9929    0.9956      2974
       vi-VN     0.9993    0.9973    0.9983      2974
       zh-CN     0.9812    0.9832    0.9822      2974
       zh-TW     0.9832    0.9815    0.9823      2974

    accuracy                         0.9889    151674
   macro avg     0.9889    0.9889    0.9889    151674
weighted avg     0.9889    0.9889    0.9889    151674
```

Keywords : language identification ; language identification ; multilingual ; classification
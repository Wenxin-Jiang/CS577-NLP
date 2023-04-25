---
tags:
- Transformers
- Token Classification
- Slot Annotation
- token-classification
- sequence-tagger-model
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

## Demo: How to use in HuggingFace Transformers Pipeline

Requires [transformers](https://pypi.org/project/transformers/): ```pip install transformers```

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, TokenClassificationPipeline

tokenizer = AutoTokenizer.from_pretrained('qanastek/XLMRoberta-Alexa-Intents-NER-NLU')
model = AutoModelForTokenClassification.from_pretrained('qanastek/XLMRoberta-Alexa-Intents-NER-NLU')
predict = TokenClassificationPipeline(model=model, tokenizer=tokenizer)
res = predict("réveille-moi à neuf heures du matin le vendredi")
print(res)
```

Outputs:

![English - Hebrew - Spanish](123.png)

```python
[{'word': '▁neuf', 'score': 0.9911066293716431, 'entity': 'B-time', 'index': 6, 'start': 15, 'end': 19},
{'word': '▁heures', 'score': 0.9200698733329773, 'entity': 'I-time', 'index': 7, 'start': 20, 'end': 26},
{'word': '▁du', 'score': 0.8476170897483826, 'entity': 'I-time', 'index': 8, 'start': 27, 'end': 29},
{'word': '▁matin', 'score': 0.8271021246910095, 'entity': 'I-time', 'index': 9, 'start': 30, 'end': 35},
{'word': '▁vendredi', 'score': 0.9813069701194763, 'entity': 'B-date', 'index': 11, 'start': 39, 'end': 47}]
```

## Training data

[MASSIVE](https://huggingface.co/datasets/qanastek/MASSIVE) is a parallel dataset of > 1M utterances across 51 languages with annotations for the Natural Language Understanding tasks of intent prediction and slot annotation. Utterances span 60 intents and include 55 slot types. MASSIVE was created by localizing the SLURP dataset, composed of general Intelligent Voice Assistant single-shot interactions.

## Named Entities

* O
* currency_name
* personal_info
* app_name
* list_name
* alarm_type
* cooking_type
* time_zone
* media_type
* change_amount
* transport_type
* drink_type
* news_topic
* artist_name
* weather_descriptor
* transport_name
* player_setting
* email_folder
* music_album
* coffee_type
* meal_type
* song_name
* date
* movie_type
* movie_name
* game_name
* business_type
* music_descriptor
* joke_type
* music_genre
* device_type
* house_place
* place_name
* sport_type
* podcast_name
* game_type
* timeofday
* business_name
* time
* definition_word
* audiobook_author
* event_name
* general_frequency
* relation
* color_type
* audiobook_name
* food_type
* person
* transport_agency
* email_address
* podcast_descriptor
* order_type
* ingredient
* transport_descriptor
* playlist_name
* radio_name

## Evaluation results

```plain
                      precision    recall  f1-score   support

                   O     0.9537    0.9498    0.9517   1031927
          alarm_type     0.8214    0.1800    0.2953       511
            app_name     0.3448    0.5318    0.4184       660
         artist_name     0.7143    0.8487    0.7757     11413
    audiobook_author     0.7038    0.2971    0.4178      1232
      audiobook_name     0.7271    0.5381    0.6185      5090
       business_name     0.8301    0.7862    0.8075     15385
       business_type     0.7009    0.6196    0.6577      4600
       change_amount     0.8179    0.9104    0.8617      1663
         coffee_type     0.6147    0.8322    0.7071       876
          color_type     0.6999    0.9176    0.7941      2890
        cooking_type     0.7037    0.5184    0.5970      1003
       currency_name     0.8479    0.9686    0.9042      6501
                date     0.8667    0.9348    0.8995     49866
     definition_word     0.9043    0.8135    0.8565      8333
         device_type     0.8502    0.8825    0.8661     11631
          drink_type     0.0000    0.0000    0.0000       131
       email_address     0.9715    0.9747    0.9731      3986
        email_folder     0.5913    0.9740    0.7359       884
          event_name     0.7659    0.7630    0.7645     38625
           food_type     0.6502    0.8697    0.7441     12353
           game_name     0.8974    0.6275    0.7386      4518
   general_frequency     0.8012    0.8673    0.8329      3173
         house_place     0.9337    0.9168    0.9252      7067
          ingredient     0.5481    0.0491    0.0901      1161
           joke_type     0.8147    0.9101    0.8598      1435
           list_name     0.8411    0.7275    0.7802      8188
           meal_type     0.6072    0.8926    0.7227      2282
          media_type     0.8578    0.8522    0.8550     17751
          movie_name     0.4598    0.1856    0.2645       431
          movie_type     0.2673    0.4341    0.3309       364
         music_album     0.0000    0.0000    0.0000       146
    music_descriptor     0.2906    0.3979    0.3359      1053
         music_genre     0.7999    0.7483    0.7732      5908
          news_topic     0.7052    0.5702    0.6306      9265
          order_type     0.6374    0.8845    0.7409      2614
              person     0.8173    0.9376    0.8733     33708
       personal_info     0.7035    0.7444    0.7234      1976
          place_name     0.8616    0.8228    0.8417     38881
      player_setting     0.6429    0.6212    0.6319      5409
       playlist_name     0.5852    0.5293    0.5559      3671
  podcast_descriptor     0.7486    0.5413    0.6283      4951
        podcast_name     0.6858    0.5675    0.6211      3339
          radio_name     0.8196    0.8013    0.8103      9892
            relation     0.6662    0.8569    0.7496      6477
           song_name     0.5617    0.7527    0.6433      7251
          sport_type     0.0000    0.0000    0.0000         0
                time     0.9032    0.8195    0.8593     35456
           time_zone     0.8368    0.4467    0.5824      2823
           timeofday     0.7931    0.8459    0.8187      6140
    transport_agency     0.7876    0.7764    0.7820      1051
transport_descriptor     0.5738    0.2756    0.3723       254
      transport_name     0.8497    0.5149    0.6412      1010
      transport_type     0.9303    0.8980    0.9139      6363
  weather_descriptor     0.8584    0.7466    0.7986     11702

            accuracy                         0.9092   1455270
           macro avg     0.6940    0.6668    0.6613   1455270
        weighted avg     0.9111    0.9092    0.9086   1455270
```

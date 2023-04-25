---
tags:
- Transformers
- text-classification
- intent-classification
- multi-class-classification
- natural-language-understanding
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
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

model_name = 'qanastek/XLMRoberta-Alexa-Intents-Classification'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = TextClassificationPipeline(model=model, tokenizer=tokenizer)

res = classifier("réveille-moi à neuf heures du matin le vendredi")
print(res)
```

Outputs:

```python
[{'label': 'alarm_set', 'score': 0.9998375177383423}]
```

## Training data

[MASSIVE](https://huggingface.co/datasets/qanastek/MASSIVE) is a parallel dataset of > 1M utterances across 51 languages with annotations for the Natural Language Understanding tasks of intent prediction and slot annotation. Utterances span 60 intents and include 55 slot types. MASSIVE was created by localizing the SLURP dataset, composed of general Intelligent Voice Assistant single-shot interactions.

## Intents

* audio_volume_other
* play_music
* iot_hue_lighton
* general_greet
* calendar_set
* audio_volume_down
* social_query
* audio_volume_mute
* iot_wemo_on
* iot_hue_lightup
* audio_volume_up
* iot_coffee
* takeaway_query
* qa_maths
* play_game
* cooking_query
* iot_hue_lightdim
* iot_wemo_off
* music_settings
* weather_query
* news_query
* alarm_remove
* social_post
* recommendation_events
* transport_taxi
* takeaway_order
* music_query
* calendar_query
* lists_query
* qa_currency
* recommendation_movies
* general_joke
* recommendation_locations
* email_querycontact
* lists_remove
* play_audiobook
* email_addcontact
* lists_createoradd
* play_radio
* qa_stock
* alarm_query
* email_sendemail
* general_quirky
* music_likeness
* cooking_recipe
* email_query
* datetime_query
* transport_traffic
* play_podcasts
* iot_hue_lightchange
* calendar_remove
* transport_query
* transport_ticket
* qa_factoid
* iot_cleaning
* alarm_set
* datetime_convert
* iot_hue_lightoff
* qa_definition
* music_dislikeness

## Evaluation results

```plain
                          precision    recall  f1-score   support

             alarm_query     0.9661    0.9037    0.9338      1734
            alarm_remove     0.9484    0.9608    0.9545      1071
               alarm_set     0.8611    0.9254    0.8921      2091
       audio_volume_down     0.8657    0.9537    0.9075       561
       audio_volume_mute     0.8608    0.9130    0.8861      1632
      audio_volume_other     0.8684    0.5392    0.6653       306
         audio_volume_up     0.7198    0.8446    0.7772       663
          calendar_query     0.7555    0.8229    0.7878      6426
         calendar_remove     0.8688    0.9441    0.9049      3417
            calendar_set     0.9092    0.9014    0.9053     10659
           cooking_query     0.0000    0.0000    0.0000         0
          cooking_recipe     0.9282    0.8592    0.8924      3672
        datetime_convert     0.8144    0.7686    0.7909       765
          datetime_query     0.9152    0.9305    0.9228      4488
        email_addcontact     0.6482    0.8431    0.7330       612
             email_query     0.9629    0.9319    0.9472      6069
      email_querycontact     0.6853    0.8032    0.7396      1326
         email_sendemail     0.9530    0.9381    0.9455      5814
           general_greet     0.1026    0.3922    0.1626        51
            general_joke     0.9305    0.9123    0.9213       969
          general_quirky     0.6984    0.5417    0.6102      8619
            iot_cleaning     0.9590    0.9359    0.9473      1326
              iot_coffee     0.9304    0.9749    0.9521      1836
     iot_hue_lightchange     0.8794    0.9374    0.9075      1836
        iot_hue_lightdim     0.8695    0.8711    0.8703      1071
        iot_hue_lightoff     0.9440    0.9229    0.9334      2193
         iot_hue_lighton     0.4545    0.5882    0.5128       153
         iot_hue_lightup     0.9271    0.8315    0.8767      1377
            iot_wemo_off     0.9615    0.8715    0.9143       918
             iot_wemo_on     0.8455    0.7941    0.8190       510
       lists_createoradd     0.8437    0.8356    0.8396      1989
             lists_query     0.8918    0.8335    0.8617      2601
            lists_remove     0.9536    0.8601    0.9044      2652
       music_dislikeness     0.7725    0.7157    0.7430       204
          music_likeness     0.8570    0.8159    0.8359      1836
             music_query     0.8667    0.8050    0.8347      1785
          music_settings     0.4024    0.3301    0.3627       306
              news_query     0.8343    0.8657    0.8498      6324
          play_audiobook     0.8172    0.8125    0.8149      2091
               play_game     0.8666    0.8403    0.8532      1785
              play_music     0.8683    0.8845    0.8763      8976
           play_podcasts     0.8925    0.9125    0.9024      3213
              play_radio     0.8260    0.8935    0.8585      3672
             qa_currency     0.9459    0.9578    0.9518      1989
           qa_definition     0.8638    0.8552    0.8595      2907
              qa_factoid     0.7959    0.8178    0.8067      7191
                qa_maths     0.8937    0.9302    0.9116      1275
                qa_stock     0.7995    0.9412    0.8646      1326
   recommendation_events     0.7646    0.7702    0.7674      2193
recommendation_locations     0.7489    0.8830    0.8104      1581
   recommendation_movies     0.6907    0.7706    0.7285      1020
             social_post     0.9623    0.9080    0.9344      4131
            social_query     0.8104    0.7914    0.8008      1275
          takeaway_order     0.7697    0.8458    0.8059      1122
          takeaway_query     0.9059    0.8571    0.8808      1785
         transport_query     0.8141    0.7559    0.7839      2601
          transport_taxi     0.9222    0.9403    0.9312      1173
        transport_ticket     0.9259    0.9384    0.9321      1785
       transport_traffic     0.6919    0.9660    0.8063       765
           weather_query     0.9387    0.9492    0.9439      7956

                accuracy                         0.8617    151674
               macro avg     0.8162    0.8273    0.8178    151674
            weighted avg     0.8639    0.8617    0.8613    151674
```

---
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-russian
  results: []
widget:
- src: https://cdn-media.huggingface.co/speech_samples/common_voice_ru_18849022.mp3

---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-russian
#

модель для распознания аудио. результаты модели можно потом прогнать через мою сеть исправления текстов UrukHan/t5-russian-spell

<table border="0">
 <tr>
    <td><b style="font-size:30px">Output wav2vec2</b></td>
    <td><b style="font-size:30px">Output spell correcor</b></td>
 </tr>
 <tr>
    <td>ывсем привет выныканалетоп армии и это двадцать пятый день спец операций на украине ет самый главной новости российские военные ракетами кинжалы калибр уничтожили крупную военную топливную базу украины ракетным ударом по населенному пункту под жетамиром уничтжены более стаукраинских военных в две тысячи двадцать втором году</td>
    <td>Всем привет! Вы в курсе новостей от армии. И это 25 день спецопераций на Украине. Есть самые главные новости. Российские военные ракетами «Кинжалы» и «Кинжалы» калибра уничтожили крупную военную топливную базу Украины. Ракетным ударом по населенному пункту под Жетамиром уничтожены более ста украинских военных в 2022г.</td>
 </tr>
</table>


---
Загрузите аудиофайл в формате wav для распознования. Результат можно откорректировать в другой моей сети. которая исправляет ошибки, расставляет знаки припинания и исправляет цифры. https://huggingface.co/UrukHan/t5-russian-spell

#
---
# Запуск сети     пример в колабе https://colab.research.google.com/drive/1dVZvccYJq02hmEsapWgmuJ-pLdezFnn1?usp=sharing
#
```python
from transformers import AutoModelForCTC, Wav2Vec2Processor
model = AutoModelForCTC.from_pretrained("UrukHan/wav2vec2-russian")
processor = Wav2Vec2Processor.from_pretrained("UrukHan/wav2vec2-russian")
def map_to_result(batch):
  with torch.no_grad():
    input_values = torch.tensor(batch["input_values"]).unsqueeze(0) #, device="cuda"
    logits = model(input_values).logits
  pred_ids = torch.argmax(logits, dim=-1)
  batch = processor.batch_decode(pred_ids)[0]
  return batch
 
 map_to_result()
 ```
 
 #
 ---
 # Тренировка модели с обработкой данных и созданием датасета разобрать можете в колабе:
 # https://colab.research.google.com/drive/1zkCA2PtKxD2acqLr55USh35OomoOwOhm?usp=sharing
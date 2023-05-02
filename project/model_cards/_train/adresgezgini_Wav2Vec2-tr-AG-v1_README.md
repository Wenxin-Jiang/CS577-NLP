```python
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
processor = Wav2Vec2Processor.from_pretrained("adresgezgini/Wav2Vec-tr-AG-v1")
model = Wav2Vec2ForCTC.from_pretrained("adresgezgini/Wav2Vec-tr-AG-v1")
```

Dosyalar bölümünde paylaşılan ses1.mp3[1], ses1.mp3[2] ve ses1.mp3[3] ses dosyaları açık kaynaklı canlı kitap ses kayıtları üzerinden 1 - 1.5 dakika arasında belli bir kısmın alınması ile oluşturulmuştur. Oluşturulan sesler ile model test edilmiş ve WER değerleri kaydedilmiştir.
<div align="center">

|Sesler|WER|   
| :---: |  :---: |      
|SES1.mp3|0,17|
|SES2.mp3|0,31|
|SES3.mp3|0,20|
</div>

[1][Sabahattin Ali - Çaydanlık | YT: Sesli Kitap Dünyası](https://www.youtube.com/watch?v=IHUfOpqw-8s)\
[2][Sabahattin Ali - Ses | YT: Sesli Kitap Dünyası](https://www.youtube.com/watch?v=XzX2wBjncOg)\
[3][Sabahattin Ali - Sıçra Köşk | YT: Sesli Kitap Dünyası](https://www.youtube.com/watch?v=SJwUaq0Nu9c)\
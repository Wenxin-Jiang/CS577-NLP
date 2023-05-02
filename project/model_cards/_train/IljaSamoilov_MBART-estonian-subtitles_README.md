---
language: 
  - et
widget:
- text: "te olete ka noh, noh, päris korralikult ka Rahvusringhäälingu teatud mõttes sellisesse keerulisse olukorda pannud,"
- text: "Et, et, et miks mitte olla siis tasakaalus, ma noh, hüpoteetiliselt viskan selle palli üles,"

---


Model usage:
```
tokenizer = MBart50Tokenizer.from_pretrained("IljaSamoilov/MBART-estonian-subtitles", src_lang="et_EE", tgt_lang="et_EE")
model = MBartForConditionalGeneration.from_pretrained("IljaSamoilov/MBART-estonian-subtitles")
```
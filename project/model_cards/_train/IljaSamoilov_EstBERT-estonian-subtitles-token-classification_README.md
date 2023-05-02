---
language: 
  - et
widget:
- text: "Et, et, et miks mitte olla siis tasakaalus, ma noh, hüpoteetiliselt viskan selle palli üles,"
- text: "te olete ka noh, noh, päris korralikult ka Rahvusringhäälingu teatud mõttes sellisesse keerulisse olukorda pannud,"

---

Importing the model and tokenizer:

```
tokenizer = AutoTokenizer.from_pretrained("IljaSamoilov/EstBERT-estonian-subtitles-token-classification")
model = AutoModelForTokenClassification.from_pretrained("IljaSamoilov/EstBERT-estonian-subtitles-token-classification")
```
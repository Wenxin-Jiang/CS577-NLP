---
language: 
  - et
widget:
- text: "te olete ka noh, noh, päris korralikult ka Rahvusringhäälingu teatud mõttes sellisesse keerulisse olukorda pannud,"
- text: "Et, et, et miks mitte olla siis tasakaalus, ma noh, hüpoteetiliselt viskan selle palli üles,"

---

Dataset must be processed as following:

```

def preprocess_function_with_seconds(ds):

    inputs = ds['generated']
    targets =  ds['subtitle']

    model_inputs = tokenizer(inputs, truncation=True, max_length=128, padding=True, return_tensors="np")
    secs = list(map(lambda x: "{:.1f}".format(x), ds["seconds"]))
    sec_inputs = tokenizer(secs, truncation=True, max_length=128, padding=True, return_tensors="np")

    model_inputs['input_ids'] = np.concatenate((sec_inputs['input_ids'][:,1:2], model_inputs['input_ids']), 1)
    model_inputs['attention_mask'] = np.concatenate((sec_inputs['attention_mask'][:,1:2], model_inputs['attention_mask']), 1)

    with tokenizer.as_target_tokenizer():
        labels = tokenizer(targets, truncation=True, max_length=128, padding=True, return_tensors="np")

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs    
```
    
Importing the model and tokenizer:

```
tokenizer = MBart50Tokenizer.from_pretrained("IljaSamoilov/MBART-estonian-subtitles-with-seconds", src_lang="et_EE", tgt_lang="et_EE")
model = MBartForConditionalGeneration.from_pretrained("IljaSamoilov/MBART-estonian-subtitles-with-seconds")
```
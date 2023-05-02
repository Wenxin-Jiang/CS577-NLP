---
widget:
- text: "christmas is celbrated on decembr 25 evry ear"

---


# Spell checker using T5 base transformer
A simple spell checker built using T5-Base transformer. To use this model 

```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Bhuvana/t5-base-spellchecker")

model = AutoModelForSeq2SeqLM.from_pretrained("Bhuvana/t5-base-spellchecker")


def correct(inputs):
    input_ids = tokenizer.encode(inputs,return_tensors='pt')
    sample_output = model.generate(
        input_ids,
        do_sample=True,
        max_length=50,
        top_p=0.99,
        num_return_sequences=1
    )
    res = tokenizer.decode(sample_output[0], skip_special_tokens=True)
    return res


text = "christmas is celbrated on decembr 25 evry ear"

print(correct(text))

```

This should print the corrected statement
```
christmas is celebrated on december 25 every year
```

You can also type the text under the Hosted inference API and get predictions online. 



---
annotations_creators: []
language:
- ro
language_creators:
- machine-generated
license: 
- apache-2.0
multilinguality:
- monolingual
pretty_name: BlackKakapo/t5-small-paraphrase-ro
size_categories:
- 10K<n<100K
source_datasets:
- original
tags: []
task_categories:
- text2text-generation
task_ids: []
---
# Romanian paraphrase

![v2.0](https://img.shields.io/badge/V.2-17.08.2022-brightgreen)

Fine-tune t5-small-paraphrase-ro model for paraphrase. Since there is no Romanian dataset for paraphrasing, I had to create my own [dataset](https://huggingface.co/datasets/BlackKakapo/paraphrase-ro-v2). The dataset contains ~30k examples.

### How to use

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("BlackKakapo/t5-small-paraphrase-ro-v2")
model = AutoModelForSeq2SeqLM.from_pretrained("BlackKakapo/t5-small-paraphrase-ro-v2")
```

### Or

```python
from transformers import T5ForConditionalGeneration, T5TokenizerFast 

model = T5ForConditionalGeneration.from_pretrained("BlackKakapo/t5-small-paraphrase-ro-v2")
tokenizer = T5TokenizerFast.from_pretrained("BlackKakapo/t5-small-paraphrase-ro-v2")
```

### Generate

```python
text = "Am impresia că fac multe greșeli."

encoding = tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]

beam_outputs = model.generate(
    input_ids=input_ids, 
    attention_mask=attention_masks,
    do_sample=True,
    max_length=256,
    top_k=20,
    top_p=0.9,
    early_stopping=False,
    num_return_sequences=5
)

final_outputs = []

for beam_output in beam_outputs:
    text_para = tokenizer.decode(beam_output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
    
    if text.lower() != text_para.lower() or text not in final_outputs:
        final_outputs.append(text_para)
        

print(final_outputs)      
```
### Output

```out
['Am impresia că fac multe erori.']
```
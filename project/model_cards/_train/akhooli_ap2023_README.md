---
language: "ar"
tags:
- text-generation
datasets:
- APCD
widget:
 - text: "."
 - text: "عيد بأية حال"
 - text: "يا قدس"
 - text: "يا قدس"
 - text: "ألا ليت"
---

# GPT2-Arabic-Poetry-2023

## Model description

Fine-tuned model of Arabic poetry dataset based on aragpt2-medium.

## Intended uses & limitations

#### How to use

Try this [HF Space](https://huggingface.co/spaces/akhooli/poetry).  
From script: 
```
from transformers import pipeline
pipe = pipeline('text-generation', framework='pt', device=-1, model='akhooli/ap2023', tokenizer='akhooli/ap2023')
gen = pipe(prompt, max_length=96, temperature = 0.95,repetition_penalty=1.05,
               num_beams=3, num_return_sequences=2, do_sample = True, 
               top_p = 1.0, top_k = 50, return_full_text=True)[0]["generated_text"]
poetry =""
for line in gen.split('.')[:-1]:
        poetry += line 
print(poetry)
```

#### Limitations and bias

Both the GPT2-small-arabic (trained on Arabic Wikipedia) and this model have several limitations in terms of coverage and training performance. 
Use them as demonstrations or proof of concepts but not as production code.

## Training data

This pretrained model used poems from several eras with a total of around 1.4M lines (1.25M used for training). 
The dataset was trained (fine-tuned) based on the [aragpt2-medium](https://huggingface.co/aubmindlab/aragpt2-medium) transformer model.

## Training procedure

Training was done using HF Trainer using free GPU on Kaggle.

## Eval results 
Final perplexity reached was 52, eval_accuracy = 0.3704, eval_loss = 3.9513

### BibTeX entry and citation info

```bibtex
@inproceedings{Abed Khooli,
  year={2023}
}
```
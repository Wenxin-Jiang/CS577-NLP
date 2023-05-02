---
language: en
widget:
- text: Robert Boyle \\n In the late 17th century, Robert Boyle proved that air is necessary for combustion.
---

# MixQG (base-sized model)

MixQG is a new question generation model pre-trained on a collection of QA datasets with a mix of answer types. It was introduced in the paper [MixQG: Neural Question Generation with Mixed Answer Types](https://arxiv.org/abs/2110.08175) and the associated code is released in [this](https://github.com/salesforce/QGen) repository.

### How to use
Using Huggingface pipeline abstraction:
```
from transformers import pipeline

nlp = pipeline("text2text-generation", model='Salesforce/mixqg-base', tokenizer='Salesforce/mixqg-base')
    
CONTEXT = "In the late 17th century, Robert Boyle proved that air is necessary for combustion."
ANSWER = "Robert Boyle"

def format_inputs(context: str, answer: str):
    return f"{answer} \\n {context}"

text = format_inputs(CONTEXT, ANSWER)

nlp(text)
# should output [{'generated_text': 'Who proved that air is necessary for combustion?'}]
```

Using the pre-trained model directly:
```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained('Salesforce/mixqg-base')
model = AutoModelForSeq2SeqLM.from_pretrained('Salesforce/mixqg-base')

CONTEXT = "In the late 17th century, Robert Boyle proved that air is necessary for combustion."
ANSWER = "Robert Boyle"

def format_inputs(context: str, answer: str):
    return f"{answer} \\n {context}"

text = format_inputs(CONTEXT, ANSWER)

input_ids = tokenizer(text, return_tensors="pt").input_ids
generated_ids = model.generate(input_ids, max_length=32, num_beams=4)
output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
print(output)
# should output "Who proved that air is necessary for combustion?"
```

### Citation
```
@misc{murakhovska2021mixqg,
      title={MixQG: Neural Question Generation with Mixed Answer Types}, 
      author={Lidiya Murakhovs'ka and Chien-Sheng Wu and Tong Niu and Wenhao Liu and Caiming Xiong},
      year={2021},
      eprint={2110.08175},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
---
language: en
tags:
- generative qa
datasets:
- eli5
- stackexchange(pets, cooking, gardening, diy, crafts)
---

Work by [Frederico Vicente](https://huggingface.co/mrvicente) & [Diogo Tavares](https://huggingface.co/d-c-t). We finetuned BART Large for the task of generative question answering. It was trained on eli5, askScience and stackexchange using the following forums: pets, cooking, gardening, diy, crafts. 

Check demo: https://huggingface.co/spaces/unlisboa/bart_qa_assistant

### Usage

```python

from transformers import (
      BartForConditionalGeneration,
      BartTokenizer
)
import torch
import json

def read_json_file_2_dict(filename, store_dir='.'):
    with open(f'{store_dir}/{filename}', 'r', encoding='utf-8') as file:
        return json.load(file)

def get_device():
    # If there's a GPU available...
    if torch.cuda.is_available():
        device = torch.device("cuda")
        n_gpus = torch.cuda.device_count()
        first_gpu = torch.cuda.get_device_name(0)

        print(f'There are {n_gpus} GPU(s) available.')
        print(f'GPU gonna be used: {first_gpu}')
    else:
        print('No GPU available, using the CPU instead.')
        device = torch.device("cpu")
    return device

model_name = 'unlisboa/bart_qa_assistant'
tokenizer = BartTokenizer.from_pretrained(model_name)
device = get_device()
model = BartForConditionalGeneration.from_pretrained(model_name).to(device)
model.eval()
                                                                                                                                                          
model_input = tokenizer(question, truncation=True, padding=True, return_tensors="pt")
generated_answers_encoded = model.generate(input_ids=model_input["input_ids"].to(device),attention_mask=model_input["attention_mask"].to(device),
                                                                                      force_words_ids=None,
                                                                                      min_length=1,
                                                                                      max_length=100,
                                                                                      do_sample=True,
                                                                                      early_stopping=True,
                                                                                      num_beams=4,
                                                                                      temperature=1.0,
                                                                                      top_k=None,
                                                                                      top_p=None,
                                                                                      # eos_token_id=tokenizer.eos_token_id,
                                                                                      no_repeat_ngram_size=2,
                                                                                      num_return_sequences=1,
                                                                                      return_dict_in_generate=True,
                                                                                      output_scores=True)
response = tokenizer.batch_decode(generated_answers_encoded['sequences'], skip_special_tokens=True,clean_up_tokenization_spaces=True)    
print(response)

```

Have fun!
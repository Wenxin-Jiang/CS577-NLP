---
language: he

thumbnail: https://avatars1.githubusercontent.com/u/3617152?norod.jpg
widget:
- text: "עוד בימי קדם"
- text: "תריסר מכשפות סג"
- text:  "\n\nהאיש האחרון בעולם /"
- text: "פעם אחת, לפני שנים רבות"
- text: "הרמיוני הסתירה את"
- text: "לפתע, אור ירוק"

license: mit
---

# hebrew-gpt_neo-xl-poetry

Hebrew poetry text generation model which was fine tuned upon on [hebrew-gpt_neo-xl](https://huggingface.co/Norod78/hebrew-gpt_neo-xl).
## Datasets

An assortment of various Hebrew books, magazines and poetry corpuses

## Training Config

Similar to [this one](https://github.com/Norod/hebrew-gpt_neo/tree/main/hebrew-gpt_neo-xl/configs) <BR>

## Usage

### Google Colab Notebook

Available [here ](https://colab.research.google.com/github/Norod/hebrew-gpt_neo/blob/main/hebrew-gpt_neo-xl/Norod78_hebrew_gpt_neo_xl_Colab.ipynb) <BR>


#### Simple usage sample code

```python

!pip install tokenizers==0.10.3 transformers==4.8.0

from transformers import AutoTokenizer, AutoModelForCausalLM
  
tokenizer = AutoTokenizer.from_pretrained("Norod78/hebrew-gpt_neo-xl-poetry")
model = AutoModelForCausalLM.from_pretrained("Norod78/hebrew-gpt_neo-xl-poetry", pad_token_id=tokenizer.eos_token_id)

prompt_text = "אני אוהב שוקולד ועוגות"
max_len = 512
sample_output_num = 3
seed = 1000

import numpy as np
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
n_gpu = 0 if torch.cuda.is_available()==False else torch.cuda.device_count()

print(f"device: {device}, n_gpu: {n_gpu}")

np.random.seed(seed)
torch.manual_seed(seed)
if n_gpu > 0:
    torch.cuda.manual_seed_all(seed)

model.to(device)

encoded_prompt = tokenizer.encode(
    prompt_text, add_special_tokens=False, return_tensors="pt")

encoded_prompt = encoded_prompt.to(device)

if encoded_prompt.size()[-1] == 0:
        input_ids = None
else:
        input_ids = encoded_prompt

print("input_ids = " + str(input_ids))

if input_ids != None:
  max_len += len(encoded_prompt[0])
  if max_len > 2048:
    max_len = 2048

print("Updated max_len = " + str(max_len))

stop_token = "<|endoftext|>"
new_lines = "\n\n\n"

sample_outputs = model.generate(
    input_ids,
    do_sample=True, 
    max_length=max_len, 
    top_k=50, 
    top_p=0.95, 
    num_return_sequences=sample_output_num
)

print(100 * '-' + "\n\t\tOutput\n" + 100 * '-')
for i, sample_output in enumerate(sample_outputs):

  text = tokenizer.decode(sample_output, skip_special_tokens=True)
  
  # Remove all text after the stop token
  text = text[: text.find(stop_token) if stop_token else None]

  # Remove all text after 3 newlines
  text = text[: text.find(new_lines) if new_lines else None]

  print("\n{}: {}".format(i, text))
  print("\n" + 100 * '-')

```

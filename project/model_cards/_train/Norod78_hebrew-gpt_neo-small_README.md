---
language: he

thumbnail: https://avatars1.githubusercontent.com/u/3617152?norod.jpg
widget:
- text: "עוד בימי קדם"
- text: "קוראים לי דורון ואני מעוניין ל"
- text: "קוראים לי איציק ואני חושב ש"
- text: "החתול שלך מאוד חמוד ו"

license: mit
---

# hebrew-gpt_neo-small

Hebrew text generation model based on [EleutherAI's gpt-neo](https://github.com/EleutherAI/gpt-neo). Each was trained on a TPUv3-8 which was made avilable to me via the [TPU Research Cloud](https://sites.research.google/trc/) Program.

## Datasets

1. An assortment of various Hebrew corpuses - I have made it available [here](https://mega.nz/folder/CodSSA4R#4INvMes-56m_WUi7jQMbJQ)


2. oscar / unshuffled_deduplicated_he - [Homepage](https://oscar-corpus.com) | [Dataset Permalink](https://huggingface.co/datasets/viewer/?dataset=oscar&config=unshuffled_deduplicated_he)

The Open Super-large Crawled ALMAnaCH coRpus is a huge multilingual corpus obtained by language classification and filtering of the Common Crawl corpus using the goclassy architecture.

3. CC100-Hebrew Dataset [Homepage](https://metatext.io/datasets/cc100-hebrew) 

Created by Conneau & Wenzek et al. at 2020, the CC100-Hebrew This dataset is one of the 100 corpora of monolingual data that was processed from the January-December 2018 Commoncrawl snapshots from the CC-Net repository. The size of this corpus is 6.1G., in Hebrew language.

## Training Config

Available [here](https://github.com/Norod/hebrew-gpt_neo/tree/main/hebrew-gpt_neo-small/configs) <BR>

## Usage

### Google Colab Notebook

Available [here ](https://colab.research.google.com/github/Norod/hebrew-gpt_neo/blob/main/hebrew-gpt_neo-small/Norod78_hebrew_gpt_neo_small_Colab.ipynb) <BR>


#### Simple usage sample code

```python

!pip install tokenizers==0.10.2 transformers==4.6.0

from transformers import AutoTokenizer, AutoModelForCausalLM
  
tokenizer = AutoTokenizer.from_pretrained("Norod78/hebrew-gpt_neo-small")
model = AutoModelForCausalLM.from_pretrained("Norod78/hebrew-gpt_neo-small", pad_token_id=tokenizer.eos_token_id)

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

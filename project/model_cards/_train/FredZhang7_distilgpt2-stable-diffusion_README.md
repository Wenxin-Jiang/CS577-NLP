---
license: creativeml-openrail-m
tags:
- stable-diffusion
- prompt-generator
- distilgpt2
datasets:
- FredZhang7/krea-ai-prompts
- Gustavosta/Stable-Diffusion-Prompts
- bartman081523/stable-diffusion-discord-prompts
widget:
- text: "amazing"
- text: "a photo of"
- text: "a sci-fi"
- text: "a portrait of"
- text: "a person standing"
- text: "a boy watching"
---
# DistilGPT2 Stable Diffusion Model Card


<a href="https://huggingface.co/FredZhang7/distilgpt2-stable-diffusion-v2"> <font size="4"> <bold> Version 2 is here! </bold> </font> </a>


DistilGPT2 Stable Diffusion is a text generation model used to generate creative and coherent prompts for text-to-image models, given any text.
This model was finetuned on 2.03 million descriptive stable diffusion prompts from [Stable Diffusion discord](https://huggingface.co/datasets/bartman081523/stable-diffusion-discord-prompts), [Lexica.art](https://huggingface.co/datasets/Gustavosta/Stable-Diffusion-Prompts), and (my hand-picked) [Krea.ai](https://huggingface.co/datasets/FredZhang7/krea-ai-prompts). I filtered the hand-picked prompts based on the output results from Stable Diffusion v1.4.

Compared to other prompt generation models using GPT2, this one runs with 50% faster forwardpropagation and 40% less disk space & RAM.


### PyTorch

```bash
pip install --upgrade transformers
```

```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# load the pretrained tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')
tokenizer.add_special_tokens({'pad_token': '[PAD]'})
tokenizer.max_len = 512

# load the fine-tuned model
model = GPT2LMHeadModel.from_pretrained('FredZhang7/distilgpt2-stable-diffusion')

# generate text using fine-tuned model
from transformers import pipeline
nlp = pipeline('text-generation', model=model, tokenizer=tokenizer)
ins = "a beautiful city"

# generate 10 samples
outs = nlp(ins, max_length=80, num_return_sequences=10)

# print the 10 samples
for i in range(len(outs)):
    outs[i] = str(outs[i]['generated_text']).replace('  ', '')
print('\033[96m' + ins + '\033[0m')
print('\033[93m' + '\n\n'.join(outs) + '\033[0m')
```

Example Output:
![Example Output](./prompt-examples.png)
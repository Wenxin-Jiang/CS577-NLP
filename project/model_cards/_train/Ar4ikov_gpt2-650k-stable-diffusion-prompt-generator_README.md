---
license: mit
datasets:
- Gustavosta/Stable-Diffusion-Prompts
- bartman081523/stable-diffusion-discord-prompts
- Ar4ikov/sd_filtered_2m
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- art
- code
widget:
- text: A Tokio town landscape, sunset, by
- text: A Tokio town landscape, sunset
- text: 1girl, blue eyes, dark hair
- text: An astronaut, holding a wrench in outer space
- text: A fire soul eater demon
- text: A portrait of a beautiful woman
- text: A portret of an artist man, thick beard
---

# Stable Diffusion Prompt Generator

TODO: Complete me next time

## Introcude

...

```python
from transformers import pipeline

pipe = pipeline('text-generation', model_id='Ar4ikov/gpt2-650k-stable-diffusion-prompt-generator')


def get_valid_prompt(text: str) -> str:
  dot_split = text.split('.')[0]
  n_split = text.split('\n')[0]

  return {
    len(dot_split) < len(n_split): dot_split,
    len(n_split) > len(dot_split): n_split,
    len(n_split) == len(dot_split): dot_split   
  }[True]


prompt = 'A Tokio town landscape, sunset, by'

valid_prompt = get_valid_prompt(pipe(prompt, max_length=77)[0]['generated_text'])
print(valid_prompt)
# >>> A Tokio town landscape, sunset, by Greg Rutkowski,Artgerm,trending on Behance,light effect,high detail,3d sculpture,golden ratio,dramatic,dramatic background,digital art
```
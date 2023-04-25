---
language: zh
license: creativeml-openrail-m

tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- multilingual
- English(En)
- Chinese(Zh)
- Spanish(Es)
- French(Fr)
- Russian(Ru)
- Japanese(Ja)
- Korean(Ko)
- Arabic(Ar)
- Italian(It)
- diffusers

widget:
- text: "一张<鸣人>男孩的照片"
  example_title: 一张<鸣人>男孩的照片
---

# This is a DreamBooth model finetuned from the multilingual text-to-image model AltDiffusion.

Dreambooth is one of the method of finetune the pretrained text-to-image model.Given as input just a few images of a subject, it learns to bind a unique identifier with that specific subject.

AltDiffusion which is a multilingual text-to-image model.It currently supports 9 languages and will support more in future.
We can use the dreambooth to finetune the AltDiffusion,so that we can get a multilingual Dreambooth model which could supports 9 languages.

Here we give a example model finetuned use a dozen pictures of Uzumaki Naruto downloaded from web.The example code of inference is shown bellow.You can have a try and maybe train your own dreambooth.Hopes have fun!

## Example code of inference
```
from diffusers import AltDiffusionPipeline, DPMSolverMultistepScheduler
import torch

pipe = AltDiffusionPipeline.from_pretrained("BAAI/DreamBooth-AltDiffusion")
pipe = pipe.to("cuda")

pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

prompt = "一张<鸣人>男孩的照片"
image = pipe(prompt, num_inference_steps=25).images[0]
image.show()
```

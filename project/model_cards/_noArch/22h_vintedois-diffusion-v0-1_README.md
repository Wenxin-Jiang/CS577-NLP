---
license: creativeml-openrail-m
tags:
- text-to-image
---
### Vintedois (22h) Diffusion model trained by [Predogl](https://twitter.com/Predogl) and [piEsposito](https://twitter.com/piesposi_to) with open weights, configs and prompts (as it should be)

This model was trained on a large amount of high quality images with simple prompts to generate beautiful images without a lot of prompt engineering.

You can enforce style by prepending your prompt with `estilovintedois` if it is not good enough.

It should also be very dreamboothable, being able to generate high fidelity faces with a little amount of steps.

**You can use this model commercially or whatever, but we are not liable if you do messed up stuff with it.**

### Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run vintedois-diffusion-v0-1 :
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/22h/vintedois-diffusion-v0-1)


### Model card

Everything from [Stable Diffusion v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5), plus the fact that this is being built by two indie devs, so it was not extensively tested for new biases.

You can run this concept via `diffusers` [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb)

### Sample results

<img src="https://huggingface.co/22h/vintedois-diffusion-v0-1/resolve/main/joined.png" width=1024/>

### Example prompts

- Prompt: photo of an old man in a jungle, looking at the camera
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44
<img src="https://huggingface.co/22h/vintedois-diffusion-v0-1/resolve/main/44-euler-a-photo%20of%20an%20old%20man%20in%20a%20jungle%2C%20looking%20at%C2%A0the%C2%A0camera.png" width=512/>

- Prompt: kneeling cat knight, portrait, finely detailed armor, intricate design, silver, silk, cinematic lighting, 4k
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 50
- Seed: 44
<img src="https://huggingface.co/22h/vintedois-diffusion-v0-1/resolve/main/44-euler-a-kneeling%20cat%20knight%2C%20portrait%2C%20finely%20detailed%20armor%2C%20intricate%20design%2C%20silver%2C%20silk%2C%20cinematic%20lighting%2C%204k.png" width=512/>


- Prompt: a beautiful girl In front of the cabin, the country, by Artgerm Lau and Krenz Cushart，hyperdetailed, trending on artstation, trending on deviantart
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 50
- Seed: 44
<img src="https://huggingface.co/22h/vintedois-diffusion-v0-1/resolve/main/44-euler-a-a%20beautiful%20girl%20In%20front%20of%20the%20cabin%2C%20the%20country%2C%20by%20Artgerm%20Lau%20and%20Krenz%20Cushart%EF%BC%8Chyperdetailed%2C%20trending%20on%20artstation%2C%20tre.png" width=512/>

- Prompt: destroyed city
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 50
- Seed: 44
<img src="https://huggingface.co/22h/vintedois-diffusion-v0-1/resolve/main/44-euler-a-destroyed%20city.png" width=512/>

- Prompt: victorian city landscape
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 50
- Seed: 44
<img src="https://huggingface.co/22h/vintedois-diffusion-v0-1/resolve/main/44-euler-a-victorian%20city%20landscape.png" width=512/>

- Prompt: prehistoric native living room
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 50
- Seed: 44
<img src="https://huggingface.co/22h/vintedois-diffusion-v0-1/resolve/main/44-euler-a-prehistoric%20native%20living%20room.png" width=512/>

Thanks for the Google Developer Expert program for providing us with a GCP credits grant.
---
license: openrail++
language:
- en
tags:
- stable-diffusion
- text-to-image
- diffusers
thumbnail: "https://huggingface.co/nitrosocke/Future-Diffusion/resolve/main/images/future-diffusion-thumbnail-2.jpg"
inference: false
---

### Future Diffusion

This is the fine-tuned Stable Diffusion 2.0 model trained on high quality 3D images with a futuristic Sci-Fi theme.
Use the tokens   
`future style`   
 in your prompts for the effect.
Trained on Stability.ai's  [Stable Diffusion 2.0 Base](https://huggingface.co/stabilityai/stable-diffusion-2-base) with 512x512 resolution.

**If you enjoy my work and want to test new models before release, please consider supporting me**
[![Become A Patreon](https://badgen.net/badge/become/a%20patron/F96854)](https://patreon.com/user?u=79196446)

**Disclaimer: The SD 2.0 model is just over 24h old at this point and we still need to figure out how it works exactly. Please view this as an early prototype and experiment with the model.**

**Characters rendered with the model:**
![Characters Samples](https://huggingface.co/nitrosocke/Future-Diffusion/resolve/main/images/future-diffusion-samples01s.png)
**Cars and Animals rendered with the model:**
![Misc. Samples](https://huggingface.co/nitrosocke/Future-Diffusion/resolve/main/images/future-diffusion-samples02s.png)
**Landscapes rendered with the model:**
![Landscape 1](https://huggingface.co/nitrosocke/Future-Diffusion/resolve/main/images/future-diffusion-samples03s.png)

#### Prompt and settings for the Characters:
**future style [subject] Negative Prompt: duplicate heads bad anatomy**   
 _Steps: 20, Sampler: Euler a, CFG scale: 7, Size: 512x704_

#### Prompt and settings for the Landscapes:
**future style city market street level at night Negative Prompt: blurry fog soft**   
 _Steps: 20, Sampler: Euler a, CFG scale: 7, Size: 1024x576_

This model was trained using the diffusers based dreambooth training by ShivamShrirao using prior-preservation loss and the _train-text-encoder_ flag in 7.000 steps.

## License

This model is open access and available to all, with a CreativeML Open RAIL++-M License further specifying rights and usage.
[Please read the full license here](https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/LICENSE-MODEL)
---
license: openrail++
language:
- en
tags:
- stable-diffusion
- text-to-image
- diffusers
thumbnail: "https://huggingface.co/nitrosocke/redshift-diffusion-768/resolve/main/images/redshift-diffusion-768-thumbnail.jpg"
inference: false
---

### Future Diffusion

This is the fine-tuned Stable Diffusion 2.0 model trained on high quality 3D images with a 768x768 pixel resolution.
Use the tokens   
`redshift style`   
 in your prompts for the effect.
Trained on Stability.ai's  [Stable Diffusion 2.0](https://huggingface.co/stabilityai/stable-diffusion-2) with 768x768 resolution.

**If you enjoy my work and want to test new models before release, please consider supporting me**
[![Become A Patreon](https://badgen.net/badge/become/a%20patron/F96854)](https://patreon.com/user?u=79196446)

- **The weights are now available! You can download them here: [redshift-diffusion-768.ckpt](https://huggingface.co/nitrosocke/redshift-diffusion-768/resolve/main/redshift-diffusion-768.ckpt)**
- **You can try out the model online here: [Diffusion Space Demo](https://huggingface.co/spaces/nitrosocke/Diffusion_Space)**
- **or try out this model with my local Diffusers based [Gradio WebUI](https://github.com/nitrosocke/diffusers-webui)**


**Characters rendered with the model:**
![Characters Samples](https://huggingface.co/nitrosocke/redshift-diffusion-768/resolve/main/images/redshift-diffusion-768-samples01s.jpg)
**Cars and Animals rendered with the model:**
![Misc. Samples](https://huggingface.co/nitrosocke/redshift-diffusion-768/resolve/main/images/redshift-diffusion-768-samples02s.jpg)
**Landscapes rendered with the model:**
![Landscape 1](https://huggingface.co/nitrosocke/redshift-diffusion-768/resolve/main/images/redshift-diffusion-768-samples03s.jpg)
![Landscape 2](https://huggingface.co/nitrosocke/redshift-diffusion-768/resolve/main/images/redshift-diffusion-768-samples04s.jpg)

#### Prompt and settings for the Characters:
**redshift style portrait black female cyberpunk hacker tattoos colorful short hair wearing a crop top redshift style Negative Prompt: mutated body double head bad anatomy long face long neck long body text watermark signature**   
 _Steps: 20, Sampler: Euler a, CFG scale: 7, Size: 768x1024_

#### Prompt and settings for the Landscapes:
**redshift style beautiful fjord at sunrise Negative Prompt: fog blurry soft**   
 _Steps: 20, Sampler: Euler a, CFG scale: 7, Size: 1536x768_

This model was trained using the diffusers based dreambooth training by ShivamShrirao using prior-preservation loss and the _train-text-encoder_ flag in 7.500 steps.

## License

This model is open access and available to all, with a CreativeML Open RAIL++-M License further specifying rights and usage.
[Please read the full license here](https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/LICENSE-MODEL)
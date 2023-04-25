---
license: openrail++
language:
- en
- ja
- es
- zh
widget:
- text: environment concept art
  example_title: Concept Art 1
- text: a beautiful illustration of a fantasy forest
  example_title: Fantasy Forest
tags:
- stable-diffusion
- sygil-diffusion
- text-to-image
- sygil-devs
- finetune
- stable-diffusion-1.5
inference: true
pinned: true
metrics:
- accuracy
- bertscore
- bleu
- bleurt
- brier_score
- cer
- character
- charcut_mt
- chrf
- code_eval
---


# About the model
-----------------
This model is a fine-tune of Stable Diffusion, trained on the [Imaginary Network Expanded Dataset](https://github.com/Sygil-Dev/INE-dataset), with the big advantage of allowing the use of multiple namespaces (labeled tags) to control various parts of the final generation.
While current models usually are prone to “context errors” and need substantial negative prompting to set them on the right track, the use of namespaces in this model (eg. “species:seal” or “studio:dc”) stop the model from misinterpreting a seal as the singer Seal, or DC Comics as Washington DC. 
This model is also able to understand other languages besides English, currently it can partially understand prompts in Chinese, Japanese and Spanish. More training is already being done in order to have the model completely understand those languages and have it work just like how it works with English prompts.

As the model is fine-tuned on a wide variety of content, it’s able to generate many types of images and compositions, and easily outperforms the original model when it comes to portraits, architecture, reflections, fantasy, concept art, anime, landscapes and a lot more without being hyper-specialized like other community fine-tunes that are currently available. 

**Note: The prompt engineering techniques needed are slightly different from other fine-tunes and the original Stable Diffusion model, so while you can still use your favorite prompts, for best results you might need to tweak them to make use of namespaces. A more detailed guide will be available later on, but you can use the tags and namespaces found here [Dataset Explorer](https://huggingface.co/spaces/Sygil/INE-dataset-explorer) should be able to start you off on the right track.

If you find my work useful, please consider supporting me on [GitHub Sponsors](https://github.com/sponsors/ZeroCool940711)! 

This model is still in its infancy and it's meant to be constantly updated and trained with more and more data as time goes by, so feel free to give us feedback on our [Discord Server](https://discord.gg/UjXFsf6mTu) or on the discussions section on huggingface. We plan to improve it with more, better tags in the future, so any help is always welcome 😛
[![Join the Discord Server](https://badgen.net/discord/members/fTtcufxyHQ?icon=discord)](https://discord.gg/UjXFsf6mTu)


# Showcase
![Showcase image](pictures/showcase-6.jpg)


## Examples

Using the [🤗's Diffusers library](https://github.com/huggingface/diffusers) to run Sygil Diffusion in a simple and efficient manner.

```bash
pip install diffusers transformers accelerate scipy safetensors
```
Running the pipeline (if you don't swap the scheduler it will run with the default DDIM, in this example we are swapping it to DPMSolverMultistepScheduler):

```python
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

model_id = "Sygil/Sygil-Diffusion"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

prompt = "a beautiful illustration of a fantasy forest"
image = pipe(prompt).images[0]
    
image.save("fantasy_forest_illustration.png")
```

**Notes**:
- Despite not being a dependency, we highly recommend you to install [xformers](https://github.com/facebookresearch/xformers) for memory efficient attention (better performance)
- If you have low GPU RAM available, make sure to add a `pipe.enable_attention_slicing()` after sending it to `cuda` for less VRAM usage (to the cost of speed).

## Available Checkpoints:
  - #### Stable:
    - [Sygil Diffusion v0.1](https://huggingface.co/Sygil/Sygil-Diffusion/blob/main/sygil-diffusion-v0.1.ckpt): Trained on Stable Diffusion 1.5 for 800,000 steps.
    - [Sygil Diffusion v0.2](https://huggingface.co/Sygil/Sygil-Diffusion/blob/main/sygil-diffusion-v0.2.ckpt): Resumed from Sygil Diffusion v0.1 and trained for a total of 1.77 million steps.
    - [Sygil Diffusion v0.3](https://huggingface.co/Sygil/Sygil-Diffusion/blob/main/sygil-diffusion-v0.3.ckpt): Resumed from Sygil Diffusion v0.2 and trained for a total of 2.01 million steps.
    - [Sygil Diffusion v0.4](https://huggingface.co/Sygil/Sygil-Diffusion/blob/main/sygil-diffusion-v0.4.ckpt): Resumed from Sygil Diffusion v0.3 and trained for a total of 2.37 million steps.
  - #### Beta:
    - No active beta right now.
  
  Note: Checkpoints under the Beta section are updated daily or at least 3-4 times a week. This is usually the equivalent of 1-2 training session,
  this is done until they are stable enough to be moved into a proper release, usually every 1 or 2 weeks.
  While the beta checkpoints can be used as they are only the latest version is kept on the repo and the older checkpoints are removed when a new one
  is uploaded to keep the repo clean. The HuggingFace inference API as well as the diffusers library will always use the latest beta checkpoint in the diffusers format.
  For special cases we might make additional repositories to keep a copy of the diffusers model like when a model uses a different Stable Diffusion model as base (eg. Stable Diffusion 1.5 vs 2.1).
  
## Training

**Training Data**:
The model was trained on the following dataset:
- [Imaginary Network Expanded Dataset](https://github.com/Sygil-Dev/INE-dataset) dataset.

**Hardware and others**
- **Hardware:** 1 x Nvidia RTX 3050 8GB GPU
- **Hours Trained:** 857 hours approximately.
- **Optimizer:** AdamW
- **Adam Beta 1**: 0.9
- **Adam Beta 2**: 0.999
- **Adam Weight Decay**: 0.01
- **Adam Epsilon**: 1e-8
- **Gradient Checkpointing**: True
- **Gradient Accumulations**: 400
- **Batch:** 1
- **Learning Rate:** 1e-7
- **Learning Rate Scheduler:** cosine_with_restarts
- **Learning Rate Warmup Steps:** 10,000
- **Lora unet Learning Rate**: 1e-7
- **Lora Text Encoder Learning Rate**: 1e-7
- **Resolution**: 512 pixels
- **Total Training Steps:** 2,370,200


  Note: For the learning rate I'm testing something new, after changing from using the `constant` scheduler to `cosine_with_restarts` after v0.3 was released, I noticed
   it practically uses the optimal learning rate while trying to minimize the loss value, so, when every training session finishes I use for the next session the latest
   learning rate value shown for the last few steps from the last session, this makes it so it will overtime decrease at a constant rate. When I add a lot of data to the training dataset
   at once, I move the learning rate back to 1e-7 which then the scheduler will move down again as it learns more from the new data, this makes it so the training
   doesn't overfit or uses a learning rate too low that makes the model not learn anything new for a while.
   

Developed by: [ZeroCool94](https://github.com/ZeroCool940711) at [Sygil-Dev](https://github.com/Sygil-Dev/)

## Community Contributions:
  - [Kevin Turner (keturn)](https://huggingface.co/keturn): created the [INE-dataset-explorer](https://huggingface.co/spaces/Sygil/INE-dataset-explorer) space for better browsing of the INE dataset.
    
*This model card is based on the [Stable Diffusion v1](https://github.com/CompVis/stable-diffusion/blob/main/Stable_Diffusion_v1_Model_Card.md) and [DALL-E Mini model card](https://huggingface.co/dalle-mini/dalle-mini).*


# License
This model is open access and available to all, with a CreativeML Open RAIL++-M License further specifying rights and usage. [Please read the full license here](https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/LICENSE-MODEL)
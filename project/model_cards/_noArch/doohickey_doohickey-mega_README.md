---
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
---

Models better suited for High-Resolution Image Synthesis. The main model (doohickey/doohickey-mega) has been finetuned from [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) near a resolution of 768x768 (suggested method of generating from model is with [Doohickey](https://colab.research.google.com/github/aicrumb/doohickey/blob/main/Doohickey_Diffusion.ipynb)).

Current models:

| name | description | datasets used |
| ---  | ---         | ---           |
| doohickey/doohickey-mega/v1-3000steps.ckpt | first try, rlly good hd, bad results w/ other aspect ratios than 1:1 trained at 704x704 | A-1k|
| doohickey/doohickey-mega/v2-3000steps.ckpt | same as last one but worse | A-1k + ~1k samples from LAION-2b-En-Aesthetic >=768x768 |
| doohickey/doohickey-mega/v3-3000.ckpt | with new CLIP model ([laion/CLIP-ViT-L-14-laion2B-s32B-b82K](https://hf.co/laion/CLIP-ViT-L-14-laion2B-s32B-b82K)) (CLIP model also finetuned the 3k steps), models past this point were trained with various aspect ratios from 640x640 min to 768x768 max resolution. (examples 768x640 or 704x768) | A-1k + E-10k |
| doohickey/doohickey-mega/v3-6000.ckpt | 3k steps on top of v3-3000.ckpt, better at hands! (just UNet finetune, added a RandomHorizontalFlip operation at 50%) | A-1k |
| doohickey/doohickey-mega/v3-7000.ckpt | continuation of last model,  I thought Colab would crash after 3k steps but it kept going for a little while saving ckpts every 1k steps. | A-1k |
| doohickey/doohickey-mega/v3-8000.ckpt | see last description, v3-6000 + 2k steps | A-1k |

The currently loaded model for diffusers is doohickey/doohickey-mega/v3-8000.ckpt

Datasets:
| name | description |
| --- | --- |
| A-1K | 1k scraped images, captioned with BLIP (more refined aesthetic) |
| E-10k | 10k scraped images captioned with BLIP (less refined aesthetic) |

_Limitations and Biases from Stable Diffusion also apply to this model._


<div style="font-size:10px">
This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies:

  1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
  2. The authors claim no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
  3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
  Please read the full license carefully here: https://huggingface.co/spaces/CompVis/stable-diffusion-license
</div>
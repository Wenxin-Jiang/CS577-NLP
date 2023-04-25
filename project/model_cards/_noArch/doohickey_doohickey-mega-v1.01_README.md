---
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
---

Models better suited for High-Resolution Image Synthesis. The main model (doohickey/doohickey-mega) has been finetuned from [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) near a resolution of 768x768 (suggested method of generating from model is with [Doohickey](https://colab.research.google.com/github/aicrumb/doohickey/blob/main/Doohickey_Diffusion.ipynb)).

This is a version of Stable Diffusion finetuned to use [laion/CLIP-ViT-L-14-laion2B-s32B-b82K](https://huggingface.co/laion/CLIP-ViT-L-14-laion2B-s32B-b82K) instead of the stock openai clip model. While doohickey-mega finetuned the CLIP model as well, this ckpt was finetuned without the CLIP model being trained. In total 6000 steps.

_Limitations and Biases from Stable Diffusion also apply to this model._


<div style="font-size:10px">
This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies:

  1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
  2. The authors claim no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
  3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
  Please read the full license carefully here: https://huggingface.co/spaces/CompVis/stable-diffusion-license
</div>
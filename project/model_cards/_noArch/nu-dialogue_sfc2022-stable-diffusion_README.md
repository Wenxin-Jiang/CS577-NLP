---
language: ja
license: other
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- ja
- japanese
inference: true
# extra_gated_prompt: |-
#   One more step before getting this model.
#   This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
#   The CreativeML OpenRAIL License specifies: 
#   1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
#   2. rinna Co., Ltd. claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
#   3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
#   Please read the full license here: https://huggingface.co/spaces/CompVis/stable-diffusion-license
  
#   By clicking on "Access repository" below, you accept that your *contact information* (email address and username) can be shared with the model authors as well.
    
# extra_gated_fields:
#  I have read the License and agree with its terms: checkbox
---


# SFCOCO Stable Diffusion Model Card

SFCOCO Stable Diffusion is a Japanese-specific latent text-to-image diffusion model capable of generating photo-realistic images given any text input.

This model was fine-tuned by using a powerful Japanese-specific latent text-to-image diffusion model, [Japanese Stable Diffusion](https://huggingface.co/rinna/japanese-stable-diffusion).
We use the [Stable Diffusion text-to-image fine-tuning script](https://github.com/huggingface/diffusers/tree/main/examples/text_to_image) of [🤗 Diffusers](https://github.com/huggingface/diffusers)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nu-dialogue/clip-prefix-caption-jp/blob/master/notebooks/sfc2022_stable_diffusion.ipynb)

## Model Details
- **Developed by:** Atsumoto Ohashi
- **Model type:** Diffusion-based text-to-image generation model
- **Language(s):** Japanese
- **Model Description:** This is a model that can be used to generate and modify images based on text prompts. It is a [Latent Diffusion Model (LDM)](https://arxiv.org/abs/2112.10752) that used [Japanese Stable Diffusion](https://huggingface.co/rinna/japanese-stable-diffusion) as a pre-trained model. 
- **Resources for more information:** [Japanese Stable Diffusion GitHub Repository](https://github.com/rinnakk/japanese-stable-diffusion)

## Examples

Firstly, install our package as follows. This package is modified [🤗's Diffusers library](https://github.com/huggingface/diffusers) to run Japanese Stable Diffusion.


```bash
pip install git+https://github.com/rinnakk/japanese-stable-diffusion
```

Run this command to log in with your HF Hub token if you haven't before:

```bash
huggingface-cli login
```

Running the pipeline with the k_lms scheduler:
```python
import torch
from torch import autocast
from diffusers import LMSDiscreteScheduler
from japanese_stable_diffusion import JapaneseStableDiffusionPipeline
model_id = "nu-dialogue/sfc2022-stable-diffusion"
device = "cuda"
# Use the K-LMS scheduler here instead
scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)
pipe = JapaneseStableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, use_auth_token=True, torch_dtype=torch.float16)
pipe = pipe.to(device)

prompt = "福澤諭吉像の写真"
with autocast("cuda"):
    image = pipe(prompt, guidance_scale=7.5)["sample"][0]  
    
image.save("output.png")
```
_Note: `JapaneseStableDiffusionPipeline` is almost same as diffusers' `StableDiffusionPipeline` but added some lines to initialize our models properly._ 


## Training

**Training Data**
We used the SFCOCO2021 and SFCOCO2022 dataset for training the model.
You can see these datasets in [this repository](https://github.com/nu-dialogue/clip-prefix-caption-jp).

**Training Procedure**
SFCOCO Stable Diffusion has the same architecture as Japanese Stable Diffusion and was trained by using Japanese Stable Diffusion.
We use the [Stable Diffusion text-to-image fine-tuning script](https://github.com/huggingface/diffusers/tree/main/examples/text_to_image) of [🤗 Diffusers](https://github.com/huggingface/diffusers)

## Citation

```bibtex
@InProceedings{Rombach_2022_CVPR,
      author    = {Rombach, Robin and Blattmann, Andreas and Lorenz, Dominik and Esser, Patrick and Ommer, Bj\"orn},
      title     = {High-Resolution Image Synthesis With Latent Diffusion Models},
      booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
      month     = {June},
      year      = {2022},
      pages     = {10684-10695}
  }
```

```bibtex
@misc{japanese_stable_diffusion,
    author    = {Shing, Makoto and Sawada, Kei},
    title     = {Japanese Stable Diffusion},
    howpublished = {\url{https://github.com/rinnakk/japanese-stable-diffusion}},
    month     = {September},
    year      = {2022},
}
```


*This model card was written by: Atsumoto Ohashi and is based on the [Japanese Stable Diffusion Model Card](https://github.com/rinnakk/japanese-stable-diffusion).*
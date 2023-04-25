---
license: creativeml-openrail-m
tags:
- text-to-image
- safetensors
- stable-diffusion
---
### Broken-Mirror-Style Dreambooth model trained by Kagerage with [TheLastBen's fast-DreamBooth](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) notebook


Test the concept via A1111 Colab [fast-Colab-A1111](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb)
Or you can run your new concept via `diffusers` [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb)

In my experience, the best prompting style is "brkmror cracked and shattered mirror, professional photo, descriptor of location, portrait of person, bokeh", potentially with a negative prompt of "closed eyes"

Sampler DPM++ SDE Karras with at least 25 steps gives slightly better faces from my testing, CFG 7 seems fine, and since this is trained on top of 2.1, the minimum resolution is 768x768.

Or course though, feel free to experiment!

\(NOTE!!! This 2.1 based model is FP16, so it may not render outputs properly without Xformers\)

Sample pictures of this concept:

  
  
  
  ![0](https://huggingface.co/Kagerage/broken-mirror-style/resolve/main/sample_images/00036-4212333230-brkmror_cracked_and_shattered_mirror,_professional_photo,_field_of_sunflowers,_portrait_of_woman,_bokeh.png)
      ![1](https://huggingface.co/Kagerage/broken-mirror-style/resolve/main/sample_images/00039-140956230-brkmror_cracked_and_shattered_mirror,_professional_photo,_snow_covered_mountain_peak,_portrait_of_black_woman,_bokeh.png)
      ![2](https://huggingface.co/Kagerage/broken-mirror-style/resolve/main/sample_images/00041-1640278942-brkmror_cracked_and_shattered_mirror,_professional_photo,_early_summer_beach_at_dusk_with_shipwreck,_portrait_of_youthful_japane.png)
      ![3](https://huggingface.co/Kagerage/broken-mirror-style/resolve/main/sample_images/00038-1234041848-brkmror_cracked_and_shattered_mirror,_professional_photo,_field_of_roses,_portrait_of_black_woman,_bokeh.png)
      

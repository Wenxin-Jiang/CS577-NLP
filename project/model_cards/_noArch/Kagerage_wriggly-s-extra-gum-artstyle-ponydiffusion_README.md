---
license: creativeml-openrail-m
tags:
- text-to-image
- safetensors
- stable-diffusion
---
### Wriggly's-Extra-Gum-artstyle-ponydiffusion Dreambooth model trained by Kagerage with [TheLastBen's fast-DreamBooth](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) notebook


Test the concept via A1111 Colab [fast-Colab-A1111](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb)
Or you can run your new concept via `diffusers` [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb)

As the name suggests, this model was trained on that weird hand-drawn looking artwork that you'd find on the inside of a pack of Wriggly's Extra gum, ontop of Pony-diffusion-v2.

PROMPTING ADVICE: Best results come from using the trigger word like "gvgtgm traditional print lineart drawing", or "gvgtgm traditional print badly drawn lineart drawing" (Oof...) for a more true to training data image

prompt for either "anthro/feral male/female/whatever pony/whatever" or "anthro/feral male/female/whatever pony/whatever with tail/whatever"

anything else should be added at the end, so prompt would look like "gvgtgm traditional print lineart drawing, solo anthro female pony with tail, sweater and jeans, snow, park, trees"
![0](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-ponydiffusion/resolve/main/sample_images/00445-3775115334-gvgtgm%20traditional%20print%20lineart%20drawing%2C%20solo%20anthro%20female%20pony%20with%20tail%2C%20sweater%20and%20jeans%2C%20snow%2C%20park%2C%20trees.png)

negative prompt "ugly, red, green, blue, clipped highlights, contrast", or for solo images, "ugly, multiple, red, green, blue, clipped highlights, contrast", or exclude "ugly" for a (Possibly) more true to training data image

Recommended CFG is 7

Non-anthro ponies are seemingly very difficult to get, and I'm not sure how to make this model generate them.

Sample pictures of this concept:

  
  ![1](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-ponydiffusion/resolve/main/sample_images/00451-250025809-gvgtgm%20traditional%20print%20lineart%20drawing%2C%20solo%20anthro%20female%20unicorn%20pony%20with%20wings%2C%20sweater%20and%20jeans%2C%20city%2C%20night.png)
      ![2](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-ponydiffusion/resolve/main/sample_images/00446-646835085-gvgtgm%20traditional%20print%20lineart%20drawing%2C%20solo%20anthro%20female%20pony%20with%20tail%2C%20sweater%20and%20jeans%2C%20field%2C%20dusk.png)
      ![3](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-ponydiffusion/resolve/main/sample_images/00551-426350136-gvgtgm%20traditional%20print%20lineart%20drawing%2C%20anthro%20male%20pony%2C%20sweater%20and%20jeans%2C%20in%20crowded%20movie%20theater.png)
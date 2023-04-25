---
license: creativeml-openrail-m
tags:
- text-to-image
- safetensors
- stable-diffusion
---
### Wriggly's-Extra-Gum-artstyle-waifudiffusion Dreambooth model trained by Kagerage with [TheLastBen's fast-DreamBooth](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) notebook


Test the concept via A1111 Colab [fast-Colab-A1111](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb)
Or you can run your new concept via `diffusers` [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb)

As the name suggests, this model was trained on that weird hand-drawn looking artwork that you'd find on the inside of a pack of Wriggly's Extra gum, ontop of Yiffy-e18.

PROMPTING ADVICE: Best results come from using the trigger word like "gvgtgm lineart drawing" or "gvgtgm stylized lineart drawing" or "gvgtgm shading lineart drawing", or "gvgtgm badly drawn lineart drawing" (Oof...) for a more true to training data image

prompt for either "anthro/feral male/female/whatever lion/wolf/whatever" or "anthro/feral male/female/whatever lion/wolf/whatever with tail/whatever"

anything else should be added at the end, so prompt would look like "gvgtgm stylized lineart drawing, solo anthro male wolf with tail, buff, sweater and jeans, snow, park, trees"
![0](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-furry/resolve/main/sample_images/00245-2833040163-gvgtgm%20stylized%20lineart%20drawing%2C%20solo%20anthro%20male%20wolf%20with%20tail%2C%20buff%2C%20sweater%20and%20jeans%2C%20snow%2C%20park%2C%20trees.png)

negative prompt "ugly" or "ugly, badly drawn", or for solo images, "ugly, multiple" or "ugly, badly drawn, multiple", or exclude "ugly" and "badly drawn" for a (Possibly) more true to training data image, and if you're getting too many improperly shaded images, add "3d \(artwork\)" at the end of the negative prompts. Also, "abstract" seemingly reduces visual clutter, which can be helpful.

Recommended CFG is 7

Non-anthro furries are a bit challenging to generate with this model, likely do to how homogenous the training dataset was.

Sample pictures of this concept:

![1](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-furry/resolve/main/sample_images/00312-1134468466-gvgtgm%20shading%20lineart%20drawing%2C%20anthro%20wolves%20with%20tail%2C%20female_male%2C%20eye%20contact%2C%20happy%2C%20sweater%20and%20jeans%2C%20heavy%20snow%2C%20city%2C%20c.png)
    ![2](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-furry/resolve/main/sample_images/00193-981263969-gvgtgm%20shading%20lineart%20drawing%2C%20anthro%20wolves%20with%20tail%2C%20male_male%20pressing%20heads%20together%2C%20cute%2C%20sweater%20and%20jeans%2C%20heavy%20snow%2C.png)
    ![3](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-furry/resolve/main/sample_images/00167-128089252-gvgtgm%20shading%20lineart%20drawing%2C%20anthro%20wolves%20with%20tail%2C%20female_female%20hug%2C%20sweater%20and%20jeans%2C%20heavy%20snow%2C%20city%2C%20cars%2C%20trees%2C%20he.png)

Bonus images from trial and error
![4](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-furry/resolve/main/sample_images/00000-3671938673-gvgtgm%20illustration%2C%20two%20male%20anthro%20dog%2C%20chibi%2C%20tail.png)
    ![5](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-furry/resolve/main/sample_images/00003-3671938676-gvgtgm%20illustration%2C%20two%20male%20anthro%20dog%2C%20chibi%2C%20tail.png)
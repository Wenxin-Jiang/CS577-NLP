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

As the name suggests, this model was trained on that weird hand-drawn looking artwork that you'd find on the inside of a pack of Wriggly's Extra gum, ontop of Waifu Diffusion 1.3.

PROMPTING ADVICE: Best results come from using the trigger word like "gvgtgm lineart drawing", or "gvgtgm badly drawn lineart drawing" (Oof...) for a more true to training data image

prompt for either "(anime name) anime 1boy/1girl/whatever", "1boy/1girl/whatever" for something more akin to the training data, and either "modern anime 1boy/1girl/whatever" or "quality anime 1boy/1girl/whatever" for an inbetween of the training data and a general anime style

anything else should be added at the end, so prompt would look like "gvgtgm lineart drawing, jojo anime 1boy, sweater and jeans, snow, park, trees, upper-body portrait"
![0](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-waifudiffusion/resolve/main/sample_images/00159-3255709159-gvgtgm%20lineart%20drawing%2C%20jojo%20anime%201boy%2C%20sweater%20and%20jeans%2C%20snow%2C%20park%2C%20trees%2C%20upper-body%20portrait.png)

Recommended sampler is anything non-ancestral, as to avoid softness. CFG 7 seems to work fine. Looks like it generates decent results without the Waifu Diffusion VAE, not sure how it acts with it enabled.

Sample pictures of this concept:
![1](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-waifudiffusion/resolve/main/sample_images/00028-4290858058-gvgtgm%20lineart%20drawing%2C%20one%20piece%20anime%201boy%20and%201girl%2C%20sweater%20and%20jeans%2C%20snow%2C%20park%2C%20trees%2C%20upper-body%20couples%20portrait%2C%20blush.png)
    ![2](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-waifudiffusion/resolve/main/sample_images/00052-3589974798-gvgtgm%20lineart%20drawing%2C%20naruto%20anime%202boys%2C%20yaoi%20kiss%2C%20sweater%20and%20jeans%2C%20heavy%20snow%2C%20city%2C%20cars%2C%20trees%2C%20upper-body%20couples%20port.png)
    ![3](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-waifudiffusion/resolve/main/sample_images/00066-2248729145-gvgtgm%20lineart%20drawing%2C%20dragon%20quest%20anime%202girls%2C%20yuri%20hug%2C%20sweater%20and%20jeans%2C%20heavy%20snow%2C%20city%2C%20cars%2C%20trees%2C%20headshot%20couples.png)


Bonus images from trial and error
![4](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-waifudiffusion/resolve/main/sample_images/00280-702031273-Ojamajo%20Doremi%20style%20gvgtgm%2C%201girl%20in%20front%20of%20a%20mug%20of%20coffee%2C%20smile%2C%20hands%20on%20table.png)
    ![5](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-waifudiffusion/resolve/main/sample_images/00290-3748953017-Hokudo%20no%20Ken%20style%20gvgtgm%2C%201girl%20in%20front%20of%20a%20mug%20of%20coffee%2C%20smile%2C%20hands%20on%20table.png)
    ![6](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-waifudiffusion/resolve/main/sample_images/00299-1407802124-One%20Piece%20style%20gvgtgm%2C%201girl%20in%20front%20of%20a%20mug%20of%20coffee%2C%20smile%2C%20hands%20on%20table.png)
    ![7](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-waifudiffusion/resolve/main/sample_images/00412-2383188430-dragon%20quest%20gvgtgm%2C%201girl%20in%20front%20of%20a%20mug%20of%20coffee%2C%20smile%2C%20hands%20on%20table.png)
    ![8](https://huggingface.co/Kagerage/wriggly-s-extra-gum-artstyle-waifudiffusion/resolve/main/sample_images/00851-678242046-gvgtgm%20anime%20illustration%2C%20nekomimi%2C%201girl%2C%20happy%2C%20date%2C%20fullbody%2C%20tail%2C%20maid.png)
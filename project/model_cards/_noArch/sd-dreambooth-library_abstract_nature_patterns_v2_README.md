---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
---
### abstract_nature_patterns_v2 Dreambooth model trained by apurik-parv with  https://github.com/ShivamShrirao/diffusers dreambooth implementation.
inference prompt : **abnapa**\\
The model is an attempt at teaching symmetry and scales associated with nature to SD 1.5 base model.
This version v2 is trained on better curated images for 40,000 steps. I am still working on finding what the model really does and if it has any impact on the base model.
With that being said, the following are my findings, at the outset it seems that
-Images have better symmetry and lighting.
-Images have less artifacts.
-Does not seem to work with large canvas such as 1024x1024 the repetition problem isstill there.
Feel free to experiment with the model.
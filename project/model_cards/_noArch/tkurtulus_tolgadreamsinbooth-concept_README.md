---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
---
### "TolgaDreamsInBooth" is fine-tuned version of Dreambooth text-to-image model

- This model trained with [TheLastBen's fast-DreamBooth](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) notebook
- Labelled myself as "tkrut11" while training. You can use this label to create my portrait based images. 

# Sample prompt:

detailed portrait of tkrut11 Holographic Futuristic sci-fi fashion cyberpunk, (neotokyo), synthwave, (aesthetics), futuristic, bladerunner movie scene by ismail inceoglu dragan bibin hans thoma greg rutkowski Alexandros Pyromallis Nekro Rene Margitte illustrated Perfect face, fine details, realistic shaded, fine-face, pretty face sharp chine

External usage :

```python
from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("tkurtulus/tolgadreamsinbooth-concept")
```

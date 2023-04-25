---
license: creativeml-openrail-m
tags:
- text-to-image
---
### 2d-art-sprites Dreambooth model trained by ana-tamais with [TheLastBen's fast-DreamBooth](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) notebook



You can test this model using this [Colab Notebook for Inference](https://colab.research.google.com/drive/1pFaEJHa7mxFruBfm2hDnR8S6aEo7sAFx?usp=sharing)

Sample pictures of 2dart concept:

<img src="https://huggingface.co/ana-tamais/2d-art-sprites/resolve/main/concept_images/2dart_1.png" width=256></img>
<img src="https://huggingface.co/ana-tamais/2d-art-sprites/resolve/main/concept_images/2dart_4.png" width=256></img>
<img src="https://huggingface.co/ana-tamais/2d-art-sprites/resolve/main/concept_images/2dart_9.png" width=256></img>
    
We saved the training data in `dataset.zip`, and some generated results in `results.zip`.

### Some recommendations 
We recommend to set the:
- prompt as: `"[some wizard, paladin, healer, etc.], in the style of 2dart, white background, no background, full body"`
- negative prompt as: `"deformed, mutilated limbs, background, multiple people"`
- guidance scale between `9 and 10`
- sampling method as `Euler`
- sampling steps as `60`
- batch size as `1` - avoid high batch size, unless you have a high memory GPU

This set of hyperparameters lead us to stable and good results.

This model was trained using images which the character has some human format or is a not deformed living being. So if you try to predict something like "sword, mirror, candle, etc" (non-living things), we saw the model doesn't perform so well.

You need at least a Tesla T4 to be able to run the inference step using the given [notebook](https://colab.research.google.com/drive/1pFaEJHa7mxFruBfm2hDnR8S6aEo7sAFx?usp=sharing).
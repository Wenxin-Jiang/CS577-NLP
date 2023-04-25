---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
inference: true
datasets:
- Guizmus/AnimeChanStyle
- skytnt/fbanimehq
- skytnt/anime-segmentation
- Nerfgun3/bad_prompt
- Nerfgun3/shatter_style
- Nerfgun3/ouroboros_embeddings
library_name: diffusers
pipeline_tag: text-to-image
---
# 2D-Mix

Made with Automatic1111 Checkpoint Merger
Anything-V3.0-pruned + Waifu-v1-3-float16 + NAI + sd-v1-5-pruned-emaonly + trinart_stable_diffusion_epoch3
Examples:
<img src=https://i.imgur.com/EK3OeKY.png width=50% height=50%>
Christina Hendricks (realistic photo:1.0), (masterpiece:1.0), (highest quality:1.0), (high quality:1.0), (detailed face:1.0), (detailed eyes:1.0), highres
Negative prompt: text, signature, Doll, deformed, asymmetric, cropped, censored, frame, mock-up, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts, watermark, username, blurry, artist name
Steps: 30, Sampler: Euler a, CFG scale: 9, Seed: 365192021, Size: 512x512, Model hash: 63ac6702, Model: 2D-Mix, ENSD: 31337
<img src=https://i.imgur.com/ZTuxGqi.png width=50% height=50%>
beautiful geisha in full sky blue kimono facing away from the camera looking back over shoulder with arm extended to the right, elegant, vintage, ornate, art nouveau, complimentary colors, painted by Will Murai, Artgerm, Alphonse Mucha, Akihiko Yoshida, dramatic color, Phil Noto, Krenz Cushart, digital painting
Negative prompt: text, signature, Doll, deformed, asymmetric, cropped, censored, frame, mock-up, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts, watermark, username, blurry, artist name
Steps: 40, Sampler: Euler a, CFG scale: 11, Seed: 3633019598, Size: 512x512, Model hash: 63ac6702, Model: 2D-Mix, Clip skip: 2, ENSD: 31337
<img src=https://i.imgur.com/reY3XDN.png width=50% height=50%>
woman in colorful kimono AND man in coloful yukata
Negative prompt: gray, hazy, text, signature, cropped
Steps: 33, Sampler: Euler, CFG scale: 15, Seed: 4230961168, Size: 512x512, Model hash: 63ac6702, Model: 2D-Mix, Clip skip: 5, ENSD: 31337
<img src=https://i.imgur.com/0foCNeo.png width=50% height=50%>
woman in colorful kimono AND man in coloful yukata
Negative prompt: gray, hazy, text, signature, cropped
Steps: 33, Sampler: Euler, CFG scale: 15, Seed: 4230961169, Size: 512x512, Model hash: 63ac6702, Model: 2D-Mix, Clip skip: 5, ENSD: 31337

![showcase](https://huggingface.co/datasets/Guizmus/AnimeChanStyle/resolve/main/showcase_dataset.jpg)
This is the dataset used for making the model  : https://huggingface.co/Guizmus/AnimeChanStyle
The images were made by the users of Stable Diffusion discord using CreativeML-OpenRail-M licenced models, in the intent to make this dataset.
90 pictures captioned with their content by hand, with the suffix ",AnimeChan Style"
The collection process was made public during less than a day, until enough variety was introduced to train through a Dreambooth method a style corresponding to the different members of this community
The picture captioned are available in [this zip file](https://huggingface.co/datasets/Guizmus/AnimeChanStyle/resolve/main/AnimeChanStyle%20v2.3.zip)
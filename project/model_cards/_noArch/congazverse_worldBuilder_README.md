---
language:
- en
license: openrail++
thumbnail: "https://huggingface.co/congazverse/worldBuilder/resolve/main/shibuyajapan.png"
tags:
- stable-diffusion
- text-to-image
- image-to-image
- hdri
- 360 VR
---

## A HDRI-themed model to automatically generate HDRI and 360VR of any Indoor, Outdoor and Urban locations.
Textual Inversion embedding on 768x768 images of various HDRI.

Download both hdrimaker.ckpt and hdrimaker.yaml to your Stable-diffusion folder.

>>> link to Examples: https://panoraven.com/en/slider/qWY5x96nsK <<<

# Random prompts:
Here are some examples using modifiers after the subject, but feel free to use try writing your prompts without them at first. 


- Example prompt A:
  ![Fairy Town](https://huggingface.co/congazverse/worldBuilder/resolve/main/fairytown.png)
  close up of a street in a beautiful fairytale world with castles and stone houses, ( horizontal symmetry:1.5), (reflected horizontally:1.5), pixel perfect, perfectly seamless, soft edges, uhd, rtx, 
- negative prompt:
  low quality, not symmetrical, badly reflected, pixelated, soft blur, blurry, bad seams, not seamless, not patterned, misaligned 
  50 steps - CFG 8
  
- Example prompt B:
  ![Amazonian Forest](https://huggingface.co/congazverse/worldBuilder/resolve/main/amazonianjungle.png)
   a walk through the amazonian forest with colourful flowers and birds hidden in the trees
  50 steps - CFG 10
  
- Example prompt C:
  ![Ikea Loft](https://huggingface.co/congazverse/worldBuilder/resolve/main/ikealoft.png)
   a beautifully furnished loft with a high ceiling and modern Ikea furniture, ( horizontal symmetry:1.5), (reflected horizontally :1.5), 360VR, pixel perfect, perfectly seamless, soft edges, uhd, rtx, four walls
- Negative prompt:
  low quality, not symmetrical, badly reflected, pixelated, soft blur, blurry, bad seams, not seamless, not patterned, misaligned
  50 steps - CFG 10

# Tips:
-  Play with your image resolution to get a different result.

# Image resolution:
- Square format: 
768x768, 1024x1024, 1280x1280 > powerful GPU > 1536x1536
- HDRI format:
1024x512, 1280x640 > powerful GPU > 1536x768

# Upscaler:
LDSR is recommended
Scaling 1.5, 2 and 4

# HDRI preview:
- Panoraven is a brilliant website which allows you to quickly view and share your panorama (Registration isn't needed)
https://panoraven.com/en/share-360-photo
- 360 Panorama viewer is another simple viewer to preview your images https://renderstuff.com/tools/360-panorama-web-viewer/

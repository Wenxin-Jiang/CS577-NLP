---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- science
- trypophobia
widget:
- text: a zoomed out photo of a daffodil, with tryp22 pattern in the background, HD
---
 

<br>

<img src="https://github.com/nazianafis/Resources/blob/main/TRYP22/banner.png?raw=true" width=800 align="center">



## Description

This is a Stable Diffusion model fine-tuned on a private dataset containing 22 self-created TRYPOPHOBIA-TRIGGERING images, for the DreamBooth Hackathon 🔥 **science** theme. To participate or learn more, visit [this page](https://huggingface.co/dreambooth-hackathon). 

To generate your own images with this particular pattern, use prompt **"a photo of [your-subject] with tryp22 pattern in the background"**, or experiment with other variations.

<span style="color: #db2323; font-size: 1em;"> <b>GENERATED IMAGES MAY TRIGGER TRYPOPHOBIA. VIEWER DISCRETION IS ADVISED. </b> </span>



What is Trypophobia? <br>
Trypophobia refers to a strong fear or disgust of closely packed holes. The name combines the Greek words “trypa” (punching or drilling holes) and “phobia” (fear or aversion). The exact cause of trypophobia is unknown, and research in this area is limited.


My motivation behind choosing this topic: [Medium Link](https://medium.com/geekculture/stable-diffusion-model-fine-tuned-on-trypophobia-triggering-images-tryp22-pattern-ce1bb5259b37)



## Examples

1. *"a zoomed-out photo of [a single red rose, a blooming pink lotus, a daffodil], with tryp22 pattern in the background, HD"*
<img src="https://github.com/nazianafis/Resources/blob/main/TRYP22/flowers.png?raw=true" height=2700 width=900>


2. *"a macro shot of  a bug on a flower, tryp22 pattern background"*
<img src="https://github.com/nazianafis/Resources/blob/main/TRYP22/bugs.png?raw=true" height=2700 width=900>



3. *"a high-quality [close-up of a cat, close-up of a dog, photo of a frog], tryp22 pattern"*
<img src="https://github.com/nazianafis/Resources/blob/main/TRYP22/animals.png?raw=true" height=2700 width=900>



4. *"an HD photo of [Spiderman's, Hulk's, Batman's] face, with tryp22 pattern"*
<img src="https://github.com/nazianafis/Resources/blob/main/TRYP22/superheroes.png?raw=true" height=2700 width=900>



## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('nazianafis/tryp22-pattern')
image = pipeline().images[0]
image
```
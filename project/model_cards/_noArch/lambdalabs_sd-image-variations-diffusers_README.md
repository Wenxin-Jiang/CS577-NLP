---
thumbnail: "https://repository-images.githubusercontent.com/523487884/fdb03a69-8353-4387-b5fc-0d85f888a63f"
datasets:
- ChristophSchuhmann/improved_aesthetics_6plus
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- image-to-image
---

# Stable Diffusion Image Variations Model Card

📣 V2 model released, and blurriness issues fixed! 📣

🧨🎉 Image Variations is now natively supported in 🤗 Diffusers! 🎉🧨

![](https://raw.githubusercontent.com/justinpinkney/stable-diffusion/main/assets/im-vars-thin.jpg)

## Version 2

This version of Stable Diffusion has been fine tuned from [CompVis/stable-diffusion-v1-4-original](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original) to accept CLIP image embedding rather than text embeddings. This allows the creation of "image variations" similar to DALLE-2 using Stable Diffusion. This version of the weights has been ported to huggingface Diffusers, to use this with the Diffusers library requires the [Lambda Diffusers repo](https://github.com/LambdaLabsML/lambda-diffusers).

This model was trained in two stages and longer than the original variations model and gives better image quality and better CLIP rated similarity compared to the original version

See training details and v1 vs v2 comparison below.


## Example

Make sure you are using a version of Diffusers >=0.8.0 (for older version see the old instructions at the bottom of this model card)

```python
from diffusers import StableDiffusionImageVariationPipeline
from PIL import Image

device = "cuda:0"
sd_pipe = StableDiffusionImageVariationPipeline.from_pretrained(
  "lambdalabs/sd-image-variations-diffusers",
  revision="v2.0",
  )
sd_pipe = sd_pipe.to(device)

im = Image.open("path/to/image.jpg")
tform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize(
        (224, 224),
        interpolation=transforms.InterpolationMode.BICUBIC,
        antialias=False,
        ),
    transforms.Normalize(
      [0.48145466, 0.4578275, 0.40821073],
      [0.26862954, 0.26130258, 0.27577711]),
])
inp = tform(im).to(device).unsqueeze(0)

out = sd_pipe(inp, guidance_scale=3)
out["images"][0].save("result.jpg")
```

### The importance of resizing correctly... (or not)

Note that due a bit of an oversight during training, the model expects resized images without anti-aliasing. This turns out to make a big difference and is important to do the resizing the same way during inference. When passing a PIL image to the Diffusers pipeline antialiasing will be applied during resize, so it's better to input a tensor which you have prepared manually according to the transfrom in the example above!

Here are examples of images generated without (top) and with (bottom) anti-aliasing during resize. (Input is [this image](https://github.com/SHI-Labs/Versatile-Diffusion/blob/master/assets/ghibli.jpg))

![](alias-montage.jpg)

![](default-montage.jpg)

### V1 vs V2

Here's an example of V1 vs V2, version two was trained more carefully and for longer, see the details below. V2-top vs V1-bottom

![](v2-montage.jpg)

![](v1-montage.jpg)

Input images:

![](inputs.jpg)

One important thing to note is that due to the longer training V2 appears to have memorised some common images from the training data, e.g. now the previous example of the Girl with a Pearl Earring almosts perfectly reproduce the original rather than creating variations. You can always use v1 by specifiying `revision="v1.0"`.

v2 output for girl with a pearl earing as input (guidance scale=3)

![](earring.jpg)

# Training


**Training Procedure**
This model is fine tuned from Stable Diffusion v1-3 where the text encoder has been replaced with an image encoder. The training procedure is the same as for Stable Diffusion except for the fact that images are encoded through a ViT-L/14 image-encoder including the final projection layer to the CLIP shared embedding space. The model was trained on LAION improved aesthetics 6plus.

- **Hardware:** 8 x A100-40GB GPUs (provided by [Lambda GPU Cloud](https://lambdalabs.com/service/gpu-cloud))
- **Optimizer:** AdamW

- **Stage 1** - Fine tune only CrossAttention layer weights from Stable Diffusion v1.4 model
  - **Steps**: 46,000
  - **Batch:** batch size=4, GPUs=8, Gradient Accumulations=4. Total batch size=128
  - **Learning rate:** warmup to 1e-5 for 10,000 steps and then kept constant

- **Stage 2** - Resume from Stage 1 training the whole unet
  - **Steps**: 50,000
  - **Batch:** batch size=4, GPUs=8, Gradient Accumulations=5. Total batch size=160
  - **Learning rate:** warmup to 1e-5 for 5,000 steps and then kept constant


Training was done using a [modified version of the original Stable Diffusion training code](https://github.com/justinpinkney/stable-diffusion).


# Uses
_The following section is adapted from the [Stable Diffusion model card](https://huggingface.co/CompVis/stable-diffusion-v1-4)_

## Direct Use
The model is intended for research purposes only. Possible research areas and
tasks include

- Safe deployment of models which have the potential to generate harmful content.
- Probing and understanding the limitations and biases of generative models.
- Generation of artworks and use in design and other artistic processes.
- Applications in educational or creative tools.
- Research on generative models.

Excluded uses are described below.

 ### Misuse, Malicious Use, and Out-of-Scope Use

The model should not be used to intentionally create or disseminate images that create hostile or alienating environments for people. This includes generating images that people would foreseeably find disturbing, distressing, or offensive; or content that propagates historical or current stereotypes.

#### Out-of-Scope Use
The model was not trained to be factual or true representations of people or events, and therefore using the model to generate such content is out-of-scope for the abilities of this model.

#### Misuse and Malicious Use
Using the model to generate content that is cruel to individuals is a misuse of this model. This includes, but is not limited to:

- Generating demeaning, dehumanizing, or otherwise harmful representations of people or their environments, cultures, religions, etc.
- Intentionally promoting or propagating discriminatory content or harmful stereotypes.
- Impersonating individuals without their consent.
- Sexual content without consent of the people who might see it.
- Mis- and disinformation
- Representations of egregious violence and gore
- Sharing of copyrighted or licensed material in violation of its terms of use.
- Sharing content that is an alteration of copyrighted or licensed material in violation of its terms of use.

## Limitations and Bias

### Limitations

- The model does not achieve perfect photorealism
- The model cannot render legible text
- The model does not perform well on more difficult tasks which involve compositionality, such as rendering an image corresponding to “A red cube on top of a blue sphere”
- Faces and people in general may not be generated properly.
- The model was trained mainly with English captions and will not work as well in other languages.
- The autoencoding part of the model is lossy
- The model was trained on a large-scale dataset
  [LAION-5B](https://laion.ai/blog/laion-5b/) which contains adult material
  and is not fit for product use without additional safety mechanisms and
  considerations.
- No additional measures were used to deduplicate the dataset. As a result, we observe some degree of memorization for images that are duplicated in the training data.
  The training data can be searched at [https://rom1504.github.io/clip-retrieval/](https://rom1504.github.io/clip-retrieval/) to possibly assist in the detection of memorized images.

### Bias

While the capabilities of image generation models are impressive, they can also reinforce or exacerbate social biases.
Stable Diffusion v1 was trained on subsets of [LAION-2B(en)](https://laion.ai/blog/laion-5b/),
which consists of images that are primarily limited to English descriptions.
Texts and images from communities and cultures that use other languages are likely to be insufficiently accounted for.
This affects the overall output of the model, as white and western cultures are often set as the default. Further, the
ability of the model to generate content with non-English prompts is significantly worse than with English-language prompts.

### Safety Module

The intended use of this model is with the [Safety Checker](https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion/safety_checker.py) in Diffusers.
This checker works by checking model outputs against known hard-coded NSFW concepts.
The concepts are intentionally hidden to reduce the likelihood of reverse-engineering this filter.
Specifically, the checker compares the class probability of harmful concepts in the embedding space of the `CLIPModel` *after generation* of the images.
The concepts are passed into the model with the generated image and compared to a hand-engineered weight for each NSFW concept.


## Old instructions

If you are using a diffusers version <0.8.0 there is no `StableDiffusionImageVariationPipeline`,
in this case you need to use an older revision (`2ddbd90b14bc5892c19925b15185e561bc8e5d0a`) in conjunction with the lambda-diffusers repo:


First clone [Lambda Diffusers](https://github.com/LambdaLabsML/lambda-diffusers) and install any requirements (in a virtual environment in the example below):

```bash
git clone https://github.com/LambdaLabsML/lambda-diffusers.git
cd lambda-diffusers
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then run the following python code:

```python
from pathlib import Path
from lambda_diffusers import StableDiffusionImageEmbedPipeline
from PIL import Image
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionImageEmbedPipeline.from_pretrained(
"lambdalabs/sd-image-variations-diffusers",
revision="2ddbd90b14bc5892c19925b15185e561bc8e5d0a",
)
pipe = pipe.to(device)

im = Image.open("your/input/image/here.jpg")
num_samples = 4
image = pipe(num_samples*[im], guidance_scale=3.0)
image = image["sample"]

base_path = Path("outputs/im2im")
base_path.mkdir(exist_ok=True, parents=True)
for idx, im in enumerate(image):
    im.save(base_path/f"{idx:06}.jpg")
```



*This model card was written by: Justin Pinkney and is based on the [Stable Diffusion model card](https://huggingface.co/CompVis/stable-diffusion-v1-4).*
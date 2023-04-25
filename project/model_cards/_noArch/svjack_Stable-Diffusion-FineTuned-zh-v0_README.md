---
language: zh
license: other
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- zh
- Chinese
inference: false
extra_gated_prompt: |-
  One more step before getting this model.
  This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
  The CreativeML OpenRAIL License specifies: 

  1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
  2. rinna Co., Ltd. claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
  3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
  Please read the full license here: https://huggingface.co/spaces/CompVis/stable-diffusion-license
  
  By clicking on "Access repository" below, you accept that your *contact information* (email address and username) can be shared with the model authors as well.
    
extra_gated_fields:
 I have read the License and agree with its terms: checkbox
---


# Chinese Stable Diffusion Model Card

<!--
![rinna](https://github.com/rinnakk/japanese-clip/blob/master/data/rinna.png?raw=true)
-->

svjack/Stable-Diffusion-FineTuned-zh-v0 is a Chinese-specific latent text-to-image diffusion model capable of generating images given any Chinese text input.

This model was trained by using a powerful text-to-image model, [diffusers](https://github.com/huggingface/diffusers)
For more information about our training method, see [train_zh_model.py](https://github.com/svjack/Stable-Diffusion-Chinese-Extend/blob/main/train_zh_model.py).
With the help of a good baseline model [Taiyi-Stable-Diffusion-1B-Chinese-v0.1](IDEA-CCNL/Taiyi-Stable-Diffusion-1B-Chinese-v0.1) from [IDEA-CCNL](https://github.com/IDEA-CCNL/Fengshenbang-LM)

<!--
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rinnakk/japanese-stable-diffusion/blob/master/scripts/txt2img.ipynb)
-->

## Model Details
- **Developed by:** Zhipeng Yang
- **Model type:** Diffusion-based text-to-image generation model
- **Language(s):** Chinese
- **License:** [The CreativeML OpenRAIL M license](https://huggingface.co/spaces/CompVis/stable-diffusion-license) is an [Open RAIL M license](https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses), adapted from the work that [BigScience](https://bigscience.huggingface.co/) and [the RAIL Initiative](https://www.licenses.ai/) are jointly carrying in the area of responsible AI licensing. See also [the article about the BLOOM Open RAIL license](https://bigscience.huggingface.co/blog/the-bigscience-rail-license) on which our license is based.
- **Model Description:** This is a model that can be used to generate and modify images based on text prompts. It is a [Latent Diffusion Model (LDM)](https://arxiv.org/abs/2112.10752) that used [Stable Diffusion](https://github.com/CompVis/stable-diffusion) as a pre-trained model. 
- **Resources for more information:** [https://github.com/svjack/Stable-Diffusion-Chinese-Extend](https://github.com/svjack/Stable-Diffusion-Chinese-Extend)

## Examples

Firstly, install our package as follows. This package is modified [🤗's Diffusers library](https://github.com/huggingface/diffusers) to run Chinese Stable Diffusion.


```bash
diffusers==0.6.0
transformers
torch
datasets
accelerate
sentencepiece
```

Run this command to log in with your HF Hub token if you haven't before:

```bash
huggingface-cli login
```

Running the pipeline with the LMSDiscreteScheduler scheduler:

```python
from diffusers import StableDiffusionPipeline
pipeline = StableDiffusionPipeline.from_pretrained("svjack/Stable-Diffusion-FineTuned-zh-v0")
pipeline.safety_checker = lambda images, clip_input: (images, False)
pipeline = pipeline.to("cuda")

prompt = '女孩们打开了另一世界的大门'
image = pipeline(prompt, guidance_scale=7.5).images[0]
```
### Generator Results comparison
[https://github.com/svjack/Stable-Diffusion-Chinese-Extend](https://github.com/svjack/Stable-Diffusion-Chinese-Extend)

![0](https://github.com/svjack/Stable-Diffusion-Chinese-Extend/blob/main/imgs/dragon_v0.jpg?raw=true)
![1](https://github.com/svjack/Stable-Diffusion-Chinese-Extend/blob/main/imgs/dragon_style_v0.jpg?raw=true)
![2](https://github.com/svjack/Stable-Diffusion-Chinese-Extend/blob/main/imgs/girl_v0.jpg?raw=true)
![3](https://github.com/svjack/Stable-Diffusion-Chinese-Extend/blob/main/imgs/girl_style_v0.jpg?raw=true)

<!--
_Note: `JapaneseStableDiffusionPipeline` is almost same as diffusers' `StableDiffusionPipeline` but added some lines to initialize our models properly._ 


## Misuse, Malicious Use, and Out-of-Scope Use
_Note: This section is taken from the [DALLE-MINI model card](https://huggingface.co/dalle-mini/dalle-mini), but applies in the same way to Stable Diffusion v1._


The model should not be used to intentionally create or disseminate images that create hostile or alienating environments for people. This includes generating images that people would foreseeably find disturbing, distressing, or offensive; or content that propagates historical or current stereotypes.

### Out-of-Scope Use
The model was not trained to be factual or true representations of people or events, and therefore using the model to generate such content is out-of-scope for the abilities of this model.

### Misuse and Malicious Use
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
- The model was trained mainly with Japanese captions and will not work as well in other languages.
- The autoencoding part of the model is lossy
- The model was trained on a subset of a large-scale dataset
  [LAION-5B](https://laion.ai/blog/laion-5b/) which contains adult material
  and is not fit for product use without additional safety mechanisms and
  considerations.
- No additional measures were used to deduplicate the dataset. As a result, we observe some degree of memorization for images that are duplicated in the training data.
  The training data can be searched at [https://rom1504.github.io/clip-retrieval/](https://rom1504.github.io/clip-retrieval/) to possibly assist in the detection of memorized images.

### Bias

While the capabilities of image generation models are impressive, they can also reinforce or exacerbate social biases. 
Japanese Stable Diffusion was trained on Japanese datasets including [LAION-5B](https://laion.ai/blog/laion-5b/) with Japanese captions, 
which consists of images that are primarily limited to Japanese descriptions. 
Texts and images from communities and cultures that use other languages are likely to be insufficiently accounted for. 
This affects the overall output of the model.
Further, the ability of the model to generate content with non-Japanese prompts is significantly worse than with Japanese-language prompts.

### Safety Module

The intended use of this model is with the [Safety Checker](https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion/safety_checker.py) in Diffusers. 
This checker works by checking model outputs against known hard-coded NSFW concepts.
The concepts are intentionally hidden to reduce the likelihood of reverse-engineering this filter.
Specifically, the checker compares the class probability of harmful concepts in the embedding space of the `CLIPTextModel` *after generation* of the images. 
The concepts are passed into the model with the generated image and compared to a hand-engineered weight for each NSFW concept.


## Training

**Training Data**
We used the following dataset for training the model:

- Approximately 100 million images with Japanese captions, including the Japanese subset of [LAION-5B](https://laion.ai/blog/laion-5b/).

**Training Procedure**
Japanese Stable Diffusion has the same architecture as Stable Diffusion and was trained by using Stable Diffusion. Because Stable Diffusion was trained on English dataset and the CLIP tokenizer is basically for English, we had 2 stages to transfer to a language-specific model, inspired by [PITI](https://arxiv.org/abs/2205.12952).

1. Train a Japanese-specific text encoder with our Japanese tokenizer from scratch with the latent diffusion model fixed. This stage is expected to map Japanese captions to Stable Diffusion's latent space. 
2. Fine-tune the text encoder and the latent diffusion model jointly. This stage is expected to generate Japanese-style images more. 

[//]: # (_Note: Japanese Stable Diffusion is still running and this checkpoint is the current best one. We might update to a better checkpoint via this repository._)
-->
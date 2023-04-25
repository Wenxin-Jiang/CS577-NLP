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


# Chinese Stable Diffusion Pokemon Model Card

<!--
![rinna](https://github.com/rinnakk/japanese-clip/blob/master/data/rinna.png?raw=true)
-->

Stable-Diffusion-Pokemon-zh is a Chinese-specific latent text-to-image diffusion model capable of generating  Pokemon images given any text input.

This model was trained by using a powerful text-to-image model, [diffusers](https://github.com/huggingface/diffusers)
For more information about our training method, see [train_zh_model.py](https://github.com/svjack/Stable-Diffusion-Pokemon/blob/main/train_zh_model.py). 

<!--
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rinnakk/japanese-stable-diffusion/blob/master/scripts/txt2img.ipynb)
-->

## Model Details
- **Developed by:** Zhipeng Yang
- **Model type:** Diffusion-based text-to-image generation model
- **Language(s):** Chinese
- **License:** [The CreativeML OpenRAIL M license](https://huggingface.co/spaces/CompVis/stable-diffusion-license) is an [Open RAIL M license](https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses), adapted from the work that [BigScience](https://bigscience.huggingface.co/) and [the RAIL Initiative](https://www.licenses.ai/) are jointly carrying in the area of responsible AI licensing. See also [the article about the BLOOM Open RAIL license](https://bigscience.huggingface.co/blog/the-bigscience-rail-license) on which our license is based.
- **Model Description:** This is a model that can be used to generate and modify images based on text prompts. It is a [Latent Diffusion Model (LDM)](https://arxiv.org/abs/2112.10752) that used [Stable Diffusion](https://github.com/CompVis/stable-diffusion) as a pre-trained model. 
- **Resources for more information:** [https://github.com/svjack/Stable-Diffusion-Pokemon](https://github.com/svjack/Stable-Diffusion-Pokemon)

## Examples

Firstly, install our package as follows. This package is modified [🤗's Diffusers library](https://github.com/huggingface/diffusers) to run Chinese Stable Diffusion.


```bash
pip install git+https://github.com/rinnakk/japanese-stable-diffusion
pip install diffusers==0.4.1
sudo apt-get install git-lfs
git clone https://huggingface.co/svjack/Stable-Diffusion-Pokemon-zh
```

Run this command to log in with your HF Hub token if you haven't before:

```bash
huggingface-cli login
```

Running the pipeline with the LMSDiscreteScheduler scheduler:

```python
import torch
import pandas as pd

from torch import autocast
from diffusers import LMSDiscreteScheduler

import torch
from transformers import BertForSequenceClassification, BertConfig, BertTokenizer, BertForTokenClassification
from transformers import CLIPProcessor, CLIPModel
import numpy as np

from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import *
from japanese_stable_diffusion.pipeline_stable_diffusion import *

class StableDiffusionPipelineWrapper(StableDiffusionPipeline):

    @torch.no_grad()
    def __call__(
        self,
        prompt: Union[str, List[str]],
        height: int = 512,
        width: int = 512,
        num_inference_steps: int = 50,
        guidance_scale: float = 7.5,
        negative_prompt: Optional[Union[str, List[str]]] = None,
        num_images_per_prompt: Optional[int] = 1,
        eta: float = 0.0,
        generator: Optional[torch.Generator] = None,
        latents: Optional[torch.FloatTensor] = None,
        output_type: Optional[str] = "pil",
        return_dict: bool = True,
        callback: Optional[Callable[[int, int, torch.FloatTensor], None]] = None,
        callback_steps: Optional[int] = 1,
        **kwargs,
    ):
        if isinstance(prompt, str):
            batch_size = 1
        elif isinstance(prompt, list):
            batch_size = len(prompt)
        else:
            raise ValueError(f"`prompt` has to be of type `str` or `list` but is {type(prompt)}")

        if height % 8 != 0 or width % 8 != 0:
            raise ValueError(f"`height` and `width` have to be divisible by 8 but are {height} and {width}.")

        if (callback_steps is None) or (
            callback_steps is not None and (not isinstance(callback_steps, int) or callback_steps <= 0)
        ):
            raise ValueError(
                f"`callback_steps` has to be a positive integer but is {callback_steps} of type"
                f" {type(callback_steps)}."
            )

        # get prompt text embeddings
        text_inputs = self.tokenizer(
            prompt,
            padding="max_length",
            max_length=self.tokenizer.model_max_length,
            return_tensors="pt",
        )
        text_input_ids = text_inputs.input_ids

        if text_input_ids.shape[-1] > self.tokenizer.model_max_length:
            removed_text = self.tokenizer.batch_decode(text_input_ids[:, self.tokenizer.model_max_length :])
            logger.warning(
                "The following part of your input was truncated because CLIP can only handle sequences up to"
                f" {self.tokenizer.model_max_length} tokens: {removed_text}"
            )
            text_input_ids = text_input_ids[:, : self.tokenizer.model_max_length]
        text_embeddings = self.text_encoder(text_input_ids.to(self.device))[0]

        # duplicate text embeddings for each generation per prompt, using mps friendly method
        bs_embed, seq_len, _ = text_embeddings.shape
        text_embeddings = text_embeddings.repeat(1, num_images_per_prompt, 1)
        text_embeddings = text_embeddings.view(bs_embed * num_images_per_prompt, seq_len, -1)

        # here `guidance_scale` is defined analog to the guidance weight `w` of equation (2)
        # of the Imagen paper: https://arxiv.org/pdf/2205.11487.pdf . `guidance_scale = 1`
        # corresponds to doing no classifier free guidance.
        do_classifier_free_guidance = guidance_scale > 1.0
        # get unconditional embeddings for classifier free guidance
        if do_classifier_free_guidance:
            uncond_tokens: List[str]
            if negative_prompt is None:
                uncond_tokens = [""]
            elif type(prompt) is not type(negative_prompt):
                raise TypeError(
                    f"`negative_prompt` should be the same type to `prompt`, but got {type(negative_prompt)} !="
                    f" {type(prompt)}."
                )
            elif isinstance(negative_prompt, str):
                uncond_tokens = [negative_prompt]
            elif batch_size != len(negative_prompt):
                raise ValueError(
                    f"`negative_prompt`: {negative_prompt} has batch size {len(negative_prompt)}, but `prompt`:"
                    f" {prompt} has batch size {batch_size}. Please make sure that passed `negative_prompt` matches"
                    " the batch size of `prompt`."
                )
            else:
                uncond_tokens = negative_prompt

            max_length = text_input_ids.shape[-1]
            uncond_input = self.tokenizer(
                uncond_tokens,
                padding="max_length",
                max_length=max_length,
                truncation=True,
                return_tensors="pt",
            )
            uncond_embeddings = self.text_encoder(uncond_input.input_ids.to(self.device))[0]

            # duplicate unconditional embeddings for each generation per prompt, using mps friendly method
            seq_len = uncond_embeddings.shape[1]
            uncond_embeddings = uncond_embeddings.repeat(batch_size, num_images_per_prompt, 1)
            uncond_embeddings = uncond_embeddings.view(batch_size * num_images_per_prompt, seq_len, -1)

            # For classifier free guidance, we need to do two forward passes.
            # Here we concatenate the unconditional and text embeddings into a single batch
            # to avoid doing two forward passes
            text_embeddings = torch.cat([uncond_embeddings, text_embeddings])

        # get the initial random noise unless the user supplied it

        # Unlike in other pipelines, latents need to be generated in the target device
        # for 1-to-1 results reproducibility with the CompVis implementation.
        # However this currently doesn't work in `mps`.
        latents_shape = (batch_size * num_images_per_prompt, self.unet.in_channels, height // 8, width // 8)
        latents_dtype = text_embeddings.dtype
        if latents is None:
            if self.device.type == "mps":
                # randn does not work reproducibly on mps
                latents = torch.randn(latents_shape, generator=generator, device="cpu", dtype=latents_dtype).to(
                    self.device
                )
            else:
                latents = torch.randn(latents_shape, generator=generator, device=self.device, dtype=latents_dtype)
        else:
            if latents.shape != latents_shape:
                raise ValueError(f"Unexpected latents shape, got {latents.shape}, expected {latents_shape}")
            latents = latents.to(self.device)

        # set timesteps
        self.scheduler.set_timesteps(num_inference_steps)

        # Some schedulers like PNDM have timesteps as arrays
        # It's more optimized to move all timesteps to correct device beforehand
        timesteps_tensor = self.scheduler.timesteps.to(self.device)

        # scale the initial noise by the standard deviation required by the scheduler
        latents = latents * self.scheduler.init_noise_sigma

        # prepare extra kwargs for the scheduler step, since not all schedulers have the same signature
        # eta (η) is only used with the DDIMScheduler, it will be ignored for other schedulers.
        # eta corresponds to η in DDIM paper: https://arxiv.org/abs/2010.02502
        # and should be between [0, 1]
        accepts_eta = "eta" in set(inspect.signature(self.scheduler.step).parameters.keys())
        extra_step_kwargs = {}
        if accepts_eta:
            extra_step_kwargs["eta"] = eta

        for i, t in enumerate(self.progress_bar(timesteps_tensor)):
            # expand the latents if we are doing classifier free guidance
            latent_model_input = torch.cat([latents] * 2) if do_classifier_free_guidance else latents
            latent_model_input = self.scheduler.scale_model_input(latent_model_input, t)

            # predict the noise residual
            ###text_embeddings
            #print("before :" ,text_embeddings.shape)
            eh_shape = text_embeddings.shape
            if i == 0:
                eh_pad = torch.zeros((eh_shape[0], eh_shape[1], 768 - 512))
                eh_pad = eh_pad.to(self.device)
                text_embeddings = torch.concat([text_embeddings, eh_pad], -1)

            #print("after :" ,text_embeddings.shape)
            noise_pred = self.unet(latent_model_input, t, encoder_hidden_states=text_embeddings).sample

            # perform guidance
            if do_classifier_free_guidance:
                noise_pred_uncond, noise_pred_text = noise_pred.chunk(2)
                noise_pred = noise_pred_uncond + guidance_scale * (noise_pred_text - noise_pred_uncond)

            # compute the previous noisy sample x_t -> x_t-1
            latents = self.scheduler.step(noise_pred, t, latents, **extra_step_kwargs).prev_sample

            # call the callback, if provided
            if callback is not None and i % callback_steps == 0:
                callback(i, t, latents)

        latents = 1 / 0.18215 * latents
        image = self.vae.decode(latents).sample

        image = (image / 2 + 0.5).clamp(0, 1)

        # we always cast to float32 as this does not cause significant overhead and is compatible with bfloa16
        image = image.cpu().permute(0, 2, 3, 1).float().numpy()

        if self.safety_checker is not None:
            safety_checker_input = self.feature_extractor(self.numpy_to_pil(image), return_tensors="pt").to(
                self.device
            )
            image, has_nsfw_concept = self.safety_checker(
                images=image, clip_input=safety_checker_input.pixel_values.to(text_embeddings.dtype)
            )
        else:
            has_nsfw_concept = None

        if output_type == "pil":
            image = self.numpy_to_pil(image)

        if not return_dict:
            return (image, has_nsfw_concept)

        return StableDiffusionPipelineOutput(images=image, nsfw_content_detected=has_nsfw_concept)


scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012,
     beta_schedule="scaled_linear", num_train_timesteps=1000)

#pretrained_model_name_or_path = "zh_model_20000"
#### sudo apt-get install git-lfs
#### git clone https://huggingface.co/svjack/Stable-Diffusion-Pokemon-zh
pretrained_model_name_or_path = "Stable-Diffusion-Pokemon-zh"

tokenizer = BertTokenizer.from_pretrained(pretrained_model_name_or_path, subfolder = "tokenizer")
text_encoder = BertForTokenClassification.from_pretrained(pretrained_model_name_or_path, subfolder = "text_encoder")

vae = AutoencoderKL.from_pretrained(pretrained_model_name_or_path, subfolder="vae")
unet = UNet2DConditionModel.from_pretrained(pretrained_model_name_or_path, subfolder="unet")

tokenizer.model_max_length = 77
pipeline_wrap = StableDiffusionPipelineWrapper(
            text_encoder=text_encoder,
            vae=vae,
            unet=unet,
            tokenizer=tokenizer,
            scheduler=scheduler,
            safety_checker=StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"),
            feature_extractor=CLIPFeatureExtractor.from_pretrained("openai/clip-vit-base-patch32"),
        )
pipeline_wrap.safety_checker = lambda images, clip_input: (images, False)
pipeline_wrap = pipeline_wrap.to("cuda")

imgs = pipeline_wrap("一个头上戴着盆栽的卡通人物",
                    num_inference_steps = 100
)
image = imgs.images[0]
    
image.save("output.png")
```
### Generator Results comparison
[https://github.com/svjack/Stable-Diffusion-Pokemon](https://github.com/svjack/Stable-Diffusion-Pokemon)

![0](https://github.com/svjack/Stable-Diffusion-Pokemon/blob/main/imgs/zh_plant.jpg?raw=true)
![1](https://github.com/svjack/Stable-Diffusion-Pokemon/blob/main/imgs/zh_bird.jpg?raw=true)
![2](https://github.com/svjack/Stable-Diffusion-Pokemon/blob/main/imgs/zh_blue_dragon.jpg?raw=true)

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
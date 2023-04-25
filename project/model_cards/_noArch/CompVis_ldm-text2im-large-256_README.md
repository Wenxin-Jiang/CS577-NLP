---
license: apache-2.0
tags:
- pytorch
- diffusers
- text-to-image
---


# High-Resolution Image Synthesis with Latent Diffusion Models (LDM)

**Paper**: [High-Resolution Image Synthesis with Latent Diffusion Models (LDM)s](https://arxiv.org/abs/2112.10752)

**Abstract**:

*By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond. Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining. However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations. To enable DM training on limited computational resources while retaining their quality and flexibility, we apply them in the latent space of powerful pretrained autoencoders. In contrast to previous work, training diffusion models on such a representation allows for the first time to reach a near-optimal point between complexity reduction and detail preservation, greatly boosting visual fidelity. By introducing cross-attention layers into the model architecture, we turn diffusion models into powerful and flexible generators for general conditioning inputs such as text or bounding boxes and high-resolution synthesis becomes possible in a convolutional manner. Our latent diffusion models (LDMs) achieve a new state of the art for image inpainting and highly competitive performance on various tasks, including unconditional image generation, semantic scene synthesis, and super-resolution, while significantly reducing computational requirements compared to pixel-based DMs.*

## Safety
Please note that text-to-image models are known to at times produce harmful content. 
Please raise any concerns you may have.


## Usage

```python
# !pip install diffusers transformers
from diffusers import DiffusionPipeline

model_id = "CompVis/ldm-text2im-large-256"

# load model and scheduler
ldm = DiffusionPipeline.from_pretrained(model_id)

# run pipeline in inference (sample random noise and denoise)
prompt = "A painting of a squirrel eating a burger"
images = ldm([prompt], num_inference_steps=50, eta=0.3, guidance_scale=6).images

# save images
for idx, image in enumerate(images):
    image.save(f"squirrel-{idx}.png")
```

## Demo

[Hugging Face Spaces](https://huggingface.co/spaces/CompVis/ldm-text2im-large-256-diffusers)

## Samples

1. ![sample_0](https://huggingface.co/CompVis/ldm-text2im-large-256/resolve/main/images/squirrel-0.png)
2. ![sample_1](https://huggingface.co/CompVis/ldm-text2im-large-256/resolve/main/images/squirrel-1.png)
3. ![sample_2](https://huggingface.co/CompVis/ldm-text2im-large-256/resolve/main/images/squirrel-2.png)
4. ![sample_3](https://huggingface.co/CompVis/ldm-text2im-large-256/resolve/main/images/squirrel-3.png)

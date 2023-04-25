---
license: apache-2.0
tags:
- pytorch
- diffusers
- unconditional-image-generation
---

# Latent Diffusion Models (LDM)

**Paper**: [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)

**Abstract**:

*By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond. Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining. However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations. To enable DM training on limited computational resources while retaining their quality and flexibility, we apply them in the latent space of powerful pretrained autoencoders. In contrast to previous work, training diffusion models on such a representation allows for the first time to reach a near-optimal point between complexity reduction and detail preservation, greatly boosting visual fidelity. By introducing cross-attention layers into the model architecture, we turn diffusion models into powerful and flexible generators for general conditioning inputs such as text or bounding boxes and high-resolution synthesis becomes possible in a convolutional manner. Our latent diffusion models (LDMs) achieve a new state of the art for image inpainting and highly competitive performance on various tasks, including unconditional image generation, semantic scene synthesis, and super-resolution, while significantly reducing computational requirements compared to pixel-based DMs.*

**Authors**

*Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Björn Ommer*

## Usage

### Inference with a pipeline

```python
!pip install diffusers
from diffusers import DiffusionPipeline

model_id = "CompVis/ldm-celebahq-256"

# load model and scheduler
pipeline = DiffusionPipeline.from_pretrained(model_id)

# run pipeline in inference (sample random noise and denoise)
image = pipeline(num_inference_steps=200)["sample"]

# save image
image[0].save("ldm_generated_image.png")
```

### Inference with an unrolled loop

```python
!pip install diffusers
from diffusers import UNet2DModel, DDIMScheduler, VQModel
import torch
import PIL.Image
import numpy as np
import tqdm

seed = 3

# load all models
unet = UNet2DModel.from_pretrained("CompVis/ldm-celebahq-256", subfolder="unet")
vqvae = VQModel.from_pretrained("CompVis/ldm-celebahq-256", subfolder="vqvae")
scheduler = DDIMScheduler.from_config("CompVis/ldm-celebahq-256", subfolder="scheduler")

# set to cuda
torch_device = "cuda" if torch.cuda.is_available() else "cpu"

unet.to(torch_device)
vqvae.to(torch_device)

# generate gaussian noise to be decoded
generator = torch.manual_seed(seed)
noise = torch.randn(
    (1, unet.in_channels, unet.sample_size, unet.sample_size),
    generator=generator,
).to(torch_device)

# set inference steps for DDIM
scheduler.set_timesteps(num_inference_steps=200)

image = noise
for t in tqdm.tqdm(scheduler.timesteps):
    # predict noise residual of previous image
    with torch.no_grad():
        residual = unet(image, t)["sample"]

    # compute previous image x_t according to DDIM formula
    prev_image = scheduler.step(residual, t, image, eta=0.0)["prev_sample"]

    # x_t-1 -> x_t
    image = prev_image

# decode image with vae
with torch.no_grad():
    image = vqvae.decode(image)

# process image
image_processed = image.cpu().permute(0, 2, 3, 1)
image_processed = (image_processed + 1.0) * 127.5
image_processed = image_processed.clamp(0, 255).numpy().astype(np.uint8)
image_pil = PIL.Image.fromarray(image_processed[0])

image_pil.save(f"generated_image_{seed}.png")
```


## Samples

1. ![sample_0](https://huggingface.co/CompVis/latent-diffusion-celeba-256/resolve/main/images/generated_image_0.png)
2. ![sample_1](https://huggingface.co/CompVis/latent-diffusion-celeba-256/resolve/main/images/generated_image_1.png)
3. ![sample_2](https://huggingface.co/CompVis/latent-diffusion-celeba-256/resolve/main/images/generated_image_2.png)
4. ![sample_3](https://huggingface.co/CompVis/latent-diffusion-celeba-256/resolve/main/images/generated_image_3.png)

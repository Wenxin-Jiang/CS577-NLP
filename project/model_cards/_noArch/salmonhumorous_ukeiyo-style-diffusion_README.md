---
---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
datasets:
- ProGamerGov/StableDiffusion-v1-5-Regularization-Images
---
# Ukeiyo-style Diffusion

This is the fine-tuned Stable Diffusion model trained on traditional Japanese Ukeiyo-style images.
Use the tokens  **_ukeiyoddim style_**  in your prompts for the effect.
The model repo also contains a ckpt file , so that you can use the model with your own implementation of 
stable diffusion.

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
#!pip install diffusers transformers scipy torch
from diffusers import StableDiffusionPipeline
import torch
model_id = "salmonhumorous/ukeiyo-style-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "illustration of ukeiyoddim style landscape"
image = pipe(prompt).images[0]
image.save("./ukeiyo_landscape.png")
```

## Training procedure and data

The training for this model was done using a RTX 3090. The training was completed in 28 minutes for a total of 2000 steps. A total of 33 instance images (Images of the style I was aiming for) and 1k Regularization images was used. Regularization images dataset used by [ProGamerGov](https://huggingface.co/datasets/ProGamerGov/StableDiffusion-v1-5-Regularization-Images).

Training notebook used by [Shivam Shrirao](https://colab.research.google.com/github/ShivamShrirao/diffusers/blob/main/examples/dreambooth/DreamBooth_Stable_Diffusion.ipynb).

### Training hyperparameters

The following hyperparameters were used during training:
- number of steps : 2000
- learning_rate: 1e-6
- train_batch_size: 1
- scheduler_type: DDIM
- number of instance images : 33
- number of regularization images : 1000
- lr_scheduler : constant
- gradient_checkpointing

### Results

Below are the sample results for different training steps :
![img](https://huggingface.co/salmonhumorous/ukeiyo-style-diffusion/resolve/main/resourceImages/grid.png)

### Sample images by model trained for 2000 steps :

prompt = "landscape" 
![img](https://huggingface.co/salmonhumorous/ukeiyo-style-diffusion/resolve/main/resourceImages/collage1.png)
prompt = "ukeiyoddim style landscape"
![img](https://huggingface.co/salmonhumorous/ukeiyo-style-diffusion/resolve/main/resourceImages/collage2.png)
prompt = " illustration of ukeiyoddim style landscape"
![img](https://huggingface.co/salmonhumorous/ukeiyo-style-diffusion/resolve/main/resourceImages/collage2.png)

![img](https://huggingface.co/salmonhumorous/ukeiyo-style-diffusion/resolve/main/resourceImages/sample1.png)

### Acknowledgement

Many thanks to [nitrosocke](https://huggingface.co/nitrosocke), for inspiration and for the [guide](https://github.com/nitrosocke/dreambooth-training-guide). Also thanks, to all the amazing people making stable diffusion easily accessible for everyone.


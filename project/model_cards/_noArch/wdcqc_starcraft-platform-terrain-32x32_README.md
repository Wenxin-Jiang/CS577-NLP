---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- landscape
pipeline_tag: other
widget:
- text: isometric scspace terrain
datasets:
- wdcqc/starcraft-remastered-melee-maps
---

# DreamBooth model for Starcraft:Remastered terrain

This is a Stable Diffusion model fine-tuned on Starcraft terrain images on the Space Platform tileset with DreamBooth. It can be used by adding the `instance_prompt`: **isometric scspace terrain**

It was trained on 32x32 terrain images from 265 melee maps including original Blizzard maps and those downloaded from Battle.net, scmscx.com and broodwarmaps.net.

Run it on Huggingface Spaces:

https://huggingface.co/spaces/wdcqc/wfd

Or use this notebook on Colab:

https://colab.research.google.com/github/wdcqc/WaveFunctionDiffusion/blob/remaster/colab/WaveFunctionDiffusion_Demo.ipynb

In addition to Dreambooth, a custom VAE model (`AutoencoderTile`) is trained to encode and decode the latents to/from tileset probabilities ("waves") and then generated as Starcraft maps.

A WFC Guidance, inspired by the Wave Function Collapse algorithm, is also added to the pipeline. For more information about guidance please see this page: [Fine-Tuning, Guidance and Conditioning](https://github.com/huggingface/diffusion-models-class/tree/main/unit2)

This model was created as part of the DreamBooth Hackathon. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on starcraft terrain images for the landscape theme.

GitHub: https://github.com/wdcqc/WaveFunctionDiffusion


## Usage

First clone the git repository:

```bash
git clone https://github.com/wdcqc/WaveFunctionDiffusion.git
```

Then create a Jupyter notebook under the repository folder:

```python
# Load pipeline
from wfd.wf_diffusers import WaveFunctionDiffusionPipeline
from wfd.wf_diffusers import AutoencoderTile

wfc_data_path = "tile_data/wfc/platform_32x32.npz"

# Use CUDA (otherwise it will take 15 minutes)
device = "cuda"

tilenet = AutoencoderTile.from_pretrained(
    "wdcqc/starcraft-platform-terrain-32x32",
    subfolder="tile_vae"
).to(device)
pipeline = WaveFunctionDiffusionPipeline.from_pretrained(
    "wdcqc/starcraft-platform-terrain-32x32",
    tile_vae = tilenet,
    wfc_data_path = wfc_data_path
)
pipeline.to(device)

# Generate pipeline output
# need to include the dreambooth keyword "isometric scspace terrain"
pipeline_output = pipeline(
    "isometric scspace terrain, corgi",
    num_inference_steps = 50,
    wfc_guidance_start_step = 20,
    wfc_guidance_strength = 5,
    wfc_guidance_final_steps = 20,
    wfc_guidance_final_strength = 10,
)
image = pipeline_output.images[0]

# Display raw generated image
from IPython.display import display
display(image)

# Display generated image as tiles
wave = pipeline_output.waves[0]
tile_result = wave.argmax(axis=2)

from wfd.scmap import demo_map_image
display(demo_map_image(tile_result, wfc_data_path = wfc_data_path))

# Generate map file
from wfd.scmap import tiles_to_scx
import random, time

tiles_to_scx(
    tile_result,
    "outputs/generated_{}_{:04d}.scx".format(time.strftime("%Y%m%d_%H%M%S"), random.randint(0, 1e4)),
    wfc_data_path = wfc_data_path
)

# Open the generated map file in `outputs` folder with Scmdraft 2
```
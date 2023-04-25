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
widget:
- text: isometric starcraft ashworld terrain
datasets:
- wdcqc/starcraft-remastered-melee-maps
library_name: diffusers
---

# DreamBooth model for Starcraft:Remastered terrain

![INDEX_FULL.JPG](https://huggingface.co/wdcqc/starcraft-terrain-64x64/resolve/main/outputs/index_full.jpg)

This is a Stable Diffusion model fine-tuned on Starcraft terrain images with DreamBooth. It can be used by adding the `instance_prompt`: **isometric starcraft _tileset_ terrain**

The _tileset_ should be one of `ashworld`, `badlands`, `desert`, `ice`, `jungle`, `platform`, `twilight` or `installation`, which corresponds to Starcraft terrain tilesets.

It was trained on 64x64 terrain images from 1,808 melee maps including original Blizzard maps and those downloaded from Battle.net, scmscx.com and broodwarmaps.net.

Run it on Huggingface Spaces:

https://huggingface.co/spaces/wdcqc/wfd

Or use this notebook on Colab:

https://colab.research.google.com/github/wdcqc/WaveFunctionDiffusion/blob/remaster/colab/WaveFunctionDiffusion_Demo.ipynb

In addition to Dreambooth, a custom VAE model (`AutoencoderTile`) for each tileset is trained to decode the latents to tileset probabilities ("waves") and generate as Starcraft maps.

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
from wfd.scmap import find_tile_data, get_tileset_keyword

# Tilesets: ashworld, badlands, desert, ice, jungle, platform, twilight, install
tileset = "ice"

# The data files are located in wfd/scmap/tile_data/wfc
wfc_data_path = find_tile_data("wfc/{}_64x64.npz".format(tileset))

# Use CUDA (otherwise it will take 15 minutes)
device = "cuda"

tilenet = AutoencoderTile.from_pretrained(
    "wdcqc/starcraft-terrain-64x64",
    subfolder="tile_vae_{}".format(tileset)
).to(device)
pipeline = WaveFunctionDiffusionPipeline.from_pretrained(
    "wdcqc/starcraft-terrain-64x64",
    tile_vae = tilenet,
    wfc_data_path = wfc_data_path
)
pipeline.to(device)

# Double speed (only works for CUDA)
pipeline.set_precision("half")

# Generate pipeline output
# need to include the dreambooth keywords "isometric starcraft {tileset_keyword} terrain"
tileset_keyword = get_tileset_keyword(tileset)
pipeline_output = pipeline(
    "lost temple, isometric starcraft {} terrain".format(tileset_keyword),
    num_inference_steps = 50,
    guidance_scale = 3.5,
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
    "outputs/{}_{}_{:04d}.scx".format(tileset, time.strftime("%Y%m%d_%H%M%S"), random.randint(0, 1e4)),
    wfc_data_path = wfc_data_path
)

# Open the generated map file in `outputs` folder with Scmdraft 2
```
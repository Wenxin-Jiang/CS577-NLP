---
language:
- en
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- art
- artistic
- diffusers
- protogen
inference: true
license: creativeml-openrail-m
---
<center><img src="https://huggingface.co/darkstorm2150/Protogen_x5.3_Official_Release/resolve/main/Protogen%20x5.3-512.png" style="height:400px; border-radius: 7%; border: 10px solid #663380; padding-top:0px;" span title="Protogen x5.3 Raw Output"></center>



<center><h1>Protogen x5.3 (Photorealism) Official Release</h1></center>
<center><p><em>Research Model by <a href="https://instagram.com/officialvictorespinoza">darkstorm2150</a></em></p></center>
</div>

## Table of contents
* [General info](#general-info)
* [Granular Adaptive Learning](#granular-adaptive-learning)
* [Setup](#setup)
* [Space](#space)
* [CompVis](#compvis)
* [Diffusers](#🧨-diffusers)
* [Checkpoint Merging Data Reference](#checkpoint-merging-data-reference)
* [License](#license)

## General info

Protogen x5.3 - One Step Closer to Reality by [darkstorm2150](https://instagram.com/officialvictorespinoza)

Protogen was warm-started with [Stable Diffusion v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) and continued fine-tuned from [darkstorm2150/Protogen_x3.4_Official_Release](https://huggingface.co/darkstorm2150/Protogen_x3.4_Official_Release)
Robodiffusion has been removed and 10% Dreamlike-PhotoReal V.2 added, the result is better sampling at 768px to 1024px of humans and surroundings, The results are immediate!!!

Also this bad boy comes with a license, so do please read it, thank you!

* Model control

Now its recommended that you add nude, naked to your negative prompts, its a horny model, well 10% but still....cant be too careful!

As for realism, you can use this template

modelshoot style, (extremely detailed 8k wallpaper),a medium shot photo of a (what you want here), Intricate, High Detail, dramatic

It should also be very "dreambooth-able", being able to generate high fidelity faces with a little amount of steps (see [dreambooth](https://github.com/huggingface/diffusers/tree/main/examples/dreambooth)).

## Granular Adaptive Learning

Granular adaptive learning is a machine learning technique that focuses on adjusting the learning process at a fine-grained level, rather than making global adjustments to the model. This approach allows the model to adapt to specific patterns or features in the data, rather than making assumptions based on general trends.

Granular adaptive learning can be achieved through techniques such as active learning, which allows the model to select the data it wants to learn from, or through the use of reinforcement learning, where the model receives feedback on its performance and adapts based on that feedback. It can also be achieved through techniques such as online learning where the model adjust itself as it receives more data.

Granular adaptive learning is often used in situations where the data is highly diverse or non-stationary and where the model needs to adapt quickly to changing patterns. This is often the case in dynamic environments such as robotics, financial markets, and natural language processing.

## Setup
To run this model, download the model.ckpt and install it in your "stable-diffusion-webui\models\Stable-diffusion" directory

## Space

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/darkstorm2150/Stable-Diffusion-Protogen-webui)
### CompVis

## CKPT

[Download ProtoGen x5.3.ckpt (4.27GB)](https://huggingface.co/darkstorm2150/Protogen_v5.3_Official_Release/blob/main/ProtoGen_X5.3.ckpt)

[Download ProtoGen x5.3-pruned-fp16.ckpt (1.89GB)](https://huggingface.co/darkstorm2150/Protogen_x5.3_Official_Release/resolve/main/ProtoGen_X5.3-pruned-fp16.ckpt)

## Safetensors

[Download ProtoGen x5.3.safetensors (4.27GB)](https://huggingface.co/darkstorm2150/Protogen_x5.3_Official_Release/resolve/main/ProtoGen_X5.3.safetensors)

[Download ProtoGen x5.3-pruned-fp16.safetensors (1.89GB)](https://huggingface.co/darkstorm2150/Protogen_x5.3_Official_Release/resolve/main/ProtoGen_X5.3-pruned-fp16.safetensors)

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion Pipeline](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

```python
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch

prompt = (
"modelshoot style, (extremely detailed CG unity 8k wallpaper), full shot body photo of the most beautiful artwork in the world, "
"english medieval witch, black silk vale, pale skin, black silk robe, black cat, necromancy magic, medieval era, "
"photorealistic painting by Ed Blinkey, Atey Ghailan, Studio Ghibli, by Jeremy Mann, Greg Manchess, Antonio Moro, trending on ArtStation, "
"trending on CGSociety, Intricate, High Detail, Sharp focus, dramatic, photorealistic painting art by midjourney and greg rutkowski"
)

model_id = "darkstorm2150/Protogen_v5.3_Official_Release"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

image = pipe(prompt, num_inference_steps=25).images[0]

image.save("./result.jpg")
```

## PENDING DATA FOR MERGE, RPGv2 not accounted..
## Checkpoint Merging Data Reference

<style>
.myTable {
border-collapse:collapse; 
}
.myTable th { 
background-color:#663380;
color:white; 
}
.myTable td, .myTable th { 
padding:5px;
border:1px solid #663380; 
}
</style>
<table class="myTable">
<tr>
<th>Models</th>
<th>Protogen v2.2 (Anime)</th>
<th>Protogen x3.4 (Photo)</th>
<th>Protogen x5.3 (Photo)</th>
<th>Protogen x5.8 (Sci-fi/Anime)</th>
<th>Protogen x5.9 (Dragon)</th>
<th>Protogen x7.4 (Eclipse)</th>
<th>Protogen x8.0 (Nova)</th>
<th>Protogen x8.6 (Infinity)</th>
</tr>
<tr>
<td>seek_art_mega v1</td>
<td>52.50%</td>
<td>42.76%</td>
<td>42.63%</td>
<td></td>
<td></td>
<td></td>
<td>25.21%</td>
<td>14.83%</td>
</tr>
<tr>
<td>modelshoot v1</td>
<td>30.00%</td>
<td>24.44%</td>
<td>24.37%</td>
<td>2.56%</td>
<td>2.05%</td>
<td>3.48%</td>
<td>22.91%</td>
<td>13.48%</td>
</tr>
<tr>
<td>elldreth v1</td>
<td>12.64%</td>
<td>10.30%</td>
<td>10.23%</td>
<td></td>
<td></td>
<td></td>
<td>6.06%</td>
<td>3.57%</td>
</tr>
<tr>
<td>photoreal v2</td>
<td></td>
<td></td>
<td>10.00%</td>
<td>48.64%</td>
<td>38.91%</td>
<td>66.33%</td>
<td>20.49%</td>
<td>12.06%</td>
</tr>
<tr>
<td>analogdiffusion v1</td>
<td></td>
<td>4.75%</td>
<td>4.50%</td>
<td></td>
<td></td>
<td></td>
<td>1.75%</td>
<td>1.03%</td>
</tr>
<tr>
<td>openjourney v2</td>
<td></td>
<td>4.51%</td>
<td>4.28%</td>
<td></td>
<td></td>
<td>4.75%</td>
<td>2.26%</td>
<td>1.33%</td>
</tr>
<tr>
<td>hassan1.4</td>
<td>2.63%</td>
<td>2.14%</td>
<td>2.13%</td>
<td></td>
<td></td>
<td></td>
<td>1.26%</td>
<td>0.74%</td>
</tr>
<tr>
<td>f222</td>
<td>2.23%</td>
<td>1.82%</td>
<td>1.81%</td>
<td></td>
<td></td>
<td></td>
<td>1.07%</td>
<td>0.63%</td>
</tr>
<tr>
<td>hasdx</td>
<td></td>
<td></td>
<td></td>
<td>20.00%</td>
<td>16.00%</td>
<td>4.07%</td>
<td>5.01%</td>
<td>2.95%</td>
</tr>
<tr>
<td>moistmix</td>
<td></td>
<td></td>
<td></td>
<td>16.00%</td>
<td>12.80%</td>
<td>3.86%</td>
<td>4.08%</td>
<td>2.40%</td>
</tr>
<tr>
<td>roboDiffusion v1</td>
<td></td>
<td>4.29%</td>
<td></td>
<td>12.80%</td>
<td>10.24%</td>
<td>3.67%</td>
<td>4.41%</td>
<td>2.60%</td>
</tr>
<tr>
<td>RPG v3</td>
<td></td>
<td>5.00%</td>
<td></td>
<td></td>
<td>20.00%</td>
<td>4.29%</td>
<td>4.29%</td>
<td>2.52%</td>
</tr>
<tr>
<td>anything&everything</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>4.51%</td>
<td>0.56%</td>
<td>0.33%</td>
</tr>
<tr>
<td>dreamlikediff v1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>5.0%</td>
<td>0.63%</td>
<td>0.37%</td>
</tr>
<tr>
<td>sci-fidiff v1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3.10%</td>
</tr>
<tr>
<td>synthwavepunk v2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3.26%</td>
</tr>
<tr>
<td>mashupv2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>11.51%</td>
</tr>
<tr>
<td>dreamshaper 252</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>4.04%</td>
</tr>
<tr>
<td>comicdiff v2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>4.25%</td>
</tr>
<tr>
<td>artEros</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>15.00%</td>
</tr>
</table>

## License

By downloading you agree to the terms of these licenses

<a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license">CreativeML Open RAIL-M</a>

<a href="https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/blob/main/LICENSE.md">Dreamlike License</a>

<a href="https://huggingface.co/coreco/seek.art_MEGA/blob/main/LICENSE.txt">Seek Art Mega License</a>
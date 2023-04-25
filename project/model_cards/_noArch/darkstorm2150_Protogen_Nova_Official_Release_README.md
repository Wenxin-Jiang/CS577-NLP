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
widget:
- text: >-
    modelshoot style, (extremely detailed CG unity 8k wallpaper), full shot body
    photo of the most beautiful artwork in the world, english medieval witch,
    black silk vale, pale skin, black silk robe, black cat, necromancy magic,
    medieval era, photorealistic painting by Ed Blinkey, Atey Ghailan, Studio
    Ghibli, by Jeremy Mann, Greg Manchess, Antonio Moro, trending on ArtStation,
    trending on CGSociety, Intricate, High Detail, Sharp focus, dramatic,
    photorealistic painting art by midjourney and greg rutkowski
  example_title: Model photo
license: creativeml-openrail-m
---
<center><img src="https://huggingface.co/darkstorm2150/Protogen_Nova_Official_Release/resolve/main/Protogen%20Nova-512.png" style="height:400px; border-radius: 7%; border: 10px solid #663380; padding-top:0px;" span title="Protogen Nova Raw Output with a bladerunner 2049 embedding ;)"></center>



<center><h1>Protogen Nova</h1></center>
<center><p><em>Research Model by <a href="https://instagram.com/officialvictorespinoza">darkstorm2150</a></em></p></center>
</div>

## Table of contents
* [General info](#general-info)
* [Granular Adaptive Learning](#granular-adaptive-learning)
* [Setup](#setup)
* [Space](#space)
* [CompVis](#compvis)
* [Diffusers](#diffusers)
* [Checkpoint Merging Data Reference](#checkpoint-merging-data-reference)
* [License](#license)

## General info
The Protogen Nova is a checkpoint model that merges all the previous models into one

This merger includes
* Protogen v2.2 (Anime)
* Protogen x3.4 (Photorealism)
* ProtoGen x5.3 (Photorealism)
* ProtoGen x5.8 Rebuilt (Scifi+Anime)
* ProtoGen x5.9 (Dragon)
* ProtoGen x7.4 (Eclipse)

As part the of the checkpoint merging, Granular Adaptive Learning is a technique where traininig data is lessen selectively from 30% to 0.05%, and as the training is eventually saturated, the process reduces loss and introduces elements from various checkpoints

## Granular Adaptive Learning

Granular adaptive learning is a machine learning technique that focuses on adjusting the learning process at a fine-grained level, rather than making global adjustments to the model. This approach allows the model to adapt to specific patterns or features in the data, rather than making assumptions based on general trends.

Granular adaptive learning can be achieved through techniques such as active learning, which allows the model to select the data it wants to learn from, or through the use of reinforcement learning, where the model receives feedback on its performance and adapts based on that feedback. It can also be achieved through techniques such as online learning where the model adjust itself as it receives more data.

Granular adaptive learning is often used in situations where the data is highly diverse or non-stationary and where the model needs to adapt quickly to changing patterns. This is often the case in dynamic environments such as robotics, financial markets, and natural language processing.

## Setup
To run this model, download the model.ckpt and install it in your "stable-diffusion-webui\models\Stable-diffusion" directory

## Space


## CompVis


## Diffusers


## Checkpoint Merging Data Reference - PENDING DATA FOR MERGE, RPGv2 not accounted..

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
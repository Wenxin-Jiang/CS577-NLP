---
language:
- en
thumbnail: "https://huggingface.co/lexaprosaic/Imperial-Diffusion/blob/main/282D6868-546F-4841-B8DC-D12BBD54E52A.jpeg"
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- safetensors
- diffusers
inference: true
---

This is a preliminary model based on the famous collection of images taken by Sergei Prokudin-Gorskii, also known as the oldest and most comprehensive set of color photography known to exist. They were taken between the years of 1909 and 1915 in pre-revolutionary Russia, and offer a glimpse into the past that few other datasets can claim.

- Based on sd 1.5 fork
- Dataset consists of 1,277 pre-composited 512px images extracted from the Library of Congress public access portal
- Trained on an A100 GPU for six hours at 2000 step epochs
- Finetuned with large-scale EveryDream yaml
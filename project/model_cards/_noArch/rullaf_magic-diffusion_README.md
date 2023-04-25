---
datasets:
- rullaf/mtg-art
pipeline_tag: text-to-image
tags:
- art
---

# Magic Diffusion

A text2img model derived from StableDiffusion 1.5, fine-tuned with [EveryDream-trainer](https://github.com/victorchall/EveryDream-trainer) on a dataset consisting of post-processed Magic the Gathering card art crops (32,159), and hi-resolution images of the art (13,048). Annotations are based on card metadata and various other sources, including art description.

## Comparison

For MtG card art, this model performs comparably to Fantasy Card Diffusion v1. Both outperform generic models such as Open Journey v2, and baseline Stable Diffusion 1.5.

Conclusions:
* Magic Diffusion v3 likes to draw borders and frames
* Fantasy Card Diffusion v1 better preserves the MtG art style than Magic Diffusion v3, but it suffers from halftone/rosetta artifacts
* OpenJourney v2 is much hornier than the rest of the models, but the results for generic concepts are comparable
* Stable Diffusion v1.5 produces noticeably worse results than the other models, and requires a lot of negative keywords
* All models seem to benefit from feature description, such as “sliver creature with long beak and tendrils” instead of just “sliver”

### Settings

* Magic Diffusion v3 – this model
* Fantasy Card Diffusion v1 – https://huggingface.co/volrath50/fantasy-card-diffusion
* Open Journey v2 – https://huggingface.co/prompthero/openjourney-v2
* Stable Diffusion 1.5 – https://huggingface.co/runwayml/stable-diffusion-v1-5

All images were generated with identical settings:
* 40 steps / 80 steps
* 512x512
* CFG 7
* Euler a

Presumably the results could be further improved with better prompts, targeted at specific models, but that is not the point of this comparison. Magic Diffusion does better without “artist signature”, Fantasy Card Diffusion may benefit from “halftone rosetta”, and Stable Diffusion 1.5 likes to draw the card frames.

### Sliver

Prompt

> speedy sliver creature Creature a fast sliver is speeding through the Mardu steppe landscape Khans of tarkir  beautiful composition, MTG card art by John avon

Negative Prompt

> text frame card border human humanoid artist signature


![sliver comparison](https://huggingface.co/rullaf/magic-diffusion/resolve/main/examples/sliver.png)


### Taylor

Prompt

> mtg card art Taylor Swift wandering bard legendary creature human bard by chris rahn by volkan baga by zoltan boros armored bard taylor swift holding her weapons and instruments beautiful composition detailed realistic fantasy painting masterpiece best quality

Negative Prompt

> guitar lowres bad anatomy bad hands text error missing fingers extra digit fewer digits cropped worst quality low quality normal quality jpeg artifacts signature watermark username blurry

![taylor comparison](https://huggingface.co/rullaf/magic-diffusion/resolve/main/examples/taylor.png)



### Mox

Prompt

> mox topaz artifact on a chain rare mtg card art by dan frazier

Negative Prompt

> card border frame lowres cropped worst quality low quality normal quality jpeg artifacts watermark blurry

![mox comparison](https://huggingface.co/rullaf/magic-diffusion/resolve/main/examples/mox.png)

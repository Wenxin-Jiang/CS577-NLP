---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Avrik/abstract-anim-spritesheets/resolve/main/AnimationGrid.gif"
tags:
- stable-diffusion
- text-to-image
- image-to-image
---
# Abstract Animation Sprite Sheets

An experimental Dreambooth model trained on individual frames of looping 3D animations that were then laid out on a 4x4 grid. Generates sprite sheets that can create very interesting abstract animations.

Use the token **AbstrAnm spritesheet**. Size must be set at 512x512 or your outputs may not work properly.

**Example prompt:** <i>AbstrAnm spritesheet, animation of a red glowing orb in the sky, highly detailed, fog, atmosphere, glow, sprites, animated, abstract</i>
<br>
**Negative prompt:** <i>high contrast, text, overlay</i>
<br>
Steps: 30, Sampler: DPM++ 2M Karras, CFG scale: 8

Feel free to experiment with other types of prompts and/or model merges.

![Sample Generations](https://huggingface.co/Avrik/abstract-anim-spritesheets/resolve/main/AnimationGrid.gif)

You can also upscale it 4x to produce 512x512 animations. Used SD Upscale from AUTOMATIC1111's web UI to add more sharpness and detail.

![Upscaled](https://huggingface.co/Avrik/abstract-anim-spritesheets/resolve/main/AnimationGridUpscale.gif)

Discovered it's actually quite flexible and could even animate less abstract concepts.

![New Animations](https://huggingface.co/Avrik/abstract-anim-spritesheets/resolve/main/natureanims.gif)

**Prompt 1:** <i>AbstrAnm spritesheet, animation of magical swirling clouds in the clear blue sky, floating in crystal clear water, circular, sunny, timelapse, lens flare, nature, 35mm lens shot, photorealistic, sprites, animated, art by Greg Rutkowski</i>
<br>
**Negative prompt:** <i>text, overlay, abstract, boring, empty, barren, simple background</i>
<br>
Steps: 25, Sampler: DPM++ 2S a, CFG scale: 10

**Prompt 2:** <i>AbstrAnm spritesheet, animation of a beautiful flower blowing in the wind, serene, pink, sunny, timelapse, lens flare, nature, 35mm lens shot, photorealistic, sprites, animated, art by Greg Rutkowski</i>
**Negative prompt:** <i>text, overlay, abstract, boring, empty, barren, simple background</i>
<br>
Steps: 25, Sampler: DPM++ 2S a, CFG scale: 10

Some issues with this model:
- May not loop seamlessly
- Tends to be too noisy
- Sprites aren't usually perfect squares
- Small size and short animation (could experiment with training on larger resolutions in the future)
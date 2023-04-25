---
language: 
  - eng
thumbnail: "https://s3.amazonaws.com/moonup/production/uploads/1670737333905-630e54c81ef92d4e37a331b8.jpeg"
tags:
  - stable-diffusion
  - textual-inversion
  - embedding
  - text-to-image
license: "cc0-1.0"
---

# bad-artist 'negative' embedding

![grid-0.jpg](https://s3.amazonaws.com/moonup/production/uploads/1670737110801-630e54c81ef92d4e37a331b8.jpeg)
### Model Card WIP.

The images above were generated with **only "solo"** in the positive prompt, and "sketch by bad-artist" (this embedding) in the negative.
<br/>
The embedding uses only **2 tokens**.

Textual-inversion embedding for use in unconditional (negative) prompt.
<br/>
Inspired partly by https://huggingface.co/datasets/Nerfgun3/bad_prompt.

There are currently 2 version:
  - 'bad-artist': Not as strong, but produces pretty unique images (recommended)
  - 'bad-artist-anime': More generic anime style (this was the first version uploaded)

I recommend using with 'by', so for example "sketch **by bad-artist**", or "painting **by bad-artist**", or "photograph **by bad-artist**", etc.

Trained with 2 vectors per token for 15000 (1850x8) steps, at 500x500, on an Anything-v3-based model.

Full generation parameters for images above (using the 'bad-artist' version, not the 'bad-artist-anime' version):
```
solo
Negative prompt: sketch by bad-artist
Steps: 15, Sampler: DPM++ 2M Karras, CFG scale: 4, Seed: 1476197242, Size: 512x640, Clip skip: 2
```
---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-model
---

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('WiNE-iNEFF/Minecraft-Skin-Diffusion')
image = pipeline().images[0].convert('RGBA')
image
```

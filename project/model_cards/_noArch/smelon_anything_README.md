---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---
# Smelon.com备份
# Anything备份版

# Anything V3

欢迎使用 Anything V3 - weebs 的潜在扩散模型。该模型旨在通过几个提示生成高质量、高度详细的动漫风格。与其他动漫风格的 Stable Diffusion 模型一样，它也支持 danbooru 标签生成图像。

例如 **_1girl, white hair, golden eyes, beautiful eyes, detail, flower meadow, cumulonimbus clouds, lighting, detailed sky, garden_** 

## 🧨 Diffusers

该模型可以像任何其他稳定扩散模型一样使用。想要查询更多的信息，
请看 [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

您还可以将模型导出到 [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx) [MPS](https://huggingface.co/docs/diffusers/optimization/mps) 或者 [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Linaqruf/anything-v3.0"
branch_name= "diffusers"

pipe = StableDiffusionPipeline.from_pretrained(model_id, revision=branch_name, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "pikachu"
image = pipe(prompt).images[0]

image.save("./pikachu.png")
```

## 例子

以下是使用此模型生成的一些图像示例：

**动漫女孩:**
![Anime Girl](https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/1girl.png)
```
1girl, brown hair, green eyes, colorful, autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden
Steps: 50, Sampler: DDIM, CFG scale: 12
```
**动漫男孩:**
![Anime Boy](https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/1boy.png)
```
1boy, medium hair, blonde hair, blue eyes, bishounen, colorful, autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden
Steps: 50, Sampler: DDIM, CFG scale: 12
```
**风景:**
![Scenery](https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/scenery.png)
```
scenery, shibuya tokyo, post-apocalypse, ruins, rust, sky, skyscraper, abandoned, blue sky, broken window, building, cloud, crane machine, outdoors, overgrown, pillar, sunset
Steps: 50, Sampler: DDIM, CFG scale: 12
```

## 许可证

该模型是开放访问的，所有人都可以使用，CreativeML OpenRAIL-M 许可证进一步指定了权利和使用。
CreativeML OpenRAIL许可证规定。

1. 你不能使用该模型来故意生产或分享非法或有害的产出或内容。
2. 作者对你产生的产出没有任何权利，你可以自由使用它们，并对它们的使用负责，不得违反许可证中的规定。
3. 你可以重新分配权重，并在商业上和/或作为服务使用该模型。如果你这样做，请注意你必须包括与许可证中相同的使用限制，并将CreativeML OpenRAIL-M的副本分享给你的所有用户（请完全和仔细地阅读许可证）
[请在此阅读完整的许可证](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
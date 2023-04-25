---
tags:
- dreambooth-hackathon
pipeline_tag: text-to-image
---
中国奇谭第一季画风模型

import torch

from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("sd-dreambooth-library/cnstory", torch_dtype=torch.float16, use_auth_token=True)

pipe = pipe.to("cuda")

prompt = "a photograph of an astronaut riding a horse, cnstory artstyle"

image = pipe(prompt).images[0]

image.save(f"astronaut_rides_horse.png")

![下载.png](https://s3.amazonaws.com/moonup/production/uploads/1673866469001-63044d493926de1f7ec709f4.png)
![下载.png](https://s3.amazonaws.com/moonup/production/uploads/1673871174058-63044d493926de1f7ec709f4.png)
![img_v2_7ced34a2-4084-43ba-a02c-439b583eaf1g.jpg](https://s3.amazonaws.com/moonup/production/uploads/1673871184343-63044d493926de1f7ec709f4.jpeg)
![下载 (1).png](https://s3.amazonaws.com/moonup/production/uploads/1673871191196-63044d493926de1f7ec709f4.png)
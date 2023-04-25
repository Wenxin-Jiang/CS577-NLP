---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
- dreambooth
---
### Trained dreambooth with my personal images with Stable diffusion 1.5.

### Diffusers
```py
from diffusers import StableDiffusionPipeline
import torch

model_id = "mallapraveen/ai_art_sd_v1.5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "Portrait of praveen as Captain America, muscular, fantasy, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by Leonardo da Vinci and John Singer Sargent and Michelangelo"
image = pipe(prompt).images[0]  
    
image.save("capamerica.png")
```

Sample pictures of this concept:
  
![0](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/22.png)
![1](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/24.png)
![3](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/26.png)
![4](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/16.png)
![5](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/33.png)
![6](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/32.png)
![7](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/23.png)
![8](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/40.png)
![9](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/45.png)
![10](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/34.png)
![11](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/18.png)
![12](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/28.png)
![13](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/42.png)
![14](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/11.png)
![15](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/39.png)
![16](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/15.png)
![17](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/17.png)
![18](https://huggingface.co/mallapraveen/praveen/resolve/main/sample_images/14.png)
---
license: creativeml-openrail-m
language: 
  - en
thumbnail: "https://huggingface.co/Norod78/sd2-dreambooth-ClaymationXmas/resolve/main/collage_1.jpeg"
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
datasets:
- Norod78/ChristmasClaymation-blip-captions
inference: true
widget:
- text: Whilly Wonka, ClaymationXmas
- text: Pikachu, ClaymationXmas, very detailed, clean, high quality, sharp image, Naoto Hattori
---
# sd2-dreambooth-ClaymationXmas
## Use ClaymationXmas in your prompt

### WebUI Examples
See [examples](https://huggingface.co/Norod78/sd2-dreambooth-ClaymationXmas/tree/main/examples) folder for images generated with this model using a1111's WebUI

### WebUI Example Collage
![Collage 1](https://huggingface.co/Norod78/sd2-dreambooth-ClaymationXmas/resolve/main/collage_1.jpeg)
![Collage 2](https://huggingface.co/Norod78/sd2-dreambooth-ClaymationXmas/resolve/main/collage_2.jpeg)
![Collage 3](https://huggingface.co/Norod78/sd2-dreambooth-ClaymationXmas/resolve/main/collage_3.jpeg)
![Collage 4](https://huggingface.co/Norod78/sd2-dreambooth-ClaymationXmas/resolve/main/collage_4.jpeg)

```py

from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch

def main():
    #////////////////////////////////////////////
    seed = 42
    model = "Norod78/sd2-dreambooth-ClaymationXmas"
    #////////////////////////////////////////////

    torch.manual_seed(seed)
    generator = torch.Generator()
    generator.manual_seed(seed)

    scheduler = DPMSolverMultistepScheduler(
        beta_start=0.00085,
        beta_end=0.012,
        beta_schedule="scaled_linear",
        num_train_timesteps=1000,
        trained_betas=None,
        predict_epsilon=True,
        thresholding=False,
        algorithm_type="dpmsolver++",
        solver_type="midpoint",
        lower_order_final=True,
)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    pipe = StableDiffusionPipeline.from_pretrained(model, scheduler=scheduler,torch_dtype=dtype, generator=generator,use_auth_token=True).to(device)

    #////////////////////////////////////////////
    num_inference_steps = 20
    width=512
    height=512
    samples=4
    #////////////////////////////////////////////

    prompt = "Willy Wonka, ClaymationXmas"
    result = pipe([prompt] * samples, num_inference_steps=num_inference_steps, height=height, width=width)
    images = result["images"]
    for i, image in enumerate(images):       
        prompt_to_print = str(i) + "-" + prompt
        output_file = prompt_to_print.replace(" ", "_") + "-" + str(width) + "x" +str(height)+ "_" + str(num_inference_steps) + "steps" + "_seed" + str(seed) + ".jpg"
        image.save(output_file)
        print("Saved: " + str(output_file))

if __name__ == '__main__':
    main()
```

Fine Tuned by [@Norod78](https://twitter.com/Norod78)

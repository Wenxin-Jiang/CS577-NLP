---
tags:
- huggan
- gan
- unconditional-image-generation
datasets:
- huggan/few-shot-aurora
# See a list of available tags here:
# https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Types.ts#L12
# task: unconditional-image-generation or conditional-image-generation or image-to-image
license: mit
---

# Generate aurora image using FastGAN

## Model description

[FastGAN model](https://arxiv.org/abs/2101.04775) is a Generative Adversarial Networks (GAN) training on a small amount of high-fidelity images with minimum computing cost. Using a skip-layer channel-wise excitation module and a self-supervised discriminator trained as a feature-encoder, the model was able to converge after some hours of training for either 100 high-quality images or 1000 images datasets.

This model was trained on a dataset of 272 high-quality images of aurora.


#### How to use

```python
# Clone this model 
git clone https://huggingface.co/huggan/fastgan-few-shot-aurora/

def load_generator(model_name_or_path):
    generator = Generator(in_channels=256, out_channels=3)
    generator = generator.from_pretrained(model_name_or_path, in_channels=256, out_channels=3)
    _ = generator.eval()

    return generator
    
def _denormalize(input: torch.Tensor) -> torch.Tensor:
    return (input * 127.5) + 127.5
    
# Load generator
generator = load_generator("huggan/fastgan-few-shot-aurora")

# Generate a random noise image
noise = torch.zeros(1, 256, 1, 1, device=device).normal_(0.0, 1.0)
with torch.no_grad():
  gan_images, _ = generator(noise)
  
gan_images = _denormalize(gan_images.detach())
save_image(gan_images, "sample.png", nrow=1, normalize=True)
```

#### Limitations and bias

* Converge faster and better with small datasets (less than 1000 samples)

## Training data

[few-shot-aurora](https://huggingface.co/datasets/huggan/few-shot-aurora)

## Generated Images

![Example image](example.png)

### BibTeX entry and citation info

```bibtex
@article{FastGAN,
  title={Towards Faster and Stabilized GAN Training for High-fidelity Few-shot Image Synthesis},
  author={Bingchen Liu, Yizhe Zhu, Kunpeng Song, Ahmed Elgammal},
  journal={ICLR},
  year={2021}
}
```
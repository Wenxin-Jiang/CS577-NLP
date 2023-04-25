---
tags:
- huggan
- gan
- unconditional-image-generation
license: mit
datasets:
- huggan/smithsonian_butterflies_subset
# See a list of available tags here:
# https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Types.ts#L12

---

# Butterfly GAN

## Model description

Based on [paper:](https://openreview.net/forum?id=1Fqg133qRaI) *Towards Faster and Stabilized GAN Training for High-fidelity Few-shot Image Synthesis* 

which states:
"Notably, the model converges from scratch with just a **few hours of training** on a single RTX-2080 GPU, and has a consistent performance, even with **less than 100 training samples**"

also dubbed the Light-GAN model. This model was trained using the script [here](https://github.com/huggingface/community-events/tree/main/huggan/pytorch/lightweight_gan) which is adapted from the lucidrains [repo](https://github.com/lucidrains/lightweight-gan).

Differently from the script above, I used the transforms from the official repo. Because our training images were already cropped and aligned. 
official paper implementation [repo](https://github.com/odegeasslbc/FastGAN-pytorch)

```py
transform_list = [
            transforms.Resize((int(im_size),int(im_size))),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ]        
```

## Intended uses & limitations

Intended for fun & learning~

#### How to use

```python

import torch
from huggan.pytorch.lightweight_gan.lightweight_gan import LightweightGAN # install the community-events repo above

gan = LightweightGAN.from_pretrained("ceyda/butterfly_cropped_uniq1K_512")
gan.eval()
batch_size = 1
with torch.no_grad():
        ims = gan.G(torch.randn(batch_size, gan.latent_dim)).clamp_(0., 1.)*255
        ims = ims.permute(0,2,3,1).detach().cpu().numpy().astype(np.uint8)
        # ims is [BxWxHxC] call Image.fromarray(ims[0])
```

#### Limitations and bias

- During training I filtered the dataset to have only 1 butterfly from each species available.
Otherwise the model generated less varied butterflies  (a few species with more images would dominate).
- The dataset was also filtered using CLIP scores for ['pretty butterfly','one butterfly','butterfly with open wings','colorful butterfly']. 
While this was done to eliminate images that contained no butterflies(just scientific tags, cluttered images) from the [full dataset](https://huggingface.co/datasets/ceyda/smithsonian_butterflies). 
It is easy to imagine where this type of approach would be problematic in certain scenarios; who is to say which butterfly is "pretty" and should be in the dataset.ie; CLIP failing to identify a butterfly might exclude it from the dataset causing bias.

## Training data

1000 images are used, while it was possible to increase this number, we didn't have time to manually curate the dataset.

& also wanted to see if it was possible to do low data training as mention in the paper.
 
More details are on the [data card](https://huggingface.co/datasets/huggan/smithsonian_butterflies_subset)

## Training procedure

Trained on 2xA4000s for ~1day. Can see good results within 7-12h.
Importans params: "--batch_size 64 --gradient_accumulate_every 4 --image_size 512 --mixed_precision fp16"
Training logs can be seen [here](https://wandb.ai/cceyda/butterfly-gan/runs/2e0bm7h8?workspace=user-cceyda)

## Eval results

calculated FID score on 100 images. results for different checkpoints are [here](https://wandb.ai/cceyda/butterfly-gan-fid?workspace=user-cceyda)

but can't say it is too meaningful (due to the shortcomings of FID score)

## Generated Images

Play with the [demo](https://huggingface.co/spaces/huggan/butterfly-gan)

### BibTeX entry and citation info

Made during the huggan sprint.

Model trained by: Ceyda Cinarel https://twitter.com/ceyda_cinarel

Additional contributions by Jonathan Whitaker https://twitter.com/johnowhitaker
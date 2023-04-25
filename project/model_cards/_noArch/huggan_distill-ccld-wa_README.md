---
library_name : pytorch
tags:
- huggan
- diffusion
- text-to-image
datasets:
- huggan/wikiart
task: conditional-image-generation
license: mit
---

# Distill CLOOB-conditioned Latent Diffusion trained on WikiArt

## Model description

This is a smaller version of [this model](https://huggingface.co/huggan/ccld_wa), which is a cloob-conditioned latent diffusion model fine-tuned on the [WikiArt dataset](https://huggingface.co/datasets/huggan/wikiart), reducing the latent diffusion model size from 1.2B parameters to 105M parameters with a knowledge distillation method.

[CLOOB](https://ml-jku.github.io/cloob/) is a model that encodes images and texts in an unified latent space, similar to what OpenAI's CLIP does. The latent diffusion model takes a CLOOB-encoded latent vector as a condition, this can be from a pompt or an image.

## Intended uses & limitations

The latent diffusion model is the only difference with [the teacher model](https://huggingface.co/huggan/ccld_wa), the autoencoder was not changed, nor the CLOOB model. So these are not provided in this repository.


model_student.ckpt: The latent diffusion model checkpoint

#### How to use

You need some dependencies from multiple repositories linked in this repository : [CLOOB latent diffusion](https://github.com/JD-P/cloob-latent-diffusion) :

* [CLIP](https://github.com/openai/CLIP/tree/40f5484c1c74edd83cb9cf687c6ab92b28d8b656)
* [CLOOB](https://github.com/crowsonkb/cloob-training/tree/136ca7dd69a03eeb6ad525da991d5d7083e44055) : the model to encode images and texts in an unified latent space, used for conditioning the latent diffusion.
* [Latent Diffusion](https://github.com/CompVis/latent-diffusion/tree/f13bf9bf463d95b5a16aeadd2b02abde31f769f8) : latent diffusion model definition
* [Taming transformers](https://github.com/CompVis/taming-transformers/tree/24268930bf1dce879235a7fddd0b2355b84d7ea6) : a pretrained convolutional VQGAN is used as an autoencoder to go from image space to the latent space in which the diffusion is done.
* [v-diffusion](https://github.com/crowsonkb/v-diffusion-pytorch/tree/ffabbb1a897541fa2a3d034f397c224489d97b39) : contains some functions for sampling using a diffusion model with text and/or image prompts.

An example code to use the model to sample images from a text prompt can be seen in a [Colab Notebook](https://colab.research.google.com/drive/1XGHdO8IAGajnpb-x4aOb-OMYfZf0WDTi?usp=sharing), or directly in the [app source code](https://huggingface.co/spaces/huggan/wikiart-diffusion-mini/blob/main/app.py) for the Gradio demo on [this Space](https://huggingface.co/spaces/huggan/wikiart-diffusion-mini)

#### Limitations and bias

The student latent diffusion model was trained only on images from the WikiArt dataset, but the VQGAN autoencoder, the CLOOB model and the teacher latent diffusion model all come from pretrained checkpoints and were trained on images and texts from the internet.

According to the [Latent Diffusion paper](https://arxiv.org/abs/2112.10752): “Deep learning modules tend to reproduce or exacerbate biases that are already present in the data”. 

## Training data

This model was trained on the [WikiArt dataset](https://huggingface.co/datasets/huggan/wikiart) only. Only the images were used during training, no text prompt, so we did not use the information of style/genre/artist.

## Training procedure

This latent diffusion model was trained with a Knowledge Distillation process with [huggan/ccld_wa](https://huggingface.co/huggan/ccld_wa) as a teacher model. Training of the teacher model largely followed the guidelines in [JD-P's github repo](https://github.com/JD-P/cloob-latent-diffusion).
The model was fine-tuned on the Wikiart dataset for ~12 hours on 2 A6000 GPUs kindly provided by Paperspace. The knowledge distillation process was done on the WikiArt dataset as well. The training of the student model took 17 hours on 1 A6000 GPU provided by Paperspace. [Here](https://wandb.ai/gigant/distill-ccld/reports/Distill-Diffusion-105M--VmlldzoxODQwMTUz) is the `wandb` report for this training.

### Links

* [Model card for the teacher model on HuggingFace](https://huggingface.co/huggan/ccld_wa), trained by Jonathan Whitaker. He described the model and training procedure on his [blog post](https://datasciencecastnet.home.blog/2022/04/12/fine-tuning-a-cloob-conditioned-latent-diffusion-model-on-wikiart/)
* [Model card for the student model on HuggingFace](https://huggingface.co/huggan/distill-ccld-wa), trained by me. You can check my [WandB report](https://wandb.ai/gigant/distill-ccld/reports/Distill-Diffusion-105M--VmlldzoxODQwMTUz?accessToken=mfbrz1ghfakmh01lybsuycwm3qj3isv60uynnvmina3tiwz5e5ufbjui5xqhmaqi). This version has 105M parameters, against 1.2B parameters for the teacher version. It is lighter, and allows for faster inference, while maintaining some of the original model capability at generating paintings from prompts.
* [Gradio demo app on HuggingFace's Spaces](https://huggingface.co/spaces/huggan/wikiart-diffusion-mini) to try out the model with an online demo app
* [iPython Notebook](https://github.com/giganttheo/distill-ccld/blob/master/distillCCLD_(Wikiart)_demo.ipynb) to use the model in Python
* [WikiArt dataset on `datasets` hub](https://huggingface.co/datasets/huggan/wikiart)
* [GitHub repository](https://github.com/giganttheo/distill-ccld)

---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/images/showcase_main.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
- diffusers
library_name: "EveryDream"
inference: false
---

# Introduction

This is a collection of models made from and for the users of the Stable Diffusion Discord server. Different categories of channel exist, the "Dreamers Communities" presenting a panel of subjects, like Anime, 3D, or Architectural. Each of these channels has users posting images made through the use of Stable diffusion. After asking the users, and, depending on the activity of each channel, collecting a dataset from new submissions or from the history of the channel, I intend to build multiple models representing the style of each, so that users can produce things in the style they like and mix it with other things more easily.

Those are mainly done through the use of EveryDream, and should result in a Mega Model towards the end for the datasets that are compatible. Some model like the Anime one require to stay on a different starting point, and may not get merged.




# CharacterChan Style


## Dataset & training

This model was based on [RunwayML SD 1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) model with updated VAE.

The dataset was a collaborative effort of the Stable Diffusion #CharacterChan channel, made of pictures from the users themselves using their different techniques.

50 total pictures in the dataset, 160 repeats total each, over 4 Epoch on LR1e-6.

This was trained using EveryDream with a full caption of all training pictures.

The style will be called by the use of the token **CharacterChan Style**.

## Showcase & Downloads v1

![Showcase](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/images/showcase_CharacterChanStyle-v1.jpg)

[CKPT (2GB)](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/diffusers/CharacterChan/CharacterChanStyle-v1.ckpt)

[CKPT with training optimizers (11GB)](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/ckpt/CharacterChanStyle-v1_with_optimizers.ckpt)

[Diffusers](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/tree/main/diffusers/CharacterChan)

[Dataset](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/datasets/CharacterChanStyle-v1.zip)


# CreatureChan Style


## Dataset & training

This model was based on [RunwayML SD 1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) model with updated VAE.

The dataset was a collaborative effort of the Stable Diffusion #CreatureChan channel, made of pictures from the users themselves using their different techniques.

50 total pictures in the dataset, 160 repeats total each, over 4 Epoch on LR1e-6.

This was trained using EveryDream with a full caption of all training pictures.

The style will be called by the use of the token **CreatureChan Style**.

## Showcase & Downloads v1

![Showcase](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/images/showcase_CreatureChanStyle-v1.jpg)

[CKPT (2GB)](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/diffusers/CreatureChan/CreatureChanStyle-v1.ckpt)

[CKPT with training optimizers (11GB)](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/ckpt/CreatureChanStyle-v1_with_optimizers.ckpt)

[Diffusers](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/tree/main/diffusers/CreatureChan)

[Dataset](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/datasets/CreatureChanStyle-v1.zip)




# 3DChan Style


## Dataset & training

This model was based on [RunwayML SD 1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) model with updated VAE.

The dataset was a collaborative effort of the Stable Diffusion #3D channel, made of pictures from the users themselves using their different techniques.

120 total pictures in the dataset, 500 repeats total each, over 10 Epoch on LR1e-6.

This was trained using EveryDream with a full caption of all training pictures.

The style will be called by the use of the token **3D Style**.

Other significant tokens : rick roll, fullbody shot, bad cosplay man

## Showcase & Downloads v1

![Showcase](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/images/showcase_3DChanStyle-v1.jpg)

[CKPT (2GB)](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/diffusers/3DStyle/3DStyle-v1.ckpt)

[CKPT with training optimizers (11GB)](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/ckpt/3DStyle-v1_with_optimizers.ckpt)

[Diffusers](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/tree/main/diffusers/3DStyle)

[Dataset](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/datasets/3DChanStyle-v1.zip)




# AnimeChan Style

## Dataset & training

This model was based on [Trinart](https://huggingface.co/naclbit/trinart_stable_diffusion_v2) model.

The dataset was a collaborative effort of the Stable Diffusion #anime channel, made of pictures from the users themselves using their different techniques.

100 total pictures in the dataset, 300 repeats total each, over 6 Epoch on LR1e-6.

This was trained using EveryDream with a full caption of all training pictures.

The style will be called by the use of the token **AnimeChan Style**.

## Showcase & Downloads v2

![Showcase](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/images/showcase_AnimeChan-v2.jpg)

[CKPT (2GB)](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/diffusers/AnimeStyle/AnimeChanStyle-v2.ckpt)

[Diffusers](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/tree/main/diffusers/AnimeStyle)

[Dataset](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/datasets/AnimeChanStyle-v2.zip)

## Showcase & Downloads v1

![Showcase](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/images/showcase_AnimeChan-v1.jpg)

[CKPT (2GB)](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/ckpt/AnimeChanStyle-v1.ckpt)

[Dataset](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/datasets/AnimeChanStyle-v1.zip)




# License

These models are open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
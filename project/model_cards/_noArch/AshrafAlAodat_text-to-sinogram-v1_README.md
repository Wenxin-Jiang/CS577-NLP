---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
inference: true
extra_gated_prompt: |-
  This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
  The CreativeML OpenRAIL License specifies: 

  1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
  2. Riffusion claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
  3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
  Please read the full license carefully here: https://huggingface.co/spaces/CompVis/stable-diffusion-license
      
extra_gated_heading: Please read the LICENSE to access this model
---

# Text-To-Sinogram

is an app for generation of sinogram with stable diffusion.

* Model checkpoint: https://huggingface.co/AshrafAlAodat/text-to-sinogram-v1

This repository contains the model files, including:

 * a diffusers formated library
 * a compiled checkpoint file
 * a traced unet for improved inference speed

## Model V1

It is a latent text-to-image diffusion model capable of generating sinogram images given any text input. These sinograms can be reconstructed back to the original image.

The model was created by [Ashraf Al-Aodat](https://github.com/Ashraf-Al-Aodat) as a proof of concept.

You can use the model directly.

The model was created by fine-tuning the **Stable-Diffusion-v1-5** checkpoint. Read about Stable Diffusion here [🤗's Stable Diffusion blog](https://huggingface.co/blog/stable_diffusion).

## Model Output

Examples of some generated sinograms using the prompt **bat**..

![sinograms](https://huggingface.co/AshrafAlAodat/text-to-sinogram-v1/resolve/main/sig.png)

After image reconstruction..

![reconstructions](https://huggingface.co/AshrafAlAodat/text-to-sinogram-v1/resolve/main/rec.png)

### Model Details
- **Developed by:** Ashraf Al-Aodat
- **Model type:** Diffusion-based text-to-image generation model
- **Language(s):** English
- **License:** [The CreativeML OpenRAIL M license](https://huggingface.co/spaces/CompVis/stable-diffusion-license) is an [Open RAIL M license](https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses), adapted from the work that [BigScience](https://bigscience.huggingface.co/) and [the RAIL Initiative](https://www.licenses.ai/) are jointly carrying in the area of responsible AI licensing. See also [the article about the BLOOM Open RAIL license](https://bigscience.huggingface.co/blog/the-bigscience-rail-license) on which our license is based.
- **Model Description:** This is a model that can be used to generate and modify images based on text prompts. It is a [Latent Diffusion Model](https://arxiv.org/abs/2112.10752) that uses a fixed, pretrained text encoder ([CLIP ViT-L/14](https://arxiv.org/abs/2103.00020)) as suggested in the [Imagen paper](https://arxiv.org/abs/2205.11487).

### Direct Use 
The model is intended for research purposes only. Possible research areas and
tasks include

- Generation of artworks, and use in creative processes.
- Applications in educational or creative tools.
- Research on generative models.

### Datasets
The modeal was trained on the [sinograms](https://huggingface.co/datasets/AshrafAlAodat/sinograms) dataset.

### Fine Tuning

Check out the [diffusers training examples](https://huggingface.co/docs/diffusers/training/overview) from Hugging Face. Fine tuning requires a dataset of sinogram images of objects, with associated text describing them. Note that the CLIP encoder is able to understand and connect many words even if they never appear in the dataset. It is also possible to use a [dreambooth](https://huggingface.co/blog/dreambooth) method to get custom styles.

## Citation

If you build on this work, please cite it as follows:

```
@article{TODO,
  author = {Al-Aodat, Ashraf*},
  title = {{Text-To-Sinogram - Stable diffusion for sinogram generation a proof of concept}},
  year = {2022}
}
```

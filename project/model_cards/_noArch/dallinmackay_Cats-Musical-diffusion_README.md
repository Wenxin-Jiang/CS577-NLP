---
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/dallinmackay/Cats-Musical-diffusion/resolve/main/cats_preview1.jpg"
tags:
- stable-diffusion
- text-to-image
---
### Cats the Musical Diffusion

This is a fine-tuned Stable Diffusion model (based on v1.5) trained on screenshots from the film **_Cats (2019)_**. Use the token **_ctsmscl_** at the BEGINNING of your prompts to use the style (e.g., "ctsmscl, thanos"). This model works best with the Euler sampler (NOT Euler_a). It will take some experimenting to get good results, my sample images are heavily cherry-picked this time (~10% success rate for likeness of real people). Use (prompt) [weighting] to balance the style with the character.

[CKPT download link](https://huggingface.co/dallinmackay/Cats-Musical-diffusion/resolve/main/Cats-Musical-Style-ctsmscl.ckpt)

The model you didn't ask for, and didn't know you needed. Trained on the horribly uncanny musical, Cats, which was based on an even more horrible previous version, which was based on a horrible live stage musical. It has endured all opposition, and who am I to stand in it's way? This model is inevitable.

--

**Cat people rendered with this model:**
  
  _prompt and settings used: **(ctsmscl), [person]** | **Steps: 45, Sampler: Euler, CFG scale: 5**_
![Character Samples](https://huggingface.co/dallinmackay/Cats-Musical-diffusion/resolve/main/cats_preview1.jpg)

--

**Roughly the entire main cast of Game of Thrones as cats:**
![Character Samples2](https://huggingface.co/dallinmackay/Cats-Musical-diffusion/resolve/main/cats_preview2.jpg)

--

This model was trained with Dreambooth, using TheLastBen colab notebook
--
### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

--
[![Become A Patreon](https://badgen.net/badge/become/a%20patron/F96854)](https://www.patreon.com/dallinmackay)
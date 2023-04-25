---
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/dallinmackay/JWST-Deep-Space-diffusion/resolve/main/previewJWST.jpg"
tags:
- stable-diffusion
- text-to-image
---
### JWST Deep Space Diffusion

This is a fine-tuned Stable Diffusion model (based on v1.5) trained on images taken by the **_James Webb Space Telescope_**, as well as Judy Schmidt. Use the token **_JWST_** in your prompts to use the style (e.g., "jwst, green spiral galaxy").

[CKPT download link](https://huggingface.co/dallinmackay/JWST-Deep-Space-diffusion/resolve/main/JWST-Deep-Space.ckpt)

**Images rendered with this model:**
  
  _prompt and settings used: **"JWST"** | **Steps: 25, Sampler: Euler_a, CFG scale: 7**_
![Image Samples](https://huggingface.co/dallinmackay/JWST-Deep-Space-diffusion/resolve/main/previewJWST.jpg)

--
[![Become A Patreon](https://badgen.net/badge/become/a%20patron/F96854)](https://www.patreon.com/dallinmackay) 
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
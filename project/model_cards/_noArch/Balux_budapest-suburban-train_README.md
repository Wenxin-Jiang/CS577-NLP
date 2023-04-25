---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
- TheLastBen
- DreamBooth
---
### Budapest Suburban Train Rebirth

The idea here was to take the (in-)famous suburban train of Budapest, 
(the LEW MXA or as we call it HÉV that is in operation since 1971) 
and inject its characteristics into modern transportation vehicles.  

Sample pictures of this concept:  

  
  ![4](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00025-1456692169-bphev_that_lo___.png)
      ![0](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00029-1456692168-bphev_that_lo___.png)
      ![1](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00012-4167716434-bphev_that_lo___.png)
      ![2](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00010-688308651-bphev_that_loo____(1).png)
      ![3](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00016-128078272-bphev_that_loo___.png)
      ![5](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00009-688308651-bphev_that_loo___.png)
      ![6](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00019-2714121182-bphev_that_lo___.png)
      ![7](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00013-670878413-bphev_that_loo____(1).png)
      ![8](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00015-1858717141-bphev_that_lo___.png)
      ![9](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00018-153612987-bphev_that_loo___.png)
      ![10](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00026-1456692168-bphev_that_lo___.png)
      ![11](https://huggingface.co/Balux/budapest-suburban-train/resolve/main/sample_images/00024-1560078007-bphev_that_lo___.png)


The instance of the LEW MXA can be invoked by the token "bphev" in the prompt.  

The 1st sample image was generated with the followings:  
  Prompt: bphev that looks like a (scifi) vehicle , sharp, photo realistic, cinematic light, focus, photorealism, beautiful reflections  
  Negative prompt: blur, blurred, out of frame, low resolution, low quality, cropped, (noise)  
  Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1456692169, Size: 512x512, Model hash: 5f06aa6f  

All the rest was created following the above recipe with mild alternations + img2img upscaling.

Test the concept on Google Colab: [fast-Colab-A1111](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb)

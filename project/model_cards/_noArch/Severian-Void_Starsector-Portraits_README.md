---
language:
- en
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
license: creativeml-openrail-m

---
# Starsector Portraits

This is a fine-tuned Stable Diffusion model trained on images from the videogame Starsector in order to provide mod makers with access to more easily creatable portraits in the style of the game.

Use the token **starsectorportrait** in your prompts for the effect.

# Example prompts & tips
"a starsectorportrait of a person wearing a green balaclava and armored spacesuit"

"an older man wearing a fancy suit with a purple cape, style of starsectorportrait"

Even with the training I found it was still useful to include some other phrases and tokens that can be helpful to more accurately match the base art style:

**sabattier effect** to get a more accurate lighting effect

**brush strokes** to achieve the more painterly feel of the portraits

**conte** if brush strokes is not doing enough or adding colorful artifacts to images this is another option

# Sample images from the model:
![output Samples](https://huggingface.co/Severian-Void/Starsector-Portraits/resolve/main/3_IMAGES/patherflightschool.png)
![output Samples](https://huggingface.co/Severian-Void/Starsector-Portraits/resolve/main/3_IMAGES/RandomPortraits.png)

# File Versions and Comparison Details
All model versions are trained using a hand labeled image set of 556 images with black/white backgrounds and flipped versions of the same images

Any model versions with **pploss** in the name were trained with prior preservation loss enabled and used a regularization set of 8000 portrait images comprised of photos/paintings/digitalart of humans in modern day attire.

**1.5 trained model vs 1.4 trained model and hypernetwork presence**

![output Samples](https://huggingface.co/Severian-Void/Starsector-Portraits/resolve/main/3_IMAGES/1.4_vs_1.5_comparrison.png)

**2.0 trained model vs 2.1 finetuned model**

![output Samples](https://huggingface.co/Severian-Void/Starsector-Portraits/resolve/main/3_IMAGES/v2.0_vs_v2.1_comparison.png)

**CFG and SAMPLE STEP comparisons between rc_v1 model files**

(prompt: "a starsectorportrait of a person" sampler: euler_a)

![output Samples](https://huggingface.co/Severian-Void/Starsector-Portraits/resolve/main/3_IMAGES/rc_v1_step_compare.png)
![output Samples](https://huggingface.co/Severian-Void/Starsector-Portraits/resolve/main/3_IMAGES/rc_v1_cfg_compare.png)

**Adaptability comparisons between rc_v1 model files**

(prompt: "a starsectorportrait of an alien cat" sampler: euler_a)

![output Samples](https://huggingface.co/Severian-Void/Starsector-Portraits/resolve/main/3_IMAGES/rc_v1_adaptability.png)

# Hypernetworks
Fine tuning hypernetworks to help with various aspects of image generation. 

**HN_ssportrait_v2_1.5_13431.pt:** Hypernetwork finetuned for the 1.5 trained model on the full data set it greatly improves overall accuracy of the the generated portraits. I highly recommend using this along with the 1.5 model for all portrait generation.

**HN_ssportrait_rc_v1_no-helmet_finetune_v1:** Hypernetwork finetuned for the 1.4 trained model using the full data set minus images with faces that are covered, should promote much cleaner facial detail and image quality while still providing for a decent range of helmet generation. Negative prompting for helmet can also help if you find helmets are still generated too frequently.
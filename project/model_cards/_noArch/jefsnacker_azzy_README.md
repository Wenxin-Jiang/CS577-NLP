---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- animal
widget:
- text: portrait of azzy cat anthro as a dapper bartender with a big, fluffy tail, retro futurism, art deco, detailed, painterly digital art by wlop and cory loftis and delphin enjolras, 🐿🍸🍋, furaffinity, trending on artstation
---
# Dreambooth model of my cat azzy
#### Model by [jefsnacker](https://huggingface.co/jefsnacker) and [chel-z](https://huggingface.co/chel-z)
<img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy08.jpeg" style="height:200px">

This is a Stable Diffusion model fine-tuned on pictures of Azriel with DreamBooth.
It can be used by modifying the `instance_prompt`: **photo of azzy cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organization page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

You can also train your own concepts and upload them to the library by using [this notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_training.ipynb).
And you can run your new concept via `diffusers`: [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb).

## Example Output
---

<img src="https://huggingface.co/jefsnacker/azzy/resolve/main/output_images/overwatch.png">

**Prompt:** azzy cat as an anime character in overwatch\
**Guidance Scale:** 7\
**Seed:** 42

---
<img src="https://huggingface.co/jefsnacker/azzy/resolve/main/output_images/dapper.png">

**Prompt:** portrait of azzy cat anthro as a dapper bartender with a big, fluffy tail, retro futurism, art deco, detailed, painterly digital art by wlop and cory loftis and delphin enjolras, 🐿🍸🍋, furaffinity, trending on artstation\
**Guidance Scale:** 9\
**Seed:** 42

---

<img src="https://huggingface.co/jefsnacker/azzy/resolve/main/output_images/armored.png">

**Prompt:** Portrait painting of a cute azzy cat with armor, ultra realistic, concept art, intricate details, eerie, highly detailed, photorealistic, octane render, 8 k, unreal engine. art by artgerm and greg rutkowski and charlie bowater and magali villeneuve and alphonse mucha\
**Guidance Scale:** 12\
**Seed:** 42

---

<img src="https://huggingface.co/jefsnacker/azzy/resolve/main/output_images/cartoon.png">

**Prompt:** Cute and adorable cartoon fluffy azzy cat with cap, fantasy, dreamlike, city scenario, surrealism, super cute, trending on artstation\
**Guidance Scale:** 7\
**Seed:** 42


---

<img src="https://huggingface.co/jefsnacker/azzy/resolve/main/output_images/tux.png">

**Prompt:** azzy cat wearing a tuxedo at a wedding\
**Guidance Scale:** 4.5\
**Seed:** 42

---

<img src="https://huggingface.co/jefsnacker/azzy/resolve/main/output_images/software.png">

**Prompt:** portrait of azzy cat as the average ai software engineer working at a computer\
**Guidance Scale:** 5\
**Seed:** 42

---

<img src="https://huggingface.co/jefsnacker/azzy/resolve/main/output_images/tekken.png">

**Prompt:** Screenshot of game on ps 4 azzy cat fighting against godzilla character, xp bars, health bars, unreal engine\
**Guidance Scale:** 7\
**Seed:** 42

---

<img src="https://huggingface.co/jefsnacker/azzy/resolve/main/output_images/swimming.png">

**Prompt:** azzy cat swimming underwater\
**Guidance Scale:** 6\
**Seed:** 42

---

<img src="https://huggingface.co/jefsnacker/azzy/resolve/main/output_images/spacesuit.png">

**Prompt:** photo of azzy cat in a spacesuit\
**Guidance Scale:** 4\
**Seed:** 42

## Sample Images
12 images of Azriel were used to train the model.

<table>
  <tr>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy00.jpg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy01.jpeg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy02.jpeg" style="height:200px"> </td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy03.jpg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy04.jpg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy05.jpg" style="height:200px"> </td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy06.jpeg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy07.jpeg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy08.jpeg" style="height:200px"> </td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy09.jpeg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy10.jpeg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/jefsnacker/azzy/resolve/main/concept_images/azzy11.jpeg" style="height:200px"> </td>
  </tr>
</table>


## Usage

```python
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

pipe = StableDiffusionPipeline.from_pretrained(
    "jefsnacker/azzy", 
    scheduler = DPMSolverMultistepScheduler.from_pretrained("jefsnacker/azzy", subfolder="scheduler"),
    torch_dtype=torch.float16,
).to("cuda")

guidance_scale = 7
prompt = "Cute and adorable cartoon fluffy azzy cat with cap, with yellow eyes, fantasy, dreamlike, city scenario, surrealism, super cute, trending on artstation"

images = pipe(prompt, num_images_per_prompt=1, num_inference_steps=50, guidance_scale=guidance_scale).images
image[0]

```

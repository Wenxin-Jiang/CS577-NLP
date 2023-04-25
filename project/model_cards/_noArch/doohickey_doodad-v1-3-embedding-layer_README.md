---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: bigscience-bloom-rail-1.0
inference: false

---

### **copy pasted from the genshin stable inversion repo, all you need to know is that it's the token_embedding layer and you can load it in there with torch.load, it's a little hacky and won't give you the full style of the model but it's mostly there**

A finetuning equivalent with less VRAM requirement than finetuning Stable Diffusion itself, faster if you have all the images downloaded, less space taken up by the models since you only need CLIP

A notebook for producing your own "stable inversions" is included in this repo but I wouldn't recommend doing so (they suck). It works on Colab free tier though.

[link to notebook for you to download](https://huggingface.co/crumb/genshin-stable-inversion/blob/main/stable_inversion%20(1).ipynb)

how you can load this into a diffusers-based notebook like [Doohickey](https://github.com/aicrumb/doohickey) might look something like this (later edit: this is now included in Doohickey BETA by default)

```python
from huggingface_hub import hf_hub_download

stable_inversion = "user/my-stable-inversion" #@param {type:"string"}
inversion_path = hf_hub_download(repo_id=stable_inversion, filename="token_embeddings.pt")
text_encoder.text_model.embeddings.token_embedding.weight = torch.load(inversion_path)
```
---
language:
- en
tags:
- stable-diffusion
- text-to-image
inference: false

---

```python
torch.jit.load("unet.pt")
noise_pred = unet(latent_model_input, torch.tensor(t, dtype=torch.float32), text_embeddings) # no ['sample']
```
---
license: cc-by-nc-sa-4.0

language:
- en

thumbnail: "https://huggingface.co/GeneralAwareness/Bettermaker/resolve/main/tmped0j_g4y.png"

tags:
- stable-diffusion
- v2
- text-to-image
- image-to-image
- Embedding
---

Textual Inversion Embedding by General Awareness For SD 2.x trained on 768x768 images from various sources.

Install by downloading the .pt embedding, and put it in the \embeddings folder.

This embedding was made to be primarily used as a negative prompt (with your other negatives as well) as it changes, or refines, the final image, but in all the testing that I did, as well as others, the final images were just better.

---
Usage: In the negative prompt just add Bettermaker with the rest that you currently use.  If you do use it with your positive prompt call it as such - image in Bettermaker style, Bettermaker style, Bettermaker, in the style of Bettermaker, or by Bettermaker.
---


scary clown image in vint-3000 style, highly detailed, 8 k, hdr, smooth, sharp focus, high resolution, award - winning photo, (selective color red eyes)

![Single Samples](https://huggingface.co/GeneralAwareness/Bettermaker/resolve/main/tmpabzuhf7x.png)

Using the embedding in the negative prompt of the above
![Single_Samples](https://huggingface.co/GeneralAwareness/Bettermaker/resolve/main/tmpvhc5tm63.png)

Adding the embedding (Bettermaker) at the end.  Using the other calling forms results in differences from wild to unusable.
![Single_Samples](https://huggingface.co/GeneralAwareness/Bettermaker/resolve/main/tmpk27ptg2j.png)

Not using this embedding.
![Single_Samples](https://huggingface.co/GeneralAwareness/Bettermaker/resolve/main/tmpi_h16e3c.png)
Using this embedding in the negative prompt.
![Single_Samples](https://huggingface.co/GeneralAwareness/Bettermaker/resolve/main/tmp2w_h2ct1.png)
Adding my nirphoto-3000 with this embedding in the negative as well.
![Single_Samples](https://huggingface.co/GeneralAwareness/Bettermaker/resolve/main/tmpowemwff6.png)
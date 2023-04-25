---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
---
### Craig-Wazowski-style Dreambooth model trained by Kagerage with [TheLastBen's fast-DreamBooth](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) notebook


Test the concept via A1111 Colab [fast-Colab-A1111](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb)
Or you can run your new concept via `diffusers` [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb)

Consistancy is a little rough here, as it seems to struggle choosing between being painterly or realistic, but it works well enough for me. Pre-append every prompt with "GregRutkowski artwork, ", as this seems to give better results than putting it at the end of the prompt. Also use a CFG between 9.0 and 12.0, with a non-ancestral sampler, as these values personally gave me the best quality outputs. Also negative prompts, they help.

NOTE: This model is FP16, so it may have issues working without Xformers, though I haven't tested this myself. Extra note, it was trained on the 768 model, so don't go below that. As with the standard 2.1 768 model, extreme aspect ratios above 768x768 work pretty decently, despite the training images being 1:1.

Sample pictures of this concept:



![0](https://huggingface.co/Kagerage/craig-wazowski-style/resolve/main/sample_images/00015-2847494744-GregRutkowski_artwork,_shallow_people_taking_selfies,_defined_faces.png)
    ![1](https://huggingface.co/Kagerage/craig-wazowski-style/resolve/main/sample_images/00122-324663361-(GregRutkowski_1.35)%20portrait%20artwork%2C%201girl%20(anime_0.2)%20catgirl%20nekomimi%2C%20(cat%20ears_1.2)%2C%20cute%2C%20slight%20(cat-like_1.4)%20closed%20mo.png)
    ![2](https://huggingface.co/Kagerage/craig-wazowski-style/resolve/main/sample_images/00007-3086692139-GregRutkowski%20artwork%2C%20landscape%20view%20of%20active%20volcano%20in%20vicious%20plains.png)
    ![3](https://huggingface.co/Kagerage/craig-wazowski-style/resolve/main/sample_images/00024-2865323196-GregRutkowski_artwork,_Elon_Musk_driving_an_SUV,_passengers_seat_view.png)
    ![4](https://huggingface.co/Kagerage/craig-wazowski-style/resolve/main/sample_images/00008-1642941557-gregrutkowski%20artwork%2C%20flaming%20dumpster%20floating%20through%20a%20flooded%20city.png)
    ![5](https://huggingface.co/Kagerage/craig-wazowski-style/resolve/main/sample_images/00010-3302942428-GregRutkowski%20artwork%2C%20landscape%20view%20of%20Zion.png)

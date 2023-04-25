---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: creativeml-openrail-m
inference: true
pipeline_tag: text-to-image
---

# i modelli 'Inizio'
<img src=https://ac-p.namu.la/20230106sac/980c715bd45a7fb0cfe8ce06715c6c4034825fa4d4d07267a5585eb709f2cefa.png
width=100% height=100%>
Inizio is the series of custom mixed models. Based on many released open-source models, and support .safetensors format only.
[WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)-amicable

## Summary
This model repository includes 7 models currently:

 1. *Inizio Fantasma*: Blossom mix+[Anything 3.0](https://huggingface.co/Linaqruf/anything-v3.0)+[SamDoesArtsUltMerge](https://civitai.com/models/68/samdoesarts-ultmerge); weighted, M=0.2. Quietly impressive semi-realistic model.
 2. *Inizio Inseguitore*: [ALG](https://arca.live/b/aiart/64297100)+[SamDoesArtsUltMerge](https://civitai.com/models/68/samdoesarts-ultmerge)+Blossom Mix; add difference, M=0.3. Similar to Inizio Fantasma, but anime-style focused.
 3. *Inizio Foschia*: [ALG](https://arca.live/b/aiart/64297100)+Inizio Fantasma+[A Certain Model](https://huggingface.co/JosephusCheung/ACertainModel); weighted, M=0.7. Similar to Inizio Inseguitore.
 4. *Inizio Replicante*: Inizio Foschia+[DBmai](https://tieba.baidu.com/p/8136937175)+[Finale 5o](https://arca.live/b/aiart/65251337); weighted, M=0.5. Well-tuned Semi-Realistic Anime model. The most fashionable.
 5. *Inizio Skinjob*: Inizio Replicante+[Berry Mix](https://rentry.co/LFTBL)+[ElyOrange](https://huggingface.co/WarriorMama777/OrangeMixs); weighted, M=0.6. Well-tuned Semi-Realistic Anime model.
 6. *Inizio Deckard*: ([Kribo Nstal](https://civitai.com/models/1225/kribomix-nstal)+Inizio Skinjob; weighted, M=0.5)+Inizio Fantasma+Kribo Nstal; weighted, M=0.5.
 7. *Inizio Unico* Inizio Fantasma+Inizio Inseguitore+Inizio Foschia+Inizio Replicante+Inizio Skinjob+Inizio Deckard; weighted, M=1/6. The most advanced Inizio model.

## Recommend Settings (Especially for Inizio Unico)
- Variable Automatic Encoder: [SD MSE 840k.vae.pt](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.ckpt)
- Embedding:[bad_prompt_ver2](https://huggingface.co/datasets/Nerfgun3/bad_prompt/resolve/main/bad_prompt_version2.pt)
- Clip skip: 3
- Prompt: object-related tag first, quality-related tag later; [prompt list](https://docs.google.com/document/d/1X26U00Pxsqmyi47RjxDBMDLCcmyN23z-NEDBgd-vW-c/edit?usp=sharing)
- Resolution: 1024x576->1366x768 w/ HighRes. Fix
- HighRes. Fix: Latent or ESRGAN; upscale by 2

## Sample Image
>  <img src=https://ac2-p.namu.la/20230106sac2/39fd2e16ccf9b0f0254fb97993a575783c8f58a0031c86c54e55ba116e9e21fb.png
> width=100% height=100%>
> ▲ X / Y Plot #1
>
>  <img src=https://ac-p.namu.la/20230106sac/5ded2216805dcbadd5ad581497c881582e8234a2f0ca3200163e89d9d86d8443.png
> width=100% height=100%>
> ▲ X / Y Plot #2
>
>  <img src=https://ac-p.namu.la/20230106sac/d9ac67ac785d8e70c759eac374a9328a5548a1f4f9ed1a4a15dd842eb0ae6f20.png
> width=100% height=100%>
> ▲ X / Y Plot #3
>
>  <img src=https://ac-p.namu.la/20230106sac/fa3ff5f04a30c8ef68d4e937c1511d6806d3d6b0bb27e6bcc4dba056ad5d6b76.png
> width=30% height=30%>
> ▲ Inizio Skinjob
> 
> <img src=https://ac-p.namu.la/20230106sac/17be3a43666816c43776455f31a04f47b01817632b53fb67341444d11318dfd3.png
> width=30% height=30%>
> <img src=https://ac-p.namu.la/20230108sac/ab8169d92f6c9a3bcc47a4cb3138c92bd41bfb794e0020ec3e601834ebd30252.png
> width=30% height=30%>
> <img src=https://ac-p.namu.la/20230108sac/2dbb20abadbed8734fb7b4a8fb1c77485e25de9bfdb671bb91e15d9853cbf972.png
> width=30% height=30%>
> <img src=https://ac-p.namu.la/20230108sac/269e9b1e7f0c9eb2db7c3b5100c1cce6fc75df5fe8c2f02499db55e4b18943f4.jpg
> width=100% height=100%>
> ▲ Inizio Unico
>

## License Information
This model follows Creative ML Open RAIL-M: [Stable Diffusion License](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
But, You may use whatever you want. I don't like to set such restriction.

## Contact
*vitorriofungi@gmail.com* or [*Find Cinnamomo on AI Art Channel*](https://arca.live/b/aiart)
---
license: other
tags:
- stable-diffusion
- text-to-image
model-index:
- name: Defmix-v1.0
  results: []
---

<!-- This model card has been generated automatically according to the information. You should
probably proofread and complete it, then remove this comment. -->

<br>

# ■*Defmix-v1.0*

<strong>*Defmix*</strong>は、<strong>*ACertainThings*</strong>をベースに下記のモデルを*U-Net*の階層ごとに重みを変化させてマージしたモデルです。

- <strong>*Counterfeit v1.0*</strong>
- <strong>*Counterfeit v2.0*</strong>
- <strong>*Basil Mix*</strong>
- <strong>*Anything v4.0*</strong>

*Vae*ファイルは好みのものを使用してください。<br>
彩度の低下がどうしても見られる場合は、対処療法になりますが<br>
*Negative Prompt*に"*greyscale*"を入力することである程度問題を解決できることを確認しています。

<br>


# ■*Examples*

このモデルは人物の描写と背景の広大さを両立することを目的としています。<br>
*Sampler*の違いによって絵柄の調整が可能だと思います。
<br>
- *Sampler: DDIM*
- *Steps: 20*
- *CFG Scale: 5*
- *Clip Skip: 2*
<br>

Positive: a girl<br>
Negative: nsfw, ugly, worst quality, low resolution
<br>

<img src="https://imgur.com/vVInoh3.png" width="768" height="768">


- *Sampler: LMS*
- *Steps: 20*
- *CFG Scale: 5*
- *Clip Skip: 2*
<br>

Positive: a girl<br>
Negative: nsfw, ugly, worst quality, low resolution
<br>

<img src="https://imgur.com/NDw6HLh.png" width="768" height="768">

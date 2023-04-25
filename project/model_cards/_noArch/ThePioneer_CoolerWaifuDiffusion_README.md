---
license: other
language:
- en
- ja
library_name: diffusers
pipeline_tag: text-to-image
tags:
- art
---




<style>
  code {
    white-space : pre-wrap !important;
    word-break: break-word;
  }
</style>
# モデル説明 (model explanation)
- [CoolJapanDiffusion 2.1.1](https://huggingface.co/aipicasso/cool-japan-diffusion-2-1-1/blob/main/v2-1-1.ckpt)と[WaifuDiffusion 1.4 anime epoch2](https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/wd-1-4-anime_e2.ckpt)のマージ。比率はckptファイル名の記載の通り。
- colabのWebUIで動かせる。
  - [これ](https://colab.research.google.com/drive/1ldhBc70wvuvkp4Af_vNTzTfBXwpf_cH5?usp=sharing)の以下の書き換えを行う。やり方は[ここ](https://the-pioneer.notion.site/Colab-Automatic1111-6043f15ef44d4ba0b11920c95d33a78c)。
- ~~リアル系モデルとマージしようとすると、発色が鮮やかになりすぎる傾向あり。~~SD 2.1 768とのマージが原因。512系とのマージなら問題なし。
```python
!aria2c --summary-interval=10 -x 16 -s 16 --allow-overwrite=true -Z https://huggingface.co/JosephusCheung/ACertainModel/resolve/main/ACertainModel-half.ckpt
```

- **注意: URLを引用符で囲まないとエラーになることが判明したのでご注意ください**
```python

!aria2c --summary-interval=10 -x 16 -s 16 --allow-overwrite=true -Z "https://huggingface.co/ThePioneer/CoolerWaifuDiffusion/resolve/main/0.65(wd-1-4-anime_e2)%20%2B%200.35(v2-1-1).ckpt"
!aria2c --summary-interval=10 -x 16 -s 16 --allow-overwrite=true -Z "https://huggingface.co/ThePioneer/CoolerWaifuDiffusion/raw/main/0.65(wd-1-4-anime_e2)%20%2B%200.35(v2-1-1).yaml"
```

- Some merged model of [CoolJapanDiffusion 2.1.1](https://huggingface.co/aipicasso/cool-japan-diffusion-2-1-1/blob/main/v2-1-1.ckpt) and [WaifuDiffusion 1.4 anime epoch2](https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/wd-1-4-anime_e2.ckpt). The merge ration of each model is written on the ckpt file name.
- You can run this model on colab WebUI.
  - Rewrite the following line of [this notebook](https://colab.research.google.com/drive/1ldhBc70wvuvkp4Af_vNTzTfBXwpf_cH5?usp=sharing) following the instructions I posted [here](https://the-pioneer.notion.site/Colab-Automatic1111-6043f15ef44d4ba0b11920c95d33a78c).
- ~~Trying to merge with a realistic model will probably result in a model with too vivid color.~~ It was because I was trying to merge with a SD 2.1 768 based model. It works fine with a SD 2.1 512 based model.
```python
!aria2c --summary-interval=10 -x 16 -s 16 --allow-overwrite=true -Z https://huggingface.co/JosephusCheung/ACertainModel/resolve/main/ACertainModel-half.ckpt
```

- **NOTE: you need to wrap the URL with a quotation as follows**
```python

!aria2c --summary-interval=10 -x 16 -s 16 --allow-overwrite=true -Z "https://huggingface.co/ThePioneer/CoolerWaifuDiffusion/resolve/main/0.65(wd-1-4-anime_e2)%20%2B%200.35(v2-1-1).ckpt"
!aria2c --summary-interval=10 -x 16 -s 16 --allow-overwrite=true -Z "https://huggingface.co/ThePioneer/CoolerWaifuDiffusion/raw/main/0.65(wd-1-4-anime_e2)%20%2B%200.35(v2-1-1).yaml"
```

# サンプル画像 (sample images)
## prompt
```
masterpiece, best quality, A teenage girl wearing a white feather down jacket, smile, in the style of Kyoto Animation in the 2010s, official art, ((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya, beautiful symmetric face, ponytail, beautifully detailed hair, posing of Haruhi Suzumiya, at a snowing mountain in winter, detailed background, alone, solo, 8k, ((((sharp contrast)))), watercolor
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, too many arms, too many heads, wrong anatomy, ((lowres, jpeg artifacts)), [[[[3d]]]], 2d, (((text))), logo, signature, ((loli)), twintails, ponytail, long hair, plaits, pajamas, blushing, boy, sad face, bells, fanart, pixiv, card game, ahoge, ribbon, headband, thick eyebrow, bakemonogatari, black outlines, solid outlines, bold outlines, outlines, technicolor, ((blurry)), vivid colors, vector art, anime, manga, posters, [[oily skin]], huge breasts, baby face, bruises, simple background
Steps: 50
Sampler: Euler a
CFG scale: 7
Seed: 2930115154
Size: 768x768
```

## xy plot
- 最適なモデルは何を生成するかによって変わりうる。
- The best model may depend on what to generate.
![sample1_75_95](https://huggingface.co/ThePioneer/CoolerWaifuDiffusion/resolve/main/xy_grid-0000-2930115154-masterpiece%2C%20best%20quality%2C%20A%20teenage%20girl%20wearing%20a%20white%20feather%20down%20jacket%2C%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%20201.png)
![sample2_65_80](https://huggingface.co/ThePioneer/CoolerWaifuDiffusion/resolve/main/xy_grid-0001-2930115154-masterpiece%2C%20best%20quality%2C%20A%20teenage%20girl%20wearing%20a%20white%20feather%20down%20jacket%2C%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%20201.png)
![sample3_40_65_1](https://huggingface.co/ThePioneer/CoolerWaifuDiffusion/resolve/main/xy_grid-0002-2930115154-masterpiece%2C%20best%20quality%2C%20A%20teenage%20girl%20wearing%20a%20white%20feather%20down%20jacket%2C%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%20201.png)
![sample4_40_65_2](https://huggingface.co/ThePioneer/CoolerWaifuDiffusion/resolve/main/xy_grid-0003-321423-masterpiece%2C%20best%20quality%2C%20A%20teenage%20girl%20wearing%20a%20white%20feather%20down%20jacket%2C%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%20201.png)


# License: The Libertarian OpenRAIL License
注意: アップロード者が日本語母語話者であるため、翻訳版と日本語版に差異がある場合、**元の日本語版**が優先されるものとする。

Caution: Since the uploader is a Japanese native, in the event of any differences in meaning between the original Japanese version and a translation, **the original Japanese version** takes precedence.

要約: ほぼCreativeML Open RAIL-M。但しリバタリアン的解釈によって再構成。CreativeML Open RAIL-Mの制限は、同解釈において維持されているものと判断する。

Summary: A CreativeML Open RAIL-M, interpreted and reconstructed under a libertarian manner. The restriction of CreativeML Open RAIL-M is considered to be valid under such interpretation.

## 主な相違 (differences from the original CreativeML Open RAIL-M license)
- 違法性は、無罪推定の原則に基づき、有罪確定を以て、かつそれのみによって判断する（有罪が確定するまで、法令違反であるように見えても、ライセンス者は違法とはみなさない）。
  - ex. フェアユース文化圏は無論、親告罪である日本においても、著作者が訴えない範囲のほどほどの二次創作は、事実上問題視しない。
- 本モデル及び派生モデルによる生成物はパブリック・ドメイン（CC0 1.0）とすることを義務付け、生成者を含む任意の人物による（再）利用の自由を保障する。
  - Stability.aiが運営するDream Studioが生成物をCC0 1.0としているが、元のモデルライセンスと両立していることに注意せよ。
- 派生モデルでは、本ライセンスと同等以上の制限とともに、同等以上の自由も保障しなければならない。

- The violation of law or regulation will be judged by and only by your conviction per the presumption of innocence (unless you are convicted, it is not enough to claim it is illegal for the Licensor, even if it looks like it).
  - ex. Fanart in Japan is technically illegal, unlike countries which have fair use, but as long as it is in the moderate range and the copright holder won't sue you, we will practically do not consider it as problematic.
- Outputs you generated by the Model or Derivatives of the Model must be distributed under public domain (CC0 1.0), to ensure not only you but anyone can (re)use it freely.
  - Note that Dream Studio, run by Stability.ai demands the output be CC0 1.0 as well, but still isn't against the original model license.
- Derivatives of the Model will always have to include - at minimum - the same use-based restrictions <u>and the same open permissions</u>.

## 全文 (full license)
### 日本語版
[License_ja.md](https://huggingface.co/ThePioneer/MoeDiffusionPlusPlus/blob/main/License_ja.md)を参照。

### English version
[License_en.md](https://huggingface.co/ThePioneer/MoeDiffusionPlusPlus/blob/main/License_en.md)を参照。
---
license: other
language:
- ja
- en
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
- [MoeDiffusionPlusPlus](https://huggingface.co/ThePioneer/MoeDiffusionPlusPlus/blob/main/MoeDiffusion%2B%2B_V2.ckpt) 0.7 : [DreamShaper 3.3 (full)](https://civitai.com/models/4384/dreamshaper) 0.3。
- [WaifuDiffusionのvae](https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/vae/kl-f8-anime.ckpt)と、[StableDiffusionのvae](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/blob/main/vae-ft-mse-840000-ema-pruned.ckpt)をbake inして、MoeDiffusion系の発色の弱さを改善。
- **マージ元のルーツにNAIリークやInsta系モデルが含まれるという噂があるので、NAIリークアンチ・Insta系モデルアンチには非推奨**
- 理想の黒髪ポニテ顔が出せることを目指したMoeDiffusionPlusPlusを、midjourney並みに表現の幅が広いDreamShaperとマージ。
- [Beauty Score](https://www.beautyscoretest.com/)で90を超える写実調美人画も生成可能となった。
  - **実在人物の到達者は確認できていない領域の美貌を生み出せる**ということを意味する。
<!-- sfw版をマージしたので、nsfwは出にくい（たまに出る）。 not sure anymore-->
- 頻繁に指示を無視する暴れ馬モデル同士だったが、なぜかマージしたらかなり落ち着いた。
- colabのWebUIで動かせる。
  - [これ](https://colab.research.google.com/drive/1ldhBc70wvuvkp4Af_vNTzTfBXwpf_cH5?usp=sharing)の以下の書き換えを行う。やり方は[ここ](https://the-pioneer.notion.site/Colab-Automatic1111-6043f15ef44d4ba0b11920c95d33a78c)。
```python
!aria2c --summary-interval=10 -x 16 -s 16 --allow-overwrite=true -Z https://huggingface.co/JosephusCheung/ACertainModel/resolve/main/ACertainModel-half.ckpt
```

- [MoeDiffusionPlusPlus](https://huggingface.co/ThePioneer/MoeDiffusionPlusPlus/blob/main/MoeDiffusion%2B%2B_V2.ckpt) 0.7 : [DreamShaper 3.3 (full)](https://civitai.com/models/4384/dreamshaper) 0.3。
- Improved the coloring which has been a problem of MoeDiffusion series, by baking in [the vae of WaifuDiffusion](https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/vae/kl-f8-anime.ckpt) and [the vae of StableDiffusion](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/blob/main/vae-ft-mse-840000-ema-pruned.ckpt).
- **Since the original models might have the root back in NovelAI leak and Instagram based models, according to some rumors, I do not recommend you use it, if you are a hater of NAI leak/Instagram based models and their derivatives.**

- A merged model of MoeDiffusionPlusPlus, which was created to generate my favorite waifu under a better control, and DreamShaper, which can generate as wide a range of expression as midjourney.
- You can now generate a superbeauty with the [Beauty Score](https://www.beautyscoretest.com/) over 90.
  - I haven't found any real person that reached this level so far, and it means you can create **a beauty that maybe nobody has reached** (yet?).
<!-- Since I've merged the sfw version, it's not very easy for you to get an nsfw output (though it will appear once in a while). -->
- As YaguruMagiku very often ignores the prompt, the mixed model, which is still controlable compared to the original YaguruMagiku, may generate some unexpected results. I recommend you generate 4 images at a time.
- You can run this model on colab WebUI.
  - Rewrite the following line of [this notebook](https://colab.research.google.com/drive/1ldhBc70wvuvkp4Af_vNTzTfBXwpf_cH5?usp=sharing) following the instructions I posted [here](https://the-pioneer.notion.site/Colab-Automatic1111-6043f15ef44d4ba0b11920c95d33a78c).
```python
!aria2c --summary-interval=10 -x 16 -s 16 --allow-overwrite=true -Z https://huggingface.co/JosephusCheung/ACertainModel/resolve/main/ACertainModel-half.ckpt
```


# サンプル画像 (sample images)
``art by yaguru magiku``プロンプトを適切な強さで追加することで、YaguruMagikuスタイルの顔を出力できる。逆に外すことで、DreamShaper風の写実タッチに近づけることもできる。

Add the propmpt ``art by yaguru magiku`` with a proper strength to get the face in the style of YaguruMagiku. To generate a more photorealistic image close to DreamShaper, you can just remove the tag.

![sample1](https://huggingface.co/ThePioneer/MoeSharpV1/resolve/main/00161-1990744884-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20white%20feather%20jacket%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202010s%2C.png)
```
art by yaguru magiku, A teenage girl wearing a white feather jacket, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, at a snowing mountain on a winter day, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background, bruises
Steps: 50
Sampler: Euler a
CFG scale: 7,
Size: 512x512
```

![sample2](https://huggingface.co/ThePioneer/MoeSharpV1/resolve/main/00187-1448517714-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20knight%20armor%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202010s%2C%20of.png)
```
art by yaguru magiku, A teenage girl wearing a black knight armor, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, at a medieval european castle on an autumn day, fantasy, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background, bruises
Steps: 50
Sampler: Euler a
CFG scale: 7
Size: 512x512
```

![sample3](https://huggingface.co/ThePioneer/MoeSharpV1/resolve/main/00193-2486332963-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20western%20knight%20armor%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202.png)
```
art by yaguru magiku, A teenage girl wearing a black western knight armor, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, at Ancient Rome on a spring day, fantasy, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background, bruises
Steps: 50
Sampler: Euler a
CFG scale: 7
Size: 512x512
```

![sample4](https://huggingface.co/ThePioneer/MoeSharpV1/resolve/main/00190-1448517717-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20knight%20armor%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202010s%2C%20of.png)
```
art by yaguru magiku, A teenage girl wearing a black knight armor, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, at a medieval european castle on an autumn day, fantasy, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background, bruises
Steps: 50
Sampler: Euler a
CFG scale: 7
Seed: 1448517717
Size: 512x512
```

![sample5](https://huggingface.co/ThePioneer/MoeSharpV1/resolve/main/00200-3132630260-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20western%20knight%20armor%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202.png)
```
art by yaguru magiku, A teenage girl wearing a black western knight armor, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, at Ancient Egypt near the great Pyramid, fantasy, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background, bruises
Steps: 50
Sampler: Euler a
CFG scale: 7
Size: 512x512
```

![sample6](https://huggingface.co/ThePioneer/MoeSharpV1/resolve/main/00202-3132630262-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20western%20knight%20armor%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202.png)
```
art by yaguru magiku, A teenage girl wearing a black western knight armor, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, at Ancient Egypt near the great Pyramid, fantasy, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background, bruises
Steps: 50
Sampler: Euler a
CFG scale: 7
Size: 512x512
```

![sample7](https://huggingface.co/ThePioneer/MoeSharpV1/resolve/main/00205-1319183938-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20western%20knight%20armor%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202.png)
```
art by yaguru magiku, A teenage girl wearing a black western knight armor, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, at Ancient Egypt near the great Pyramid, fantasy, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background, bruises
Steps: 50
Sampler: Euler a
CFG scale: 7
Size: 512x512
```

![sample8](https://huggingface.co/ThePioneer/MoeSharpV1/resolve/main/00259-2838978517-A%20photograph%20of%20a%20beautiful%20Chinese%20Taiwanese%20superstar%2C%20((perfect%20face))%2C%20%5Bsexy%20face%5D%2C%20(pretty%20face)%2C%20((beautiful%20face))%2C%20symme.png)
```
A photograph of a beautiful Chinese Taiwanese superstar, ((perfect face)), [sexy face], (pretty face), ((beautiful face)), symmetric face, ponytail, smiling, big eyes, long eyebrows, contours, makeups, front shot, ((((((photorealistic, hyperrealistic)))))), 3d
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background, bruises, Asian face, African face, ((European face):0), head out of frame, multiple people, anime, manga, comic, wrinkles, selfies, side shot, flat nose, cheekbones
Steps: 20
Sampler: Euler a
CFG scale: 7
Size: 512x512
```

cf. beauty score
![result over 90](https://huggingface.co/ThePioneer/MoeSharpV1/resolve/main/91_success.png)

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
[License_ja.md](https://huggingface.co/ThePioneer/MoeSharpV1/blob/main/License_ja.md)を参照。

### English version
[License_en.md](https://huggingface.co/ThePioneer/MoeSharpV1/blob/main/License_en.md)を参照。
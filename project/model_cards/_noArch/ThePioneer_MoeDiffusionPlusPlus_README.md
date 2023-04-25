---
license: other
library_name: diffusers
tags:
- art
language:
- en
- ja
pipeline_tag: text-to-image
---
<style>
  code {
    white-space : pre-wrap !important;
    word-break: break-word;
  }
</style>

# モデル説明 (model explanation)
- V1 = [MoeDiffusion](https://huggingface.co/ThePioneer/MoeDiffusion/blob/main/MoeDiffusion.ckpt) 1.0 + ([HassanBlend 1.5](https://huggingface.co/hassanblend/HassanBlend1.5.1.2/blob/main/HassanBlend1.5.ckpt) - [VMix03](https://huggingface.co/fhreinfls/VMix/blob/main/V03.ckpt)) * 0.2
- V2 = [MoeDiffusion](https://huggingface.co/ThePioneer/MoeDiffusion/blob/main/MoeDiffusion.ckpt) 0.6 : [HassanBlend 1.5](https://huggingface.co/hassanblend/HassanBlend1.5.1.2/blob/main/HassanBlend1.5.ckpt) 0.2 : [VMix03](https://huggingface.co/fhreinfls/VMix/blob/main/V03.ckpt) : 0.2
- **マージ元のルーツにNAIリークやInsta系モデルが含まれるという噂があるので、NAIリークアンチ・Insta系モデルアンチには非推奨**
- 理想の黒髪ポニテ顔が出せるYaguruMagikuを、ある程度顔が近くて制御しやすいAbyssOrangeMix2と混ぜてみた。
  - よってマージ者の目的である黒髪ポニテ以外の動作は興味ないし、知らない。
- sfw版をマージしたので、nsfwは出にくい（たまに出る）。
- YaguruMagikuが顔はいいけど指示を無視する暴れ馬モデルなので、各種マージで少しは落ち着かせたが、4枚同時生成を推奨。
- vaeを入れた方が多分発色は良くなる…が、既にマージした結果、それなりに良くなっているかも。
- colabのWebUIで動かせる。
  - [これ](https://colab.research.google.com/drive/1ldhBc70wvuvkp4Af_vNTzTfBXwpf_cH5?usp=sharing)の以下の書き換えを行う。やり方は[ここ](https://the-pioneer.notion.site/Colab-Automatic1111-6043f15ef44d4ba0b11920c95d33a78c)。
```python
!aria2c --summary-interval=10 -x 16 -s 16 --allow-overwrite=true -Z https://huggingface.co/JosephusCheung/ACertainModel/resolve/main/ACertainModel-half.ckpt
```

- V1 = [MoeDiffusion](https://huggingface.co/ThePioneer/MoeDiffusion/blob/main/MoeDiffusion.ckpt) 1.0 + ([HassanBlend 1.5](https://huggingface.co/hassanblend/HassanBlend1.5.1.2/blob/main/HassanBlend1.5.ckpt) - [VMix03](https://huggingface.co/fhreinfls/VMix/blob/main/V03.ckpt)) * 0.2
- V2 = [MoeDiffusion](https://huggingface.co/ThePioneer/MoeDiffusion/blob/main/MoeDiffusion.ckpt) 0.6 : [HassanBlend 1.5](https://huggingface.co/hassanblend/HassanBlend1.5.1.2/blob/main/HassanBlend1.5.ckpt) 0.2 : [VMix03](https://huggingface.co/fhreinfls/VMix/blob/main/V03.ckpt) : 0.2
- **Since the original models might have the root back in NovelAI leak and Instagram based models, according to some rumors, I do not recommend you use it, if you are a hater of NAI leak/Instagram based models and their derivatives.**
- What I wanted was to control my favorite waifu with a black hair and ponytail, which can be generated only in YaguruMagiku afaik, and therefore I have mixed YaguruMagiku with AbyssOrangeMix2, which can generate a relatively close face, and is controlable.
  - Thus I do not care about other styles. It *should* work, but no guarantees.
- Since I've merged the sfw version, it's not very easy for you to get an nsfw output (though it will appear once in a while).
- As YaguruMagiku very often ignores the prompt, the mixed model, which is still controlable compared to the original YaguruMagiku, may generate some unexpected results. I recommend you generate 4 images at a time.
- I think the coloring will be better if you add an vae; or so it was supposed to, but after the various merge I find it confortable enough, at least for myself. 
- You can run this model on colab WebUI.
  - Rewrite the following line of [this notebook](https://colab.research.google.com/drive/1ldhBc70wvuvkp4Af_vNTzTfBXwpf_cH5?usp=sharing) following the instructions I posted [here](https://the-pioneer.notion.site/Colab-Automatic1111-6043f15ef44d4ba0b11920c95d33a78c).
```python
!aria2c --summary-interval=10 -x 16 -s 16 --allow-overwrite=true -Z https://huggingface.co/JosephusCheung/ACertainModel/resolve/main/ACertainModel-half.ckpt
```


# サンプル画像 (sample images)
``art by yaguru magiku``プロンプトを適切な強さで追加することで、YaguruMagikuスタイルの顔を出力できる。

Add the propmpt ``art by yaguru magiku`` with a proper strength to get the face in the style of YaguruMagiku.

## V1
![sample 1-1](https://huggingface.co/ThePioneer/MoeDiffusionPlusPlus/resolve/main/00068-69522375-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20yukata%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202010s%2C%20official.png)
```
art by yaguru magiku, A teenage girl wearing a black yukata, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, in the universe with stars and galaxies, psychedelic art, rainbows, transcendence, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background
Steps: 50
Sampler: Euler a
CFG scale: 7
Size: 768x768
```

![sample 1-2](https://huggingface.co/ThePioneer/MoeDiffusionPlusPlus/resolve/main/00071-69522378-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20yukata%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202010s%2C%20official.png)
```
art by yaguru magiku, A teenage girl wearing a black yukata, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, in the universe with stars and galaxies, psychedelic art, rainbows, transcendence, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background
Steps: 50
Sampler: Euler a
CFG scale: 7
Size: 768x768
```

![sample 1-3](https://huggingface.co/ThePioneer/MoeDiffusionPlusPlus/resolve/main/00004-874453381-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20bikini%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202010s%2C%20official.png)
```
art by yaguru magiku, A teenage girl wearing a black bikini, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, at a beach on a summer day, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background
Steps: 50
Sampler: Euler a
CFG scale: 7
Size: 512x512
```

## V2
![sample 2-1](https://huggingface.co/ThePioneer/MoeDiffusionPlusPlus/resolve/main/00060-1876616744-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20yukata%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202010s%2C%20official.png)
```
art by yaguru magiku, A teenage girl wearing a black yukata, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, in the universe with stars and galaxies, psychedelic art, rainbows, transcendence, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background
Steps: 50
Sampler: Euler a
CFG scale: 7
Size: 768x768
```

![sample 2-2](https://huggingface.co/ThePioneer/MoeDiffusionPlusPlus/resolve/main/00062-1876616746-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20yukata%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202010s%2C%20official.png)
```
art by yaguru magiku, A teenage girl wearing a black yukata, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, in the universe with stars and galaxies, psychedelic art, rainbows, transcendence, alone, solo, 8k, posing of Haruhi Suzumiya
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background
Steps: 50
Sampler: Euler a
CFG scale: 7
Size: 768x768
```

![sample 2-3](https://huggingface.co/ThePioneer/MoeDiffusionPlusPlus/resolve/main/00054-3233330302-art%20by%20yaguru%20magiku%2C%20A%20teenage%20girl%20wearing%20a%20black%20bikini%2C%20angry%20smile%2C%20in%20the%20style%20of%20Kyoto%20Animation%20in%20the%202010s%2C%20official.png)
```
art by yaguru magiku, A teenage girl wearing a black bikini, angry smile, in the style of Kyoto Animation in the 2010s, official art, ((((black hair)), eyes of Haruhi Suzumiya, face of Haruhi Suzumiya)), beautiful symmetric face, ponytail, at a beach on a summer day, ((alone, solo)), 8k, posing of Haruhi Suzumiya, vivid colors
Negative prompt: low quality, bad face, ((ugly face)), asymmetric face, ((((bad anatomy)))), ((bad hand)), too many fingers, missing fingers, too many legs, lowres, jpeg artifacts, (((text))), logo, signature, sad face, ((loli)), twintails, plaits, pajamas, jackets, blushing, boy, adult, bells, fanart, pixiv, card game, ahoge, ribbon, weapons, armors, tools, white background, simple background, sepia, grayscale, greyscale, bruises
Steps: 50, Sampler: Euler a, CFG scale: 7, Seed: 3233330301, Size: 768x768
```

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
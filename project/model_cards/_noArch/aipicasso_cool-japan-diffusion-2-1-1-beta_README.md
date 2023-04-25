---
license: other
tags:
  - stable-diffusion
  - text-to-image
---

# Cool Japan Diffusion 2.1.1 Beta Model Card

![アイキャッチ](eyecatch.jpg)

[注意事项。中国将对图像生成的人工智能实施法律限制。 ](http://www.cac.gov.cn/2022-12/11/c_1672221949318230.htm) （中国国内にいる人への警告）

English version is [here](README_en.md).

# はじめに
Cool Japan Diffusion (for learning) はStable Diffsionをファインチューニングして、アニメやマンガ、ゲームなどのクールジャパンを表現することに特化したモデルです。なお、内閣府のクールジャパン戦略とは特に関係はありません。

# ライセンスについて
ライセンスについては、もとのライセンス CreativeML Open RAIL++-M License に例外を除き商用利用禁止を追加しただけです。
例外を除き商用利用禁止を追加した理由は創作業界に悪影響を及ぼしかねないという懸念からです。
この懸念が払拭されれば、次のバージョンから元のライセンスに戻し、商用利用可能とします。
ちなみに、元のライセンスの日本語訳は[こちら](https://qiita.com/robitan/items/887d9f3153963114823d)になります。 
営利企業にいる方は法務部にいる人と相談してください。
趣味で利用する方はあまり気にしなくても一般常識を守れば大丈夫なはずです。
なお、ライセンスにある通り、このモデルを改造しても、このライセンスを引き継ぐ必要があります。

# 法律や倫理について
本モデルは日本にて作成されました。したがって、日本の法律が適用されます。
本モデルの学習は、著作権法第30条の4に基づき、合法であると主張します。
また、本モデルの配布については、著作権法や刑法175条に照らしてみても、
正犯や幇助犯にも該当しないと主張します。詳しくは柿沼弁護士の[見解](https://twitter.com/tka0120/status/1601483633436393473?s=20&t=yvM9EX0Em-_7lh8NJln3IQ)を御覧ください。
ただし、ライセンスにもある通り、本モデルの生成物は各種法令に従って取り扱って下さい。

しかし、本モデルを配布する行為が倫理的に良くないとは作者は思っています。
これは学習する著作物に対して著作者の許可を得ていないためです。
ただし、学習するには著作者の許可は法律上必要もなく、検索エンジンと同様法律上は問題はありません。
したがって、法的な側面ではなく、倫理的な側面を調査する目的も本配布は兼ねていると考えてください。

# 使い方
手軽に楽しみたい方は、こちらの[Space](https://huggingface.co/spaces/aipicasso/cool-japan-diffusion-latest-demo)をお使いください。
詳しい本モデルの取り扱い方は[こちらの取扱説明書](https://alfredplpl.hatenablog.com/entry/2023/01/11/182146)にかかれています。
モデルは[ここ](https://huggingface.co/aipicasso/cool-japan-diffusion-2-1-1-beta/resolve/main/v2-1-1-beta.ckpt)からダウンロードできます。

以下、一般的なモデルカードの日本語訳です。

## モデル詳細
- **開発者:** Robin Rombach, Patrick Esser, Alfred Increment
- **モデルタイプ:** 拡散モデルベースの text-to-image 生成モデル
- **言語:** 日本語
- **ライセンス:** CreativeML Open RAIL++-M-NC License
- **モデルの説明:** このモデルはプロンプトに応じて適切な画像を生成することができます。アルゴリズムは [Latent Diffusion Model](https://arxiv.org/abs/2112.10752) と [OpenCLIP-ViT/H](https://github.com/mlfoundations/open_clip) です。
- **補足:**
- **参考文献:**

      @InProceedings{Rombach_2022_CVPR,
          author    = {Rombach, Robin and Blattmann, Andreas and Lorenz, Dominik and Esser, Patrick and Ommer, Bj\"orn},
          title     = {High-Resolution Image Synthesis With Latent Diffusion Models},
          booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
          month     = {June},
          year      = {2022},
          pages     = {10684-10695}
      }

## モデルの使用例

Stable Diffusion v2と同じ使い方です。
たくさんの方法がありますが、２つのパターンを提供します。
- Web UI
- Diffusers

### Web UIの場合

こちらの[取扱説明書](https://alfredplpl.hatenablog.com/entry/2023/01/11/182146)に従って作成してください。

### Diffusersの場合

[🤗's Diffusers library](https://github.com/huggingface/diffusers) を使ってください。

まずは、以下のスクリプトを実行し、ライブラリをいれてください。

```bash
pip install --upgrade git+https://github.com/huggingface/diffusers.git transformers accelerate scipy
```

次のスクリプトを実行し、画像を生成してください。

```python
from diffusers import StableDiffusionPipeline, EulerAncestralDiscreteScheduler
import torch

model_id = "aipicasso/cool-japan-diffusion-2-1-1-beta"

scheduler = EulerAncestralDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)#,use_auth_token="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")
pipe = pipe.to("cuda")

prompt = "anime, a portrait of a girl with black short hair and red eyes, kimono, full color illustration, official art, 4k, detailed"
negative_prompt="(((deformed))), blurry, ((((bad anatomy)))), bad pupil, disfigured, poorly drawn face, mutation, mutated, (extra limb), (ugly), (poorly drawn hands), bad hands, fused fingers, messy drawing, broken legs censor, low quality, ((mutated hands and fingers:1.5), (long body :1.3), (mutation, poorly drawn :1.2), ((bad eyes)), ui, error, missing fingers, fused fingers, one hand with more than 5 fingers, one hand with less than 5 fingers, one hand with more than 5 digit, one hand with less than 5 digit, extra digit, fewer digits, fused digit, missing digit, bad digit, liquid digit, long body, uncoordinated body, unnatural body, lowres, jpeg artifacts, 2d, 3d, cg, text"
image = pipe(prompt,negative_prompt=negative_prompt, width=512, height=512, num_inference_steps=20).images[0]
image.save("girl.png")


```

**注意**:
- [xformers](https://github.com/facebookresearch/xformers) を使うと早くなるらしいです。
- GPUを使う際にGPUのメモリが少ない人は `pipe.enable_attention_slicing()` を使ってください。

#### 想定される用途

- コンテスト
    - [AIアートグランプリ](https://www.aiartgrandprix.com/)への投稿
        - ファインチューニングに用いた全データを開示し、審査基準を満たしていることを判断してもらうようにします。
        - コンテストに向けて、要望があれば、Hugging Face の Community などで私に伝えてください。
- 画像生成AIに関する報道
    - 公共放送だけでなく、営利企業でも可能
        - 画像合成AIに関する情報を「知る権利」は創作業界に悪影響を及ぼさないと判断したためです。また、報道の自由などを尊重しました。
- クールジャパンの紹介
    - 他国の人にクールジャパンとはなにかを説明すること。
        - 他国の留学生はクールジャパンに惹かれて日本に来ることがおおくあります。そこで、クールジャパンが日本では「クールでない」とされていることにがっかりされることがとても多いとAlfred Incrementは感じております。他国の人が憧れる自国の文化をもっと誇りに思ってください。
- 研究開発
    - Discord上でのモデルの利用
        - プロンプトエンジニアリング
        - ファインチューニング（追加学習とも）
            - DreamBooth など
        - 他のモデルとのマージ
    - Latent Diffusion Modelとクールジャパンとの相性
    - 本モデルの性能をFIDなどで調べること
    - 本モデルがStable Diffusion以外のモデルとは独立であることをチェックサムやハッシュ関数などで調べること
- 教育
    - 美大生や専門学校生の卒業制作
    - 大学生の卒業論文や課題制作
    - 先生が画像生成AIの現状を伝えること
- 自己表現
    - SNS上で自分の感情や思考を表現すること
- Hugging Face の Community にかいてある用途
    - 日本語か英語で質問してください

#### 想定されない用途
- 物事を事実として表現するようなこと
- 収益化されているYouTubeなどのコンテンツへの使用
- 商用のサービスとして直接提供すること
- 先生を困らせるようなこと
- その他、創作業界に悪影響を及ぼすこと

# 使用してはいけない用途や悪意のある用途
- デジタル贋作 ([Digital Forgery](https://arxiv.org/abs/2212.03860)) は公開しないでください（著作権法に違反するおそれ）
    - 特に既存のキャラクターは公開しないでください（著作権法に違反するおそれ）
        - なお、学習していない[キャラクターも生成できる](https://twitter.com/ThePioneerJPnew/status/1609074173892235264?s=20&t=-rY1ufzNeIDT3Fm5YdME6g)そうです。（このツイート自体は研究目的として許可しています。）
- 他人の作品を無断でImage-to-Imageしないでください（著作権法に違反するおそれ）
- わいせつ物を頒布しないでください (刑法175条に違反するおそれ）
    - いわゆる業界のマナーを守らないようなこと
- 事実に基づかないことを事実のように語らないようにしてください（威力業務妨害罪が適用されるおそれ）
    - フェイクニュース

## モデルの限界やバイアス

### モデルの限界

- よくわかっていない

### バイアス

Stable Diffusionと同じバイアスが掛かっています。
気をつけてください。

## 学習

**学習データ**

次のデータを主に使ってStable Diffusionをファインチューニングしています。

- VAEについて
    - Danbooruなどの無断転載サイトを除いた日本の国内法を遵守したデータ: 60万種類 （データ拡張により無限枚作成）
- U-Netについて
    - Danbooruなどの無断転載サイトを除いた日本の国内法を遵守したデータ: 80万ペア

**学習プロセス**

Stable DiffusionのVAEとU-Netをファインチューニングしました。

- **ハードウェア:** RTX 3090
- **オプティマイザー:** AdamW
- **Gradient Accumulations**: 1
- **バッチサイズ:** 1

## 評価結果

## 環境への影響

ほとんどありません。

- **ハードウェアタイプ:** RTX 3090
- **使用時間（単位は時間）:** 500
- **クラウド事業者:** なし
- **学習した場所:** 日本
- **カーボン排出量:** そんなにない

## 参考文献
    @InProceedings{Rombach_2022_CVPR,
        author    = {Rombach, Robin and Blattmann, Andreas and Lorenz, Dominik and Esser, Patrick and Ommer, Bj\"orn},
        title     = {High-Resolution Image Synthesis With Latent Diffusion Models},
        booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
        month     = {June},
        year      = {2022},
        pages     = {10684-10695}
    }

*このモデルカードは [Stable Diffusion v2](https://huggingface.co/stabilityai/stable-diffusion-2/raw/main/README.md) に基づいて、Alfred Incrementがかきました。

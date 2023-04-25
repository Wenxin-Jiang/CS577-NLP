---
license: other
tags:
  - stable-diffusion
  - text-to-image
widget:
- text: "anime, a beautuful girl with black hair and red eyes, kimono, 4k, detailed"
  example_title: "Girl (Anime)"
- text: "manga, monochrome, a cute girl with long white hair"
  example_title: "Girl (Manga)"
- text: "anime, buildings in Tokyo, 4k, detailed"
  example_title: "Bldg. (Anime)"
- text: "manga, monochrome, buildings in Tokyo, highly detailed"
  example_title: "Bldg. (Manga)"
---

# Cool Japan Diffusion for learning 2.0 Model Card

![アイキャッチ](eyecatch.png)

[注意事项。从2023年1月10日起，中国将对图像生成的人工智能实施法律限制。 ](http://www.cac.gov.cn/2022-12/11/c_1672221949318230.htm) （中国国内にいる人への警告）

This model is released for Japanese people mainly.
Therefore, the documents of the model are written in Japanese.
The documents will be translated into English for the foreign countries after I obtain the consensus from Japanese people.
Thank you for your cooperations. （日本語が読めない人へのお願い）

# はじめに
学習用Cool Japan DiffusionはStable Dissuionをファインチューニングして、イラスト用に特化したモデルです。本来は、Cool Japan Diffusionという拡散モデルを学習させるために作られました。ただし、今回、諸事情により、緊急で提供することにしました。なお、内閣府のクールジャパン戦略とは特に関係はありません。

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

しかし、本モデルを配布する行為が倫理的にあまり良いとは作者は思っていません。
したがって、倫理的な側面を調査する目的も本配布は兼ねていると考えてください。

# 使い方
手軽に楽しみたい方は、右側にあるテキストフォームに入れて生成してみてください。Fくんが作った[Space](https://huggingface.co/spaces/fkunn1326/CoolJapaneseDiffusion)でも試せます。
本格的に使いたい方は上記の注意を読んだ上で、この[記事](https://note.com/it_navi/n/nb460e11bf7e9)をよんで使ってみてください。
なお、使い方のチュートリアルは[こちら](https://alfredplpl.hatenablog.com/entry/2022/12/10/192423)です。

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

こちらの[記事](https://note.com/it_navi/n/nb460e11bf7e9)に従って作成してください。

### Diffusersの場合

[🤗's Diffusers library](https://github.com/huggingface/diffusers) を使ってください。

まずは、以下のスクリプトを実行し、ライブラリをいれてください。

```bash
pip install --upgrade git+https://github.com/huggingface/diffusers.git transformers accelerate scipy
```

次のスクリプトを実行し、画像を生成してください。

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "alfredplpl/cool-japan-diffusion-for-learning-2-0"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "anime, a beautuful girl with black hair and red eyes, kimono, 4k, detailed"
image = pipe(prompt, height=512, width=512).images[0]

image.save("girl.png")
```

**注意**:
- [xformers](https://github.com/facebookresearch/xformers) を使うと早くなるらしいです。
- GPUを使う際にGPUのメモリが少ない人は `pipe.enable_attention_slicing()` を使ってください。

#### 想定される用途

- コンテスト
    - [AIアートグランプリ](https://www.aiartgrandprix.com/)への投稿
        - ファインチューニングに用いた全データを開示し、審査基準を満たしていることを判断してもらうようにします。また、事前に申請して、確認を取るようにします。
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
女性はきれいに出力されるもの、男性はきれいに出力されにくいバイアスがあります。
また、出力する人が存在する場所によって人種の偏りが見られることが[報告](https://twitter.com/ThePioneerJPnew/status/1602214001764892673?s=20&t=Zo-b-vsG7QdaTc44Wnrl7Q)されています。
イラストに特化していますが、プロンプトによっては実写のようなものを作ることができることが[報告](https://twitter.com/ThePioneerJPnew/status/1602331663068909569?s=20&t=Zo-b-vsG7QdaTc44Wnrl7Q)されています。
気をつけてください。

## 学習

**学習データ**

次のデータを主に使ってStable Diffusionをファインチューニングしています。

- Twitterに掲載されたイラストやマンガ: Twitter APIで取得した画像約20万枚

**学習プロセス**

Stable DiffusionのVAEとU-Netをファインチューニングしました。

- **ハードウェア:** RTX 3090
- **オプティマイザー:** AdamW
- **Gradient Accumulations**: 1
- **バッチサイズ:** 1

## 評価結果

# CLIP Score
CLIP Scoreは高ければ、高いほど、プロンプトに応じた画像を生成していることを示す指標です。
[Izumi Satoshi](https://twitter.com/izumisatoshi05) さんからの [報告](https://twitter.com/izumisatoshi05/status/1602738618258591744?s=20&t=yvM9EX0Em-_7lh8NJln3IQ)によると、以下のとおりです。

|  モデル  |  CLIP Score  |
| ---- | ---- |
|  [Waifu Diffusion v1.3](https://huggingface.co/hakurei/waifu-diffusion-v1-3)   |  33.9  |
|  本モデル  |  34.8  |

ただし、[条件についての報告](https://twitter.com/izumisatoshi05/status/1602738619667853312?s=20&t=yvM9EX0Em-_7lh8NJln3IQ)によると、本モデルのほうが有利になる条件であるとされています。
気をつけてください。

# FID, DaFID-512
FIDは低ければ低いほど、２つのデータセットが画像認識的に近いということを示す指標です。
DaFID-512はFIDの中でも二次元イラストに特化した指標らしいです。
Birdmanさんからの[報告](https://birdmanikioishota.blog.fc2.com/blog-entry-15.html)によると、[High Resolution Anime Face Dataset](https://www.kaggle.com/datasets/subinium/highresolution-anime-face-dataset-512x512)と各モデルから生成された1万枚を比較した結果、以下のとおりです。

![報告結果](./FID_results.png)

## 環境への影響

ほとんどありません。

- **ハードウェアタイプ:** RTX 3090
- **使用時間（単位は時間）:** 300
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

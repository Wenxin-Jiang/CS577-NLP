---
license: creativeml-openrail-m
language:
- en
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image

---

以下の5人の[東北ずん子プロジェクト](https://zunko.jp/)のキャラクターイラストを用いてDreamBoothで学習したモデルです．

- ``itako``: 東北イタコ
- ``zunko``: 東北ずん子
- ``kiritan``: 東北きりたん
- ``zundamon``: ずんだもん (人間形態)
- ``metan``: 四国めたん

学習画像はなるべく衣装にバリエーションをもたせているので，「公式衣装」は出にくいです．

🌐オンラインですぐに試せる[Google Colab Notebook](https://colab.research.google.com/drive/1p93qo7yrp2JNd57M94-ug-hiXUXj8JqF?usp=sharing)でも利用できます


🔈 キャラクターを増やして学習したモデル[shirayu/sd-tohoku-v2](https://huggingface.co/shirayu/sd-tohoku-v2)を公開しました (2023-01-04)

## ファイル形式

1. [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)などckptファイルを読み込むツールの場合

    [sd-tohoku-v1.model.ckpt](https://huggingface.co/shirayu/sd-tohoku-v1/resolve/main/sd-tohoku-v1.model.ckpt)(約2GB)をダウンロードして読み込んでください

2. [diffusers](https://github.com/huggingface/diffusers)から利用する場合

    ```python
    from diffusers import DiffusionPipeline
    pipeline = DiffusionPipeline.from_pretrained("shirayu/sd-tohoku-v1")
    ```

## 紹介動画

<a href="https://www.nicovideo.jp/watch/sm41313614">
<img src="https://img.cdn.nimg.jp/s/nicovideo/thumbnails/41313614/41313614.80180214.original/r1280x720l?key=23adae7a647d3afa1049dc9c39204802d20870ca260b75939dd016ba127cebd8" width="500" alt="東北ずん子プロジェクトのキャラをAIお絵描き！">東北ずん子プロジェクトのキャラをAIお絵描き！　(ニコニコ動画)
</a>

## ライセンス

[CreativeML Open RAIL-M license 1.0](https://hf.space/static/bigscience/license/index.html)

また，各種法令・各種ガイドラインにご留意ください．
例えば，生成された画像が東北ずん子プロジェクトのキャラクターを含む場合，
[「東北ずん子プロジェクト キャラクター利用の手引き」](https://zunko.jp/guideline.html)に基づいて利用してください．

## 学習設定

- 元モデル: [Nilaier/Waifu-Diffusers](https://huggingface.co/Nilaier/Waifu-Diffusers) (fbd1958)
    - Base model: [hakurei/waifu-diffusion-v1-3](https://huggingface.co/hakurei/waifu-diffusion-v1-3)
    - VAE: [hakurei/waifu-diffusion-v1-4](https://huggingface.co/hakurei/waifu-diffusion-v1-4)
- 学習画像
    - 5キャラクター計69枚
        - itako: 東北イタコ  18枚
        - zunko: 東北ずん子  13枚
        - kiritan: 東北きりたん 13枚
        - zundamon: ずんだもん (人間形態) 9枚
        - metan: 四国めたん 16枚
    - アルファチャンネルは削除 + 白背景 + センタリング + 512x512にリサイズ
- 学習元コード: [ShivamShrirao/diffusers](https://github.com/ShivamShrirao/diffusers) (``7232c2a``)
    - [``examples/dreambooth/train_dreambooth.py``](https://github.com/ShivamShrirao/diffusers/blob/7232c2a/examples/dreambooth/train_dreambooth.py)
- 学習設定
    - Instance ID: ``itako``, ``kiritan``, ``zunko``, ``metan``, ``zundamon`` (5種)
    - Instance prompt: ``<ID> 1girl``
    - Tesla T4で約110分
    - その他設定:

    ```txt
    --prior_loss_weight=0.5 \
    --seed=3434554 \
    --resolution=512 \
    --center_crop \
    --train_batch_size=1 \
    --train_text_encoder \
    --mixed_precision="fp16" \
    --use_8bit_adam \
    --gradient_checkpointing \
    --gradient_accumulation_steps=2 \
    --learning_rate=1e-6 \
    --lr_scheduler="constant" \
    --lr_warmup_steps=0 \
    --num_class_images=50 \
    --sample_batch_size=3 \
    --max_train_steps=8000
    ```

## 学習に使った画像

<img src="https://pbs.twimg.com/media/Ff6FF1NaMAAL8N5?format=jpg&name=small" width="500" alt="学習に使った画像">

## 生成例

<img src="https://pbs.twimg.com/media/Ff6AgzyaMAExeb3?format=png&name=900x900" width="500" alt="東北きりたんの生成例">

```txt
kiritan, 1girl, volleyball, kawaii, in gymnasium, head
Negative prompt: chibi, out of frame, armature drawing, mutated hands and fingers, poor drawing, amateur, bad painting, bad painting of arms, bad anatomy, mutation, extra limbs, ugly, fat
Steps: 40, Sampler: Euler a, CFG scale: 7.5, Seed: 575469807, Size: 704x512
```

<img src="https://pbs.twimg.com/media/Ff6Ank1aYAY7bxk?format=png&name=900x900" width="500" alt="ずんだもんの生成例">

```txt
zundamon , maid dress, in cafe, Kyoto Animation
Negative prompt: chibi, out of frame, armature drawing, mutated hands and fingers, poor drawing, amateur, bad painting, bad painting of arms, bad anatomy, mutation, extra limbs, ugly, fat
Steps: 40, Sampler: Euler a, CFG scale: 7.5, Seed: 429473516, Size: 512x704
```

<img src="https://pbs.twimg.com/media/Ff6AuXoakAAPtYa?format=png&name=900x900" width="500" alt="東北イタコの生成例">

```txt
itako, dating in park, cute winter fashion
Negative prompt: out of frame, amateur drawing, mutated hands and fingers, poor drawing, amateur, bad painting, bad painting of arms, bad anatomy, mutation, extra limbs, ugly, fat
Steps: 60, Sampler: Euler a, CFG scale: 7.5, Seed: 2722676181, Size: 704x512
```

<img src="https://pbs.twimg.com/media/Ff6A2lQakAAj1Bb?format=png&name=small" width="500" alt="東北ずん子と四国めたんの生成例">

```txt
zunko and metan sit on bench, in school uniform, drink tea, 2girls, in 2020s anime style
Negative prompt: chibi, armature drawing, mutated hands and fingers, poor drawing, amateur, bad painting, bad painting of arms, bad anatomy, mutation, extra limbs, ugly
Steps: 40, Sampler: Euler a, CFG scale: 7.5, Seed: 2262270937, Size: 640x512
```

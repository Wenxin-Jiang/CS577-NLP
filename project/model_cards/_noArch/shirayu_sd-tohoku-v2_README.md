---
license: creativeml-openrail-m
language:
- en
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image

---

[東北ずん子プロジェクト](https://zunko.jp/)のキャラクターイラストを用いてDreamBoothで学習したモデルです．

- ``itako``: 東北イタコ
- ``zunko``: 東北ずん子
- ``kiritan``: 東北きりたん
- ``zundamon``: ずんだもん (人間形態)
- ``metan``: 四国めたん
- ``usagi``: 中国うさぎ
- ``awamo``: 沖縄あわも
- ``shinobi``: 関西しのび
- ``hokamel``: 北海道めろん
- ``sora``: 九州そら
- ``chanko``: 大江戸ちゃんこ

学習画像はなるべく衣装にバリエーションをもたせているので，「公式衣装」は出にくいです．

[shirayu/sd-tohoku-v1](https://huggingface.co/shirayu/sd-tohoku-v1)と比べてキャラクターが増え，
学習元モデルも変更しています．
ただし，以前のモデルより完全に優れているといえるかは不明です．

[shirayu/sd-tohoku-v1](https://huggingface.co/shirayu/sd-tohoku-v1)と比較して，
その時々によって使い分けをされることをおすすめします．

また，元モデルのリリースノートの[Waifu Diffusion 1.4 Anime Release Notes](https://gist.github.com/harubaru/8581e780a1cf61352a739f2ec2eef09b)も参考にしてください．

## ファイル形式

1. [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)などckptファイルを読み込むツールの場合

    [sd-tohoku-v2.model.ckpt](https://huggingface.co/shirayu/sd-tohoku-v2/resolve/main/ckpt/sd-tohoku-v2.model.ckpt)(約2.5GB)と[sd-tohoku-v2.yaml](https://huggingface.co/shirayu/sd-tohoku-v2/resolve/main/ckpt/sd-tohoku-v2.model.yaml)をダウンロードして読み込んでください

2. [diffusers](https://github.com/huggingface/diffusers)から利用する場合

    ```python
    from diffusers import DiffusionPipeline
    pipeline = DiffusionPipeline.from_pretrained("shirayu/sd-tohoku-v2")
    ```

## 紹介動画

## ライセンス

[CreativeML Open RAIL-M license 1.0](https://hf.space/static/bigscience/license/index.html)

また，各種法令・各種ガイドラインにご留意ください．
例えば，生成された画像が東北ずん子プロジェクトのキャラクターを含む場合，
[「東北ずん子プロジェクト キャラクター利用の手引き」](https://zunko.jp/guideline.html)に基づいて利用してください．

## 学習設定

- 元モデル: [Waifu Diffusion 1.4 Anime Epoch 1](https://huggingface.co/hakurei/waifu-diffusion-v1-4) (``wd-1-4-anime_e1.ckpt``)
- 学習画像
    - 11キャラクター計111枚
    - アルファチャンネルは削除 + 白背景 + センタリング + 448x640にリサイズ
    - 正則化画像なし
- 学習元コード: [kohya-ss/sd-scripts](https://github.com/kohya-ss/sd-scripts) (``e31177adf3a2524696495e1caf8b188be1d320b6``)
- 学習設定
    - Instance ID: ``itako``, ``zunko``, ``kiritan``, ``zundamon``, ``metan``, ``usagi``, ``awamo``, ``shinobi``, ``hokamel``, ``sora``, ``chanko`` (11種)
    - Instance prompt: ``<ID>, 1girl``
    - NVIDIA A100で約160分, 600エポック
- 学習用コマンド

    ```bash
    accelerate launch \
        --num_cpu_threads_per_process 12 \
        train_db.py \
        --pretrained_model_name_or_path="wd-1-4-anime_e1.ckpt" \
        --train_data_dir="/content/data/img_train" \
        --reg_data_dir="/content/data/img_reg"  \
        --output_dir="/content/data/output_models" \
        --prior_loss_weight=1.0  \
        --resolution="448,640"  \
        --train_batch_size="4" \
        --learning_rate="1e-6"  \
        --max_train_steps="8400"  \
        --use_8bit_adam  \
        --cache_latents \
        --v2 \
        --logging_dir="/content/data/logs" \
        --save_every_n_epochs "10" \
        --save_last_n_epochs "1" \
        --save_state \
        --mixed_precision='fp16'
    ```

    後半300エポックは``--output_dir``を変え，``--resume /content/data/output_models/last-state``で再開．

## 学習に使った画像

<img src="https://huggingface.co/shirayu/sd-tohoku-v2/resolve/main/images/train_input.png" width="500" alt="学習に使った画像">

## 生成例

<img src="https://huggingface.co/shirayu/sd-tohoku-v2/resolve/main/images/example_chanko.png" width="500" alt="生成例(大江戸ちゃんこ)">

```txt
masterpiece, best quality, chanko, 1girl, white dress, sing on a stage, hold a microphone
Negative prompt: out of frame, armature drawing, mutated hands and fingers, poor drawing, amateur, bad painting, bad painting of arms, bad anatomy, mutation, extra limbs, ugly, fat
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7.5, Seed: 4103437300, Size: 512x704, Model hash: c6343649
```

<img src="https://huggingface.co/shirayu/sd-tohoku-v2/resolve/main/images/example_sora.png" width="500" alt="生成例(九州そら)">

```txt
sora, skirt, reading a book in room, smile, masterpiece, best quality, high quality, absurdres, Anime key visual
Negative prompt: worst quality, low quality, medium quality, deleted, lowres, comic, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
Steps: 55, Sampler: Euler a, CFG scale: 7.5, Seed: 4198993211, Size: 512x640, Model hash: c6343649
```

<img src="https://huggingface.co/shirayu/sd-tohoku-v2/resolve/main/images/example_usagi.png" width="500" alt="生成例(中国うさぎ)">

```txt
usagi,  1girl, miko in shrine, cleaning by holding a broom, standing, masterpiece, best quality, high quality, absurdres, Anime key visual
Negative prompt: worst quality, low quality, medium quality, deleted, lowres, comic, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7.5, Seed: 347036291, Size: 896x704, Model hash: c6343649
```

<img src="https://huggingface.co/shirayu/sd-tohoku-v2/resolve/main/images/example_awamo.png" width="500" alt="生成例(沖縄あわも)">

```txt
awamo, 1girl, summer, mountain, jumping, masterpiece, best quality, high quality, absurdres, Anime key visual, blue hair
Negative prompt: worst quality, low quality, medium quality, deleted, lowres, comic, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
Steps: 38, Sampler: DPM++ SDE Karras, CFG scale: 7.5, Seed: 1779198846, Size: 640x896, Model hash: c6343649
```

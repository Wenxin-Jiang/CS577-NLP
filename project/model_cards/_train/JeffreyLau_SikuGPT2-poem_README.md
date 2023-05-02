---
language: zh 
widget:
- text: "[CLS] 明 月 幾 時 有 ，"
- text: "[CLS] 大 漠 孤 烟 直 ，"
- text: "[CLS] 李 白 乘 舟 將 慾 行 ，"

max_length: 50

---


# SikuGPT2-Poem Model

## Model description

The model is used to generate Chinese ancient poems. You can download the model via HuggingFace from the link [SikuGPT2-poem](https://huggingface.co/JeffreyLau/SikuGPT2-poem).

Since the parameter skip_special_tokens is used in the pipelines.py, special tokens such as [SEP], [UNK] will be deleted, the output results of Hosted inference API (right) may not be properly displayed.

## How to use

You can use the model directly with a pipeline for text generation:

When the parameter skip_special_tokens is True:

```python
>>> from transformers import BertTokenizer, GPT2LMHeadModel,TextGenerationPipeline
>>> tokenizer = BertTokenizer.from_pretrained("JeffreyLau/SikuGPT2-poem")
>>> model = GPT2LMHeadModel.from_pretrained("JeffreyLau/SikuGPT2-poem")
>>> text_generator = TextGenerationPipeline(model, tokenizer)   
>>> text_generator("[CLS]明 月 幾 時 有 ，", max_length=50, do_sample=True)
    [{'generated_text': '[CLS] 明 月 幾 時 有 ， 斜 陽 正 照 人 。 落 花 雖 一 夜 ， 何 處 好 春 春 不 管 。 西 風 摇 落 不 禁 愁 ， 一 夜 寒 聲 入 客 喉 。 十 月 寒 威 侵 客 鬢 ， 四 更 清 怨 入 心 肝 。 春 風 吹 作 萬 紅 銷 ， 玉 頰 金 腮 醉 欲 眠 。 柳 色 相 和 風 雨 惡 ， 不 堪 芳 節 又 斜 暉 。 何 日 君 王 許 入 朝 ， 五 雲 驄 馬 走 黃 埃 。 白 麻 賜 出 朝 回 日 ， 一 片 春 光 滿 上 都 。 萬 里 飛 雲 上 翠 微 ， 日 華 摇 曳 照 樓 臺 。 自 從 此 際 無 人 賞 ， 還 傍 城 邊 一 穗 歸 。 三 徑 深 幽 古 未 逢 ， 野 人 行 已 自 多 求 。 高 亭 對 水 空 無 策 ， 冷 雨 疎 櫺 獨 自 垂 。 好 句 滿 山 皆 已 有 ， 清 詩 三 兩 未 全 無 。 一 徑 危 亭 接 武 湖 ， 長 沙 自 有 世 情 知 。 無 人 到 處 題 名 處 ， 不 爲 春 風 一 點 開 。 一 春 佳 處 到 清 明 ， 日 日 詩 如 錦 繡 囊 。 却 是 梅 花 有 餘 韵 ， 便 隨 風 雨 寄 林 坰 。 秋 宵 獨 坐 最 多 情 ， 客 裏 無 人 獨 坐 明 。 月 暗 竹 窗 深 又 白 ， 霜 濃 樹 葉 下 還 清 。 誰 同 坐 待 東 園 桂 ， 獨 對 寒 窗 獨 自 明 。 平 生 最 羨 太 常 孫 ， 十 二 行 人 日 暮 歸 。 夜 半 天 壇 雲 雨 合 ， 玉 鸞 啼 罷 九 成 宮 。 萬 古 蒼 梧 葉 ， 南 天 白 象 尊 。 千 年 無 鶴 舞 ， 一 夜 有 龍 吟 。'}]
```

When the parameter skip_special_tokens is False:

```python
>>> from transformers import BertTokenizer, GPT2LMHeadModel,TextGenerationPipeline
>>> tokenizer = BertTokenizer.from_pretrained("JeffreyLau/SikuGPT2-poem")
>>> model = GPT2LMHeadModel.from_pretrained("JeffreyLau/SikuGPT2-poem")
>>> text_generator = TextGenerationPipeline(model, tokenizer)   
>>> text_generator("[CLS] 明 月 幾 時 有 ，", max_length=100, do_sample=True)
    [{'generated_text': '[CLS] 明 月 幾 時 有 ， 斜 陽 正 照 人 。 落 花 雖 一 夜 ， 何 處 好 春 春 不 管 。 西 風 摇 落 不 禁 愁 ， 一 夜 寒 聲 入 客 喉 。 十 月 寒 威 侵 客 鬢 ， 四 更 清 怨 入 心 肝 。 春 風 吹 作 萬 紅 銷 ， 玉 頰 金 腮 醉 欲 眠 。 柳 色 相 和 風 雨 惡 ， 不 堪 芳 節 又 斜 暉 。 何 日 君 王 許 入 朝 ， 五 雲 驄 馬 走 黃 埃 。 白 麻 賜 出 朝 回 日 ， 一 片 春 光 滿 上 都 。 萬 里 飛 雲 上 翠 微 ， 日 華 摇 曳 照 樓 臺 。 自 從 此 際 無 人 賞 ， 還 傍 城 邊 一 穗 歸 。 三 徑 深 幽 古 未 逢 ， 野 人 行 已 自 多 求 。 高 亭 對 水 空 無 策 ， 冷 雨 疎 櫺 獨 自 垂 。 好 句 滿 山 皆 已 有 ， 清 詩 三 兩 未 全 無 。 一 徑 危 亭 接 武 湖 ， 長 沙 自 有 世 情 知 。 無 人 到 處 題 名 處 ， 不 爲 春 風 一 點 開 。 一 春 佳 處 到 清 明 ， 日 日 詩 如 錦 繡 囊 。 却 是 梅 花 有 餘 韵 ， 便 隨 風 雨 寄 林 坰 。 秋 宵 獨 坐 最 多 情 ， 客 裏 無 人 獨 坐 明 。 月 暗 竹 窗 深 又 白 ， 霜 濃 樹 葉 下 還 清 。 誰 同 坐 待 東 園 桂 ， 獨 對 寒 窗 獨 自 明 。 平 生 最 羨 太 常 孫 ， 十 二 行 人 日 暮 歸 。 夜 半 天 壇 雲 雨 合 ， 玉 鸞 啼 罷 九 成 宮 。 萬 古 蒼 梧 葉 ， 南 天 白 象 尊 。 千 年 無 鶴 舞 ， 一 夜 有 龍 吟 。'}]
```

## Training data

“Siku Quanshu” full-text corpus was used as Training Data which is same as the project of [SikuBERT](https://huggingface.co/SIKU-BERT/sikubert) to train SikuGPT2.

[Chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) was used as Training Data to train SikuGPT2-poem based on SikuGPT2.

## Training procedure

The model is Pre-trained by [run_clm.py](https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling/run_clm.py). We pre-train the model with a sequence length of 512. We use extended vocabulary to handle out-of-vocabulary words.


## Citation
The paper has not been published. You can just cite this url instead.

## SikuBERT 
https://github.com/hsc748NLP/SikuBERT-for-digital-humanities-and-classical-Chinese-information-processing

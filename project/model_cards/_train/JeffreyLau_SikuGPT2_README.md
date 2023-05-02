---
language: zh 
widget:
- text: "當 是 時 "
- text: "子 曰 "

---


# SikuGPT2 Model

## Model description

The model is used to generate Chinese ancient article. You can download the model via HuggingFace from the link [SikuGPT2](https://huggingface.co/JeffreyLau/SikuGPT2).

Since the parameter skip_special_tokens is used in the pipelines.py, special tokens such as [SEP], [UNK] will be deleted, the output results of Hosted inference API (right) may not be properly displayed.

## How to use

You can use the model directly with a pipeline for text generation:

When the parameter skip_special_tokens is True:

```python
>>> from transformers import BertTokenizer, GPT2LMHeadModel,TextGenerationPipeline
>>> tokenizer = BertTokenizer.from_pretrained("JeffreyLau/SikuGPT2")
>>> model = GPT2LMHeadModel.from_pretrained("JeffreyLau/SikuGPT2")
>>> text_generator = TextGenerationPipeline(model, tokenizer)   
>>> text_generator("當 是 時 ", max_length=100, do_sample=True)
    [{'generated_text': '當 是 時 王 世 充 已 在 西 夏 恐 兵 出 相 擊 則 遣 信 報 之 且 曰 必 以 五 百 騎 徑 渡 江 由 是 中 國 稍 安 今 賊 既 渡 江 必 無 東 救 上 曰 信 可 謂 不 亡 矣 世 充 將 何 從 與 之 書 使 者 來 上 既 見 信 書 即 遣 二 將 邀 之 使 者 皆 已 去 上 問 之 信 曰 汝 之 去 將 何 以 為 效 對 曰 吾 聞 上 使 者 至 即 令 其 人 還 信 答 書 曰 臣 受 漢 恩 厚 無 以 報 塞 然 所 以 不 從 者 誠 以 天 地 之 德 尚 寛 不 殺 之 恩 豈 待 吾 命 而 自 殺 耶 昔 劉 累 為 漢 將 不 受 命 乃 自 為 主 爾 今 既 為 漢 將 不 受 命 乃 自 殺 以 自 安 耳 上 曰 善 而 以 問 張 子 房 趙 李 牧 張 子 房 皆 言 可 與 為 盟 主 也 其 後 漢 亡 張 魯 反 於 西 河 王 霸 為 漢 公 主 求 和 乃 上 書 求 和 於 上 曰 臣 聞 古 之 受 命 者 惟 太 公 得 之 故 曰 上 天 降 威 以 作 民 主 夫 豈 能 以 一 人 之 身 而 制 天 下 之 大 敵 哉 太 公 得 之 故 曰 大 公 者 何 也 曰 夫 受 命 者 必 有 天 下 為 天 下 所 尊 服 不 必 皆 得 其 人 也 古 者 天 子 之 命 臣 為 天 子 者 皆 為 君 之 子 今 天 下 皆 為 臣 之 子 茍 不 得 其 道 則 一 人 之 身 百 姓 何 所 賴 之 可 得 然 則 命 之 不 可 謂 之 命 矣 上 曰 古 之 受 命 者 奈 何 對 曰 上 古 之 帝 也 命 已 絶 而 天 下 不 復 定 天 必 祚 之 故 命 之 不 可 謂 之 有 天 下 也 天 下 各 保 其 社 稷 其 餘 衆 官 無 有 分'}]
```

When the parameter skip_special_tokens is False:

```python
>>> from transformers import BertTokenizer, GPT2LMHeadModel,TextGenerationPipeline
>>> tokenizer = BertTokenizer.from_pretrained("JeffreyLau/SikuGPT2")
>>> model = GPT2LMHeadModel.from_pretrained("JeffreyLau/SikuGPT2")
>>> text_generator = TextGenerationPipeline(model, tokenizer)   
>>> text_generator("當 是 時 ", max_length=100, do_sample=True)
    [{'generated_text': '當 是 時 王 世 充 已 在 西 夏 恐 兵 出 相 擊 則 遣 信 報 之 且 曰 必 以 五 百 騎 徑 渡 江 由 是 中 國 稍 安 今 賊 既 渡 江 必 無 東 救 上 曰 信 可 謂 不 亡 矣 世 充 將 何 從 與 之 書 使 者 來 上 既 見 信 書 即 遣 二 將 邀 之 使 者 皆 已 去 上 問 之 信 曰 汝 之 去 將 何 以 為 效 對 曰 吾 聞 上 使 者 至 即 令 其 人 還 信 答 書 曰 臣 受 漢 恩 厚 無 以 報 塞 然 所 以 不 從 者 誠 以 天 地 之 德 尚 寛 不 殺 之 恩 豈 待 吾 命 而 自 殺 耶 昔 劉 累 為 漢 將 不 受 命 乃 自 為 主 爾 今 既 為 漢 將 不 受 命 乃 自 殺 以 自 安 耳 上 曰 善 而 以 問 張 子 房 趙 李 牧 張 子 房 皆 言 可 與 為 盟 主 也 其 後 漢 亡 張 魯 反 於 西 河 王 霸 為 漢 公 主 求 和 乃 上 書 求 和 於 上 曰 臣 聞 古 之 受 命 者 惟 太 公 得 之 故 曰 上 天 降 威 以 作 民 主 夫 豈 能 以 一 人 之 身 而 制 天 下 之 大 敵 哉 太 公 得 之 故 曰 大 公 者 何 也 曰 夫 受 命 者 必 有 天 下 為 天 下 所 尊 服 不 必 皆 得 其 人 也 古 者 天 子 之 命 臣 為 天 子 者 皆 為 君 之 子 今 天 下 皆 為 臣 之 子 茍 不 得 其 道 則 一 人 之 身 百 姓 何 所 賴 之 可 得 然 則 命 之 不 可 謂 之 命 矣 上 曰 古 之 受 命 者 奈 何 對 曰 上 古 之 帝 也 命 已 絶 而 天 下 不 復 定 天 必 祚 之 故 命 之 不 可 謂 之 有 天 下 也 天 下 各 保 其 社 稷 其 餘 衆 官 無 有 分'}]
```

## Training data

“Siku Quanshu” full-text corpus was used as Training Data which is same as the project of [SikuBERT](https://huggingface.co/SIKU-BERT/sikubert) to train SikuGPT2.

## Training procedure

The model is Pre-trained by [run_clm.py](https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling/run_clm.py). We pre-train the model with a sequence length of 512. We use extended vocabulary to handle out-of-vocabulary words.


## Citation
The paper has not been published. You can just cite this url instead.

## SikuBERT 
https://github.com/hsc748NLP/SikuBERT-for-digital-humanities-and-classical-Chinese-information-processing

## SikuGPT
https://github.com/SIKU-BERT/sikuGPT

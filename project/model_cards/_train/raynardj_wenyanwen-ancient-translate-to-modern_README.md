---
language:
- zh
- zh
tags:
- translation
- 古文
- 文言文
- ancient
- classical
widget:
- text: "此诚危急存亡之秋也"

---

# From Classical(ancient) Chinese to Modern Chinese
> This model translate Classical(ancient) Chinese to Modern Chinese, so I guess who's interested in the problemset can speak at least modern Chinese, hence... let me continue the documentation in Chinese

# 文言文（古文）到现代文的翻译器
> 这个模型已有做成应用， [【随无涯】](https://huggingface.co/spaces/raynardj/duguwen-classical-chinese-to-morden-translate)是一个huggingface spaces + streamlit 的古文阅读应用（含海量书籍）， 可以在阅读时翻译
> 输入文言文， 可以是断句 或者 未断句的文言文， 模型会预测现代文的表述。 其他模型：
* 从[现代文翻译到文言文](https://huggingface.co/raynardj/wenyanwen-chinese-translate-to-ancient)

> 从文言文到现代文的翻译器, 欢迎前往[我的github文言诗词项目页面探讨、加⭐️ ](https://github.com/raynardj/yuan)

> 训练语料是就是九十多万句句对， [数据集链接📚](https://github.com/BangBOOM/Classical-Chinese)。 训练时source序列（古文序列）， 按照50%的概率整句去除所有标点符号。

## 推荐的inference 通道
**注意**
* 你必须将```generate```函数的```eos_token_id```设置为102就可以翻译出完整的语句， 不然翻译完了会有残留的语句(因为做熵的时候用pad标签=-100导致)。
目前huggingface 页面上compute按钮会有这个问题， 推荐使用以下代码来得到翻译结果
* 请设置```generate```的参数```num_beams>=3```, 以达到较好的翻译效果
* 请设置```generate```的参数```max_length```256， 不然结果会吃掉句子
```python
from transformers import (
  EncoderDecoderModel,
  AutoTokenizer
)
PRETRAINED = "raynardj/wenyanwen-ancient-translate-to-modern"
tokenizer = AutoTokenizer.from_pretrained(PRETRAINED)
model = EncoderDecoderModel.from_pretrained(PRETRAINED)
def inference(text):
    tk_kwargs = dict(
      truncation=True,
      max_length=128,
      padding="max_length",
      return_tensors='pt')
   
    inputs = tokenizer([text,],**tk_kwargs)
    with torch.no_grad():
        return tokenizer.batch_decode(
            model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            num_beams=3,
            max_length=256,
            bos_token_id=101,
            eos_token_id=tokenizer.sep_token_id,
            pad_token_id=tokenizer.pad_token_id,
        ), skip_special_tokens=True)
```

## 目前版本的案例
> 当然， 拿比较熟知的语句过来， 通常会有些贻笑大方的失误， 大家如果有好玩的调戏案例， 也欢迎反馈
```python
>>> inference('非我族类其心必异')
['不 是 我 们 的 族 类 ， 他 们 的 心 思 必 然 不 同 。']
>>> inference('肉食者鄙未能远谋')
['吃 肉 的 人 鄙 陋 ， 不 能 长 远 谋 划 。']
# 这里我好几批模型都翻不出这个**输**字（甚至有一个版本翻成了秦始皇和汉武帝）， 可能并不是很古朴的用法， 
>>> inference('江山如此多娇引无数英雄竞折腰惜秦皇汉武略输文采唐宗宋祖稍逊风骚')
['江 山 如 此 多 ， 招 引 无 数 的 英 雄 ， 竞 相 折 腰 ， 可 惜 秦 皇 、 汉 武 ， 略 微 有 文 采 ， 唐 宗 、 宋 祖 稍 稍 逊 出 风 雅 。']
>>> inference("清风徐来水波不兴")
['清 风 慢 慢 吹 来 ， 水 波 不 兴 。']
>>> inference("无他唯手熟尔")
['没 有 别 的 事 ， 只 是 手 熟 罢 了 。']
>>> inference("此诚危急存亡之秋也")
['这 实 在 是 危 急 存 亡 的 时 候 。']
```

## 其他文言诗词的资源
* [项目源代码 🌟, 欢迎+star提pr](https://github.com/raynardj/yuan)
* [跨语种搜索 🔎](https://huggingface.co/raynardj/xlsearch-cross-lang-search-zh-vs-classicical-cn)
* [现代文翻译古汉语的模型 ⛰](https://huggingface.co/raynardj/wenyanwen-chinese-translate-to-ancient)
* [古汉语到现代文的翻译模型, 输入可以是未断句的句子 🚀](https://huggingface.co/raynardj/wenyanwen-ancient-translate-to-modern)
* [断句模型 🗡](https://huggingface.co/raynardj/classical-chinese-punctuation-guwen-biaodian)
* [意境关键词 和 藏头写诗🤖](https://huggingface.co/raynardj/keywords-cangtou-chinese-poetry)
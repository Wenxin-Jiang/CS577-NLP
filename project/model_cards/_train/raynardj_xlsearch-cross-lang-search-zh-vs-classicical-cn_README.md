---

language:
- zh
tags:
- search

---

# Cross Language Search
## Search cliassical CN with modern ZH
* In some cases, Classical Chinese feels like another language, I even trained 2 translation models ([1](https://huggingface.co/raynardj/wenyanwen-chinese-translate-to-ancient) and [2](https://huggingface.co/raynardj/wenyanwen-ancient-translate-to-modern)) to prove this point.
* That's why, when people wants to be savvy about their words, we choose to quote our ancestors. It's exactly like westerners like to quote Latin or Shakespeare, the difference is we have a much bigger pool to choose.
* This model helps you **find** text within **ancient Chinese** literature, but you can **search with modern Chinese**

# 跨语种搜索
## 博古搜今
* 我不记得是谁， 哪个朝代，我只记得大概这么一个事儿，我就能模糊找到原文
* 我不记得原文， 但是我只记得原文想表达的现代汉语意思， 希望能找出来引用一下。
* 我在写文章， 有个观点， 我想碰运气看看古人有没有提过同样类似的说法。
* 我只是想更有效率地阅读古文

推荐的使用通道如下，当然， cosine距离搜索相关的框架和引擎很多， 大家自己看着适用的选

装包
```shell
pip install -Uqq unpackai
pip install -Uqq SentenceTransformer
```

搜索语句的函数
```python
from unpackai.interp import CosineSearch
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

TAG = "raynardj/xlsearch-cross-lang-search-zh-vs-classicical-cn"
encoder = SentenceTransformer(TAG)

# all_lines is a list of all your sentences
# all_lines 是一个你所有句子的列表， 可以是一本书， 按照句子分割， 也可以是很多很多书
all_lines = ["句子1","句子2",...]
vec = encoder.encode(all_lines, batch_size=32, show_progress_bar=True)

# consine距离搜索器
cosine = CosineSearch(vec)

def search(text):
    enc = encoder.encode(text) # encode the search key
    order = cosine(enc) # distance array
    sentence_df = pd.DataFrame({"sentence":np.array(all_lines)[order[:5]]})
    return sentence_df
```

将史记打成句子以后， 搜索效果是这样的：

```python
>>> search("他是一个很慷慨的人")
```
```
sentence
0	季布者，楚人也。为气任侠，有名於楚。
1	董仲舒为人廉直。
2	大将军为人仁善退让，以和柔自媚於上，然天下未有称也。
3	勃为人木彊敦厚，高帝以为可属大事。
4	石奢者，楚昭王相也。坚直廉正，无所阿避。
```

```python
>>> search("进入军营，必须缓缓牵着马骑")
```
```
sentence
0	壁门士吏谓从属车骑曰：将军约，军中不得驱驰。
1	起之为将，与士卒最下者同衣食。卧不设席，行不骑乘，亲裹赢粮，与士卒分劳苦。
2	既出，沛公留车骑，独骑一马，与樊哙等四人步从，从间道山下归走霸上军，而使张良谢项羽。
3	顷之，上行出中渭桥，有一人从穚下走出，乘舆马惊。
4	元狩四年春，上令大将军青、骠骑将军去病将各五万骑，步兵转者踵军数十万，而敢力战深入之士皆属骠骑。
```

## 其他资源清单
* [项目源代码 🌟, 欢迎+star提pr](https://github.com/raynardj/yuan)
* [跨语种搜索 🔎](https://huggingface.co/raynardj/xlsearch-cross-lang-search-zh-vs-classicical-cn)
* [现代文翻译古汉语的模型 ⛰](https://huggingface.co/raynardj/wenyanwen-chinese-translate-to-ancient)
* [古汉语到现代文的翻译模型, 输入可以是未断句的句子 🚀](https://huggingface.co/raynardj/wenyanwen-ancient-translate-to-modern)
* [断句模型 🗡](https://huggingface.co/raynardj/classical-chinese-punctuation-guwen-biaodian)
* [意境关键词 和 藏头写诗🤖](https://huggingface.co/raynardj/keywords-cangtou-chinese-poetry)
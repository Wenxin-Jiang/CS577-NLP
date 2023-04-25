---
language:
- zh
tags:
- ner
- punctuation
- 古文
- 文言文
- ancient
- classical
widget:
- text: "郡邑置夫子庙于学以嵗时释奠盖自唐贞观以来未之或改我宋有天下因其制而损益之姑苏当浙右要区规模尤大更建炎戎马荡然无遗虽修学宫于荆榛瓦砾之余独殿宇未遑议也每春秋展礼于斋庐已则置不问殆为阙典今寳文阁直学士括苍梁公来牧之明年实绍兴十有一禩也二月上丁修祀既毕乃愓然自咎揖诸生而告之曰天子不以汝嘉为不肖俾再守兹土顾治民事神皆守之职惟是夫子之祀教化所基尤宜严且谨而拜跪荐祭之地卑陋乃尔其何以掲防妥灵汝嘉不敢避其责曩常去此弥年若有所负尚安得以罢輭自恕复累后人乎他日或克就绪愿与诸君落之于是谋之僚吏搜故府得遗材千枚取赢资以给其费鸠工庀役各举其任嵗月讫工民不与知像设礼器百用具修至于堂室廊序门牖垣墙皆一新之"

---

# Classical Chinese Punctuation

> 欢迎前往[我的github文言诗词项目页面探讨、加⭐️ ](https://github.com/raynardj/yuan)， Please check the github repository for more about the [model, hit 🌟 if you like](https://github.com/raynardj/yuan)
 
* This model punctuates Classical(ancient) Chinese, you might feel strange about this task, but **many of my ancestors think writing articles without punctuation is brilliant idea** 🧐. What we have here are articles from books, letters or carved on stones where you can see no punctuation, just a long string of characters. As you can guess, NLP tech is usually a good tool to tackle this problem, and the entire pipeline can be borrowed from usual **NER task**.

* Since there are also many articles are punctuated, hence with some regex operations, labeled data is more than abundant 📚. That's why this problem is pretty much a low hanging fruit.

* so I guess who's interested in the problem set can speak at least modern Chinese, hence... let me continue the documentation in Chinese. 

# 文言文(古文) 断句模型
> 输入一串未断句文言文， 可以断句， 目前支持二十多种标点符号

## 其他文言诗词的资源
* [项目源代码 🌟, 欢迎+star提pr](https://github.com/raynardj/yuan)
* [跨语种搜索 🔎](https://huggingface.co/raynardj/xlsearch-cross-lang-search-zh-vs-classicical-cn)
* [现代文翻译古汉语的模型 ⛰](https://huggingface.co/raynardj/wenyanwen-chinese-translate-to-ancient)
* [古汉语到现代文的翻译模型, 输入可以是未断句的句子 🚀](https://huggingface.co/raynardj/wenyanwen-ancient-translate-to-modern)
* [断句模型 🗡](https://huggingface.co/raynardj/classical-chinese-punctuation-guwen-biaodian)
* [意境关键词 和 藏头写诗🤖](https://huggingface.co/raynardj/keywords-cangtou-chinese-poetry)
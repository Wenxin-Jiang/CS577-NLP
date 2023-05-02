在bert-base-chinese基础上进行新闻语料库的增量预训练的模型，token采用的是bert-base-chinese
Model
模型导出时将生成 config.json 和 pytorch_model.bin 参数文件
Tokenizer
这是一个将纯文本转换为编码的过程。注意，Tokenizer 并不涉及将词转化为词向量的过程，仅仅是将纯文本分词，添加[MASK]标记、[SEP]、[CLS]标记，并转换为字典索引。Tokenizer 类导出时将分为三个文件
vocab.txt 词典文件，每一行为一个词或词的一部分
special_tokens_map.json 特殊标记的定义方式
tokenizer_config.json 配置文件，主要存储特殊的配置
模型的所有分词器都是在 PreTrainedTokenizer 中实现的，分词的结果主要有以下内容：
"input ids": 顾名思义，是单词在词典中的编码
"token type ids":区分两个句子的编码
"attention mask":指定对哪些词进行self-Attention操作
"overflowing tokens":当指定最大长度时，溢出的单词
"num truncated tokens":溢出的token数量
"return special tokens mask":如果添加特殊标记，则这是[0，1]的列表，其中0指定特殊添加的标记，而1指定序列标记
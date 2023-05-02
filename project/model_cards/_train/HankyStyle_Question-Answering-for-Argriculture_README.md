---
language: zh
datasets:
- ArgricultureQA
model-index:
- name: HankyStyle/Question-Answering-for-Argriculture
  results:
    - task:
        type: question-answering
        name: Question Answering
      dataset:
        name: ArgricultureQA
        type: ArgricultureQA
        config: ArgricultureQA
      metrics:
      - name: Exact Match
        type: exact_match
        value: 76.00
        verified: true
      - name: F1
        type: f1
        value: 76.00
        verified: true
        
---

# bert-base-multilingual-cased for QA 

This is the [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) model, fine-tuned using the Argriculture QA and DRCD dataset. It's been trained on question-answer pairs for the task of Question Answering.

## Usage

### In Transformers
```python
from transformers import BertTokenizerFast, BertForQuestionAnswering, pipeline
model_name = "HankyStyle/Question-Answering-for-Argriculture"
tokenizer = BertTokenizerFast.from_pretrained(model_name)
model = BertForQuestionAnswering.from_pretrained(model_name)


# a) Get predictions
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
QA_input = {
    'question': '哪一種植物在根據綜合主成分分析表明可以促進枯落葉養分釋放?',
    'context': '以黃土高原主要造林樹種落葉松(Larix principis-rupprechtii)及其他擬混雜的10個樹種為對象，採集當年枯落葉并以無林荒草地腐殖質層土壤作為分解介質，在室內將落葉松與其他樹種枯落葉單獨或以一定比例混合後裝入尼龍網袋並埋入盛土培養缽中，進行恒溫(20~25℃)恒濕(50%田間持水量)下連續345 d分解培養試驗。結果表明：枯落葉單獨分解時，大量元素整體上較微量元素容易釋出。除C和 N外，其他元素釋出速率與其初始含量無顯著相關關係(C為負相關，N正相關)。根據綜合主成分分析表明，與落葉松枯落葉混合分解總體上明顯促進養分釋放的樹種為白榆(Ulmus pumila)和油松(Pinus tabulaeformis)，其次為白樺(Betula platyphylla)；總體上明顯抑制養分釋放的樹種為側柏(Platycladus orientalis)和刺槐(Robinia pseudoacacia)，其次為小葉楊(Populus simonii)。能夠促進枯落葉養分釋放的樹種將是選擇與落葉松混雜樹種時首先考慮的物種。'
}
res = nlp(QA_input)

```

## Authors
**Han Cheng Yu:** boy19990222@gmail.com

**Yao-Chung Fan:** yfan@nchu.edu.tw

## About us

[中興大學自然語言處理實驗室](https://nlpnchu.org/)研究方向圍繞於深度學習技術在文字資料探勘 (Text Mining) 與自然語言處理 (Natural Language Processing) 方面之研究，目前實驗室成員的研究主題著重於機器閱讀理解 (Machine Reading Comprehension) 以及自然語言生成 (Natural Language Generation) 兩面向。

## More Information

<p>For more info about Nchu NLP Lab, visit our <strong><a href="https://demo.nlpnchu.org/">Lab Online Demo</a></strong> repo and <strong><a href="https://github.com/NCHU-NLP-Lab">GitHub</a></strong>. 
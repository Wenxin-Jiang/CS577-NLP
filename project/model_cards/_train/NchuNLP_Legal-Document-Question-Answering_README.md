---
language: zh
datasets:
- LegalDocumentDataset

---
# bert-base-chinese for QA 

This is the [bert-base-chinese](https://huggingface.co/bert-base-chinese) model, fine-tuned using the Legal Document Dataset. It's been trained on question-answer pairs for the task of Question Answering.

## Usage

### In Transformers
```python
from transformers import BertTokenizerFast, BertForQuestionAnswering, pipeline
model_name = "NchuNLP/Legal-Document-Question-Answering"
tokenizer = BertTokenizerFast.from_pretrained(model_name)
model = BertForQuestionAnswering.from_pretrained(model_name)

# a) Get predictions
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
QA_input = {
    'question': '被告人偽造了什麼文書?',
    'context': '犯罪事實一、韓金虎在采豐開發有限公司（址設臺北市○○區○○路0段000巷00○0號，下稱采豐公司）擔任臨時派遣員工，詎其竟意圖為自己不法之所有，基於行使偽造私文書、詐欺取財等犯意，於民國110年9月2日下午5時20分前某時許，在不詳地點，在采豐公司所使用之空白工作確認單中主任簽名欄上偽簽謝宏奇之簽名，佯裝其有於110年9月1日到班工作，並經工地主任確認之意，提出與采豐公司主任曾子昕而行使之，曾子昕因見該份工作確認單上有謝奇宏之簽名，因陷於錯誤而信韓金虎確實有於110年9月1日到班工作，准發薪資新臺幣（下同）2,000元給韓金虎，足生損害於采豐公司。嗣曾子昕於110年9月3日上午11時20分許，發現工作確認單點交數量有異，遂報警處理，始悉上情。二、案經曾子昕訴由臺北市政府警察局萬華分局報告偵辦。'
}
res = nlp(QA_input)

```
## Authors
**Kei Yu Heish:** iove22@hotmail.com

**Yao-Chung Fan:** yfan@nchu.edu.tw

## About us

[中興大學自然語言處理實驗室](https://nlpnchu.org/)研究方向圍繞於深度學習技術在文字資料探勘 (Text Mining) 與自然語言處理 (Natural Language Processing) 方面之研究，目前實驗室成員的研究主題著重於機器閱讀理解 (Machine Reading Comprehension) 以及自然語言生成 (Natural Language Generation) 兩面向。

## More Information

<p>For more info about Nchu NLP Lab, visit our <strong><a href="https://demo.nlpnchu.org/">Lab Online Demo</a></strong> repo and <strong><a href="https://github.com/NCHU-NLP-Lab">GitHub</a></strong>. 
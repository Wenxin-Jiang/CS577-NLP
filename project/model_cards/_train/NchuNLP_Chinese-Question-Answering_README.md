---
language: zh
datasets:
- DeltaReadingComprehensionDataset
widget:
- text: "中興大學在哪裡?"
  context: "國立中興大學（簡稱興大、NCHU），是位於臺中的一所高等教育機構。中興大學以農業科學、農業經濟學、獸醫、生命科學、轉譯醫學、生醫工程、生物科技、綠色科技等研究領域見長 。近年中興大學與臺中榮民總醫院、彰化師範大學、中國醫藥大學等機構合作，聚焦於癌症醫學、免疫醫學及醫學工程三項領域，將實驗室成果逐步應用到臨床上，未來「衛生福利部南投醫院中興院區」將改為「國立中興大學醫學院附設醫院」。興大也與臺中市政府合作，簽訂合作意向書，共同推動數位文化、智慧城市等面相帶動區域發展。"
- text: "我住在哪裡?"
  context: "我叫翰承，我住在台中。"

---
# bert-base-chinese for QA 

This is the [bert-base-chinese](https://huggingface.co/bert-base-chinese) model, fine-tuned using the DRCD dataset. It's been trained on question-answer pairs for the task of Question Answering.

## Usage

### In Transformers
```python
from transformers import BertTokenizerFast, BertForQuestionAnswering, pipeline
model_name = "NchuNLP/Chinese-Question-Answering"
tokenizer = BertTokenizerFast.from_pretrained(model_name)
model = BertForQuestionAnswering.from_pretrained(model_name)

# a) Get predictions 
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
QA_input = {
    'question': '中興大學在哪裡？',
    'context': '國立中興大學（簡稱興大、NCHU），是位於臺中的一所高等教育機構。中興大學以農業科學、農業經濟學、獸醫、生命科學、轉譯醫學、生醫工程、生物科技、綠色科技等研究領域見長 。近年中興大學與臺中榮民總醫院、彰化師範大學、中國醫藥大學等機構合作，聚焦於癌症醫學、免疫醫學及醫學工程三項領域，將實驗室成果逐步應用到臨床上，未來「衛生福利部南投醫院中興院區」將改為「國立中興大學醫學院附設醫院」。興大也與臺中市政府合作，簽訂合作意向書，共同推動數位文化、智慧城市等面相帶動區域發展。'
}
res = nlp(QA_input)

{'score': 1.0, 'start': 21, 'end': 23, 'answer': '臺中'}

# b) Inside the Question answering pipeline

inputs = tokenizer(query, text, return_tensors="pt",padding=True, truncation=True, max_length=512, stride=256)
outputs = model(**inputs)

sequence_ids = inputs.sequence_ids()
# Mask everything apart from the tokens of the context
mask = [i != 1 for i in sequence_ids]
# Unmask the [CLS] token
mask[0] = False
mask = torch.tensor(mask)[None]

start_logits[mask] = -10000
end_logits[mask] = -10000

start_probabilities = torch.nn.functional.softmax(start_logits, dim=-1)[0]
end_probabilities = torch.nn.functional.softmax(end_logits, dim=-1)[0]

scores = start_probabilities[:, None] * end_probabilities[None, :]

max_index = scores.argmax().item()
start_index = max_index // scores.shape[1]
end_index = max_index % scores.shape[1]


inputs_with_offsets = tokenizer(query, text, return_offsets_mapping=True)
offsets = inputs_with_offsets["offset_mapping"]

start_char, _ = offsets[start_index]
_, end_char = offsets[end_index]
answer = text[start_char:end_char]

result = {
    "answer": answer,
    "start": start_char,
    "end": end_char,
    "score": scores[start_index, end_index],
}
print(result)

```

## Authors
**Han Cheng Yu:** boy19990222@gmail.com

**Yao-Chung Fan:** yfan@nchu.edu.tw

## About us

[中興大學自然語言處理實驗室](https://nlpnchu.org/)研究方向圍繞於深度學習技術在文字資料探勘 (Text Mining) 與自然語言處理 (Natural Language Processing) 方面之研究，目前實驗室成員的研究主題著重於機器閱讀理解 (Machine Reading Comprehension) 以及自然語言生成 (Natural Language Generation) 兩面向。

## More Information

<p>For more info about Nchu NLP Lab, visit our <strong><a href="https://demo.nlpnchu.org/">Lab Online Demo</a></strong> repo and <strong><a href="https://github.com/NCHU-NLP-Lab">GitHub</a></strong>. 
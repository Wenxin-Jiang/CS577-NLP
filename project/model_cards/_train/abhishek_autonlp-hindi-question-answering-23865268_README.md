---
tags:
- autonlp
- question-answering
language: hi
widget:
- text: "´सतीश धवन अंतरिक्ष केंद्र´ किस राज्य में स्थित है?"
  context: "सतीश धवन अंतरिक्ष केंद्र, भारतीय अंतरिक्ष अनुसंधान संगठन (इसरो) का प्रक्षेपण केंद्र है। यह आंध्र प्रदेश के श्रीहरीकोटा में स्थित है, इसे 'श्रीहरीकोटा रेंज' या 'श्रीहरीकोटा लाँचिंग रेंज' के नाम से भी जाना जाता है। 2002 में इसरो के पूर्व प्रबंधक और वैज्ञानिक सतीश धवन के मरणोपरांत उनके सम्मान में इसका नाम बदला गया। प्रक्षेपण यान की असेम्\u200dबली के लिए दूसरा भवन केन्\u200dद्रीय मंत्रिमंडल ने 12 सितम्\u200dबर, 2013 को सतीश धवन अंतरिक्ष केन्\u200dद्र, श्रीहरिकोटा में प्रक्षेपण यान की असेम्\u200dबली के लिए दूसरे भवन के निर्माण की मंजूरी दी। इस पर 363.95 करोड़ रुपये की अनुमानित लागत आएगी, जिसमें सात करोड़ रुपये का खर्च विदेशी मुद्रा में होगा। इस दूसरी बिल्डिंग के उपलब्\u200dध हो जाने से पीएसएलवी और जीएसएलवी की प्रक्षेपण फ्रीक्वेंसी बढ़ेगी। यह जीएसएलवी एमके-III के एकीकरण के लिए वर्तमान व्\u200dहीकल असेम्\u200dबली बिल्डिंग को अतिरिक्\u200dत सुविधा मुहैया करायेगी। तीसरे प्रक्षेपण पैड तथा भविष्\u200dय में सामान्\u200dय यान प्रक्षेपण के लिए भी इससे काफी सुविधा मिलेगी।[1]\nलांच पैड\nउपग्रह प्रक्षेपण यान लॉन्च पैड\nइस लांच पैड से उपग्रह प्रक्षेपण यान और संवर्धित उपग्रह प्रक्षेपण यान को लांच किया गया था। यह वर्तमान प्रक्षेपण स्थल के दक्षिणी सिरे पर स्थित है। इसे सेवामुक्त कर दिया गया है। शुरू में इसे उपग्रह प्रक्षेपण यान लांच करने के लिए बनाया गया था। लेकिन बाद में इसे संवर्धित उपग्रह प्रक्षेपण यान प्रक्षेपण परिसर के रूप में इस्तेमाल किया गया था।\nप्रथम लांच पैड\nद्वितीय लॉन्च पैड\nतृतीय लांच पैड\nसन्दर्भ श्रेणी:भारतीय अंतरिक्ष अनुसंधान संगठन\nश्रेणी:भारत के रॉकेट प्रक्षेपण स्थल"
datasets:
- abhishek/autonlp-data-hindi-question-answering
co2_eq_emissions: 39.76330395590446
---

# Model Trained Using AutoNLP

- Problem type: Extractive Question Answering
- CO2 Emissions (in grams): 39.76330395590446


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"question": "Who loves AutoNLP?", "context": "Everyone loves AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-hindi-question-answering-23865268
```

Or Python API:

```
import torch

from transformers import AutoModelForQuestionAnswering, AutoTokenizer

model = AutoModelForQuestionAnswering.from_pretrained("abhishek/autonlp-hindi-question-answering-23865268", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-hindi-question-answering-23865268", use_auth_token=True)

from transformers import BertTokenizer, BertForQuestionAnswering

question, text = "Who loves AutoNLP?", "Everyone loves AutoNLP"

inputs = tokenizer(question, text, return_tensors='pt')

start_positions = torch.tensor([1])

end_positions = torch.tensor([3])

outputs = model(**inputs, start_positions=start_positions, end_positions=end_positions)

loss = outputs.loss

start_scores = outputs.start_logits

end_scores = outputs.end_logits
```
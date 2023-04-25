---
language:
- fa
- multilingual
thumbnail: https://upload.wikimedia.org/wikipedia/commons/a/a2/Farsi.svg
tags:
- sentiment
- sentiment-analysis
- mt5
- persian
- farsi
license: cc-by-nc-sa-4.0
datasets:
- parsinlu
metrics:
- accuracy
---

# Sentiment Analysis (آنالیز احساسات)

This is a mT5 model for sentiment analysis.
Here is an example of how you can run this model: 

```python 
import torch
from transformers import MT5ForConditionalGeneration, MT5Tokenizer
import numpy as np

model_name_or_path = "persiannlp/mt5-base-parsinlu-sentiment-analysis"
tokenizer = MT5Tokenizer.from_pretrained(model_name)
model = MT5ForConditionalGeneration.from_pretrained(model_name)


def model_predict(text_a, text_b):
    features = tokenizer( [(text_a, text_b)], padding="max_length", truncation=True, return_tensors='pt')
    output = model(**features)
    logits = output[0]
    probs = torch.nn.functional.softmax(logits, dim=1).tolist()
    idx = np.argmax(np.array(probs))
    print(labels[idx], probs)


def run_model(context, query, **generator_args):
    input_ids = tokenizer.encode(context + "<sep>" + query, return_tensors="pt")
    res = model.generate(input_ids, **generator_args)
    output = tokenizer.batch_decode(res, skip_special_tokens=True)
    print(output)
    return output


run_model(
    "یک فیلم ضعیف بی محتوا بدون فیلمنامه . شوخی های سخیف .",
    "نظر شما در مورد داستان، فیلمنامه، دیالوگ ها و موضوع فیلم  لونه زنبور چیست؟"
)

run_model(
    "فیلم تا وسط فیلم یعنی دقیقا تا جایی که معلوم میشه بچه های املشی دنبال رضان خیلی خوب و جذاب پیش میره ولی دقیقا از همونجاش سکته میزنه و خلاص...",
    "نظر شما به صورت کلی در مورد فیلم  ژن خوک چیست؟"
)
run_model(
    "اصلا به هیچ عنوان علاقه نداشتم اجرای می سی سی پی نشسته میمیرد روی پرده سینما ببینم  دیالوگ های تکراری   هلیکوپتر  ماشین  آلندلون  لئون  پاپیون  آخه چرااااااااااااااا   همون حسی که توی تالار وحدت بعد از نیم ساعت به سرم اومد امشب توی سالن سینما تجربه کردم ،حس گریز از سالن.......⁦ ⁦(ノಠ益ಠ)ノ⁩ ",
    " نظر شما در مورد صداگذاری و جلوه های صوتی فیلم  مسخره‌باز چیست؟"
)

run_model(
    " گول نخورید این رنگارنگ مینو نیست برای شرکت گرجیه و متاسفانه این محصولش اصلا مزه رنگارنگی که انتظار دارید رو نمیده ",
    " نظر شما در مورد عطر، بو، و طعم این بیسکویت و ویفر چیست؟"
)

run_model(
    "در مقایسه با سایر برندهای موجود در بازار با توجه به حراجی که داشت ارزانتر ب",
    " شما در مورد قیمت و ارزش خرید این حبوبات و سویا چیست؟"
)

run_model(
    "من پسرم عاشق ایناس ولی دیگه به خاطر حفظ محیط زیست فقط زمانهایی که مجبور باشم شیر دونه ای میخرم و سعی میکنم دیگه کمتر شیر با بسته بندی تتراپک استفاده کنم ",
    "نظر شما به صورت کلی در مورد این شیر چیست؟"
)
```


For more details, visit this page: https://github.com/persiannlp/parsinlu/ 

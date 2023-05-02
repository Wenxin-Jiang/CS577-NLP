---
language: en
datasets:
- tweet_qa
tags:
- qa
- Question Answering
widget:
- text: "question: how far away was the putt context: GET THE CIGAR READY! Miguel aces the 15th from 174 yards, and celebrates as only he knows how! The European Tour (@EuropeanTour) January, 15 2015"

---


# ByT5-base fine-tuned for Question Answering (on Tweets)
[ByT5](https://huggingface.co/google/byt5-base) base fine-tuned on [TweetQA](https://huggingface.co/datasets/tweet_qa) dataset for **Question Answering** downstream task.

# Details of ByT5 - Base 🧠

ByT5 is a tokenizer-free version of [Google's T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) and generally follows the architecture of [MT5](https://huggingface.co/google/mt5-base).
ByT5 was only pre-trained on [mC4](https://www.tensorflow.org/datasets/catalog/c4#c4multilingual) excluding any supervised training with an average span-mask of 20 UTF-8 characters. Therefore, this model has to be fine-tuned before it is usable on a downstream task.
ByT5 works especially well on noisy text data,*e.g.*, `google/byt5-base` significantly outperforms [mt5-base](https://huggingface.co/google/mt5-base) on [TweetQA](https://arxiv.org/abs/1907.06292).
Paper: [ByT5: Towards a token-free future with pre-trained byte-to-byte models](https://arxiv.org/pdf/1910.10683.pdf)
Authors: *Linting Xue, Aditya Barua, Noah Constant, Rami Al-Rfou, Sharan Narang, Mihir Kale, Adam Roberts, Colin Raffel* 


## Details of the downstream task (Question Answering) - Dataset 📚

[TweetQA](https://huggingface.co/datasets/tweet_qa)


With social media becoming increasingly more popular, lots of news and real-time events are being covered. Developing automated question answering systems is critical to the effectiveness of many applications that rely on real-time knowledge. While previous question answering (QA) datasets have focused on formal text such as news and Wikipedia, we present the first large-scale dataset for QA over social media data. To make sure that the tweets are meaningful and contain interesting information, we gather tweets used by journalists to write news articles. We then ask human annotators to write questions and answers upon these tweets. Unlike other QA datasets like SQuAD (in which the answers are extractive), we allow the answers to be abstractive. The task requires the model to read a short tweet and a question and outputs a text phrase (does not need to be in the tweet) as the answer.

- Data Instances:

Sample

```json
{
    "Question": "who is the tallest host?",
    "Answer": ["sam bee","sam bee"],
    "Tweet": "Don't believe @ConanOBrien's height lies. Sam Bee is the tallest host in late night. #alternativefacts\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\u2014 Full Frontal (@FullFrontalSamB) January 22, 2017",
    "qid": "3554ee17d86b678be34c4dc2c04e334f"
}
```
- Data Fields:
 
*Question*: a question based on information from a tweet 

*Answer*: list of possible answers from the tweet 

*Tweet*: source tweet 

*qid*: question id



## Model in Action 🚀

```sh
git clone https://github.com/huggingface/transformers.git
pip install -q ./transformers
```

```python
from transformers import AutoTokenizer, T5ForConditionalGeneration

ckpt = 'Narrativa/byt5-base-finetuned-tweet-qa'

tokenizer = AutoTokenizer.from_pretrained(ckpt)
model = T5ForConditionalGeneration.from_pretrained(ckpt).to('cuda')

def get_answer(question, context):

    input_text = 'question: %s context: %s' % (question, context)
    inputs = tokenizer([input_text], return_tensors='pt')
    input_ids = inputs.input_ids.to('cuda')
    attention_mask = inputs.attention_mask.to('cuda')
    output = model.generate(input_ids, attention_mask=attention_mask)
    return tokenizer.decode(output[0], skip_special_tokens=True)


context = "MONSTARS BASKETBALL @M0NSTARSBBALLWiggins answers Kemba's floater with a three! game tied 106-106. 8.9 to play. CHA ball!12/4/2016, 2:26:30 AM"
question = 'who answered kemba\'s "floater"?'     
    
get_answer(question, context)
# wiggins
```

Created by: [Narrativa](https://www.narrativa.com/)

About Narrativa: Natural Language Generation (NLG) | Gabriele, our machine learning-based platform, builds and deploys natural language solutions. #NLG #AI
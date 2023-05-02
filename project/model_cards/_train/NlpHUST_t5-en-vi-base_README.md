# T5-EN-VI-BASE:Pretraining Text-To-Text Transfer Transformer for English Vietnamese Translation

# Dataset

The *IWSLT'15 English-Vietnamese* data is used from [Stanford NLP group](https://nlp.stanford.edu/projects/nmt/).

For all experiments the corpus was split into training, development and test set:

| Data set    | Sentences | Download
| ----------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------
| Training    | 133,317   | via [GitHub](https://github.com/stefan-it/nmt-en-vi/raw/master/data/train-en-vi.tgz) or located in `data/train-en-vi.tgz`
| Development |   1,553   | via [GitHub](https://github.com/stefan-it/nmt-en-vi/raw/master/data/dev-2012-en-vi.tgz) or located in `data/dev-2012-en-vi.tgz`
| Test        |   1,268   | via [GitHub](https://github.com/stefan-it/nmt-en-vi/raw/master/data/test-2013-en-vi.tgz) or located in `data/test-2013-en-vi.tgz`


## Results

The results on test set.

| Model                                                                                                 | BLEU (Beam Search)
| ----------------------------------------------------------------------------------------------------- | ------------------
| [Luong & Manning (2015)](https://nlp.stanford.edu/pubs/luong-manning-iwslt15.pdf)                     | 23.30
| Sequence-to-sequence model with attention                                                             | 26.10
| Neural Phrase-based Machine Translation [Huang et. al. (2017)](https://arxiv.org/abs/1706.05565)      | 27.69
| Neural Phrase-based Machine Translation + LM [Huang et. al. (2017)](https://arxiv.org/abs/1706.05565) | 28.07
| t5-en-vi-small (pretraining, without training data)                                                                                 | **28.46** (cased) / **29.23** (uncased)
|t5-en-vi-small (fineturning with training data)  | **32.38** (cased) / **33.19** (uncased)
| t5-en-vi-base (pretraining, without training data)   | **29.66** (cased) / **30.37** (uncased)
#### Example Using

``` bash
import torch

from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
if torch.cuda.is_available():       
    device = torch.device("cuda")

    print('There are %d GPU(s) available.' % torch.cuda.device_count())

    print('We will use the GPU:', torch.cuda.get_device_name(0))
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")

model = T5ForConditionalGeneration.from_pretrained("NlpHUST/t5-en-vi-small")
tokenizer = T5Tokenizer.from_pretrained("NlpHUST/t5-en-vi-small")
model.to(device)

src = "In school , we spent a lot of time studying the history of Kim Il-Sung , but we never learned much about the outside world , except that America , South Korea , Japan are the enemies ."
tokenized_text = tokenizer.encode(src, return_tensors="pt").to(device)
model.eval()
summary_ids = model.generate(
                    tokenized_text,
                    max_length=128, 
                    num_beams=5,
                    repetition_penalty=2.5, 
                    length_penalty=1.0, 
                    early_stopping=True
                )
output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(output)
```
#### Output

``` bash

Ở trường, chúng tôi dành nhiều thời gian để nghiên cứu về lịch sử Kim Il-Sung, nhưng chúng tôi chưa bao giờ học được nhiều về thế giới bên ngoài, ngoại trừ Mỹ, Hàn Quốc, Nhật Bản là kẻ thù.

```
### Contact information
For personal communication related to this project, please contact Nha Nguyen Van (nha282@gmail.com).
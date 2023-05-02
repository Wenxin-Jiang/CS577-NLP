---
language: it
datasets: 
- tapaco
- stsb_multi_mt
license: cc-by-nc-sa-4.0
tags:
- mt5
- paraphrase-generation
- paraphrasing

---

# MT5-base fine-tuned on Tapaco and STS Benchmark datasets for Paraphrasing

MT5-base Italian paraphraser fine-tuned on [TaPaCo](https://huggingface.co/datasets/tapaco) and [STS Benchmark](https://huggingface.co/datasets/stsb_multi_mt) datasets

## Details of MT5

The **MT5** model was presented in [mT5: A massively multilingual pre-trained text-to-text transformer](https://arxiv.org/abs/2010.11934) by *Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant, Aditya Barua, Colin Raffel* in 2020. Here the abstract:

The recent "Text-to-Text Transfer Transformer" (T5) leveraged a unified text-to-text format and scale to attain state-of-the-art results on a wide variety of English-language NLP tasks. In this paper, we introduce mT5, a multilingual variant of T5 that was pre-trained on a new Common Crawl-based dataset covering 101 languages. We detail the design and modified training of mT5 and demonstrate its state-of-the-art performance on many multilingual benchmarks. We also describe a simple technique to prevent "accidental translation" in the zero-shot setting, where a generative model chooses to (partially) translate its prediction into the wrong language. All of the code and model checkpoints used in this work are publicly available.

## Model fine-tuning

The training script is a slightly modified version of this [Colab notebook](https://colab.research.google.com/drive/1DGeF190gJ3DjRFQiwhFuZalp427iqJNQ) after having prepared an adapted italian version of mt5 model by following this other [Colab notebook](https://gist.github.com/avidale/44cd35bfcdaf8bedf51d97c468cc8001)

## Model in Action

```python
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

raw_model = 'aiknowyou/mt5-base-it-paraphraser'

# Model and Tokenizer definition #
model = T5ForConditionalGeneration.from_pretrained(raw_model)
tokenizer = T5Tokenizer.from_pretrained(raw_model)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
max_size = 10000

def paraphrase(text, beams=100, grams=10, num_return_sequences=5):
    x = tokenizer(text, return_tensors='pt', padding=True).to(model.device)
    max_size = int(x.input_ids.shape[1] * 1.5 + 10)
    out = model.generate(**x, encoder_no_repeat_ngram_size=grams, num_beams=beams, num_return_sequences=num_return_sequences, max_length=max_size)
    return tokenizer.batch_decode(out, skip_special_tokens=True)
  
sentence = "Due amici si incontrano al bar per discutere del modo migliore di generare parafrasi."
print(paraphrase(sentence))

```

## Output
```
Original Question ::
"Due amici si incontrano al bar per discutere del modo migliore di generare parafrasi."

Paraphrased Questions :: 
'Due amici stanno discutendo del modo migliore per generare parafrasi.', 
'Due amici si incontrano a un bar per discutere del modo migliore per generare parafrasi.', 
'Due amici si incontrano al bar per parlare del modo migliore per generare parafrasi.', 
'Due amici sono seduti al bar per discutere del modo migliore per generare parafrasi.', 
'Due amici si incontrano in un bar per discutere del modo migliore per generare parafrasi.'
```

## Contribution

Thanks to [@tradicio](https://huggingface.co/tradicio) for adding this model.

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png

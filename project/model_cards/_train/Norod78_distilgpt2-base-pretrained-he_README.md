---
language: he

thumbnail: https://avatars1.githubusercontent.com/u/3617152?norod.jpg
widget:
- text: "האיש האחרון עלי אדמות ישב לבד בחדרו כשלפתע נשמעה נקישה"
- text: "שלום, קרואים לי"
- text: "הארי פוטר חייך חיוך נבוך"
- text: "החתול שלך מאוד חמוד ו"

license: mit
---

# distilgpt2-base-pretrained-he

A tiny GPT2 based Hebrew text generation model initially trained on a TPUv3-8 which was made avilable to me via the [TPU Research Cloud](https://sites.research.google/trc/) Program. Then was further fine-tuned on GPU.

## Dataset

### oscar (unshuffled deduplicated he) - [Homepage](https://oscar-corpus.com) | [Dataset Permalink](https://huggingface.co/datasets/viewer/?dataset=oscar&config=unshuffled_deduplicated_he)

The Open Super-large Crawled ALMAnaCH coRpus is a huge multilingual corpus obtained by language classification and filtering of the Common Crawl corpus using the goclassy architecture.

### CC-100 (he) - [HomePage](https://data.statmt.org/cc-100/)

This corpus comprises of monolingual data for 100+ languages and also includes data for romanized languages. This was constructed using the urls and paragraph indices provided by the CC-Net repository by processing January-December 2018 Commoncrawl snapshots. Each file comprises of documents separated by double-newlines and paragraphs within the same document separated by a newline. The data is generated using the open source CC-Net repository.

### Misc
* Hebrew Twitter
* Wikipedia
* Various other sources

## Training

* Done on a TPUv3-8 VM using [Huggingface's clm-flax example script](https://github.com/huggingface/transformers/blob/master/examples/flax/language-modeling/run_clm_flax.py) <BR>
* I have made a list of items which might make it easier for other to use this script. The list was posted to [This discussion forum](https://discuss.huggingface.co/t/ideas-for-beginner-friendlier-tpu-vm-clm-training/8351)
* Further training was performed on GPU

## Usage


#### Simple usage sample code

```python

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def main():
    model_name="Norod78/distilgpt2-base-pretrained-he"

    prompt_text = "שלום, קוראים לי"
    generated_max_length = 192

    print("Loading model...")
    model =  AutoModelForCausalLM.from_pretrained(model_name)
    print('Loading Tokenizer...')
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    text_generator = pipeline(task="text-generation", model=model, tokenizer=tokenizer)

    print("Generating text...")
    result = text_generator(prompt_text, num_return_sequences=1, batch_size=1, do_sample=True, top_k=40, top_p=0.92, temperature = 1, repetition_penalty=5.0, max_length = generated_max_length)

    print("result = " + str(result))

if __name__ == '__main__':
    main()
```

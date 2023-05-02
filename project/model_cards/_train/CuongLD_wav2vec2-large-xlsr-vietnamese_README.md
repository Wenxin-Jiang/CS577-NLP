---
language: vi 
datasets:
- common_voice, infore_25h
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: Cuong-Cong XLSR Wav2Vec2 Large 53
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice vi 
      type: common_voice
      args: vi 
    metrics:
       - name: Test WER
         type: wer
         value: 58.63 
---

# Wav2Vec2-Large-XLSR-53-Vietnamese 

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on Vietnamese using the [Common Voice](https://huggingface.co/datasets/common_voice), [Infore_25h dataset](https://files.huylenguyen.com/25hours.zip) (Password: BroughtToYouByInfoRe)
  
When using this model, make sure that your speech input is sampled at 16kHz.

## Usage

The model can be used directly (without a language model) as follows:

```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

test_dataset = load_dataset("common_voice", "vi", split="test[:2%]") 
processor = Wav2Vec2Processor.from_pretrained("CuongLD/wav2vec2-large-xlsr-vietnamese") 
model = Wav2Vec2ForCTC.from_pretrained("CuongLD/wav2vec2-large-xlsr-vietnamese")

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
  speech_array, sampling_rate = torchaudio.load(batch["path"])
	batch["speech"] = resampler(speech_array).squeeze().numpy()
	return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)
inputs = processor(test_dataset["speech"][:2], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():
	logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)

print("Prediction:", processor.batch_decode(predicted_ids))
print("Reference:", test_dataset["sentence"][:2])
```


## Evaluation

The model can be evaluated as follows on the Vietnamese test data of Common Voice.  

```python
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re

test_dataset = load_dataset("common_voice", "vi", split="test")
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("CuongLD/wav2vec2-large-xlsr-vietnamese") 
model = Wav2Vec2ForCTC.from_pretrained("CuongLD/wav2vec2-large-xlsr-vietnamese") 
model.to("cuda")

chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“]' 
resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
	batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()
	speech_array, sampling_rate = torchaudio.load(batch["path"])
	batch["speech"] = resampler(speech_array).squeeze().numpy()
	return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def evaluate(batch):
	inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

	with torch.no_grad():
		logits = model(inputs.input_values.to("cuda"), attention_mask=inputs.attention_mask.to("cuda")).logits

	pred_ids = torch.argmax(logits, dim=-1)
	batch["pred_strings"] = processor.batch_decode(pred_ids)
	return batch

result = test_dataset.map(evaluate, batched=True, batch_size=8)

print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))
```

**Test Result**: 58.63 % 

## Training

The Common Voice `train`, `validation`, and `Infore_25h` datasets were used for training 

The script used for training can be found [here](https://drive.google.com/file/d/1AW9R8IlsapiSGh9n3aECf23t-zhk3wUh/view?usp=sharing) 

=======================To here===============================>

Your model in then available under *huggingface.co/CuongLD/wav2vec2-large-xlsr-vietnamese* for everybody to use 🎉.

## How to evaluate my trained checkpoint

Having uploaded your model, you should now evaluate your model in a final step. This should be as simple as 
copying the evaluation code of your model card into a python script and running it. Make sure to note 
the final result on the model card **both** under the YAML tags at the very top **and** below your evaluation code under "Test Results".

## Rules of training and evaluation

In this section, we will quickly go over what data is allowed to be used as training 
data, what kind of data preprocessing is allowed be used, and how the model should be evaluated.

To make it very simple regarding the first point: **All data except the official common voice `test` data set can be used as training data**. For models trained in a language that is not included in Common Voice, the author of the model is responsible to 
leave a reasonable amount of data for evaluation.

Second, the rules regarding the preprocessing are not that as straight-forward. It is allowed (and recommended) to 
normalize the data to only have lower-case characters. It is also allowed (and recommended) to remove typographical 
symbols and punctuation marks. A list of such symbols can *e.g.* be fonud [here](https://en.wikipedia.org/wiki/List_of_typographical_symbols_and_punctuation_marks) - however here we already must be careful. We should **not** remove a symbol that 
would change the meaning of the words, *e.g.* in English, we should not remove the single quotation mark `'` since it 
would change the meaning of the word `"it's"` to `"its"` which would then be incorrect. So the golden rule here is to 
not remove any characters that could change the meaning of a word into another word. This is not always obvious and should 
be given some consideration. As another example, it is fine to remove the "Hypen-minus" sign "`-`" since it doesn't change the 
meaninng of a word to another one. *E.g.* "`fine-tuning`" would be changed to "`finetuning`" which has still the same meaning.

Since those choices are not always obvious when in doubt feel free to ask on Slack or even better post on the forum, as was 
done, *e.g.* [here](https://discuss.huggingface.co/t/spanish-asr-fine-tuning-wav2vec2/4586).

## Tips and tricks

This section summarizes a couple of tips and tricks across various topics. It will continously be updated during the week.

### How to combine multiple datasets into one

Check out [this](https://discuss.huggingface.co/t/how-to-combine-local-data-files-with-an-official-dataset/4685) post.

### How to effectively preprocess the data


### How to do efficiently load datasets with limited ram and hard drive space

Check out [this](https://discuss.huggingface.co/t/german-asr-fine-tuning-wav2vec2/4558/8?u=patrickvonplaten) post.


### How to do hyperparameter tuning


### How to preprocess and evaluate character based languages


## Further reading material

It is recommended that take some time to read up on how Wav2vec2 works in theory. 
Getting a better understanding of the theory and the inner mechanisms of the model often helps when fine-tuning the model. 

**However**, if you don't like reading blog posts/papers, don't worry - it is by no means necessary to go through the theory to fine-tune Wav2Vec2 on your language of choice.

If you are interested in learning more about the model though, here are a couple of resources that are important to better understand Wav2Vec2:

- [Facebook's Wav2Vec2 blog post](https://ai.facebook.com/blog/wav2vec-state-of-the-art-speech-recognition-through-self-supervision/)
- [Official Wav2Vec2 paper](https://arxiv.org/abs/2006.11477)
- [Official XLSR Wav2vec2 paper](https://arxiv.org/pdf/2006.13979.pdf)
- [Hugging Face Blog](https://huggingface.co/blog/fine-tune-xlsr-wav2vec2)
- [How does CTC (Connectionist Temporal Classification) work](https://distill.pub/2017/ctc/)

It helps to have a good understanding of the following points:

- How was XLSR-Wav2Vec2 pretrained? -> Feature vectors were masked and had to be predicted by the model; very similar in spirit to masked language model of BERT.

- What parts of XLSR-Wav2Vec2 are responsible for what? What is the feature extractor part used for? -> extract feature vectors from the 1D raw audio waveform; What is the transformer part doing? -> mapping feature vectors to contextualized feature vectors; ...

- What part of the model needs to be fine-tuned? -> The pretrained model **does not** include a language head to classify the contextualized features to letters. This is randomly initialized when loading the pretrained checkpoint and has to be fine-tuned. Also, note that the authors recommend to **not** further fine-tune the feature extractor.

- What data was used to XLSR-Wav2Vec2? The checkpoint we will use for further fine-tuning was pretrained on **53** languages. 

- What languages are considered to be similar by XLSR-Wav2Vec2? In the official [XLSR Wav2Vec2 paper](https://arxiv.org/pdf/2006.13979.pdf), the authors show nicely which languages share a common contextualized latent space. It might be useful for you to extend your training data with data of other languages that are considered to be very similar by the model (or you).


## FAQ

- Can a participant fine-tune models for more than one language? 
Yes! A participant can fine-tune models in as many languages she/he likes
- Can a participant use extra data (apart from the common voice data)?
Yes! All data except the official common voice `test data` can be used for training.
If a participant wants to train a model on a language that is not part of Common Voice (which 
is very much encouraged!), the participant should make sure that some test data is held out to 
make sure the model is not overfitting.
- Can we fine-tune for high-resource languages? 
Yes! While we do not really recommend people to fine-tune models in English since there are
already so many fine-tuned speech recognition models in English. However, it is very much 
appreciated if participants want to fine-tune models in other "high-resource" languages, such 
as French, Spanish, or German. For such cases, one probably needs to train locally and apply 
might have to apply tricks such as lazy data loading (check the ["Lazy data loading"](#how-to-do-lazy-data-loading) section for more details).

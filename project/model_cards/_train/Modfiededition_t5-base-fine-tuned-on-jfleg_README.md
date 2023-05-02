## t5-base-fine-tuned-on-jfleg
T5-base model fine-tuned on the [**JFLEG dataset**](https://huggingface.co/datasets/jfleg) with the objective of **text2text-generation**.

# Model Description:
T5 is an encoder-decoder model pre-trained with a multi-task mixture of unsupervised and supervised tasks and for which each task is converted into a text-to-text format.
.T5 works well on a variety of tasks out-of-the-box by prepending a different prefix to the input corresponding to each task, e.g., for translation: translate English to German: …, for summarization: summarize: ….

The T5 model was presented in [**Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer**](https://arxiv.org/pdf/1910.10683.pdf) by Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu.

## Pre-Processing:
For this task of grammar correction, we’ll use the prefix “grammar: “ to each of the input sentences.
```
Grammar: Your Sentence

```

## How to use :
You can use this model directly with the pipeline for detecting and correcting grammatical mistakes.

```
from transformers import pipeline

model_checkpoint = "Modfiededition/t5-base-fine-tuned-on-jfleg"
model = pipeline("text2text-generation", model=model_checkpoint)
text = "I am write on AI"
output = model(text)
```
Result(s)
```
I am writing on AI.
```





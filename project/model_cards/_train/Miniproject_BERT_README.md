---
language:
- en
---

# Bert-base-uncased-sentiment


BERT stands for Bidirectional Encoder Representations from Transformers. It is a recent paper published by researchers at Google AI Language. BERT makes use of Transformer, an attention mechanism that learns contextual relations between words (or sub-words) in a text. In its vanilla form, Transformer includes two separate mechanisms — an encoder that reads the text input and a decoder that produces a prediction for the task. Since BERT’s goal is to generate a language model, only the encoder mechanism is necessary.

Bidirectional - to understand the text you’re looking you’ll have to look back (at the previous words) and forward (at the next words)
Transformers - The "Attention Is All You Need" paper presented the Transformer model. The Transformer reads entire sequences of tokens at once. In a sense, the model is non-directional, while LSTMs read sequentially (left-to-right or right-to-left). The attention mechanism allows for learning contextual relations between words.
(Pre-trained) contextualized word embeddings - The ELMO paper introduced a way to encode words based on their meaning/context. Nails has multiple meanings - fingernails and metal nails. BERT was trained by masking 15% of the tokens with the goal to guess them. An additional objective was to predict the next sentence. Let’s look at examples of these tasks:
Masked Language Modeling (Masked LM)
The objective of this task is to guess the masked tokens.

Before feeding word sequences into BERT, 15% of the words in each sentence are replaced with a masked. This means that it is converted to a token which is called "masked token". Then the job of BERT is to predict that hidden or masked word in the sentence by looking at the words (non-masked words) around that masked word. The model then attempts to predict the original value of the masked words, based on the context provided by the other, non-masked, words in the sequence.

That’s [mask] she [mask] -> That’s what she said

Next Sentence Prediction (NSP)
In this training process, BERT receives pairs of sentences as input and learns to predict if the second sentence in the pair of the first sentence (which means that the second sentence occurs just after the first sentence in our training corpus).

During training, 50% of the inputs are pairs in which the second sentence is the the pair of first sentence, while in the other 50%, it is just a random sentence from the corpus which is chosen as a second sentence. That means the other 50% doesn't forms a pair.

BERT Training Dataset
The training corpus was comprised of two entries: Toronto Book Corpus (800M words) and English Wikipedia (2,500M words). While the original Transformer has an encoder (for reading the input) and a decoder (that makes the prediction), BERT uses only the decoder.

BERT is simply a pre-trained stack of Transformer Encoders. How many Encoders? We have two versions - with 12 (BERT base) and 24 (BERT Large).BERT is based on stacked layers of encoders. The difference between BERT base and BERT large is on the number of encoder layers. BERT base model has 12 encoder layers stacked on top of each other whereas BERT large has 24 layers of encoders stacked on top of each other. BERT performs better than the other models. And BERT large increases the performance of BERT base further.

The BERT paper was released along with the source code and pre-trained models.

The best part is that you can do Transfer Learning (thanks to the ideas from OpenAI Transformer) with BERT for many NLP tasks - Classification, Question Answering, Entity Recognition, etc. You can train with small amounts of data and achieve great performance!



This a bert-base-uncased model finetuned for sentiment analysis on product reviews in the English language. It predicts the sentiment of the review as a number of stars (between 1 and 5).

This model is intended for direct use as a sentiment analysis model for product reviews, or for further finetuning on related sentiment analysis tasks.

## Training data

Here is the number of product reviews we used for finetuning the model: 

| Language | Number of reviews |
| -------- | ----------------- |
| English  | 150k           |


## Accuracy

The finetuned model obtained the following accuracy on 5,000 held-out product reviews in each of the languages:

- Accuracy (exact) is the exact match on the number of stars.
- Accuracy (off-by-1) is the percentage of reviews where the number of stars the model predicts differs by a maximum of 1 from the number given by the human reviewer. 


| Language | Accuracy (exact) | Accuracy (off-by-1) |
| -------- | ---------------------- | ------------------- |
| English  | 67%                 | 95%




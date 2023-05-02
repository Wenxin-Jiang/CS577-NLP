---
license: apache-2.0
datasets:
- ML-Projects-Kiel/tweetyface
language:
- en
tags:
- gpt2

inference:
  parameters:
    num_return_sequences: 2
    
widget:
- text: "User: BarackObama\nTweet: Twitter is "
  example_title: "Barack Obama about Twitter"
- text: "User: neiltyson\nTweet: Twitter is"
  example_title: "Neil deGrasse Tyson about Twitter"
- text: "User: elonmusk\nTweet: Twitter is"
  example_title: "Elon Musk about Twitter"

- text: "User: elonmusk\nTweet: My Opinion about space"
  example_title: "Elon Musk deGrasse Tyson about Space"
- text: "User: BarackObama\nTweet: My Opinion about space"
  example_title: "Barack Obama about Space"
- text: "User: neiltyson\nTweet: My Opinion about space"
  example_title: "Neil deGrasse Tyson about Space"
---


# Tweety Face


Finetuned language model based on [GPT-2](https://huggingface.co/gpt2) to generate Tweets in a users style.


## Model description

Tweety Face is a transformer model finetuned using GTP-2 and Tweets from various Twitter users. It was created to 
generate a Twitter Tweet for a given user similar to their specific writing style. It accepts a prompt for a user
and completes the text.

This finetuned model uses the **smallest** version of GPT-2, with 124M parameters. 

## Intended uses & limitations

This model was created to experiment with prompt inputs and is not intended to create real Tweets. The generated text
is not a real representation of the given users opinion, political affiliation, behaviour, etc. Do not use this model
to impersonate a user.

### How to use

You can use this model directly with a pipeline for text generation. Since the generation relies on some randomness, we
set a seed for reproducibility:

```python
>>> from transformers import pipeline, set_seed
>>> generator = pipeline('text-generation', model='ML-Projects-Kiel/tweetyface')
>>> set_seed(42)
>>> generator("User: elonmusk\nTweet: Twitter is", max_length=30, num_return_sequences=5)

[{'generated_text': 'User: elonmusk\nTweet: Twitter is more active than ever. Even though you can’t see your entire phone list, your'},
 {'generated_text': 'User: elonmusk\nTweet: Twitter is just in a few hours until an announcement which has been approved by President. This should be a'},
 {'generated_text': 'User: elonmusk\nTweet: Twitter is currently down to a minimum of 13 tweets per day, a decline that was significantly worse than Twitter'},
 {'generated_text': 'User: elonmusk\nTweet: Twitter is a great investment to us. Will go above his legal fees to join Twitter in many countries,'},
 {'generated_text': 'User: elonmusk\nTweet: Twitter is not doing something like this – they are not using Twitter to give out their content – other than'}]
```


## Training data

The training data used for this model has been released as a dataset one can browse [here](https://huggingface.co/ML-Projects-Kiel/tweetyface).
The raw data can be found in our [Github Repository](https://github.com/ml-projects-kiel/OpenCampus-ApplicationofTransformers). The raw data
can be found in two versions. All data on the develop branch is used in a [debugging dataset](https://huggingface.co/datasets/ML-Projects-Kiel/tweetyface_debug). 
All data in the qa branch is used in the final dataset.


## Training procedure

### Preprocessing

For training first all retweets (RT) have been removed. Next the newline characters "\n" have been replaced by white
spaces and all URLs haven been replaced with the word URL. 

The texts are tokenized using a byte-level version of Byte Pair Encoding (BPE) (for unicode characters).

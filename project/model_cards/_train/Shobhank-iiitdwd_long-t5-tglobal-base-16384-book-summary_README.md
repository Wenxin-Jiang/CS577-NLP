---
tags:
- summarization
- summary
- booksum
- long-document
- long-form
license:
- apache-2.0
- bsd-3-clause
datasets:
- booksum
metrics:
- rouge
widget:
- text: large earthquakes along a given fault segment do not occur at random intervals
    because it takes time to accumulate the strain energy for the rupture. The rates
    at which tectonic plates move and accumulate strain at their boundaries are approximately
    uniform. Therefore, in first approximation, one may expect that large ruptures
    of the same fault segment will occur at approximately constant time intervals.
    If subsequent main shocks have different amounts of slip across the fault, then
    the recurrence time may vary, and the basic idea of periodic mainshocks must be
    modified. For great plate boundary ruptures the length and slip often vary by
    a factor of 2. Along the southern segment of the San Andreas fault the recurrence
    interval is 145 years with variations of several decades. The smaller the standard
    deviation of the average recurrence interval, the more specific could be the long
    term prediction of a future mainshock.
  example_title: earthquakes
- text: " A typical feed-forward neural field algorithm. Spatiotemporal coordinates\
    \ are fed into a neural network that predicts values in the reconstructed domain.\
    \ Then, this domain is mapped to the sensor domain where sensor measurements are\
    \ available as supervision. Class and Section Problems Addressed Generalization\
    \ (Section 2) Inverse problems, ill-posed problems, editability; symmetries. Hybrid\
    \ Representations (Section 3) Computation & memory efficiency, representation\
    \ capacity, editability: Forward Maps (Section 4) Inverse problems Network Architecture\
    \ (Section 5) Spectral bias, integration & derivatives. Manipulating Neural Fields\
    \ (Section 6) Edit ability, constraints, regularization. Table 2: The five classes\
    \ of techniques in the neural field toolbox each addresses problems that arise\
    \ in learning, inference, and control. (Section 3). We can supervise reconstruction\
    \ via differentiable forward maps that transform Or project our domain (e.g, 3D\
    \ reconstruction via 2D images; Section 4) With appropriate network architecture\
    \ choices, we can overcome neural network spectral biases (blurriness) and efficiently\
    \ compute derivatives and integrals (Section 5). Finally, we can manipulate neural\
    \ fields to add constraints and regularizations, and to achieve editable representations\
    \ (Section 6). Collectively, these classes constitute a 'toolbox' of techniques\
    \ to help solve problems with neural fields There are three components in a conditional\
    \ neural field: (1) An encoder or inference function \u20AC that outputs the conditioning\
    \ latent variable 2 given an observation 0 E(0) =2. 2 is typically a low-dimensional\
    \ vector, and is often referred to aS a latent code Or feature code_ (2) A mapping\
    \ function 4 between Z and neural field parameters O: Y(z) = O; (3) The neural\
    \ field itself $. The encoder \u20AC finds the most probable z given the observations\
    \ O: argmaxz P(2/0). The decoder maximizes the inverse conditional probability\
    \ to find the most probable 0 given Z: arg- max P(Olz). We discuss different encoding\
    \ schemes with different optimality guarantees (Section 2.1.1), both global and\
    \ local conditioning (Section 2.1.2), and different mapping functions Y (Section\
    \ 2.1.3) 2. Generalization Suppose we wish to estimate a plausible 3D surface\
    \ shape given a partial or noisy point cloud. We need a suitable prior over the\
    \ sur- face in its reconstruction domain to generalize to the partial observations.\
    \ A neural network expresses a prior via the function space of its architecture\
    \ and parameters 0, and generalization is influenced by the inductive bias of\
    \ this function space (Section 5)."
  example_title: scientific paper
- text: 'Is a else or outside the cob and tree written being of early client rope
    and you have is for good reasons. On to the ocean in Orange for time. By''s the
    aggregate we can bed it yet. Why this please pick up on a sort is do and also
    M Getoi''s nerocos and do rain become you to let so is his brother is made in
    use and Mjulia''s''s the lay major is aging Masastup coin present sea only of
    Oosii rooms set to you We do er do we easy this private oliiishs lonthen might
    be okay. Good afternoon everybody. Welcome to this lecture of Computational Statistics.
    As you can see, I''m not socially my name is Michael Zelinger. I''m one of the
    task for this class and you might have already seen me in the first lecture where
    I made a quick appearance. I''m also going to give the tortillas in the last third
    of this course. So to give you a little bit about me, I''m a old student here
    with better Bulman and my research centres on casual inference applied to biomedical
    disasters, so that could be genomics or that could be hospital data. If any of
    you is interested in writing a bachelor thesis, a semester paper may be mastathesis
    about this topic feel for reach out to me. you have my name on models and my email
    address you can find in the directory I''d Be very happy to talk about it. you
    do not need to be sure about it, we can just have a chat. So with that said, let''s
    get on with the lecture. There''s an exciting topic today I''m going to start
    by sharing some slides with you and later on during the lecture we''ll move to
    the paper. So bear with me for a few seconds. Well, the projector is starting
    up. Okay, so let''s get started. Today''s topic is a very important one. It''s
    about a technique which really forms one of the fundamentals of data science,
    machine learning, and any sort of modern statistics. It''s called cross validation.
    I know you really want to understand this topic I Want you to understand this
    and frankly, nobody''s gonna leave Professor Mineshousen''s class without understanding
    cross validation. So to set the stage for this, I Want to introduce you to the
    validation problem in computational statistics. So the problem is the following:
    You trained a model on available data. You fitted your model, but you know the
    training data you got could always have been different and some data from the
    environment. Maybe it''s a random process. You do not really know what it is,
    but you know that somebody else who gets a different batch of data from the same
    environment they would get slightly different training data and you do not care
    that your method performs as well. On this training data. you want to to perform
    well on other data that you have not seen other data from the same environment.
    So in other words, the validation problem is you want to quantify the performance
    of your model on data that you have not seen. So how is this even possible? How
    could you possibly measure the performance on data that you do not know The solution
    to? This is the following realization is that given that you have a bunch of data,
    you were in charge. You get to control how much that your model sees. It works
    in the following way: You can hide data firms model. Let''s say you have a training
    data set which is a bunch of doubtless so X eyes are the features those are typically
    hide and national vector. It''s got more than one dimension for sure. And the
    why why eyes. Those are the labels for supervised learning. As you''ve seen before,
    it''s the same set up as we have in regression. And so you have this training
    data and now you choose that you only use some of those data to fit your model.
    You''re not going to use everything, you only use some of it the other part you
    hide from your model. And then you can use this hidden data to do validation from
    the point of you of your model. This hidden data is complete by unseen. In other
    words, we solve our problem of validation.'
  example_title: transcribed audio - lecture
- text: "Transformer-based models have shown to be very useful for many NLP tasks.\
    \ However, a major limitation of transformers-based models is its O(n^2)O(n 2)\
    \ time & memory complexity (where nn is sequence length). Hence, it's computationally\
    \ very expensive to apply transformer-based models on long sequences n > 512n>512.\
    \ Several recent papers, e.g. Longformer, Performer, Reformer, Clustered attention\
    \ try to remedy this problem by approximating the full attention matrix. You can\
    \ checkout \U0001F917's recent blog post in case you are unfamiliar with these\
    \ models.\nBigBird (introduced in paper) is one of such recent models to address\
    \ this issue. BigBird relies on block sparse attention instead of normal attention\
    \ (i.e. BERT's attention) and can handle sequences up to a length of 4096 at a\
    \ much lower computational cost compared to BERT. It has achieved SOTA on various\
    \ tasks involving very long sequences such as long documents summarization, question-answering\
    \ with long contexts.\nBigBird RoBERTa-like model is now available in \U0001F917\
    Transformers. The goal of this post is to give the reader an in-depth understanding\
    \ of big bird implementation & ease one's life in using BigBird with \U0001F917\
    Transformers. But, before going into more depth, it is important to remember that\
    \ the BigBird's attention is an approximation of BERT's full attention and therefore\
    \ does not strive to be better than BERT's full attention, but rather to be more\
    \ efficient. It simply allows to apply transformer-based models to much longer\
    \ sequences since BERT's quadratic memory requirement quickly becomes unbearable.\
    \ Simply put, if we would have \u221E compute & \u221E time, BERT's attention\
    \ would be preferred over block sparse attention (which we are going to discuss\
    \ in this post).\nIf you wonder why we need more compute when working with longer\
    \ sequences, this blog post is just right for you!\nSome of the main questions\
    \ one might have when working with standard BERT-like attention include:\nDo all\
    \ tokens really have to attend to all other tokens? Why not compute attention\
    \ only over important tokens? How to decide what tokens are important? How to\
    \ attend to just a few tokens in a very efficient way? In this blog post, we will\
    \ try to answer those questions.\nWhat tokens should be attended to? We will give\
    \ a practical example of how attention works by considering the sentence 'BigBird\
    \ is now available in HuggingFace for extractive question answering'. In BERT-like\
    \ attention, every word would simply attend to all other tokens.\nLet's think\
    \ about a sensible choice of key tokens that a queried token actually only should\
    \ attend to by writing some pseudo-code. Will will assume that the token available\
    \ is queried and build a sensible list of key tokens to attend to.\n>>> # let's\
    \ consider following sentence as an example >>> example = ['BigBird', 'is', 'now',\
    \ 'available', 'in', 'HuggingFace', 'for', 'extractive', 'question', 'answering']\n\
    >>> # further let's assume, we're trying to understand the representation of 'available'\
    \ i.e. >>> query_token = 'available' >>> # We will initialize an empty `set` and\
    \ fill up the tokens of our interest as we proceed in this section. >>> key_tokens\
    \ = [] # => currently 'available' token doesn't have anything to attend Nearby\
    \ tokens should be important because, in a sentence (sequence of words), the current\
    \ word is highly dependent on neighboring past & future tokens. This intuition\
    \ is the idea behind the concept of sliding attention."
  example_title: bigbird blog intro
- text: "To be fair, you have to have a very high IQ to understand Rick and Morty.\
    \ The humour is extremely subtle, and without a solid grasp of theoretical physics\
    \ most of the jokes will go over a typical viewer's head. There's also Rick's\
    \ nihilistic outlook, which is deftly woven into his characterisation- his personal\
    \ philosophy draws heavily from Narodnaya Volya literature, for instance. The\
    \ fans understand this stuff; they have the intellectual capacity to truly appreciate\
    \ the depths of these jokes, to realise that they're not just funny- they say\
    \ something deep about LIFE. As a consequence people who dislike Rick & Morty\
    \ truly ARE idiots- of course they wouldn't appreciate, for instance, the humour\
    \ in Rick's existential catchphrase 'Wubba Lubba Dub Dub,' which itself is a cryptic\
    \ reference to Turgenev's Russian epic Fathers and Sons. I'm smirking right now\
    \ just imagining one of those addlepated simpletons scratching their heads in\
    \ confusion as Dan Harmon's genius wit unfolds itself on their television screens.\
    \ What fools.. how I pity them. \U0001F602\nAnd yes, by the way, i DO have a Rick\
    \ & Morty tattoo. And no, you cannot see it. It's for the ladies' eyes only- and\
    \ even then they have to demonstrate that they're within 5 IQ points of my own\
    \ (preferably lower) beforehand. Nothin personnel kid \U0001F60E"
  example_title: Richard & Mortimer
- text: "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
  example_title: eiffel
parameters:
  max_length: 64
  min_length: 8
  no_repeat_ngram_size: 3
  early_stopping: true
  repetition_penalty: 3.5
  length_penalty: 0.3
  encoder_no_repeat_ngram_size: 3
  num_beams: 4
model-index:
- name: pszemraj/long-t5-tglobal-base-16384-book-summary
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: kmfoda/booksum
      type: kmfoda/booksum
      config: kmfoda--booksum
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 36.4085
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 6.0646
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 16.7209
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 33.3405
      verified: true
    - name: loss
      type: loss
      value: .nan
      verified: true
    - name: gen_len
      type: gen_len
      value: 252.8099
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: samsum
      type: samsum
      config: samsum
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 30.9047
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 7.4715
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 22.3962
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 26.9094
      verified: true
    - name: loss
      type: loss
      value: .nan
      verified: true
    - name: gen_len
      type: gen_len
      value: 46.7973
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      config: 3.0.0
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 30.5942
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 7.252
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 17.7156
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 27.2881
      verified: true
    - name: loss
      type: loss
      value: .nan
      verified: true
    - name: gen_len
      type: gen_len
      value: 125.2507
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: xsum
      type: xsum
      config: default
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 20.3648
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 3.4126
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 13.6168
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 15.8313
      verified: true
    - name: loss
      type: loss
      value: .nan
      verified: true
    - name: gen_len
      type: gen_len
      value: 82.2177
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: billsum
      type: billsum
      config: default
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 39.6378
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 13.0017
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 23.0255
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 32.9943
      verified: true
    - name: loss
      type: loss
      value: 1.9428048133850098
      verified: true
    - name: gen_len
      type: gen_len
      value: 162.3588
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: big_patent
      type: big_patent
      config: y
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 34.7641
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 7.8744
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 19.9826
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 29.208
      verified: true
    - name: loss
      type: loss
      value: 2.8316469192504883
      verified: true
    - name: gen_len
      type: gen_len
      value: 132.7475
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: launch/gov_report
      type: launch/gov_report
      config: plain_text
      split: validation
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 37.9246
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 8.5837
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 18.0274
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 34.0816
      verified: true
    - name: loss
      type: loss
      value: 2.56695818901062
      verified: true
    - name: gen_len
      type: gen_len
      value: 220.3747
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: launch/gov_report
      type: launch/gov_report
      config: plain_text
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 37.4438
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 8.2907
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 17.6893
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 33.7141
      verified: true
    - name: loss
      type: loss
      value: 2.5776000022888184
      verified: true
    - name: gen_len
      type: gen_len
      value: 214.9692
      verified: true
---




- generalizes reasonably well to academic & narrative text.


**Contents**

<!-- TOC -->

- [Model description](#model-description)
- [How-To in Python](#how-to-in-python)
- [Intended uses & limitations](#intended-uses--limitations)
- [Training and evaluation data](#training-and-evaluation-data)
- [Inference over long documents in batches](#how-to-run-inference-over-a-very-long-30k-tokens-document-in-batches)
  [How to fine-tune further](#how-to-fine-tune-further)
- [Training procedure](#training-procedure)
- [Training hyperparameters](#training-hyperparameters)
- [Framework versions](#framework-versions)
  

<!-- /TOC -->

* * *

## Model description

A fine-tuned version of [google/long-t5-tglobal-base](https://huggingface.co/google/long-t5-tglobal-base) on the `booksum` dataset:

- 30+ epochs of fine-tuning from the base model on V100/A100 GPUs
- Training used 16384 token input / 1024 max output

Read the paper by Guo et al. here: [LongT5: Efficient Text-To-Text Transformer for Long Sequences](https://arxiv.org/pdf/2112.07916.pdf)

## How-To in Python

Install/update transformers `pip install -U transformers`

Summarize text with pipeline:

```python
import torch
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    "pszemraj/long-t5-tglobal-base-16384-book-summary",
    device=0 if torch.cuda.is_available() else -1,
)
long_text = "Here is a lot of text I don't want to read. Replace me"

result = summarizer(long_text)
print(result[0]["summary_text"])
```

Pass [other parameters related to beam search textgen](https://huggingface.co/blog/how-to-generate) when calling `summarizer` to get even higher quality results.

## Intended uses & limitations

- The current checkpoint is fairly well converged but will be updated if further improvements can be made.
    - Compare performance to [LED-base](https://huggingface.co/pszemraj/led-base-book-summary) trained on the same dataset (API gen parameters are the same).
- while this model seems to improve upon factual consistency, **do not take summaries to be foolproof and check things that seem odd**.

## Training and evaluation data

`kmfoda/booksum` dataset on HuggingFace - read [the original paper here](https://arxiv.org/abs/2105.08209). Summaries longer than 1024 LongT5 tokens were filtered out to prevent the model from learning to generate "partial" summaries.



### How to run inference over a very long (30k+ tokens) document in batches?

See `summarize.py` in [the code for my hf space Document Summarization](https://huggingface.co/spaces/pszemraj/document-summarization/blob/main/summarize.py) :)

You can also use the same code to split a document into batches of 4096, etc., and run over those with the model. This is useful in situations where CUDA memory is limited.

### How to fine-tune further?

See [train with a script](https://huggingface.co/docs/transformers/run_scripts) and [the summarization scripts](https://github.com/huggingface/transformers/tree/main/examples/pytorch/summarization).

This model was originally tuned on Google Colab with a heavily modified variant of the [longformer training notebook](https://github.com/patrickvonplaten/notebooks/blob/master/Fine_tune_Longformer_Encoder_Decoder_(LED)_for_Summarization_on_pubmed.ipynb), key enabler being deepspeed. You can try this as an alternate route to fine-tuning the model without using the command line.

* * *

## Training procedure


### Training hyperparameters

_NOTE: early checkpoints of this model were trained on a "smaller" subsection of the dataset as it was filtered for summaries of **1024 characters**. This was subsequently caught and adjusted to **1024 tokens** and then trained further for 10+ epochs._

The following hyperparameters were used during the **most recent** training round\*:

- learning_rate: 0.0005
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 128
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 2

\* Prior training sessions used roughly similar parameters; multiple sessions were required as this takes eons to train

### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

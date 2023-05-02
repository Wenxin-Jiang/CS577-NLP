---

tags:
- generated_from_trainer
widget:
 - text: "Coutinho was just about to be introduced by Villa boss Gerrard midway through the second half when Bruno Fernandes slammed home
his second goal of the game off the underside of the bar. But the Brazilian proved the catalyst for a memorable response.
First he drove at the United defence, helping to create the space which Jacob Ramsey exploited to halve the deficit. Then Ramsey slid over an excellent
cross from the left which Raphael Varane was unable to intercept as he slid back, leaving Coutinho to finish into an empty net.
The goal brought celebrations at both ends of the pitch as Emiliano Martinez also went into the crowd in relief - it was the Argentine's horrible sixth-minute error that had gifted Fernandes the visitors' opener.
Given his background - with Liverpool, Barcelona and Bayern Munich - Coutinho is a bold loan signing by Villa, and underlines the pedigree of the man they appointed as manager in November.
Gerrard is not at Villa to learn how to avoid relegation.
His demands remain as high as they were as a player and Coutinho's arrival is an example of that.
Villa are a better team since Gerrard's arrival and, after a sluggish start against opponents they dominated but lost to in the FA Cup five days ago, they grew into the game.
The club's other newboy, Lucas Digne, was among those denied by United keeper David de Gea at the end of the first half - in unorthodox fashion, with his knees.
Ollie Watkins did not really test the Spain keeper when Villa broke after Edinson Cavani lost possession in his own half. However, Emi Buendia certainly did with a near-post header. Rooted to his line, De Gea's reactions were up to the job as he beat Buendia's effort away.
When De Gea produced more saves after half-time to deny Ramsey and Digne again, it appeared the image of the night for Villa would be midfielder Morgan Sanson kicking a drinks bottle in fury after his error in gifting Fred possession to set up Fernandes for the visitors' second had been followed immediately by his substitution.
However, as it was the prelude to Coutinho's arrival, it was the moment that changed the course of the game - and the acclaim for the Brazilian at the final whistle indicated Villa's fans are already firmly behind him."
language: en 

---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-sports-titles

This model is a fine-tuned pegasus on some **sports news articles scraped from the internet. (For educational purposes only)**. The model can generate titles for sports articles. Try it out using the inference API. 

## Model description

A Pegasus model tuned on generating scientific titles has been further fine-tuned to generate titles for sports articles. While training articles on **Tennis, Football (Soccer), Cricket , Athletics and Rugby** were used to generate titles. I experimented training the Tokenizer from scratch but it did not give good results compared to the pre-trained tokenizer. 

## Usage

```python
from transformers import pipeline
#Feel free to play around with the generation parameters.
#Reduce the beam width for faster inference
#Note that the maximum length for the generated titles is 64
gen_kwargs = {"length_penalty": 0.6, "num_beams":4, "num_return_sequences": 4,"num_beam_groups":4,"diversity_penalty":2.0}

pipe = pipeline("summarization", model="RajSang/pegasus-sports-titles")

#Change the article according to your wish
article="""
Coutinho was just about to be introduced by Villa boss Gerrard midway through the second half when Bruno Fernandes slammed home
his second goal of the game off the underside of the bar. But the Brazilian proved the catalyst for a memorable response.
First he drove at the United defence, helping to create the space which Jacob Ramsey exploited to halve the deficit. Then Ramsey slid over an excellent
cross from the left which Raphael Varane was unable to intercept as he slid back, leaving Coutinho to finish into an empty net.
The goal brought celebrations at both ends of the pitch as Emiliano Martinez also went into the crowd in relief - it was the Argentine's horrible sixth-minute error that had gifted Fernandes the visitors' opener.
Given his background - with Liverpool, Barcelona and Bayern Munich - Coutinho is a bold loan signing by Villa, and underlines the pedigree of the man they appointed as manager in November.
Gerrard is not at Villa to learn how to avoid relegation.
His demands remain as high as they were as a player and Coutinho's arrival is an example of that.
Villa are a better team since Gerrard's arrival and, after a sluggish start against opponents they dominated but lost to in the FA Cup five days ago, they grew into the game.
The club's other newboy, Lucas Digne, was among those denied by United keeper David de Gea at the end of the first half - in unorthodox fashion, with his knees.
Ollie Watkins did not really test the Spain keeper when Villa broke after Edinson Cavani lost possession in his own half. However, Emi Buendia certainly did with a near-post header. Rooted to his line, De Gea's reactions were up to the job as he beat Buendia's effort away.
When De Gea produced more saves after half-time to deny Ramsey and Digne again, it appeared the image of the night for Villa would be midfielder Morgan Sanson kicking a drinks bottle in fury after his error in gifting Fred possession to set up Fernandes for the visitors' second had been followed immediately by his substitution.
However, as it was the prelude to Coutinho's arrival, it was the moment that changed the course of the game - and the acclaim for the Brazilian at the final whistle indicated Villa's fans are already firmly behind him.
"""

result=pipe(article, **gen_kwargs)[0]["summary_text"]

print(result)

''' Output
Title 1 :

Coutinho's arrival sparks Villa comeback

Title 2 :

Philippe Coutinho marked his debut for Aston Villa with a goal and an assist as Steven Gerrard's side came from two goals down to draw with Manchester United.

Title 3 :

Steven Gerrard's first game in charge of Aston Villa ended in a dramatic draw against Manchester United - but it was the arrival of Philippe Coutinho that marked the night.

Title 4 :

Liverpool loanee Philippe Coutinho marked his first appearance for Aston Villa with two goals as Steven Gerrard's side came from two goals down to draw 2-2.'''

```

## Training procedure
While training, **short titles were combined with the subtitles for the articles to improve the quality of the generated titles and the subtitles were removed from the main body of the articles.**

##Limitations

In rare cases, if the opening few lines of a passage/article are descriptive enough, the model often just copies these lines instead of looking for information further down the articles, which may not be conducive in some cases.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 2

### Training results

**Rouge1:38.2315**

**Rouge2: 18.6598**

**RougueL: 31.7393**

**RougeLsum: 31.7086**

### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3

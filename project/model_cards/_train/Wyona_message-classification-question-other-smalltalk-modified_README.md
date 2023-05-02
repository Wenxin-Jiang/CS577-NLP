---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license: apache-2.0
multilinguality:
- monolingual
pretty_name: message-classification
size_categories:
- n=10K
source_datasets:
- https://github.com/zeloru/small-english-smalltalk-corpus
tags:
- message-classification
- question-detection
widget:
- text: "How are you"
- text: "Hello there, how are you"
- text: "Hello there, nice to meet you"
- text: "The highest mountain of Switzerland is the Dufourspitze"
- text: "Which ANN algorithm has Apache Lucene implemented"
task_categories:
- text-classification
task_ids:
- semantic-similarity-scoring
---

## Table of Contents
- [Description](#description)
  - [Summary and intended uses](#summary-and-intended-uses)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
- [Considerations for Using the Model](#considerations-for-using-the-model)
  - [Known Limitations](#known-limitations)

## Description
### Summary and intended uses

Model to detect whether a sentence is a question.

For example

- __Question__: How are you
- __Question__: Hello there, how are you
- __Other__: Hello there, nice to meet you
- __Other__: The highest mountain of Switzerland is the Dufourspitze
- __Question__: Which ANN algorithm has Apache Lucene implemented
- __Other__: Hi Everyone, we have a new blog post that you all might be interested in: "Why is Vector Search so fast?"

The model can be used by bots (e.g. https://ukatie.com) to detect questions inside chatrooms, like for example Slack, MS Teams, Discord or Matrix.

### Languages

So far, English is the only supported language.

## Dataset Structure

### Data Fields

Text: Short input sentence, e.g. "Which ANN algorithm has Apache Lucene implemented"

Label: __Question__ or __Other__

### Data Splits

Question: 10K samples

Other: 10K samples


Training:  18K samples shuffled

Validation: 2K samples shuffled

## Dataset Creation

### Curation Rationale

Simple, short and basic language examples were chosen, because those contain the same kind of words and word placements as long-winded questions with rare words.

Also the goal of this is to detect questions in a chatroom, which is a medium where people often use very short sentences and a lot of greetings or small-talk.

### Source Data

#### Initial Data Collection

https://github.com/zeloru/small-english-smalltalk-corpus

It is scraped data from ESL language learning material.

Out of the already scraped data, only samples from certain conversations were taken, because of quality issues with some of them.

Because we also want to detect questions that are missing a questionmark, most of the samples had the questionmark removed. The same was done for the "other" label where "." were removed from the end of a sentence. This was done, so these identifiers don't become the only feature the model looks at.

### Annotations

#### Annotation process

The annotations of "question" or "other" were done automatically by taking questions in the conversations as "question" and the answers as "other"

## Considerations for Using the Model

### Known Limitations

There seems to be an inbalance of greeting word combinations in the beginning of sentences, for example "Hi, has anyone deployed X in Y" is falsely not detected as a question because of the "Hi, " part. This issue will be addressed in updates.

Sentences in the form of "Wondering if 'question'..." and "I'm asking for help about 'question'..." are seemingly hard to detect and need more samples in the data.

Code fragments in input sentences are sometimes detected as questions. If code is present, it should probably be filtered out beforehand.

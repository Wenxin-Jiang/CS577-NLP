---
license: apache-2.0
datasets: iarfmoose/question_generator
---

# T5-v1.1-Small Question Generator

## Model Description

This model is a sequence-to-sequence question generator which takes an answer and context as an input, and generates a question as an output. It is based on Google's pretrained [T5-v1.1-Small](https://huggingface.co/google/t5-v1_1-small) model.

It was trained with and intended to be used with [AMontgomerie/question_generator](https://github.com/AMontgomerie/question_generator).

Observationally, end-to-end generation is a little over 2x faster with T5-Small compared to T5-Base; however, the quality of the questions is generally lower.

## Intended uses & limitations

The model is trained to generate reading comprehension-style questions with answers extracted from a text. The model performs best with full sentence answers, but can also be used with single word or short phrase answers.

### How to use

The model takes concatenated answers and context as an input sequence, and will generate a full question sentence as an output sequence. The max sequence length is 512 tokens. Inputs should be organized into the following format:

```
<answer> answer text here <context> context text here
```

The input sequence can then be encoded and passed as the `input_ids` argument in the model's `generate()` method.

For best results, a large number of questions can be generated, and then filtered using [iarfmoose/bert-base-cased-qa-evaluator](https://huggingface.co/iarfmoose/bert-base-cased-qa-evaluator).

For examples, please see https://github.com/iarfmoose/question_generator.

### Limitations and bias

The model is limited to generating questions in the same style as those found in [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/), [CoQA](https://stanfordnlp.github.io/coqa/), and [MSMARCO](https://microsoft.github.io/msmarco/). The generated questions can potentially be leading or reflect biases that are present in the context. If the context is too short or completely absent, or if the context and answer do not match, the generated question is likely to be incoherent.

## Training data

The model was fine-tuned on a dataset made up of several well-known QA datasets ([SQuAD](https://rajpurkar.github.io/SQuAD-explorer/), [CoQA](https://stanfordnlp.github.io/coqa/), and [MSMARCO](https://microsoft.github.io/msmarco/)). The datasets were restructured by concatenating the answer and context fields into the previously-mentioned format. The question field from the datasets was used as the target during training. The [full training set](https://huggingface.co/datasets/iarfmoose/question_generator) was roughly 200,000 examples.

## Training procedure

The model was trained for 20 epochs over the training set with a learning rate of 1e-3. The batch size was kept at 4 to match the original training strategy used by [iarfmoose](https://huggingface.co/iarfmoose).

[bert-base-uncased](https://huggingface.co/bert-base-uncased) fine-tuned on the [QNLI](https://huggingface.co/datasets/glue) dataset for 2 epochs. 

The fine-tuning process was performed on 2x NVIDIA GeForce GTX 1080 Ti GPUs (11GB). The parameters are:

```
max_seq_length=512
per_device_train_batch_size=8
gradient_accumulation_steps=2
total train batch size (w. parallel, distributed & accumulation) = 32
learning_rate=3e-5
```

## Evaluation results

eval_accuracy = 0.916895

## More information

The QNLI (Question-answering NLI) dataset is a Natural Language Inference dataset automatically derived from the Stanford Question Answering Dataset v1.1 (SQuAD). SQuAD v1.1 consists of question-paragraph pairs, where one of the sentences in the paragraph (drawn from Wikipedia) contains the answer to the corresponding question (written by an annotator). The dataset was converted into sentence pair classification by forming a pair between each question and each sentence in the corresponding context, and filtering out pairs with low lexical overlap between the question and the context sentence. The task is to determine whether the context sentence contains the answer to the question. This modified version of the original task removes the requirement that the model select the exact answer, but also removes the simplifying assumptions that the answer is always present in the input and that lexical overlap is a reliable cue. The QNLI dataset is part of GLEU benchmark.

(source: https://paperswithcode.com/dataset/qnli)
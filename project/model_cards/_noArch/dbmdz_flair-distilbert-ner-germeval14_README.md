---
datasets:
- germeval_14
tags:
- flair
- token-classification
- sequence-tagger-model
language: de
widget:
- text: "Hugging Face ist eine französische Firma mit Sitz in New York."
license: mit
---

# Flair NER model trained on GermEval14 dataset

This model was trained on the official [GermEval14](https://sites.google.com/site/germeval2014ner/data)
dataset using the [Flair](https://github.com/flairNLP/flair) framework.

It uses a fine-tuned German DistilBERT model from [here](https://huggingface.co/distilbert-base-german-cased).

# Results

| Dataset \ Run | Run 1 | Run 2 | Run 3†    | Run 4 | Run 5 | Avg.
| ------------- | ----- | ----- | --------- | ----- | ----- | ----
| Development   | 87.05 | 86.52 | **87.34** | 86.85 | 86.46 | 86.84
| Test          | 85.43 | 85.88 | 85.72     | 85.47 | 85.62 | 85.62

† denotes that this model is selected for upload.

# Flair Fine-Tuning

We used the following script to fine-tune the model on the GermEval14 dataset:

```python
from argparse import ArgumentParser
import torch, flair              

# dataset, model and embedding imports
from flair.datasets import GERMEVAL_14
from flair.embeddings import TransformerWordEmbeddings
from flair.models import SequenceTagger    
from flair.trainers import ModelTrainer

if __name__ == "__main__":

    # All arguments that can be passed
    parser = ArgumentParser()
    parser.add_argument("-s", "--seeds", nargs='+', type=int, default='42')  # pass list of seeds for experiments
    parser.add_argument("-c", "--cuda", type=int, default=0, help="CUDA device")  # which cuda device to use
    parser.add_argument("-m", "--model", type=str, help="Model name (such as Hugging Face model hub name")

    # Parse experimental arguments
    args = parser.parse_args()

    # use cuda device as passed
    flair.device = f'cuda:{str(args.cuda)}'

    # for each passed seed, do one experimental run
    for seed in args.seeds:
        flair.set_seed(seed)

        # model
        hf_model = args.model

        # initialize embeddings
        embeddings = TransformerWordEmbeddings(
            model=hf_model,
            layers="-1",
            subtoken_pooling="first",
            fine_tune=True,
            use_context=False,
            respect_document_boundaries=False,
        )

        # select dataset depending on which language variable is passed
        corpus = GERMEVAL_14()

        # make the dictionary of tags to predict
        tag_dictionary = corpus.make_tag_dictionary('ner')

        # init bare-bones sequence tagger (no reprojection, LSTM or CRF)
        tagger: SequenceTagger = SequenceTagger(
            hidden_size=256,
            embeddings=embeddings,
            tag_dictionary=tag_dictionary,
            tag_type='ner',
            use_crf=False,
            use_rnn=False,
            reproject_embeddings=False,
        )

        # init the model trainer
        trainer = ModelTrainer(tagger, corpus, optimizer=torch.optim.AdamW)

        # make string for output folder
        output_folder = f"flert-ner-{hf_model}-{seed}"

        # train with XLM parameters (AdamW, 20 epochs, small LR)
        from torch.optim.lr_scheduler import OneCycleLR

        trainer.train(
            output_folder,
            learning_rate=5.0e-5,
            mini_batch_size=16,
            mini_batch_chunk_size=1,
            max_epochs=10,
            scheduler=OneCycleLR,
            embeddings_storage_mode='none',
            weight_decay=0.,
            train_with_dev=False,
        )
```

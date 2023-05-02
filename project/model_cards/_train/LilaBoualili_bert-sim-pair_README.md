At its core it uses an BERT-Base model (bert-base-uncased) fine-tuned on the MS MARCO passage classification task using the Sim-Pair marking strategy that highlights exact term matches between the query and the passage via marker tokens (#). It can be loaded using the TF/AutoModelForSequenceClassification classes.

Refer to our [github repository](https://github.com/BOUALILILila/ExactMatchMarking) for a usage example for ad hoc ranking.

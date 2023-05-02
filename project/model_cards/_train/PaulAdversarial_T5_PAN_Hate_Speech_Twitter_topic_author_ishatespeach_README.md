##A T5ForConditionalGeneration trained on 3 tasks from PAN Profiling Hate Speech Spreaders on Twitter dataset (EN):

* author attribution (train and test sets from the PAN task)
* topic attribution - topics were assigned with BertTopic library using embeddings from `cardiffnlp/bertweet-base-hate` Roberta model (train and test sets from the PAN task)
* hate speech identification (train set from the PAN task)


in order to generate tone of comment use prefix **hater classification:**
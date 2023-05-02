## How to use

```python
from simpletransformers.classification import ClassificationModel, ClassificationArgs

name_file = ['bash', 'c', 'c#', 'c++','css', 'haskell', 'java', 'javascript', 'lua', 'objective-c', 'perl', 'php', 'python','r','ruby', 'scala', 'sql', 'swift', 'vb.net']

deep_scc_model_args = ClassificationArgs(num_train_epochs=10,max_seq_length=300,use_multiprocessing=False)
deep_scc_model = ClassificationModel("roberta", "NTUYG/DeepSCC-RoBERTa", num_labels=19, args=deep_scc_model_args,use_cuda=True)

code = '''    public static double getSimilarity(String phrase1, String phrase2) {
        return (getSC(phrase1, phrase2) + getSC(phrase2, phrase1)) / 2.0;
    }'''
code = code.replace('\n',' ').replace('\r',' ')
predictions, raw_outputs = model.predict([code])
predict = name_file[predictions[0]]
print(predict)
```


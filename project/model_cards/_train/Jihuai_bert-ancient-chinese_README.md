---

language:

- "zh"

tags:
- "chinese"
- "classical chinese"
- "literary chinese"
- "ancient chinese"
- "bert"
- "pytorch"

inference: false 

license: "apache-2.0"

---



# **bert-ancient-chinese**



## **Introduction**

With the current wave of Artificial Intelligence and Digital Humanities sweeping the world, the automatic analysis of modern Chinese has achieved great results. However, the automatic analysis and research of ancient Chinese is relatively weak, and it is difficult to meet the actual needs of Sinology, history, philology, Chinese history and the education of Sinology and traditional culture. There are many controversies about characters, words and parts of speech in ancient Chinese, and there are many difficulties in resource construction. Digital Humanities research requires large-scale corpora and high-performance ancient natural language processing tools. In view of the fact that pre-trained language models have greatly improved the accuracy of text mining in English and modern Chinese texts, there is an urgent need for pre-trained models for the automatic processing of ancient texts.

In 2022, we took part in **[EvaHan 2022](https://circse.github.io/LT4HALA/2022/EvaHan)**, the first NLP tool evaluation competition in the field of ancient Chinese. **`bert-ancient-chinese`** is trained to further optimize the model effect in open environment. 

**If you want to refer to our work, you can refer to this [paper](https://aclanthology.org/2022.lt4hala-1.25/)：**

```
@inproceedings{wang2022uncertainty,
  title={The Uncertainty-based Retrieval Framework for Ancient Chinese CWS and POS},
  author={Wang, Pengyu and Ren, Zhichen},
  booktitle={Proceedings of the Second Workshop on Language Technologies for Historical and Ancient Languages},
  pages={164--168},
  year={2022}
}
```

You can view the introduction of the **Chinese version** through [this link](https://github.com/Jihuai-wpy/bert-ancient-chinese).



## **Further Pre-training**

**Compared with the previous pre-trained models, `bert-ancient-chinese` mainly has the following characteristics:**

- Ancient Chinese texts mostly appear in traditional Chinese characters and contain a large number of uncommon Chinese characters, which makes the `vocab table` (vocabulary) of the pre-trained model without some uncommon Chinese characters. `bert-ancient-chinese` further expands the `vocab` (dictionary) of the pre-trained model by learning in a large-scale corpus. The final `vocab table` size is **38208**, compared to `bert-base-chinese` vocabulary size of **21128**, `siku-bert` vocabulary size of **29791**, `bert-ancient-chinese` has a **larger vocabulary**, and also includes more uncommon vocabulary word, which is more conducive to improving the performance of the model in downstream tasks. The `vocab table` is the vocabulary table, which is included in the `vocab.txt` in the pre-trained model.
- `bert-ancient-chinese` uses a larger training set. Compared with `siku-bert` only using `"Siku Quanshu"` as training dataset, we use a larger-scale dataset (about six times that of `"Siku Quanshu"`), covering from the Ministry of Cong, the Ministry of Taoism, the Ministry of Buddhism, the Ministry of Confucianism, the Ministry of Poetry, the Ministry of History, the Ministry of Medicine, the Ministry of Art, the Ministry of Yi, and the Ministry of Zi, are richer in content and wider in scope than the `"Siku Quanshu"`.

- Based on the idea of `Domain-Adaptive Pretraining`, `bert-ancient-chinese` was trained on the basis of `bert-base-chinese ` and was combined with ancient Chinese corpus to obtain a pre-trained model for the field of automatic processing of ancient Chinese.



## **How to use**

### Huggingface Transformers

The `from_pretrained` method based on [Huggingface Transformers](https://github.com/huggingface/transformers) can directly obtain `bert-ancient-chinese` model online.

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("Jihuai/bert-ancient-chinese")

model = AutoModel.from_pretrained("Jihuai/bert-ancient-chinese")
```



## **Download PTM**

The model we provide is the `PyTorch` version.

### From Huggingface

Download directly through Huggingface's official website, and the model on the official website has been updated to the latest version simultaneously:

- **bert-ancient-chinese:[Jihuai/bert-ancient-chinese · Hugging Face](https://huggingface.co/Jihuai/bert-ancient-chinese)**

### From Cloud Disk

Download address:

|        Model         |                             Link                             |
| :------------------: | :----------------------------------------------------------: |
| bert-ancient-chinese | [Link](https://pan.baidu.com/s/1JC5_64gLT07wgG2hjzqxjg )  Extraction code: qs7x |



## **Evaluation & Results**

We tested and compared different pre-trained models on the training and test sets provided by the competition [EvaHan 2022](https://circse.github.io/LT4HALA/2022/EvaHan). We compare the performance of the models by fine-tuning them on the downstream tasks of `Chinese Word Segmentation(CWS)` and `part-of-speech tagging(POS Tagging)`.

We use `BERT+CRF` as the baseline model to compare the performance of `siku-bert`, `siku-roberta` and `bert-ancient-chinese` on downstream tasks. To fully utilize the entire training dataset, we employ `K-fold cross-validation`, while keeping other hyperparameters the same. The evaluation index is the `F1 value`.



<table>
   <tr>
      <td></td>
       <td colspan="2" align="center"> <i>Zuozhuan</i> </td>
       <td colspan="2" align="center"> <i>Shiji</i> </td>
   </tr>
   <tr>
      <td></td>
      <td align="center">CWS</td>
      <td align="center">POS</td>
      <td align="center">CWS</td>
      <td align="center">POS</td>
   </tr>
   <tr>
      <td align="center">siku-bert</td>
      <td align="center">96.0670%</td>
      <td align="center">92.0156%</td>
      <td align="center">92.7909%</td>
      <td align="center">87.1188%</td>
   </tr>
   <tr>
      <td align="center">siku-roberta</td>
      <td align="center">96.0689%</td>
      <td align="center">92.0496%</td>
      <td align="center">93.0183%</td>
      <td align="center">87.5339%</td>
   </tr>
   <tr>
      <td align="center">bert-ancient-chinese</td>
      <td align="center"> <b>96.3273%</b> </td>
      <td align="center"> <b>92.5027%</b> </td>
      <td align="center"> <b>93.2917%</b> </td>
      <td align="center"> <b>87.8749%</b> </td>
   </tr>
</table>


## **Citing**

If our content is helpful for your research work, please quote it in the paper.



## **Disclaim**

The experimental results presented in the report only show the performance under a specific data set and hyperparameter combination, and cannot represent the essence of each model. The experimental results may change due to random number seeds and computing equipment. **Users can use the model arbitrarily within the scope of the license, but we are not responsible for the direct or indirect losses caused by using the content of the project.**



## **Acknowledgment**

`bert-ancient-chinese` is based on [bert-base-chinese](https://huggingface.co/bert-base-chinese) to continue training.

Thanks to Prof. [Xipeng Qiu](https://xpqiu.github.io/) and the [Natural Language Processing Laboratory of Fudan University](https://nlp.fudan.edu.cn/).



## **Contact us**

Pengyu Wang：wpyjihuai@gmail.com

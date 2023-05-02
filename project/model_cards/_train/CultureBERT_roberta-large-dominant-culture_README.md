---
license: cc-by-nc-4.0
---
This model is a fine-tuned version of RoBERTa-large [1]. It was trained on 1,400 employee reviews to measure corporate culture. More specifically, it predicts which of the four culture dimensions of the Competing Values Framework [2,3] best fits the text at hands, i.e., what is the **dominant culture**.

The model assigns one of four possible labels:

0 (**clan**): Text is best described by a **clan (collaborating) culture**. <br />
1 (**adhocracy**): Text is best described by an **adhocracy (creating) culture**.<br />
2 (**market**): Text is best described by a **market (competing) culture**.<br />
3 (**hierarchy**): Text is best described by a **hierarchy (controlling) culture**.<br />


For details on the model and its performance, see Koch and Pasch (2022). Please cite this article when using the model: <br />
Koch, Sebastian; Pasch, Stefan (2022): CultureBERT: Fine-Tuning Transformer Based Language Models for Corporate Culture. Available online at http://arxiv.org/abs/2212.00509.

Please see the following **tutorial** on how to apply CultureBERT to measure corporate culture in your own text documents: https://github.com/Stefan-Pasch/CultureBERT

Other References:

[1] Liu, Y.; Ott, M.; Goyal, N.; Du, J.; Joshi, M.; Chen, D.; ... & Stoyanov, V. (2019). Roberta: A robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692. 

[2] Cameron, Kim S.; Quinn, Robert E. (2011): Diagnosing and Changing Organizational Culture. Based on the Competing Values Framework. 3rd ed. San Francisco (CA): Jossey-Bass.

[3] Quinn, Robert E.; Rohrbaugh, John (1983): A Spatial Model of Effectiveness Criteria: Towards a Competing Values Approach to Organizational Analysis. In Management Science 29 (3), pp. 363–377. DOI: 10.1287/mnsc.29.3.363.

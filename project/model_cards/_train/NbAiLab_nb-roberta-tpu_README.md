---
license: apache-2.0
---
# NB-ROBERTA Training Code
This is the current training code for the planned nb-roberta models.

We are currently planning to run the following experiments:


<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>nb-roberta-base-old (C)</strong>
   </td>
  </tr>
  <tr>
   <td>Corpus
   </td>
   <td>NbAiLab/nb_bert
   </td>
  </tr>
  <tr>
   <td>Pod size
   </td>
   <td>v4-64
   </td>
  </tr>
  <tr>
   <td>Batch size
   </td>
   <td>62*4*8 = 1984 = 2k
   </td>
  </tr>
  <tr>
   <td>Learning rate
   </td>
   <td>3e-4 (RoBERTa article is using 6e-4 and bs=8k)
   </td>
  </tr>
  <tr>
   <td>Number of steps
   </td>
   <td>250k
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>nb-roberta-base-ext (B)</strong>
   </td>
  </tr>
  <tr>
   <td>Corpus
   </td>
   <td>NbAiLab/nbailab_extended
   </td>
  </tr>
  <tr>
   <td>Pod size
   </td>
   <td>v4-64
   </td>
  </tr>
  <tr>
   <td>Batch size
   </td>
   <td>62*4*8 = 1984 = 2k
   </td>
  </tr>
  <tr>
   <td>Learning rate
   </td>
   <td>3e-4 (RoBERTa article is using 6e-4 and bs=8k)
   </td>
  </tr>
  <tr>
   <td>Number of steps
   </td>
   <td>250k
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>nb-roberta-large-ext</strong>
   </td>
  </tr>
  <tr>
   <td>Corpus
   </td>
   <td>NbAiLab/nbailab_extended
   </td>
  </tr>
  <tr>
   <td>Pod size
   </td>
   <td>v4-64
   </td>
  </tr>
  <tr>
   <td>Batch size
   </td>
   <td>32*4*8 = 2024 = 1k
   </td>
  </tr>
  <tr>
   <td>Learning rate
   </td>
   <td>2-e4 (RoBERTa article is using 4e-4 and bs=8k)
   </td>
  </tr>
  <tr>
   <td>Number of steps
   </td>
   <td>500k
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>nb-roberta-base-scandi</strong>
   </td>
  </tr>
  <tr>
   <td>Corpus
   </td>
   <td>NbAiLab/scandinavian
   </td>
  </tr>
  <tr>
   <td>Pod size
   </td>
   <td>v4-64
   </td>
  </tr>
  <tr>
   <td>Batch size
   </td>
   <td>62*4*8 = 1984 = 2k
   </td>
  </tr>
  <tr>
   <td>Learning rate
   </td>
   <td>3e-4 (RoBERTa article is using 6e-4 and bs=8k)
   </td>
  </tr>
  <tr>
   <td>Number of steps
   </td>
   <td>250k
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>nb-roberta-large-scandi</strong>
   </td>
  </tr>
  <tr>
   <td>Corpus
   </td>
   <td>NbAiLab/scandinavian
   </td>
  </tr>
  <tr>
   <td>Pod size
   </td>
   <td>v4-64
   </td>
  </tr>
  <tr>
   <td>Batch size
   </td>
   <td>32*4*8 = 1024 = 1k
   </td>
  </tr>
  <tr>
   <td>Learning rate
   </td>
   <td>2-e4 (RoBERTa article is using 4e-4 and bs=8k)
   </td>
  </tr>
  <tr>
   <td>Number of steps
   </td>
   <td>500k
   </td>
  </tr>
</table>


## Calculations
Some basic that we used when estimating the number of training steps:
* The Scandinavic Corpus is 85GB
* The Scandinavic Corpus contains 13B words
* With a conversion factor of 2.3, this is estimated to around 30B tokens
* 30B tokens / (512 seq length * 3000 batch size) = 20.000 steps





---
language: "id"
widget:
- text: "dahulu kala ada sebuah"
---

## how to use

```python
from transformers import pipeline, set_seed

path = "akahana/gpt2-indonesia"
generator = pipeline('text-generation', 
                     model=path)
set_seed(42)

kalimat = "dahulu kala ada sebuah"
preds = generator(kalimat, 
                  max_length=64,
                  num_return_sequences=3)
for data in preds:
  print(data)
  

{'generated_text': 'dahulu kala ada sebuah perkampungan yang bernama pomere. namun kini kawasan ini sudah tidak dikembangkan lagi sebagai kawasan industri seperti perusahaan pupuk. sumber-sumber lain sudah sulit ditemukan karena belum adanya kilang pupuk milik indonesia yang sering di kembangkan sehingga belum ada satupun yang masih tersisa yang tersisa. kawasan ini juga memproduksi gula aren milik pt graha bina sarana'}
{'generated_text': 'dahulu kala ada sebuah desa kecil bernama desa. desa yang terkenal seperti halnya kota terdekat lainnya adalah desa tetangga yang bernama sama."\n"sebuah masjid merupakan suatu tempat suci yang digunakan umat islam untuk beribadah. beberapa masjid yang didaftarkan berikut memiliki suatu kehormatan tersendiri bagi masing-masing denominasi islam di dunia. sebuah masjid selain memiliki fungsi sebagai tempat'}
{'generated_text': 'dahulu kala ada sebuah peradaban yang dibangun di sebelah barat sungai mississippi di sekitar desa kecil desa yang bernama sama. penduduk asli di desa ini berasal dari etnis teweh yang berpindah agama menjadi kristen, namun kemudian pindah agama menjadi kristen. desa arawak mempunyai beberapa desa lain seperti adibei, deti, riuhut dan sa'}


```
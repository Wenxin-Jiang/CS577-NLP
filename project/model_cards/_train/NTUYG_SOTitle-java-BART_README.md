## How to use

```python
import logging
from simpletransformers.seq2seq import Seq2SeqModel, Seq2SeqArgs

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

model_args = Seq2SeqArgs()

# 加载本地训练好的模型
model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="NTUYG/SOTitle-java-BART",
    args=model_args,
)

describe = """
I am a beginner at Android Java development but I have a few years of school + uni experience in Java. I am trying to write to a text file in an assets folder in my app using FileOutputStream but it doesn't seem to write to it at all since I am using InputStream to read the file after and there haven't any updates. Here is my code
"""
code = """
private void updateTextFile(String update) {
    FileOutputStream fos = null;

    try
    {
        fos = openFileOutput("Questions",MODE_PRIVATE);
        fos.write("Testing".getBytes());
    } 
    catch (FileNotFoundException e) 
    {
        e.printStackTrace();
    } 
    catch (IOException e) 
    {
        e.printStackTrace();
    } 
    finally 
    {
        if(fos!=null)
        {
            try 
            {
                fos.close();
            } 
            catch (IOException e) 
            {
                e.printStackTrace();
            }
        }
    }

    String text = "";

    try
    {
        InputStream is = getAssets().open("Questions");
        int size = is.available();
        byte[] buffer = new byte[size];
        is.read(buffer);
        is.close();
        text = new String(buffer);
    } 
    catch (IOException e) 
    {
        e.printStackTrace();
    }
    System.out.println("Tesing output " + text);
}
"""

from nltk import word_tokenize

describe = describe.replace('\n',' ').replace('\r',' ')
describe = ' '.join(word_tokenize(describe))
code = code.replace('\n',' ').replace('\r',' ')
code = ' '.join(word_tokenize(code))

# human ： Java Android Cant seem to update text file using FileOutputStream

body = describe + ' <code> ' + code +' </code>'
print(
    model.predict(
        [
            body
        ]
    )
)
```


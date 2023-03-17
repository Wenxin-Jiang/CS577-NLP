--------------------------------------------------------------------------------------------------
    WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations
--------------------------------------------------------------------------------------------------

This package contains the WiC dataset for evaluating contextualized word representations. 

The dataset is split into development (dev), training (train) and test (test) sets. Each partition 
contains two files, with the same number of lines (each line corresponds to an instance):

    * (dev/train/test).data.txt: This is a tab-separated file containing the following items: 

        target_word <tab> PoS <tab> index1-index2 <tab> example_1 <tab> example_2

	    - "target_word": the target word which is present in both examples.

   	    - "PoS": the Part-of-Speech tag of the target word (either "N": noun or "V": verb).

       	    - "index1-index2": indicates the index of target_word in example_1 and example_2, 
	       respectively.

            - "example_i": corresponds to the "i"th example. In this version all examples are 
			       tokenized.


    * (dev/train/test).gold.txt: This file contain the gold labels, which can be "T" (True) or 
	                         "F" (False) depending on whether the intended sense of the 
				 target word is the same in both examples or not.


For further details, please see https://pilehvar.github.io/wic/

NOTE: The WiC dataset has also been used as part of the SuperGLUE language understanding benchmark
      (https://super.gluebenchmark.com/tasks) and as a challenge co-located with the SemDeep workshop 
      at IJCAI 2019 (http://www.dfki.de/~declerck/semdeep-5/challenge.html).

====================================================================================================
REFERENCE PAPER
====================================================================================================

When using this dataset, please refer to the following paper:

	Mohammad Taher Pilehvar and Jose Camacho-Collados,
	WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations,
	In Proceedings of NAACL 2019 (short), Minneapolis, USA. 


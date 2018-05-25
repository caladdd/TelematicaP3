# Special Topics in Telematics - Project 3

### Team

- Catalina Patiño Forero
- Juan Pablo Calad Henao
- Mateo Agudelo Toro


### Dataset

The dataset can (*this is just an example*) be loaded into HDFS by running the following commands:

> [\<user\>@hdpmaster ~] wget https://raw.githubusercontent.com/st0263eafit/bigdata20181/master/datasets/airlines.csv

> [\<user\>@hdpmaster ~] hdfs dfs -put ~/airlines.csv /user/\<user\>/datasets/

> [\<user\>@hdpmaster ~] rm ~/airlines.csv                      # optional: remove the dataset from the local storage


### Execution

The `main.py` file takes 3 parameters (in the given order):

- **k**: the number of topics to divide the dataset in.
- **Input file**: the file to be processed.
- **Output folder**: the folder to store the output (`.csv` file) in. This folder must *not* exist before running this script.

This program is designed to be run on an Spark cluster, so it should be sumbitted as a job. Example: 

> [\<user\>@hdpmaster ~] spark-submit --master yarn main.py 25 hdfs:///user/\<user\>/datasets/airlines.csv hdfs:///user/\<user\>/outputTest > out.txt

This will print the *k* (25 in this case) topics and the keywords that compose each one of them to the `out.txt` file. Example:

![Ejemplo Temas](/EjemploTemas.jpg) 

And the new dataset (the actual output, in which *k* columns were added to the original one, each one containing how much, as a percentage, 
of each topic is contained in that row's review) is output to the specified output folder. Example:

![Ejemplo Output](/EjemploOutput.jpg) 

This new `.csv` file provides valuable information to the understanding of the reviews found in the dataset. 


### Processing

This part is actually divided into two: a *preprocessing* step and the actual *processing* step. Deeper information about **all** the 
steps can be found in the `MarcoTeorico.md` file.

#### Preprocessing

This part is composed of three steps. Before continuing, we want to point out that the preprocessing was done without the use 
of libraries other than the ones already available to pyspark in the cluster. Although this part could've been done locally, given 
the (potential) size of the dataset, we decided to take advantage of the cluster's processing power (at the expense of being unable 
to install new libraries, like we already mentioned).

1. **Normalizing**: in this step we take away every non-alphabetic character (i.e. we take only the 26 letters contained in the 
English alphabet). Then we make them all lowercase for easier processing. There is only one exception to this rule: the `'` 
character (like in *wasn't* or *didn't*); we did this because the `'` is actually part of the language and Spark ML's StopWordsRemover 
wouldn't rule out words like the former examples when in fact they are stop words (i.e. *wasnt* wasn't being recognized as a stop word, 
whereas *wasn't* is)

2. **Removing stop words**: in this step the stop words are removed from the reviews. This step is done by the Spark ML's 
StopWordsRemover. We initially wrote our own user defined function for this purpose with a custom external stop words dictionary, 
but given the problems imposed when trying to run multiple-file scripts on Spark we decided to go for an already written one. 

3. **Stemming**: in this step the words are reduced to their common base form. This leads to words like *arriv* that could be found 
in the original dataset as *arrive*, *arrived*, *arrives*, *arriving*, etc., which helps in the processing step. During our 
research about this topic, we found a more powerful technique called *lemmatization*, but we weren't unable to implement our 
own, unlike the stemming algorithm (remember that given the approach we took, we couldn't install new libraries; more information 
about this decision can be found in the `MarcoTeorico.md` file).

#### Processing

This part is also composed of three steps, and a usual (specially for this part), deeper information about **all** the steps  
can be found in the `MarcoTeorico.md` file.

1. **Generating the TF-IDF matrix**: short for term-frecuency inverse document frecuency matrix. It assigns a value to each word that appears
in the dataset with the purpose of assessing its significance (giving low values to common words and viceversa).

2. **Generating the LDA model**: infers topics from a collection of text documents. Takes the TF-IDF matrix as input.

3. **Applying the LDA model**: once the LDA model is generated, it's applied to the original dataset. The output, for each review, is a 
vector of *k* numbers, each one representing how much (as a percetage) each topic appears in the current review. The new dataset is
made by appending the elements of this vector as columns.

### Visualization

The execution step prepares the data, processes it and then outputs a new dataset with valuable data appended to the original one. 
This new data can then be used to perform an efficient analysis of the reviews found in the original dataset given the new insight. 
As an example, we performed an analysis of the negative reviews using Tableau that can be found in the `EjemploAnalisisTemasNegativos.pdf` 
file.


### References

- [Spark Text Analytics - Uncovering Data-Driven Topics Tutorial](https://community.hortonworks.com/articles/84781/spark-text-analytics-uncovering-data-driven-topics.html)
- [Spark SQL](https://spark.apache.org/docs/latest/api/python/pyspark.sql.html)
- [Reading command line arguments with python](https://stackoverflow.com/questions/1009860/how-to-read-process-command-line-arguments)

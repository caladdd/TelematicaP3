# Special Topics in Telematics - Project 3

### Team

- Catalina Patiño Forero
- Juan Pablo Calad Henao
- Mateo Agudelo Toro


### Dataset

The dataset can (this is just an *example*) be loaded into HDFS by running the following commands:

> [\<user\>@hdpmaster ~] wget https://raw.githubusercontent.com/st0263eafit/bigdata20181/master/datasets/airlines.csv

> [\<user\>@hdpmaster ~] hdfs dfs -put ~/airlines.csv /user/\<user\>/datasets/

> [\<user\>@hdpmaster ~] rm ~/airlines.csv # optional: remove the dataset from the local storage


### Execution

The `main.py` file takes 3 parameters (in the given order):

- **k**: the number of topics to divide the dataset in.
- **Input file**: the file to be processed.
- **Output folder**: the folder to store the output (`.csv`) file. This folder must *not* exists before running this script.

This program is design to be run on a Apache Spark cluster, so it should be sumbitted as a job. Example: 

> spark-submit --master yarn main.py 25 hdfs:///user/\<user\>/datasets/airlines.csv hdfs:///user/\<user\>/outputTest > out.txt

This will print the k - 25 in this case - topics and the keywords that compose each one of them to the out.txt file. Example:

![Ejemplo Temas](/EjemploTemas.jpg) 

And the new dataset (the actual output, in which k columns are added, each one containing the percentage of each topic contained 
in that row's review) is output to the specified output folder. Example:

![Ejemplo Output](/EjemploOutput.jpg) 

This new `.csv` file provides valuable information aiming to the understanding of the reviews found in the dataset. 


### Visualization

The execution step prepares the data, processes it and then outputs a new dataset with new valuable data. This data can be used
to perform an efficient analysis of the reviews found in the original dataset. As an example, we performed an *analysis of the 
negative reviews* using Tableau that can be found in the `EjemploAnalisisTemasNegativos.pdf` file.


### References

- [Spark Text Analytics - Uncovering Data-Driven Topics Tutorial](https://community.hortonworks.com/articles/84781/spark-text-analytics-uncovering-data-driven-topics.html)
- [SparkML Clustering](http://spark.apache.org/docs/2.2.0/api/python/_modules/pyspark/ml/clustering.html)
- [Reading files line by line efficiently using Python](https://stackoverflow.com/questions/8009882/how-to-a-read-large-file-line-by-line-in-python/8010133)
- [Porter's Stemmer Algorithm (the one used in NLTK) Cannonical Implementation in Python by Vivake Gupta](https://tartarus.org/martin/PorterStemmer/python.txt)
- [List of English stop words by Martin Porter](http://snowball.tartarus.org/algorithms/english/stop.txt)

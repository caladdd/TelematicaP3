# Special Topics in Telematics - Project 3


### Dataset

The dataset can be loaded into HDFS by running the following commands:

> [\<user\>@hdpmaster ~] wget https://raw.githubusercontent.com/st0263eafit/bigdata20181/master/datasets/airlines.csv

> [\<user\>@hdpmaster ~] hdfs dfs -put ~/airlines.csv /user/\<user\>/datasets/

> [\<user\>@hdpmaster ~] rm ~/airlines.csv # optional: remove the dataset from the local storage


### Execution

First, make sure that the `user` variable in `main.py` matches your own \<user\>. Then, assuming that this repository's 
files are stored in the `~/TelematicaP3/` folder, open `pyspark` and run the following inside of it

> \>\>\> exec(open("/home/\<user\>/TelematicaP3/main.py").read())


### References

- [Spark Text Analytics - Uncovering Data-Driven Topics Tutorial](https://community.hortonworks.com/articles/84781/spark-text-analytics-uncovering-data-driven-topics.html)
- [SparkML Clustering](http://spark.apache.org/docs/2.2.0/api/python/_modules/pyspark/ml/clustering.html)
- [Reading files line by line efficiently using Python](https://stackoverflow.com/questions/8009882/how-to-a-read-large-file-line-by-line-in-python/8010133)
- [Porter's Stemmer Algorithm (the one used in NLTK) Cannonical Implementation in Python by Vivake Gupta](https://tartarus.org/martin/PorterStemmer/python.txt)
- [List of English stop words by Martin Porter](http://snowball.tartarus.org/algorithms/english/stop.txt)


# TelematicaP3

[AirLines](https://community.hortonworks.com/articles/84781/spark-text-analytics-uncovering-data-driven-topics.html)

### Carga de datos a Hdfs

> user@hdpmaster$  hdfs dfs -put /datasets/airline.csv /user/jcaladh/datasets/

### Imports

* iniciar pyspark

> user@hdpmaster$  pyspark


    from pyspark.sql.functions import col, udf, struct
    from pyspark.sql.types import *
    import re

    from pyspark.ml.feature import CountVectorizer
    from pyspark.ml.feature import HashingTF, IDF, Tokenizer
    from pyspark.ml.clustering import LDA
    from pyspark.ml.linalg import Vectors, SparseVector

### Carga de datos a pyspark

    rawdata = spark.read.load("hdfs:///user/jcaladh/datasets/airlines.csv",format="csv", header=True)
    rawdata.show(10)

### Pre-procesamiento

* Correr lo de Pre-processing.py y luego lo siguente:

    exec(open("/home/jcaladh/top-telematica/TelematicaP3/Pre-processing.py").read())


### Generación de TF-IDF (Term Frequency Inverse Document Frequency)

* Correr lo de Tf-idf.py

    exec(open("/home/jcaladh/top-telematica/TelematicaP3/Tf-idf.py").read())

### Use LDA to Cluster the TF-IDF Matrix

* Correr lo de Lda.py

    exec(open("/home/jcaladh/top-telematica/TelematicaP3/Lda.py").read())
<!--
https://github.com/zaratsian/Spark/blob/master/text_analytics_datadriven_topics.py 
-->
### Referencias

[Spark](http://spark.apache.org/docs/2.2.0/api/python/_modules/pyspark/ml/clustering.html)


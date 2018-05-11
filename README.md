
# TelematicaP3

[AirLines](https://community.hortonworks.com/articles/84781/spark-text-analytics-uncovering-data-driven-topics.html)

### Carga de datos a Hdfs

> hdfs dfs -put /datasets/airline.csv /user/jcaladh/datasets/

### imports

* iniciar pyspark

> user@master$ pyspark


        from pyspark.sql.functions import col, udf, struct
        from pyspark.sql.types import *
        import re

        from pyspark.ml.feature import CountVectorizer
        from pyspark.ml.feature import HashingTF, IDF, Tokenizer
        from pyspark.ml.clustering import LDA
        from pyspark.ml.linalg import Vectors, SparseVector

### carga de datos a pyspark

        rawdata = spark.read.load("hdfs:///user/jcaladh/datasets/airlines.csv",format="csv", header=True)
        rawdata.show(10)

### Pre-procesamiento

* Correr lo de Pre-processing.py y luego lo siguente:
```
udf_cleantext = udf(cleanup_text , ArrayType(StringType()))
clean_text = rawdata.withColumn("words", udf_cleantext(struct([rawdata[x] for x in rawdata.columns])))
#Nueva tabla con columna de palabras no incluyendo stopwords
clean_text.show(10)
```

### Generación de TF-IDF (Term Frequency Inverse Document Frequency)

* Correr lo de Tf-idf.py

### Use LDA to Cluster the TF-IDF Matrix

* Correr lo de Lda.py
<!--
```python
rawdata = spark.read.load("hdfs:///user/jcaladh/datasets/airlines.csv",format="csv", header=True)
rawdata.show(10)


from pyspark.sql.functions import col, udf, struct
from pyspark.sql.types import *
import re


udf_cleantext = udf(cleanup_text , ArrayType(StringType()))
clean_text = rawdata.withColumn("words", udf_cleantext(struct([rawdata[x] for x in rawdata.columns])))
clean_text.show(10)

from pyspark.ml.feature import CountVectorizer
from pyspark.ml.feature import HashingTF, IDF, Tokenizer


from pyspark.ml.clustering import LDA
from pyspark.ml.linalg import Vectors, SparseVector
```
-->
[Spark](http://spark.apache.org/docs/2.2.0/api/python/_modules/pyspark/ml/clustering.html)


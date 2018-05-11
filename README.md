
# TelematicaP3

[AirLines](https://community.hortonworks.com/articles/84781/spark-text-analytics-uncovering-data-driven-topics.html)

### Carga de datos Hdfs

* airfile = sc.textFile("hdfs:///user/jcaladh/datasets/airlines.csv")

* airfile.saveAsTextFile("hdfs:///user/jcaladh/airlinesp3")


>rawdata = spark.read.load("hdfs:///user/jcaladh/datasets/airlines.csv",format="csv", header=True)
rawdata.show(10)


>from pyspark.sql.functions import col, udf, struct
>from pyspark.sql.types import *
>import re


>udf_cleantext = udf(cleanup_text , ArrayType(StringType()))
clean_text = rawdata.withColumn("words", udf_cleantext(struct([rawdata[x] for x in rawdata.columns])))

>clean_text.show(10)

```python

```
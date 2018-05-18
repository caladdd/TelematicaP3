
# TelematicaP3

[AirLines](https://community.hortonworks.com/articles/84781/spark-text-analytics-uncovering-data-driven-topics.html)

### Carga de datos a Hdfs

> user@hdpmaster$  hdfs dfs -put /datasets/airline.csv /user/jcaladh/datasets/

### Ejecución

* iniciar pyspark

        user@hdpmaster$  pyspark
        exec(open("/home/jcaladh/top-telematica/TelematicaP3/Topics_in_reviews.py").read())

<!--
https://github.com/zaratsian/Spark/blob/master/text_analytics_datadriven_topics.py 
-->
### Referencias

[Spark](http://spark.apache.org/docs/2.2.0/api/python/_modules/pyspark/ml/clustering.html)


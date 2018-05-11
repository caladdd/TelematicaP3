# TelematicaP3

Carga de datos Hdfs
airfile = sc.textFile("hdfs:///user/jcaladh/datasets/airlines.csv")
airfile.saveAsTextFile("hdfs:///user/jcaladh/airlinesp3")
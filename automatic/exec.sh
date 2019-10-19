#!/bin/bash
source $HOME/.bashrc


#Hadoop Variables
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"
export LD_LIBRARY_PATH=/usr/local/hadoop/lib/

#SET HBASE_HOME
export HBASE_HOME=/usr/local/hbase-1.2.2
export PATH=$PATH:$HBASE_HOME/bin

#SET SPARK_HOME
export SPARK_HOME=/usr/local/spark
export PATH=$PATH:$SPARK_HOME/bin

#changing the default version of python in spark
export PYSPARK_PYTHON=/usr/bin/python3



python3 ~/automatic/redbus_new.py
#python3 /home/rohit/automatic/ixigo.py
/usr/local/hadoop/bin/hadoop fs -put ~/automatic/*.csv /

/usr/local/spark/bin/spark-submit ~/automatic/sparksqlquery.py

/usr/local/hadoop/bin/hadoop fs -get /user/linux/sorted_Bangalore_Katpadi_30_May2019
cat sorted_Bangalore_Katpadi_30_May2019/*.csv > ~/automatic/cheap.csv
scp ~/automatic/cheap.csv prince-ubuntu:programs/goraahi/
/usr/local/hadoop/bin/hadoop fs -rm -r /user/linux/sorted_Bangalore_Katpadi_30_May2019
/usr/local/hadoop/bin/hadoop fs -rm /Bangalore_Katpadi_30_May2019.csv
rm -r sorted_Bangalore_Katpadi_30_May2019

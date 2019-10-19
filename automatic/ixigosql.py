from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType

FARE = "Fare"

if __name__ == "__main__":
    session = SparkSession.builder.appName("RaahiGo").getOrCreate()
    session.sparkContext.setLogLevel("ERROR")
    dataFrameReader = session.read

    #dataframeobject
    responses = dataFrameReader \
                  .option("header","true") \
                  .option("inferSchema",value = True) \
                  .csv("ixigo.csv")

    print("SCHEMA")
    responses.printSchema();
    session.stop();

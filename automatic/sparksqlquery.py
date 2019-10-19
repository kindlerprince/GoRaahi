from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType

import subprocess



fn = open("city.csv","r")
for line in fn:
     fields = line.split(",")

     FARE = "Fare"

     if __name__ == "__main__":
         session = SparkSession.builder.appName("RaahiGo").master("local[1]").getOrCreate()
         session.sparkContext.setLogLevel("ERROR")
         dataFrameReader = session.read

         #dataframeobject
         responses = dataFrameReader \
                       .option("header","true") \
                       .option("inferSchema",value = True) \
                       .csv("hdfs:///" + fields[0] + "_" + fields[1] + "_" + fields[3].strip('\n') + "_" + ''.join(fields[2].split()) + ".csv")


         print("SCHEMA")
         responses.printSchema();

         selectedColumns = responses.select("Bus_Name","Service_Name","Departure_Time","Arrival_Time","Duration",FARE)
         #selectedColumns.show()
         column = selectedColumns.withColumn("Fare",selectedColumns["FARE"].cast("double"))
         #print("TABLE after type casting")
         #column.show()

         #print("Cheapest first")

         #subprocess.run(["hadoop", "fs"," -rm", "-r", "/user/linux/sorted*"])
         generate = column.orderBy("Fare")
         generate.show()
         generate.write \
         .format('csv') \
         .options(delimiter='|') \
         .save("sorted_"+fields[0] + "_" + fields[1] + "_" + fields[3].strip('\n') + "_" + ''.join(fields[2].split()))
            
         
         session.stop()

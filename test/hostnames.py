from __future__ import print_function

import socket
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Hostnames").getOrCreate()
    rdd = spark.sparkContext.parallelize(range(1, 100), 5)
    hostnames = rdd.map(lambda x: socket.gethostname()).collect()
    print("######## HOSTNAMES #########")
    print(hostnames)
    print("######## HOSTNAMES #########")

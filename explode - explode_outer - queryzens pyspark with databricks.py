# Databricks notebook source
# DBTITLE 1,explode
from pyspark.sql.functions import col, explode
data = [
    (1, "Dev", ["Python", "Spark", "SQL"]),
    (2, "Aman", ["Scala"]),
    (3, "Sara", []),          # Empty array
    (4, "John", None)         # Null value
]

columns = ["id","name", "skills"]
df = spark.createDataFrame(data, columns)

# COMMAND ----------

display(df)

# COMMAND ----------

df.show()

# COMMAND ----------

df_exploded = df.select("id", "name",explode("skills"). alias("skills"))
display(df_exploded)

# COMMAND ----------

from pyspark.sql.functions import explode_outer

df_exploded_outer = df.select("id", "name", explode_outer("skills").alias("skills"))
display(df_exploded_outer)

# COMMAND ----------


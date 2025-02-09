from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, avg, sum, count
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType
import os

# Criando a SparkSession
spark = SparkSession.builder.appName("ETL_PySpark").getOrCreate()

# Definindo caminho de saída
output_path = "/home/cezarcarmo/repos/pyspark-guide/data"
os.makedirs(output_path, exist_ok=True)

# Criando DataFrame de exemplo
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("nome", StringType(), True),
    StructField("idade", IntegerType(), True),
    StructField("salario", DoubleType(), True)
])

data = [
    (1, "Alice", 25, 5000.0),
    (2, "Bob", 17, 3000.0),
    (3, "Carlos", 35, 7000.0),
    (4, "Daniela", 40, None),
    (5, "Eduardo", None, 4000.0),
    (6, "Fernanda", 30, 6000.0)
]

df = spark.createDataFrame(data, schema)

# Exibir esquema dos dados
print("Esquema do DataFrame:")
df.printSchema()

# Transformação
df = df.withColumn("Salario_Ajustado", col("salario") * 1.1)
df = df.withColumn("Categoria_Idade", when(col("idade") < 18, lit("Menor de Idade")).otherwise(lit("Adulto")))

# Removendo duplicatas
df = df.dropDuplicates()

# Tratando valores nulos
fill_values = {"salario": 0, "idade": 18}
df = df.fillna(fill_values)

# Estatísticas básicas
df.describe().show()

# Agregações
df_grouped = df.groupBy("Categoria_Idade").agg(
    avg("Salario_Ajustado").alias("Media_Salario"),
    sum("Salario_Ajustado").alias("Soma_Salario"),
    count("*").alias("Total_Registros")
)
df_grouped.show()

# Carga: Salvando os dados transformados
df.write.mode("overwrite").parquet(f"{output_path}/dados_finalizados.parquet")
df.write.mode("overwrite").json(f"{output_path}/dados_finalizados.json")
df.write.mode("overwrite").csv(f"{output_path}/dados_finalizados.csv", header=True)

df_grouped.write.mode("overwrite").parquet(f"{output_path}/estatisticas.parquet")
df_grouped.write.mode("overwrite").json(f"{output_path}/estatisticas.json")
df_grouped.write.mode("overwrite").csv(f"{output_path}/estatisticas.csv", header=True)

# Encerrando a sessão Spark
spark.stop()

print("Pipeline ETL concluído com sucesso!")

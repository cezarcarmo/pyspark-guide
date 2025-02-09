from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, broadcast, avg, sum, count

# Criando a SparkSession
spark = SparkSession.builder.appName("PySpark_Optimization").getOrCreate()

# Criando DataFrame de exemplo
data = [
    (1, "Alice", 25, 5000.0),
    (2, "Bob", 17, 3000.0),
    (3, "Carlos", 35, 7000.0),
    (4, "Daniela", 40, 8000.0),
    (5, "Eduardo", 22, 4000.0)
]
columns = ["id", "nome", "idade", "salario"]
df = spark.createDataFrame(data, columns)

# Gerenciamento de Partições
print(f"Número de partições antes: {df.rdd.getNumPartitions()}")
df = df.repartition(4)
print(f"Número de partições depois: {df.rdd.getNumPartitions()}")

# Broadcast Join
df_small = spark.createDataFrame([(1, "Engenharia"), (2, "Marketing"), (3, "TI")], ["id", "departamento"])
df_joined = df.join(broadcast(df_small), "id", "left")
df_joined.show()

# Uso de Cache e Persistência
df_cached = df.cache()
df_cached.count()

df_persisted = df.persist()
df_persisted.count()

# Catalyst Optimizer - Plano de Execução
df.explain(True)

# Estatísticas e Agregações
df_grouped = df.groupBy("idade").agg(
    avg("salario").alias("Media_Salario"),
    sum("salario").alias("Soma_Salario"),
    count("*").alias("Total_Registros")
)
df_grouped.show()

# Salvando os dados otimizados
df.write.mode("overwrite").parquet("/home/cezarcarmo/repos/pyspark-guide/data/dados_otimizados.parquet")
df_grouped.write.mode("overwrite").parquet("/home/cezarcarmo/repos/pyspark-guide/data/estatisticas_otimizadas.parquet")

# Encerrando a sessão Spark
spark.stop()
print("Script de otimização executado com sucesso!")

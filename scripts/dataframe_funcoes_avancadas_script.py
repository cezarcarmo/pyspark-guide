from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, sum, max, udf
from pyspark.sql.types import StringType
import os

# Forçar o Spark a usar o interpretador correto
os.environ["PYSPARK_PYTHON"] = "C:\\Users\\cezar\\anaconda3\\envs\\pyspark-env\\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:\\Users\\cezar\\anaconda3\\envs\\pyspark-env\\python.exe"

# Criar SparkSession
spark = SparkSession.builder.appName("FuncoesAvancadas").getOrCreate()

# Dados de exemplo
data = [
    (1, "Ana", 25),
    (2, "Carlos", 30),
    (3, "João", 45),
    (4, "Mariana", 35),
    (1, "Ana", 25) # Para testar distinct
]
columns = ["id", "nome", "idade"]

# Criar DataFrame
df = spark.createDataFrame(data, columns)

# Exibir DataFrame inicial
df.show()

# --- Agrupamento e Agregações ---
print("\n### Agrupamento e Agregações ###")

# Agrupar por nome e calcular soma de idade
grouped_df = df.groupBy("nome").sum("idade")
print("Agrupamento por nome e soma da idade:")
grouped_df.show()

# Agregações múltiplas
df_agg = df.groupBy("id").agg(
    avg("idade").alias("media_idade"),
    sum("idade").alias("soma_idade"),
    max("idade").alias("maior_idade")
)
print("Agregações múltiplas:")
df_agg.show()

# --- Joins ---
print("\n### Joins ###")

# Criar dois DataFrames para o join
df1 = spark.createDataFrame([(1, "Ana"), (2, "Carlos")], ["id", "nome"])
df2 = spark.createDataFrame([(1, 25), (3, 35)], ["id", "idade"])

# Realizar um inner join
inner_join = df1.join(df2, on="id", how="inner")
print("Inner join:")
inner_join.show()

# --- UDFs ---
print("\n### UDFs ###")

# Função personalizada
def saudacao(nome):
    return f"Olá, {nome}!"

# Registrar UDF
saudacao_udf = udf(saudacao, StringType())

# Aplicar UDF no DataFrame
df = df.withColumn("saudacao", saudacao_udf("nome"))
print("Aplicando UDF para criar uma saudação:")
df.show()

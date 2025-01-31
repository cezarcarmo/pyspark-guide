from pyspark.sql import SparkSession

# Criar uma SparkSession
spark = SparkSession.builder \
    .appName("ExemploPySpark") \
    .getOrCreate()

# Exemplo: Criar um DataFrame a partir de um arquivo CSV
file_path = "data/exemplo.csv"

# Criar DataFrame
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Mostrar as primeiras linhas
print("Exibindo as 5 primeiras linhas do DataFrame:")
df.show(5)

# Exibir o esquema do DataFrame
print("Esquema do DataFrame:")
df.printSchema()

# Encerrar a SparkSession
spark.stop()


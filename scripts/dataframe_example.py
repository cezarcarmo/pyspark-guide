from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max
import os

# Criar diretório para dados, se necessário
os.makedirs("data", exist_ok=True)

# Criar arquivo CSV de exemplo
csv_content = "id,nome,idade\n1,Ana,25\n2,Carlos,30\n3,Joao,45\n4,Mariana,35\n"
with open("/home/cezarcarmo/repos/pyspark-guide/data/exemplo.csv", "w") as f:
    f.write(csv_content)

# Criar SparkSession
spark = SparkSession.builder.appName("DataFrameExample").getOrCreate()

# Criar DataFrame a partir de uma lista
data = [(1, "Ana", 25), (2, "Carlos", 30), (3, "João", 45), (4, "Mariana", 35)]
columns = ["id", "nome", "idade"]

# Criar o DataFrame
df = spark.createDataFrame(data, columns)

# Exibir o DataFrame
df.show()

# Operações básicas
# Seleção de colunas
df.select("nome").show()

# Filtrar linhas
df.filter(df["idade"] > 30).show()

# Ordenar dados
df.orderBy("idade").show()

df.orderBy(df["idade"].desc()).show()

# Calcular a idade média e maior idade
idade_media = df.select(avg("idade").alias("idade_media"))
idade_media.show()

maior_idade = df.select(max("idade").alias("maior_idade"))
maior_idade.show()

# Ler arquivo CSV para DataFrame
df_csv = spark.read.csv("/home/cezarcarmo/repos/pyspark-guide/data/exemplo.csv", header=True, inferSchema=True)

# Exibir o DataFrame lido do arquivo CSV
df_csv.show()

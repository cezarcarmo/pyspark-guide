from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col
import os

# Criar SparkSession
spark = SparkSession.builder.appName("ETL_PySpark").getOrCreate()

# Configurar o Spark para evitar erros de NativeIO no Windows
spark.conf.set("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem")
spark.conf.set("spark.sql.parquet.enableVectorizedReader", "false")
spark.conf.set("spark.hadoop.fs.file.native", "false")
spark.conf.set("spark.hadoop.io.nativeio.NativeIO$Windows", "false")
spark.conf.set("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false")
spark.conf.set("spark.sql.sources.commitProtocolClass", "org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol")

# Criar diretório para os arquivos de dados
os.makedirs("data", exist_ok=True)

# Criar arquivo CSV de exemplo
csv_content = "id,nome,idade,cidade\n1,Ana,25,Sao Paulo\n2,Carlos,30,Rio de Janeiro\n3,João,45,Belo Horizonte\n4,Mariana,35,Curitiba\n"
with open("data/exemplo_etl.csv", "w") as f:
    f.write(csv_content)

# --- EXTRAÇÃO ---
print("\n### Extração de Dados ###")

# Ler arquivo CSV
df = spark.read.csv("data/exemplo_etl.csv", header=True, inferSchema=True)
df.show()

# --- TRANSFORMAÇÃO ---
print("\n### Transformação dos Dados ###")

# Selecionar e renomear colunas
df_transf = df.selectExpr("id", "nome", "idade + 1 as idade_atualizada", "cidade")
df_transf.show()

# Filtrar registros onde a idade seja maior que 30
df_filtrado = df_transf.filter(col("idade_atualizada") > 30)
df_filtrado.show()

# Calcular a idade média por cidade
df_media = df_filtrado.groupBy("cidade").agg(avg("idade_atualizada").alias("media_idade"))
df_media.show()

# --- CARGA ---
print("\n### Carga dos Dados ###")

# Criar diretório de saída
os.makedirs("output", exist_ok=True)

# Salvar como CSV
df_filtrado.write.csv("output/dados_filtrados.csv", header=True, mode="overwrite")

# Salvar como Parquet
df_media.write.parquet("output/dados_media.parquet", mode="overwrite")

print("Pipeline ETL concluído!")

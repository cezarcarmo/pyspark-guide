## Certifique-se de ter as credenciais e permissões necessárias para acessar os serviços de cloud.
## Substitua os placeholders com os valores apropriados.: 

    # <YOUR_ACCESS_KEY>, 
    # <YOUR_SECRET_KEY>, 
    # <bucket-name>, 
    # <path-to-file>, 
    # <project-id>, 
    # <dataset>, 
    # <table>, 
    # <account-name>, 
    # <YOUR_ACCOUNT_KEY>, 
    # <container-name> 

from pyspark.sql import SparkSession

# Inicializa a SparkSession
spark = SparkSession.builder \
    .appName("BigQuery Integration Example") \
    .config("spark.jars", "path/to/spark-bigquery-latest_2.12.jar") \
    .getOrCreate()

# Lê dados de uma tabela BigQuery
df = spark.read.format("bigquery").option("table", "<project-id>.<dataset>.<table>").load()
df.show()

# Escreve dados em uma tabela BigQuery
df.write.format("bigquery").option("table", "<project-id>.<dataset>.<table>").save()

spark.stop()
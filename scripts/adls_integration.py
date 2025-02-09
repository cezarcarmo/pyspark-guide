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
    .appName("ADLS Integration Example") \
    .config("spark.hadoop.fs.azure.account.key.<account-name>.dfs.core.windows.net", "<YOUR_ACCOUNT_KEY>") \
    .getOrCreate()

# Lê dados de um container ADLS
df = spark.read.format("csv").option("header", "true").load("abfss://<container-name>@<account-name>.dfs.core.windows.net/<path-to-file>")
df.show()

# Escreve dados em um container ADLS
df.write.format("csv").option("header", "true").save("abfss://<container-name>@<account-name>.dfs.core.windows.net/<path-to-destination>")

spark.stop()
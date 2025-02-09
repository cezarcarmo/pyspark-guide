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
    .appName("S3 Integration Example") \
    .config("spark.hadoop.fs.s3a.access.key", "<YOUR_ACCESS_KEY>") \
    .config("spark.hadoop.fs.s3a.secret.key", "<YOUR_SECRET_KEY>") \
    .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
    .getOrCreate()

# Lê dados de um bucket S3
df = spark.read.format("csv").option("header", "true").load("s3a://<bucket-name>/<path-to-file>")
df.show()

# Escreve dados em um bucket S3
df.write.format("csv").option("header", "true").save("s3a://<bucket-name>/<path-to-destination>")

spark.stop()
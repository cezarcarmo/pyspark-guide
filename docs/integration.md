### 8️⃣ Integração com Cloud (AWS, GCP, Azure)
#### Executando PySpark na AWS Glue
AWS Glue é um serviço de ETL (Extract, Transform, Load) totalmente gerenciado que facilita a preparação e o carregamento de dados para análise. Para executar PySpark na AWS Glue:
1. Crie um trabalho no AWS Glue.
2. Configure o script PySpark no console do AWS Glue.
3. Defina as conexões de dados e os destinos.
4. Execute o trabalho e monitore o progresso no console do AWS Glue.

Para mais detalhes, consulte a [documentação oficial da AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html).

#### Rodando PySpark no Databricks
Databricks é uma plataforma de análise de dados que fornece um ambiente colaborativo para trabalhar com Spark. Para rodar PySpark no Databricks:
1. Crie uma conta no Databricks e configure um cluster.
2. Importe seus notebooks ou scripts PySpark para o workspace do Databricks.
3. Configure as conexões de dados e os destinos.
4. Execute os notebooks ou scripts no cluster do Databricks.

Para mais detalhes, consulte a [documentação oficial do Databricks](https://docs.databricks.com/).

#### Integração com **S3, BigQuery, ADLS**
- **Amazon S3 (AWS):**
  - Para ler dados de um bucket S3:
    ```python
    df = spark.read.format("csv").option("header", "true").load("s3a://<bucket-name>/<path-to-file>")
    ```
  - Para escrever dados em um bucket S3:
    ```python
    df.write.format("csv").option("header", "true").save("s3a://<bucket-name>/<path-to-destination>")
    ```

- **Google BigQuery (GCP):**
  - Para ler dados de uma tabela BigQuery:
    ```python
    df = spark.read.format("bigquery").option("table", "<project-id>.<dataset>.<table>").load()
    ```
  - Para escrever dados em uma tabela BigQuery:
    ```python
    df.write.format("bigquery").option("table", "<project-id>.<dataset>.<table>").save()
    ```

- **Azure Data Lake Storage (ADLS):**
  - Para ler dados de um container ADLS:
    ```python
    df = spark.read.format("csv").option("header", "true").load("abfss://<container-name>@<account-name>.dfs.core.windows.net/<path-to-file>")
    ```
  - Para escrever dados em um container ADLS:
    ```python
    df.write.format("csv").option("header", "true").save("abfss://<container-name>@<account-name>.dfs.core.windows.net/<path-to-destination>")
    ```

Para mais detalhes sobre a integração com esses serviços, consulte as documentações oficiais:
- [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [Google BigQuery](https://cloud.google.com/bigquery/docs)
- [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/data-lake-storage/)

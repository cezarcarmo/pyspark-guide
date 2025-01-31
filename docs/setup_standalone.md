# Configuração do PySpark em Modo Standalone

Nesta seção, configuraremos o PySpark para rodar no modo **Standalone**, ideal para testes locais ou prototipagem de pequenos pipelines de dados.

---

## 🔧 **Pré-requisitos**

1. **Java instalado**:
   - O PySpark depende do Java Runtime Environment (JRE). Verifique se o Java está instalado:
     ```bash
     java -version
     ```
   - Se não estiver instalado, instale o Java Development Kit (JDK).
     - **Linux (Debian/Ubuntu):**
       ```bash
       sudo apt update
       sudo apt install openjdk-11-jdk
       ```
     - **Windows:** Baixe o JDK em [Oracle](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).

2. **Spark instalado**:
   - Baixe o Apache Spark em [Spark Downloads](https://spark.apache.org/downloads.html):
     - Escolha a versão compatível com o PySpark instalado (ex.: 3.4.0).
     - Escolha um **Hadoop pre-built package**.
   - Extraia o Spark para uma pasta acessível (ex.: `/opt/spark` no Linux ou `C:\spark` no Windows).

3. **Configuração de variáveis de ambiente**:
   - Adicione as variáveis ao arquivo de configuração do sistema:
     - **Linux:**
       ```bash
       export SPARK_HOME=/opt/spark
       export PATH=$SPARK_HOME/bin:$PATH
       ```
     - **Windows:**
       - Adicione `SPARK_HOME` nas variáveis de ambiente com o valor `C:\spark`.
       - Inclua `%SPARK_HOME%\bin` no `Path`.

4. **Ambiente Python configurado**:
   - Garanta que o ambiente Conda ou virtual já esteja configurado com o PySpark instalado.

---

## 🚀 **Executando o PySpark em Modo Standalone**

### 1️⃣ **Iniciar o Shell do PySpark**

1. No terminal, execute o comando:
   ```bash
   pyspark
   ```
2. O shell interativo será aberto, permitindo executar comandos PySpark diretamente:
   ```python
   from pyspark.sql import SparkSession
   spark = SparkSession.builder.appName("StandaloneTest").getOrCreate()
   print(spark.version)
   ```

### 2️⃣ **Executar um Script com PySpark**

1. Crie um arquivo de script chamado `standalone_test.py` na pasta `scripts/`.

2. Adicione o seguinte código:
   ```python
   from pyspark.sql import SparkSession

   # Criar uma SparkSession
   spark = SparkSession.builder \
       .appName("Standalone Mode") \
       .getOrCreate()

   # Criar um DataFrame de exemplo
   data = [(1, "Alice", 29), (2, "Bob", 35), (3, "Cathy", 32)]
   columns = ["id", "name", "age"]
   df = spark.createDataFrame(data, columns)

   # Mostrar o DataFrame
   df.show()

   # Encerrar a SparkSession
   spark.stop()
   ```

3. Execute o script:
   ```bash
   python scripts/standalone_test.py
   ```

---

## 🔥 **Testando a Configuração**

1. Certifique-se de que o Spark inicia corretamente executando:
   ```bash
   pyspark
   ```

2. Teste o script `standalone_test.py` para garantir que o ambiente está configurado.

3. Verifique os logs para quaisquer erros relacionados à configuração do Spark ou Java.

---

## 📄 **Notas Importantes**

- Certifique-se de que o `SPARK_HOME` e o `PATH` estão configurados corretamente.
- O modo Standalone é ideal para aprendizado e pequenos testes, mas para grandes volumes de dados, considere usar um cluster distribuído.

---

Para dúvidas ou problemas, consulte a [documentação oficial do Apache Spark](https://spark.apache.org/docs/latest/).


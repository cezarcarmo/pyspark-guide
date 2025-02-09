# Configuração do Ambiente PySpark

Este documento detalha os passos para configurar um ambiente de desenvolvimento PySpark utilizando **Miniconda**.

## 🔥 Criando o Ambiente Virtual com Miniconda

1. **Baixar e instalar o Miniconda**:
   ```bash
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
   bash miniconda.sh -b -p $HOME/miniconda
   export PATH="$HOME/miniconda/bin:$PATH"

2. **Criar um ambiente Conda chamado ``pyspark-env``**:

```bash
conda create --name pyspark-env python=3.8
```

3. **Ativar o ambiente**:

```bash
conda activate pyspark-env
```

4. **Instalar as dependências**:

```bash
conda install -c conda-forge pyspark jupyter findspark
```

## 🖥 Configuração do Java

1. **Instalar o Java**:

```bash
sudo apt update
sudo apt install openjdk-11-jdk
```

2. **Configurar a variável ``JAVA_HOME``**:

```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
```

3. **Adicione essas linhas ao seu arquivo de configuração de shell (~/.bashrc, ~/.zshrc, etc.)**:

```bash
echo 'export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

4. **Verificar a configuração**:

```bash
echo $JAVA_HOME
java -version
```

## 🖥 Configuração do Spark

1. **Instalar o PySpark**:

```bash
conda install -c conda-forge pyspark
```

2. **Configurar a variável ``SPARK_HOME``**:

```bash
which pyspark
```

3. **Use o caminho retornado pelo comando which pyspark para definir a variável ``SPARK_HOME``. Por exemplo, se o caminho retornado for ``/home/cezarcarmo/miniconda3/envs/pyspark-env/bin/pyspark``, defina ``SPARK_HOME`` como ``/home/cezarcarmo/miniconda3/envs/pyspark-env``**:

```bash
echo 'export SPARK_HOME=/home/cezarcarmo/miniconda3/envs/pyspark-env' >> ~/.bashrc
echo 'export PATH=$SPARK_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

4. **Adicione essas linhas ao seu arquivo de configuração de shell**:

```bash
echo 'export SPARK_HOME=/home/cezarcarmo/miniconda3/envs/pyspark-env' >> ~/.bashrc
echo 'export PATH=$SPARK_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

5. **Configurar a variável ``SPARK_LOCAL_IP``**:

```bash
export SPARK_LOCAL_IP=192.168.138.128
```

## 🖥 Configuração no VSCode

1. Abra o **VSCode** e instale as extensões:
   - **Python**
   - **Jupyter**
2. Selecione o ambiente virtual no VSCode:
   - Pressione `Ctrl+Shift+P`
   - Pesquise **Python: Select Interpreter**
   - Escolha `pyspark-env` criado com Conda

## 🚀 Testando a Configuração com Jupyter Notebook

1. **Instalar o Jupyter Notebook no ambiente**:
   ```bash
   pip install jupyter
   ```
2. **Abrir o Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```
3. **Criar um novo notebook e rodar o código abaixo para testar a integração**:
   ```python
   import findspark
   findspark.init()

   from pyspark.sql import SparkSession

   spark = SparkSession.builder.appName("TestePySpark").getOrCreate()
   print(spark.version)
   ```

Se a versão do Spark for exibida sem erros, seu ambiente está pronto! 🎉
```

### Atualização do `.gitignore`

```plaintext
# Ignore Miniconda installer
miniconda.sh
```

Com essas instruções, você deve ser capaz de configurar o ambiente PySpark corretamente e resolver os avisos relacionados ao `SPARK_LOCAL_IP` e à biblioteca nativa do Hadoop.*








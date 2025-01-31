# Guia Completo de PySpark para Engenharia de Dados

## 📌 Objetivo
Este repositório tem como objetivo fornecer um guia completo e prático sobre o uso do **PySpark** na Engenharia de Dados. O projeto abrange desde conceitos fundamentais até implementações avançadas, incluindo **Spark SQL** e integração com diversas ferramentas.

## 📂 Estrutura do Repositório
```
📂 pyspark-guide/
│── 📂 notebooks/         # Notebooks interativos com exemplos práticos
│── 📂 scripts/           # Scripts PySpark organizados para execução modular
│── 📂 data/              # Conjunto de dados para os exemplos práticos
│── 📂 docs/              # Documentação explicativa e guia de estudo
│── 📂 tests/             # Testes para validação dos pipelines
│── 📜 README.md          # Descrição do projeto
│── 📜 requirements.txt   # Dependências do projeto
│── 📜 setup.py           # Configuração do ambiente
```

## 🔥 Conteúdo do Projeto
### 1️⃣ Introdução ao PySpark
- O que é PySpark?
  - PySpark é a API em Python do Apache Spark, um framework de processamento de dados distribuídos projetado para grandes volumes de informações. Ele permite criar aplicações escaláveis para processamento de dados em clusters. Para mais detalhes, consulte [O que é PySpark?](docs/what_is_pyspark.md).
- Instalação e configuração no VSCode
- Configuração de ambiente local (Standalone, Docker, Databricks)
- Comparação: Pandas vs PySpark
  - Para um guia detalhado sobre as diferenças entre Pandas e PySpark, veja [Pandas vs PySpark](docs/pyspark_vs_pandas.md).

### 2️⃣ Fundamentos do PySpark
- Estrutura do **SparkSession** e **RDD**
- DataFrames no PySpark: Criando e manipulando
- Transformações e Ações no PySpark
- Partições e otimização de performance

### 3️⃣ Spark SQL e Manipulação de Dados
- Criando e manipulando tabelas com Spark SQL
- Filtragem, Joins e Agregações
- Funções embutidas no PySpark SQL
- Criando funções UDFs no PySpark

### 4️⃣ ETL com PySpark
- Lendo dados de diferentes fontes (**CSV, Parquet, JSON, JDBC, Delta Lake**)
- Escrevendo dados em diferentes formatos e destinos
- Transformações e tratamentos de dados
- Pipeline ETL completo com PySpark

### 5️⃣ Otimização e Performance
- Gerenciamento de Partições
- Broadcast Joins e Cache
- Uso de Catalyst Optimizer
- Melhores práticas para performance em PySpark

### 6️⃣ Integração com Cloud (AWS, GCP, Azure)
- Executando PySpark na AWS Glue
- Rodando PySpark no Databricks
- Integração com **S3, BigQuery, ADLS**

### 7️⃣ Casos Práticos de Engenharia de Dados
- Pipeline de processamento de logs
- Análise de dados de e-commerce
- Processamento de grandes volumes de dados com PySpark

## 🛠 Tecnologias Utilizadas
✅ PySpark  
✅ Spark SQL  
✅ AWS Glue (opcional)  
✅ Databricks (opcional)  
✅ Jupyter Notebook  
✅ Docker (para testes locais)  
✅ VSCode + Git  

## 🚀 Como Começar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/pyspark-guide.git
   cd pyspark-guide
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute um dos notebooks para explorar os exemplos práticos.

## 📌 Contribuição
Fique à vontade para abrir **issues** e **pull requests** para melhorias no projeto.

## 📄 Licença
Este projeto está sob a licença MIT.


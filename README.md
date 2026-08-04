<div align="center">

# 📊 S&P 500 ETL Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=Snowflake&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

⭐ **Automated ETL Pipeline for S&P 500 Company Data using Apache Airflow & Snowflake** ⭐

</div>

---

## 📌 Overview

This project demonstrates a production-inspired ETL pipeline built using Python, Apache Airflow, Docker, and Snowflake.

**The workflow automatically:**
* Extracts S&P 500 company symbols from Wikipedia
* Connects to Financial Modeling Prep API
* Transform with Pandas
* Load data into Snowflake Data Warehouse
* Executes automatically every **5 minutes** using Airflow scheduler

---

## 🏗️ ETL Architecture

```text
┌──────────────────┐      ┌─────────┐      ┌─────────────────────────┐      ┌───────────┐      ┌──────────────────┐
│ Wikipedia S&P 500│ ───> │ Extract │ ───> │ Financial Modeling Prep │ ───> │ Transform │ ───> │ Snowflake / Airflow│
└──────────────────┘      └─────────┘      └─────────────────────────┘      └───────────┘      └──────────────────┘

📋 FeaturesFeatureStatusExtract Data✅Data Cleaning✅Snowflake Loading✅Airflow Scheduling✅Automatic Retries✅Docker Support✅Environment Variables✅Modular ETL Design✅

🧰 Tech StackTechnologyPurposePythonETL DevelopmentApache AirflowWorkflow OrchestrationSnowflakeCloud Data WarehouseDockerContainerizationPandasData TransformationRequestsAPI CallsGit & GitHubVersion Control

📁 Project StructurePlaintextsp500-airflow-pipeline/
│
├── dags/
│   ├── sp500_pipeline.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── config.py
├── plugins/
├── logs/
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── .gitignore
└── .env

🔄 ETL Workflow🔍 ExtractRead S&P 500 symbols from WikipediaConnect to Financial Modeling Prep APIDownload company profiles
⚡ TransformConvert JSON $\rightarrow$ DataFrameSelect required columnsClean datasetRename columns

📥 LoadConnect to SnowflakeUpload transformed datasetStore in warehouse

⏱️ Airflow DAGPlaintextExtract ──> Transform ──> Load

Runs automatically every: Every 5 Minutes

📊 Sample OutputSymbolCompanySectorMMM3M CompanyIndustrialsAOSA. O. SmithIndustrials

📸 ScreenshotsAirflow DAGSuccessful PipelineSnowflake

🚀 Getting Started1. Clone RepositoryBashgit clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
cd YOUR_REPOSITORY

2. Install DependenciesBashpip install -r requirements.txt

3. Configure Environment VariablesCode snippetFMP_API_KEY=YOUR_API_KEY
SNOWFLAKE_PASSWORD=YOUR_PASSWORD

4. Start AirflowBashdocker compose up -d

5. Open Airflow UIGo to your browser and open:Plaintexthttp://localhost:8080

🔒 Security✅ Secrets stored using Environment Variables✅ .env ignored by Git✅ No credentials committed to repository

🔮 Future ImprovementsLoad all 500 companiesHistorical stock pricesIncremental loadingAirflow ConnectionsAirflow VariablesCI/CD deploymentData Quality ChecksEmail NotificationsUnit Testing

🛠️ Skills Demonstrated✅ Data Engineering✅ ETL Pipeline Design✅ Apache Airflow✅ Snowflake✅ Docker✅ REST APIs✅ Pandas✅ Workflow Automation✅ Cloud Data Warehousing

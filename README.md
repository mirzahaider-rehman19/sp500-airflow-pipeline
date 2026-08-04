<div align="center">

# S&P 500 ETL Pipeline

### Apache Airflow | Snowflake

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)](https://airflow.apache.org/)
[![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)](https://www.snowflake.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

⭐ **Automated ETL Pipeline for S&P 500 Company Data using Apache Airflow & Snowflake**

</div>

---

## 📖 Overview

This project demonstrates a production-inspired ETL pipeline built using Python, Apache Airflow, Docker, and Snowflake.

The workflow automatically:
- ✅ Extracts S&P 500 company symbols from Wikipedia
- ✅ Retrieves company profile data from the Financial Modeling Prep API
- ✅ Cleans and transforms the dataset using Pandas
- ✅ Loads the processed data into Snowflake
- ✅ Executes automatically every 5 minutes using Airflow Scheduler

---

## 🏗️ ETL Architecture

```text
Wikipedia S&P 500 ──> Extract ──> FMP API ──> Transform with Pandas ──> Snowflake ──> Apache Airflow Scheduler
🔄 Pipeline FlowPlaintextwikipedia
   │
   ▼
Fetch S&P 500 Symbols
   │
   ▼
Financial Modeling Prep API
   │
   ▼
Transform Data (Pandas)
   │
   ▼
Snowflake Data warehouse
   │
   ▼
Apache Airflow Scheduler
📊 FeaturesFeatureStatusExtract Data🟩Data Cleaning🟩Snowflake Loading🟩Airflow Scheduling🟩Automatic Retries🟩Docker Support🟩Environment Variables🟩Modular ETL Design🟩🧰 Tech StackTechnologyPurposePythonETL DevelopmentApache AirflowWorkflow OrchestrationSnowflakeCloud Data WarehouseDockerContainerizationPandasData TransformationRequestsAPI CallsGit & GitHubVersion Control📁 Project StructurePlaintextsp500-airflow-pipeline/
│
├── dags/
│   ├── sp500_pipeline.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── config.py
│
├── plugins/
├── logs/
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── .gitignore
└── .env

⚡ ETL Workflow📥 ExtractRead S&P 500 symbols from WikipediaConnect to Financial Modeling Prep APIDownload company profiles🔄 TransformConvert JSON ➔ DataFrameSelect required columnsClean datasetRename columns☁️ LoadConnect to SnowflakeUpload transformed datasetStore in warehouse🕒 Airflow DAGRuns automatically every: Every 5 Minutes📋 Sample OutputSymbolCompanySectorMMM3M CompanyIndustrialsAOSA. O. SmithIndustrials🚀 Getting StartedClone RepositoryBashgit clone [https://github.com/mirzahaider-rehman19/sp500-airflow-pipeline.git](https://github.com/mirzahaider-rehman19/sp500-airflow-pipeline.git)
cd sp500-airflow-pipeline
Install DependenciesBashpip install -r requirements.txt
Configure Environment VariablesCreate a .env file in the root directory:Code snippetFMP_API_KEY=YOUR_API_KEY
SNOWFLAKE_PASSWORD=YOUR_PASSWORD
Start AirflowBashdocker compose up -d
Open Airflow👉 http://localhost:8080🔒 Security✔️ Secrets stored using Environment Variables✔️ .env ignored by Git✔️ No credentials committed to repository🔮 Future ImprovementsFuture EnhancementDescriptionLoad all 500 companiesExpand scope beyond initial sampleHistorical stock pricesIntegrate time-series market datasetsIncremental loadingOptimize pipeline for delta updatesAirflow ConnectionsSecure credential management via UIAirflow VariablesDynamic runtime configurationsAWS DeploymentCloud-native hosting setupData Quality ChecksAutomated schema and anomaly validationEmail NotificationsAlerting system for task failuresCI/CD PipelineAutomated testing and deployment workflowsUnit TestingRobust code testing via Pytest🛠️ Skills DemonstratedSkill / DomainDescriptionData EngineeringDesigning robust data pipelinesETL Pipeline DesignExtract, Transform, Load orchestrationApache AirflowDAG building and task schedulingSnowflakeCloud data warehousing and queryingDockerEnvironment containerizationREST APIsFetching live external dataPandasHigh-performance data wranglingWorkflow AutomationEnd-to-end hands-free executionCloud Data WarehousingScalable cloud data management👤 AuthorMirza Haider Rehman💼 Aspiring Cloud Data Engineer⭐ If you like this project, don't forget to give it a Star!

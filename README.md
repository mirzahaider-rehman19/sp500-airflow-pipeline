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
┌──────────────────┐      ┌─────────┐      ┌─────────────────────────┐      ┌───────────┐      ┌──────────────────┐
│ Wikipedia S&P 500│ ───> │ Extract │ ───> │ Financial Modeling Prep │ ───> │ Transform │ ───> │ Snowflake / Airflow│
└──────────────────┘      └─────────┘      └─────────────────────────┘      └───────────┘      └──────────────────┘

---

## 📋 Features

| Feature | Status |
| :--- | :---: |
| **Extract Data** | ✅ |
| **Data Cleaning** | ✅ |
| **Snowflake Loading** | ✅ |
| **Airflow Scheduling** | ✅ |
| **Automatic Retries** | ✅ |
| **Docker Support** | ✅ |
| **Environment Variables** | ✅ |
| **Modular ETL Design** | ✅ |

---

## 🧰 Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | ETL Development |
| **Apache Airflow** | Workflow Orchestration |
| **Snowflake** | Cloud Data Warehouse |
| **Docker** | Containerization |
| **Pandas** | Data Transformation |

---

## 📁 Project Structure

```text
sp500-airflow-pipeline/
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
└── README.md

🔄 ETL Workflow1. ExtractExtract S&P 500 symbols from WikipediaConnect to Financial Modeling Prep APIDownload company profiles2. TransformConvert JSON $\rightarrow$ DataFrameSelect required columnsClean datasetRename columns3. LoadConnect to SnowflakeStore in warehouse⏱️ Airflow DAGRuns automatically every: Every 5 Minutes🚀 Getting Started1. Clone Repository
git clone [https://github.com/YOUR_USERNAME/sp500-airflow-pipeline.git](https://github.com/YOUR_USERNAME/sp500-airflow-pipeline.git)
cd sp500-airflow-pipeline

pip install -r requirements.txt

3. Configure Environment Variables
Create a .env file or update your configuration with:

Code snippet
FMP_API_KEY=your_fmp_api_key
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_WAREHOUSE=your_warehouse
SNOWFLAKE_DATABASE=your_database
SNOWFLAKE_SCHEMA=your_schema
Note: Make sure your .env and credentials are secure and ignored by Git (do not push passwords to GitHub!).

4. Start Airflow
Bash
docker compose up -d
5. Open Airflow UI
Go to your browser and open:

Plaintext
http://localhost:8080
🔒 Security
✅ Secrets stored using Environment Variables

✅ .env ignored by Git

✅ No credentials committed to repository

🔮 Future Improvements
Load all 500 companies

Historical stock prices

Incremental loading

Airflow Connections

Airflow Variables

CI/CD deployment

Data Quality Checks

Email Notifications

Unit Testing

🛠️ Skills Demonstrated
✅ Data Engineering

✅ ETL Pipeline Design

✅ Apache Airflow

✅ Snowflake

✅ Docker

✅ REST APIs

✅ Pandas

✅ Workflow Automation

✅ Cloud Data Warehousing





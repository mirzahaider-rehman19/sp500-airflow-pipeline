<div align="center">

# 📊 S&P 500 ETL Pipeline

### Production Ready ETL Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=Snowflake&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

⭐ **Automated ETL Pipeline for S&P 500 Company Data using Apache Airflow & Snowflake** ⭐

</div>

---

## 📌 Overview

This project demonstrates a production-inspired ETL pipeline built using **Python**, **Apache Airflow**, **Docker**, and **Snowflake**.

**The workflow automatically:**
* Extracts S&P 500 company symbols from Wikipedia
* Retrieves company profile data from the Financial Modeling Prep API
* Cleans and transforms the dataset using Pandas
* Loads the processed data into Snowflake
* Executes automatically every **5 minutes** using Airflow Scheduler

---

## 🏗️ ETL Architecture

```text
┌──────────────────┐      ┌─────────┐      ┌─────────────────────────┐      ┌───────────┐      ┌─────────────────────┐
│ Wikipedia S&P 500│ ───> │ Extract │ ───> │ Financial Modeling Prep │ ───> │ Transform │ ───> │ Snowflake / Airflow │
└──────────────────┘      └─────────┘      └─────────────────────────┘      └───────────┘      └─────────────────────┘

## 🎯 Features

| Feature | Status |
| :--- | :---: |
| 📥 **Extract Data** | ✅ |
| 🧹 **Data Cleaning** | ✅ |
| ☁️ **Snowflake Loading** | ✅ |
| ⏰ **Airflow Scheduling** | ✅ |
| 🔄 **Automatic Retries** | ✅ |
| 🐳 **Docker Support** | ✅ |
| 🔒 **Environment Variables** | ✅ |
| 📊 **Modular ETL Design** | ✅ |

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

</div>

---

## 🧰 Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | ETL Development |
| **Apache Airflow** | Workflow Orchestration |
| **Snowflake** | Cloud Data Warehouse |
| **Docker** | Containerization |
| **Pandas** | Data Transformation |
| **Requests** | API Calls |
| **Git & GitHub** | Version Control |
## 🧰 Tech Stack


📁 Project Structure
Plaintext
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
└── .env

🔄 ETL Workflow
🔍 Extract
Read S&P 500 symbols from Wikipedia

Connect to Financial Modeling Prep API

Download company profiles

⚡ TransformConvert JSON $\rightarrow$ DataFrameSelect required columnsClean datasetRename columns

📥 Load
Connect to Snowflake

Upload transformed dataset

Store in warehouse

⏱️ Airflow DAG
Plaintext
Extract ──> Transform ──> Load

Runs automatically every: Every 5 Minutes

📊 Sample OutputSymbolCompanySectorMMM3M CompanyIndustrialsAOSA. O. SmithIndustrials

📸 Screenshots
Airflow DAG
(Insert Airflow DAG Screenshot Here)

Successful Pipeline
(Insert Pipeline Screenshot Here)

Snowflake
(Insert Snowflake Screenshot Here)

🚀 Getting Started
Clone Repository
Bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)

cd YOUR_REPOSITORY

Install Dependencies
Bash
pip install -r requirements.txt

Configure Environment Variables
Code snippet
FMP_API_KEY=YOUR_API_KEY

SNOWFLAKE_PASSWORD=YOUR_PASSWORD

Start Airflow
Bash
docker compose up -d

Open Airflow UI
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

<div align="center">

## 👨‍💻 Author

### **Mirza Haider Rehman**

🎓 **Bachelor of Software Engineering **

☁️ **Aspiring Cloud Data Engineer**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)

<br>

⭐ **If you like this project, don't forget to give it a Star!**

</div>




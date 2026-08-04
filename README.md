<div align="center">

# 📊 S&P 500 ETL Pipeline
### **Apache Airflow | Snowflake**

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
wikipedia
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

```text
Apache Airflow Scheduler
📊 FeaturesFeatureStatusExtract Data🟩Data Cleaning🟩Snowflake Loading🟩Airflow Scheduling🟩Automatic Retries🟩Docker Support🟩Environment Variables🟩Modular ETL Design🟩
Wikipedia S&P 500 ──> Extract ──> FMP API ──> Transform with Pandas ──> Snowflake ──> Apache Airflow Scheduler

🧰 Tech Stack
| Technology | Purpose |
| Python | ETL Development |
| Apache Airflow | Workflow Orchestration |
| Snowflake | Cloud Data Warehouse |
| Docker | Containerization |
| Pandas | Data Transformation |
| Requests | API Calls |
| Git & GitHub | Version Control |

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
│
├── plugins/
├── logs/
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── .gitignore
└── .env
⚡ ETL Workflow
📥 Extract
Read S&P 500 symbols from Wikipedia

Connect to Financial Modeling Prep API

Download company profiles

🔄 Transform
Convert JSON ➔ DataFrame

Select required columns

Clean dataset

Rename columns

☁️ Load
Connect to Snowflake

Upload transformed dataset

Store in warehouse

🕒 Airflow DAG
Runs automatically every: Every 5 Minutes

🚀 Getting Started
Clone Repository
Bash
git clone [https://github.com/mirzahaider-rehman19/sp500-airflow-pipeline.git](https://github.com/mirzahaider-rehman19/sp500-airflow-pipeline.git)
cd sp500-airflow-pipeline
Install Dependencies
Bash
pip install -r requirements.txt
Configure Environment Variables
Create a .env file in the root directory:

Code snippet
FMP_API_KEY=YOUR_API_KEY
SNOWFLAKE_PASSWORD=YOUR_PASSWORD
Start Airflow
Bash
docker compose up -d
Open Airflow
👉 http://localhost:8080

🔒 Security
✔️ Secrets stored using Environment Variables

✔️ .env ignored by Git

✔️ No credentials committed to repository

🔮 Future Improvements
Load all 500 companies

Historical stock prices

Incremental loading

Airflow Connections

Airflow Variables

AWS Deployment

Data Quality Checks

Email Notifications

CI/CD Pipeline

Unit Testing

🛠️ Skills Demonstrated
🟩 Data Engineering

🟩 ETL Pipeline Design

🟩 Apache Airflow

🟩 Snowflake

🟩 Docker

🟩 REST APIs

🟩 Pandas

🟩 Workflow Automation

🟩 Cloud Data Warehousing

🟩 Cloud Data Warehousing

👤 Author
Mirza Haider Rehman
💼 Aspiring Cloud Data Engineer

⭐ If you like this project, don't forget to give it a Star!

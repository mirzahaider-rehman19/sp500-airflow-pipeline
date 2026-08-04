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




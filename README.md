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

```text
Wikipedia S&P 500 ──> Extract ──> FMP API ──> Transform with Pandas ──> Snowflake ──> Apache Airflow Scheduler

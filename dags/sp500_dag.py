from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from extract import extract_sp500_data
from transform import transform_sp500_data
from load import load_to_snowflake

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def pipeline_execution():
    raw_data = extract_sp500_data()
    transformed_df = transform_sp500_data(raw_data)
    load_to_snowflake(transformed_df)

with DAG(
    'sp500_financial_pipeline',
    default_args=default_args,
    description='Scrapes S&P500 tickers, fetches FMP API metrics, loads to Snowflake',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    run_etl = PythonOperator(
        task_id='run_full_sp500_etl',
        python_callable=pipeline_execution,
    )

    run_etl
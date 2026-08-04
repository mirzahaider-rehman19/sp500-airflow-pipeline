import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from config import SNOWFLAKE_CONFIG

def load_to_snowflake(df, table_name="SP500_COMPANIES"):
    """Loads transformed Pandas DataFrame directly into Snowflake Data Warehouse."""
    if df.empty:
        print("DataFrame is empty. Skipping load process.")
        return
        
    print("Connecting to Snowflake...")
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG["user"],
        password=SNOWFLAKE_CONFIG["password"],
        account=SNOWFLAKE_CONFIG["account"],
        warehouse=SNOWFLAKE_CONFIG["warehouse"],
        database=SNOWFLAKE_CONFIG["database"],
        schema=SNOWFLAKE_CONFIG["schema"]
    )
    
    try:
        cursor = conn.cursor()
        
        # Ensure Database and Schema exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {SNOWFLAKE_CONFIG['database']};")
        cursor.execute(f"USE DATABASE {SNOWFLAKE_CONFIG['database']};")
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {SNOWFLAKE_CONFIG['schema']};")
        cursor.execute(f"USE SCHEMA {SNOWFLAKE_CONFIG['schema']};")
        
        # Write DataFrame to Snowflake table
        success, nchunks, nrows, _ = write_pandas(
            conn=conn,
            df=df,
            table_name=table_name,
            auto_create_table=True,
            overwrite=True
        )
        print(f"Successfully loaded {nrows} rows into Snowflake table '{table_name}'.")
        
    finally:
        conn.close()
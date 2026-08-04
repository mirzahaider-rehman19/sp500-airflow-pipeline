import pandas as pd

def transform_sp500_data(raw_profiles):
    """Cleans raw profile JSON data into a formatted Pandas DataFrame."""
    if not raw_profiles:
        print("No raw data provided for transformation.")
        return pd.DataFrame()
        
    df = pd.DataFrame(raw_profiles)
    
    # Select key financial columns
    selected_columns = [
        "symbol", "price", "beta", "volAvg", "mktCap", 
        "lastDiv", "range", "changes", "companyName", 
        "currency", "industry", "website", "description", "ceo", "sector"
    ]
    
    available_columns = [col for col in selected_columns if col in df.columns]
    df = df[available_columns]
    
    # Upper-case column names for Snowflake standard compatibility
    df.columns = [col.upper() for col in df.columns]
    
    # Basic data cleaning
    df["PRICE"] = df["PRICE"].fillna(0.0)
    df["MKTCAP"] = df["MKTCAP"].fillna(0)
    
    print(f"Transformed Data Shape: {df.shape}")
    return df
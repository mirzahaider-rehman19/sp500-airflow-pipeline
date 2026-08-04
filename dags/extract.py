import requests
import pandas as pd
from io import StringIO
from config import API_KEY

def extract_sp500_data():
    """Scrapes S&P 500 tickers from Wikipedia and fetches profile data via FMP API."""
    print("Scraping S&P 500 tickers from Wikipedia...")
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    html = StringIO(response.text)
    tables = pd.read_html(html)
    sp500_df = tables[0]
    
    # Selecting the first 5 symbols for demonstration/testing
    symbols = sp500_df["Symbol"].head(5).tolist()
    print(f"Fetched Symbols: {symbols}")
    
    profiles = []
    for symbol in symbols:
        api_url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={API_KEY}"
        res = requests.get(api_url)
        if res.status_code == 200:
            data = res.json()
            if isinstance(data, list) and len(data) > 0:
                profiles.append(data[0])
                print(f"Extracted data for {symbol}")
            else:
                print(f"No profile found for {symbol}")
        else:
            print(f"Failed API request for {symbol}: {res.status_code}")
            
    return profiles

if __name__ == "__main__":
    result = extract_sp500_data()
    print(f"Extracted {len(result)} profiles total.")
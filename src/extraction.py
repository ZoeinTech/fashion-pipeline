import requests
import json
from pathlib import Path
from datetime import date

url = "https://dummyjson.com/products?limit=0"
raw_data = Path("data/raw")


def extract():
    snapshot_date = date.today().isoformat()
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.Tiemout:
        print("Request timed out. Please try again later.")
        exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        exit(2)
    except requests.exceptions.RequestException as e:
        print(f"Request error occurred: {e}")
        exit(3)
        
    data = response.json()
    

    raw_data.mkdir(parents=True, exist_ok=True)
    path = raw_data / f"products_{snapshot_date}.json"
    path.write_text(json.dumps(data))

    print(f"Data extracted and saved to {path}")

if __name__ == "__main__":
    extract()
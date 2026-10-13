import requests
import json
from pathlib import Path
from datetime import date

url = "https://dummyjson.com/products?limit=0"
raw_data = Path("data/raw")


def extract():
    snapshot_date = date.today().isoformat()
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()

    raw_data.mkdir(parents=True, exist_ok=True)
    path = raw_data / f"products_{snapshot_date}.json"
    path.write_text(json.dumps(data))

    print(f"Data extracted and saved to {path}")

if __name__ == "__main__":
    extract()
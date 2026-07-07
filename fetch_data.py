import requests
import pandas as pd
from datetime import date

response = requests.get("https://api.frankfurter.app/latest?from=USD&to=TRY,EUR")
data = response.json()

today = date.today().isoformat()
row = {
    "date": today,
    "usd_try": data["rates"]["TRY"],
    "usd_eur": data["rates"]["EUR"]
}

try:
    df = pd.read_csv("kur_verisi.csv")
    df = df[df["date"] != today]  # bugune ait eski kaydi sil (varsa)
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
except FileNotFoundError:
    df = pd.DataFrame([row])

df.to_csv("kur_verisi.csv", index=False)
print(f"{today} tarihli veri guncellendi:", row)

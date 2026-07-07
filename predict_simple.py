import pandas as pd

df = pd.read_csv("kur_verisi.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

print("=== Basit Tahmin (Moving Average) ===\n")

window = min(3, len(df))  # veri azsa mevcut kadarini kullan

for col, label in [("usd_try", "USD/TRY"), ("usd_eur", "USD/EUR")]:
    ma = df[col].tail(window).mean()
    son_deger = df[col].iloc[-1]
    print(f"--- {label} ---")
    print(f"Son deger: {son_deger:.4f}")
    print(f"Son {window} gunun ortalamasi (tahmin): {ma:.4f}")
    print()

print(f"Not: Sadece {len(df)} veri noktasi var, tahmin guvenilirligi veri arttikca artacak.")

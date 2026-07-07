import pandas as pd

df = pd.read_csv("kur_verisi.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

print("=== Doviz Kuru Istatistikleri ===\n")

for col, label in [("usd_try", "USD/TRY"), ("usd_eur", "USD/EUR")]:
    print(f"--- {label} ---")
    print(f"Ortalama: {df[col].mean():.4f}")
    print(f"En dusuk: {df[col].min():.4f}")
    print(f"En yuksek: {df[col].max():.4f}")

    if len(df) > 1:
        degisim = df[col].iloc[-1] - df[col].iloc[-2]
        yuzde = (degisim / df[col].iloc[-2]) * 100
        print(f"Son gunluk degisim: {degisim:+.4f} ({yuzde:+.2f}%)")
    else:
        print("Gunluk degisim icin en az 2 veri noktasi gerekli.")
    print()

df.to_csv("istatistikler_ozet.csv", index=False)

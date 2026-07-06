import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("kur_verisi.csv")
df["date"] = pd.to_datetime(df["date"])

plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["usd_try"], marker="o", label="USD/TRY")
plt.plot(df["date"], df["usd_eur"], marker="o", label="USD/EUR")
plt.title("Doviz Kuru Takibi")
plt.xlabel("Tarih")
plt.ylabel("Kur Degeri")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("kur_grafigi.png")
plt.show()
print("Grafik kaydedildi: kur_grafigi.png")

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("kur_verisi.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8), sharex=True)
fig.patch.set_facecolor("white")

def style_axis(ax, dates, values, color, label):
    ax.plot(dates, values, color=color, linewidth=2.2, marker="o", markersize=4, zorder=3)
    ax.fill_between(dates, values, values.min() - (values.max()-values.min())*0.1, 
                     color=color, alpha=0.12, zorder=2)
    padding = (values.max() - values.min()) * 0.25 if values.max() != values.min() else values.max()*0.01
    ax.set_ylim(values.min() - padding, values.max() + padding)
    ax.set_ylabel(label, fontsize=11, fontweight="bold")
    ax.grid(True, alpha=0.25, linestyle="--")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_facecolor("#fafafa")

style_axis(ax1, df["date"], df["usd_try"], "#2563eb", "USD/TRY")
style_axis(ax2, df["date"], df["usd_eur"], "#ea580c", "USD/EUR")

ax2.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
fig.autofmt_xdate(rotation=30)

fig.suptitle("Doviz Kuru Takibi", fontsize=15, fontweight="bold", y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("kur_grafigi.png", dpi=150)
plt.show()
print("Grafik kaydedildi: kur_grafigi.png")
##
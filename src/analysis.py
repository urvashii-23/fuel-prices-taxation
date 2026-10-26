import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/eu_pump_prices.csv")
data = data.dropna(subset=["petrol_eur_per_l"])
data = data.sort_values("petrol_eur_per_l")

plt.barh(data["country"], data["petrol_eur_per_l"])
plt.xlabel("Petrol price, EUR per litre (12 Oct 2026)")
plt.title("Petrol prices in the EU")
plt.tight_layout()
plt.savefig("outputs/petrol_price.png")
print("Graph saved")

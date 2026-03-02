import pandas as pd

# 1. Load the synthetic trade data
df = pd.read_csv("tradedemo.csv")  # updated name

print("Toy trade data:")
print(df)

print("\nTrade by partner (importer and trade_flow):")
print(df[["importer", "trade_flow"]])

corr_gdp = df["importer_gdp"].corr(df["trade_flow"])
corr_dist = df["distance_km"].corr(df["trade_flow"])

print(f"\nCorrelation between partner GDP and trade_flow: {corr_gdp:.2f}")
print(f"Correlation between distance and trade_flow: {corr_dist:.2f}")

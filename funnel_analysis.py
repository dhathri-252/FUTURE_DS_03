import pandas as pd

# Load dataset
df = pd.read_csv("../data/marketing_funnel.csv")

# Show dataset
print(df)

# Calculate conversion rate
df["ConversionRate"] = (df["Conversions"] / df["Visitors"]) * 100

print("\nConversion Rates:")
print(df[["Channel", "ConversionRate"]])

# Best channel
best_channel = df.loc[df["ConversionRate"].idxmax()]

print("\nBest Performing Channel:")
print(best_channel)
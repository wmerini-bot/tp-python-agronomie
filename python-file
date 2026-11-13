
import pandas as pd

# Read agricultural data
data = pd.read_csv("data/crop_data.csv")

# Display the dataset
print("AGRICULTURAL DATA")
print(data)

# Calculate average production
average_production = data["Production_t"].mean()

# Calculate total production
total_production = data["Production_t"].sum()

# Calculate productivity (tons per hectare)
data["Yield_t_ha"] = data["Production_t"] / data["Area_ha"]

# Find the crop with the highest productivity
best_crop = data.loc[data["Yield_t_ha"].idxmax(), "Crop"]

# Display analysis results
print("\n--- ANALYSIS RESULTS ---")
print("Total production:", total_production, "tons")
print("Average production:", average_production, "tons")
print("Highest productivity crop:", best_crop)

print("\nProductivity by crop:")
print(data[["Crop", "Yield_t_ha"]])

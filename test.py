import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Calculs avec NumPy
data = np.array([10, 20, 30, 40, 50])
print("Moyenne :", data.mean())
print("Écart-type :", data.std())

# 2. Structure DataFrame avec Pandas
df = pd.DataFrame({
    'Âge': [23, 45, 31, 22, 34],
    'Taille': [1.70, 1.85, 1.60, 1.75, 1.80]
})
print(df.describe())

# 3. Visualisation avec Matplotlib
plt.figure()
plt.scatter(df['Âge'], df['Taille'])
plt.title("Relation Âge - Taille")
plt.xlabel("Âge")
plt.ylabel("Taille (m)")
plt.grid(True)
plt.show()

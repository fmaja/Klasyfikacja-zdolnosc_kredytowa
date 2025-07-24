import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('data', delim_whitespace=True, header=None)

kolumny_cech = list(df.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16]])
X = df[kolumny_cech]

y = df.iloc[:, -1]
y = (y == 2).astype(int)

if y.dtype == 'object':
    y = pd.factorize(y)[0]

X = sm.add_constant(X)

# Logit
model = sm.Logit(y, X)
wynik = model.fit()

# Podsumowanie
print(wynik.summary())

# Współczynniki + p-value
wspolczynniki = wynik.params[1:]  # bez interceptu
p_values = wynik.pvalues[1:]

# Wykres
nazwy_cech = [f'A{i+1}' for i in range(len(wspolczynniki))]

plt.figure(figsize=(10, 6))
sns.barplot(x=wspolczynniki.values, y=nazwy_cech, palette="viridis")
plt.title("Wartości współczynników regresji logistycznej")
plt.axvline(0, color='red', linestyle='--')

for i, (coef, pval) in enumerate(zip(wspolczynniki.values, p_values.values)):
    plt.text(coef, i, f'', va='center',
             color='white' if abs(coef) > 0.1 else 'black',
             fontweight='bold')

plt.tight_layout()
plt.show()

print("\nP-value poszczególnych cech:")
print(p_values.sort_values())

# Top 3
top3 = p_values.sort_values().head(3)
print("\nTop 3 najbardziej istotne cechy wg p-value:")
for cecha, p in top3.items():
    coef_val = wspolczynniki[cecha]
    print(f"{nazwy_cech[cecha]}: współczynnik = {coef_val:.3f}, p-value = {p:.5f}")


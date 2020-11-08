import pandas as pd

matrix = pd.read_excel('Dataset.xlsx') # inicializa matriz com valores do Dataset.xlsx


print("\nResultados de Covid:\n")
print(matrix["SARS-Cov-2 exam result"].value_counts())
print()
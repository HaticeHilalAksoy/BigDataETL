import pandas as pd

# Dosya yolları
imports_file = "animal-fat-imports.csv"
exports_file = "animal-fat-exports.csv"


# Verileri yükleme
imports_data = pd.read_csv(imports_file)
exports_data = pd.read_csv(exports_file)

# İlk 5 satırı inceleme
print("Imports Data:")
print(imports_data.head())
print(imports_data.info())

print("\nExports Data:")
print(exports_data.head())
print(exports_data.info())

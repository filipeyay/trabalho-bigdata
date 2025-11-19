# Microatividade 1
import pandas as pd

df_original = pd.read_csv('dados.csv', sep=';', engine='python')

print("Microatividade 1: Leitura do CSV")
print(df_original)

# Microatividade 2

df_subconjunto = df_original[['ID', 'Duration', 'Calories']]

print("\nMicroatividade 2: Criação de Subconjuntos")
print(df_subconjunto)

# Microatividade 3

pd.set_option('display.max_rows', 9999)

print("\nMicroatividade 3: Configuração de Max Rows")
print(df_original.to_string())

# Microatividade 4

print("\nMicroatividade 4: Primeiras 10 linhas (head)")
print(df_original.head(10))

print("\nMicroatividade 4: Primeiras 10 linhas (tail)")
print(df_original.tail(10))

print("\nMicroatividade 5: Informações Gerais")
df_original.info()

import openpyxl
from datetime import datetime

# Pedindo ao usuário um nome para o arquivo
nome_base = input("Digite um nome para o arquivo: ")

# Removendo espaços extras e substitui caracteres problemáticos se quiser

# Exemplo o espaço, " ", por underline, "_" com o replace. Replace faz isso
nome_base = nome_base.strip().replace(" ", "_")  # opcional: substitui espaços por _

# Adiciona a extensão
nome_arquivo = f"{nome_base}.xlsx"

# Cria um workbook e salva com esse nome
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet["A1"] = "Exemplo de dados"
workbook.save(nome_arquivo)

print(f"Arquivo salvo como: {nome_arquivo}")

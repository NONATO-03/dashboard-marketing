import pandas as pd
import numpy as np
from pathlib import Path

# ----------------------------------------------------------------------
# 1. Leitura do Arquivo Original com o caminho correto
# ----------------------------------------------------------------------
delimiter = ';'  # Usando ponto e vírgula conforme o snippet

# Constroi caminho absoluto relativo ao arquivo atual (mais robusto que caminhos relativos ao CWD)
data_file = Path(__file__).resolve().parent / 'dados' / 'marketing_campaign.csv'
file_path = data_file  # variável preservada para compatibilidade

if not data_file.exists():
    dados_dir = data_file.parent
    candidates = list(dados_dir.glob('*')) if dados_dir.exists() else []
    print(f"ERRO: Arquivo não encontrado: {data_file}")
    if candidates:
        print("Arquivos encontrados em 'dados/':")
        for p in candidates:
            print(" -", p.name)
    else:
        print("Diretório 'dados' está vazio ou não existe. Verifique a estrutura do projeto.")
    raise FileNotFoundError(f"Arquivo não encontrado: {data_file}")

try:
    df = pd.read_csv(data_file, sep=delimiter)
    print(f"Arquivo lido com sucesso. Total de linhas: {df.shape[0]}")
except Exception as e:
    print(f"Falha ao ler CSV: {e}")
    raise

# ----------------------------------------------------------------------
# 2. Criação dos Arquivos Similares a Tabelas de Banco de Dados (Simulação de Fontes)
# ----------------------------------------------------------------------

# Tabela 1: Dimensão do Cliente (Dim_Cliente) - Dados estáticos do cliente
dim_cliente = df[['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Income', 
                  'Kidhome', 'Teenhome', 'Dt_Customer', 'Complain']].copy()
dim_cliente.to_csv('Dim_Cliente.csv', index=False)
print("Arquivo 'Dim_Cliente.csv' criado (Simula tabela CRM/Cadastro).")

# Tabela 2: Fato de Compras (Fact_Compras) - O que gastaram
fact_compras = df[['ID', 'MntWines', 'MntFruits', 'MntMeatProducts', 
                   'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].copy()
fact_compras.to_csv('Fact_Compras.csv', index=False)
print("Arquivo 'Fact_Compras.csv' criado (Simula tabela de Vendas/Gastos).")

# Tabela 3: Fato de Comportamento/Campanhas (Fact_Comportamento) - Como se comportaram
fact_comportamento = df[['ID', 'Recency', 'NumDealsPurchases', 'NumWebPurchases', 
                         'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth', 
                         'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 
                         'AcceptedCmp2', 'Response']].copy()
fact_comportamento.to_csv('Fact_Comportamento.csv', index=False)
print("Arquivo 'Fact_Comportamento.csv' criado (Simula tabela de Web/Campanhas).")

# ----------------------------------------------------------------------
# Fase 1 Concluída!
# ----------------------------------------------------------------------
print("\n[Fase 1 - Extração] CONCLUÍDA com sucesso.")
print("Os 3 CSVs simulados foram criados e estão prontos para a etapa de Transformação (SQL) e Mineração (Python).")
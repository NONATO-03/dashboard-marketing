# Dashboard Marketing

Repositório com scripts e notebooks para análise de campanhas de marketing e segmentação de clientes.

## Conteúdo

- `divisao.py`: script de extração que lê o arquivo de dados e gera arquivos CSV que simulam tabelas (Dim_Cliente, Fact_Compras, Fact_Comportamento).
- `notebook/analise_segmentacao_rfm`: script/notebook com pipeline de limpeza, engenharia de features e clusterização RFM (gera `output/analise_marketing_final.csv` ou `.xlsx`).
- `dados/marketing_campaign.csv`: arquivo de dados original 

## Requisitos

Recomendo criar um ambiente virtual e instalar as dependências abaixo.

Requisitos principais:

```
python (>=3.10)
pandas
numpy
scikit-learn
openpyxl  # opcional, necessário para salvar .xlsx
```

Instalação rápida (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Como executar

1. Garanta que o arquivo `dados/marketing_campaign.csv` esteja presente no diretório `dados/` (ele é lido automaticamente).
2. Para rodar o pipeline de extração:

```powershell
python .\divisao.py
```

3. Para rodar a análise e segmentação (RFM):

```powershell
python .\notebook\analise_segmentacao_rfm
```

Ao final, o resultado é salvo em `output/analise_marketing_final.csv` por padrão. Se `openpyxl` estiver instalado, o script tentará salvar em `.xlsx`.

---
Feito por: Vitor Nonato

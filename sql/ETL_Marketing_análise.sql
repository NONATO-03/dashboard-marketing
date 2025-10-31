
-- Simulação
-- Script SQL para ETL 
-- Tabela Analítica (Star Schema)  
-- Aqui, simulamos que essas 3 tabelas já foram carregadas.

-- Criação da Tabela Analítica 
-- Esta tabela será a base para a mineração e visualização de dados.

CREATE VIEW IF NOT EXISTS Tabela_Analitica_Marketing AS
SELECT
    -- Colunas de Dimensão do Cliente (Dim_Cliente)
    c.ID,
    c.Year_Birth,
    c.Education,
    c.Marital_Status,
    c.Income,
    c.Kidhome,
    c.Teenhome,
    c.Dt_Customer,
    c.Complain,
    
    -- Colunas de Fato Gastos (Fact_Compras)
    co.MntWines,
    co.MntFruits,
    co.MntMeatProducts,
    co.MntFishProducts,
    co.MntSweetProducts,
    co.MntGoldProds,
    
    -- Colunas de Fato: Comportamento (Fact_Comportamento)
    b.Recency,
    b.NumDealsPurchases,
    b.NumWebPurchases,
    b.NumCatalogPurchases,
    b.NumStorePurchases,
    b.NumWebVisitsMonth,
    
    -- Colunas de Fato: Campanhas (Target)
    b.AcceptedCmp1,
    b.AcceptedCmp2,
    b.AcceptedCmp3,
    b.AcceptedCmp4,
    b.AcceptedCmp5,
    b.Response, -- Coluna alvo para o modelo 

    -- EXEMPLO DE TRANSFORMAÇÃO em SQL
    -- Criação de um KPI simples: Gasto Total

    (co.MntWines + co.MntFruits + co.MntMeatProducts + co.MntFishProducts + co.MntSweetProducts + co.MntGoldProds) AS Total_Gasto
    
FROM Dim_Cliente c
-- JOIN as tabelas usando a chave 'ID'
LEFT JOIN Fact_Compras co ON c.ID = co.ID
LEFT JOIN Fact_Comportamento b ON c.ID = b.ID;

-- Consulta de Verificação 
SELECT * FROM Tabela_Analitica_Marketing LIMIT 10;
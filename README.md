
# Dashboard de Detecção de Falhas - Bootcamp CDIA - Mauricio Pinheiro

Este projeto apresenta um painel interativo desenvolvido com Streamlit, mostrando os resultados de um modelo de classificação multi-rótulo aplicado à detecção de falhas em chapas de aço inoxidável.

## Objetivo
Detectar até 7 categorias de falhas com base em dados como espessura, temperatura e peso das chapas.

## Como rodar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Bootcamp_CDIA.git
cd Bootcamp_CDIA
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode o app Streamlit:
```bash
streamlit run dashboard.py
```

## Arquivos

- `dashboard.py`: script principal do app
- `metricas_por_classe.csv`: dados com métricas de desempenho por classe
- `requirements.txt`: bibliotecas necessárias

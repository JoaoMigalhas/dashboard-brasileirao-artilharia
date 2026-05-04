# ⚽ Brasileirão 2025 — Dashboard de Estatísticas

Dashboard interativo com estatísticas dos artilheiros do Brasileirão 2026, desenvolvido em **Python + Streamlit** e **Power BI**, com dados consumidos em tempo real via API.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem principal |
| Requests | Consumo da API |
| Pandas | Tratamento e transformação dos dados |
| Streamlit | Dashboard interativo web |
| Plotly | Gráficos interativos |
| Power BI | Dashboard para análise de negócios |
| football-data.org | Fonte dos dados (API oficial) |

---

## 📁 Estrutura do projeto

```
brasileirao-dashboard/
├── python/
│   ├── app.py               # Dashboard Streamlit
│   ├── teste_api.py         # Script de coleta de dados via API
|   |── dash.pbix.zip        # Dashboard do powerbi zipado      
│   ├── data/
│   │   └── jogadores.csv    # Dados gerados pela API
|   |
|   |
│   └── requirements.txt     # Dependências Python
└── README.md
```

---

## 🚀 Como executar o projeto Python

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/brasileirao-dashboard.git
cd brasileirao-dashboard/python
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure sua API Key
Crie um arquivo `.env` na pasta `python/`:
```
API_KEY=sua_chave_aqui
```
> Obtenha sua chave gratuita em [football-data.org](https://www.football-data.org/)

### 4. Colete os dados
```bash
python teste_api.py
```

### 5. Rode o dashboard
```bash
streamlit run app.py
```
Acesse em `http://localhost:8501`

---

## 📊 Power BI

O arquivo `dash.pbix` pode ser aberto diretamente no **Power BI Desktop**.

Os dados são importados do arquivo `data/jogadores.csv` gerado pelo script Python.

Para atualizar os dados:
1. Rode o `teste_api.py` para gerar um CSV atualizado
2. No Power BI clique em **Atualizar**

---

## 📈 Funcionalidades

- ✅ Ranking de artilheiros com gols e assistências
- ✅ Filtro por time
- ✅ Gráfico de barras — gols por jogador
- ✅ Gráfico de dispersão — gols x assistências
- ✅ Cards com totais (jogadores, gols, assistências)
- ✅ Tabela completa dos dados

---

## 🔌 API utilizada

**football-data.org** — API gratuita com dados de competições de futebol.

- Endpoint utilizado: `GET /v4/competitions/BSA/scorers`
- Competição: Brasileirão Série A (`BSA`)
- Autenticação: Header `X-Auth-Token`

---

## 👨‍💻 Autor

**João Miguel Santos**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](www.linkedin.com/in/joão-miguel-santos-51a401297)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/JoaoMigalhas)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
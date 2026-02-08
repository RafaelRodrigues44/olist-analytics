# 📊 Olist E-Commerce Analytics Dashboard

Este projeto é uma solução completa de Business Intelligence (BI) para análise de dados do E-commerce Olist. A aplicação foi construída utilizando **Python**, **Streamlit** e **PostgreSQL** (via Supabase), seguindo uma arquitetura modular para garantir escalabilidade e fácil manutenção.

## 🏗️ Arquitetura e Design Patterns

O projeto adota uma **Arquitetura em Camadas (Layered Architecture)**, separando claramente as responsabilidades de extração de dados, regras de negócio e interface do usuário. Essa abordagem facilita a manutenção e permite que diferentes partes do sistema evoluam independentemente.

### Estrutura Modular 

* **ETL Layer (`etl/`)**: Responsável pela conexão com o banco de dados (Repository Pattern), execução de queries SQL e limpeza inicial dos dados. Nenhuma lógica visual reside aqui.
* **UI Layer (`ui/`)**: Contém componentes visuais, gráficos (Plotly) e estilos CSS. Esta camada é "burra", apenas recebe dados e os desenha.
* **Orchestrator (`app.py`)**: O ponto de entrada. Ele solicita os dados ao ETL, aplica filtros de usuário e decide qual componente da UI deve ser renderizado.

```mermaid
graph TD
    subgraph "Data Source (Local)"
        RAW[db.Olist / CSVs]
    end

    subgraph "ETL Pipeline"
        PY[upload_olist.py]
    end

    subgraph "Data Warehouse (Cloud)"
        DW[(Supabase PostgreSQL)]
    end

    subgraph "Application Layer"
        APP[app.py - Controller]
        ETL[etl/ - Repository]
        UI[ui/ - Visual Components]
    end

    subgraph "User Interface"
        ST[Streamlit Dashboard]
    end

    RAW --> PY
    PY -->|Upload| DW
    DW -->|Query| ETL
    ETL -->|Dataframes| APP
    APP -->|Processamento| UI
    UI -->|Renderização| ST
```

## 📂 Estrutura de pastas

```text
Olist-Analytics/
├── database/
│   ├── db.Olist                 # Fonte de dados bruta (SQLite ou Arquivos)
│   └── pipelines/
│       └── upload_olist.py      # Script de carga para o Data Warehouse
├── etl/
│   ├── __init__.py
│   ├── database.py              # Gerenciador de conexão SQLAlchemy
│   ├── repository.py            # Queries e acesso a dados
│   └── utils.py                 # Funções auxiliares
├── ui/
│   ├── __init__.py
│   ├── charts.py                # Geração de gráficos Plotly
│   ├── maps.py                  # Mapas coropléticos
│   ├── components.py            # Cards e KPIs
│   └── styles.py                # CSS customizado
├── .env                         # Variáveis de ambiente (NÃO COMITAR)
├── .gitignore
├── app.py                       # Orquestrador da aplicação
├── requirements.txt             # Dependências
└── README.md
```

## 🚀 Como Rodar o Projeto

Siga o passo a passo abaixo para configurar o ambiente do zero.

Pré-requisitos:

* Python 3.10+
* Git
* Conta no [Supabase](https://supabase.com/) (ou qualquer banco PostgreSQL).

### 1.📥 Obtendo os Dados

Este projeto utiliza o Brazilian E-Commerce Public Dataset by Olist.

    Baixe os dados oficiais no Kaggle  - https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

    Extraia os arquivos CSV.

    Coloque-os dentro da pasta database/.


### 2. Configurando o Data Warehouse (Supabase)

1.  Crie um novo projeto no Supabase.
2.  Vá em **Project Settings** > **Database** > **Connection string**.
3.  Copie a URL de conexão (selecione a opção "URI").
4.  A string terá este formato: `postgresql://postgres:[SUA-SENHA]@[HOST]:5432/postgres`

### 3. Configuração do Ambiente Local

Clone o repositório e navegue até a pasta:

```bash
git clone https://github.com/RafaelRodrigues44/olist-analytics.git
cd olist-analytics
```

Crie e ative o ambiente virtual (`.venv`):

**Para Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Para Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

### 4. Configurando Variáveis de Ambiente (.env)

Crie um arquivo chamado `.env` na raiz do projeto. Este arquivo guardará suas credenciais de forma segura.

**Conteúdo do `.env`:**

```ini
# Exemplo de configuração (Atenção: Caracteres especiais na senha devem ser URL Encoded)
# Se sua senha tem '@', use '%40'. Se tem '#', use '%23'.

DATABASE_URL="postgresql://postgres:SuaSenhaSegura%40123@db.pvmcbtkbsyzqyyrvkbxa.supabase.co:5432/postgres"
```

> **Nota de Segurança:** O arquivo `.env` já está no `.gitignore` para evitar que suas senhas subam para o GitHub.

### 5. Executando o Pipeline de Dados (ETL)

Antes de abrir o dashboard, precisamos enviar os dados locais (`database/db.Olist`) para a nuvem (Supabase).

Execute o script de pipeline:

```bash
python database/pipelines/upload_olist.py
```

*Este script irá ler os dados locais, conectar no Supabase usando a `DATABASE_URL` do `.env` e criar as tabelas necessárias.*

### 6. Executando o Dashboard

Com o banco de dados populado, inicie a aplicação Streamlit:

```bash
streamlit run app.py
```

O dashboard abrirá automaticamente no seu navegador em `http://localhost:8501`.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.14
* **Frontend:** Streamlit
* **Visualização:** Plotly Express
* **Banco de Dados:** PostgreSQL (Supabase)
* **ORM/Conexão:** SQLAlchemy & Pandas
* **Design:** CSS Customizado & Layout Responsivo

## 📞 Contato

Rafael - https://www.linkedin.com/in/rafael-rodrigues-ab2a981b5/ - rafael.rodrigues85@hotmail.com

*Desenvolvido como parte do portfólio de Engenharia de Dados e Fullstack Development.*
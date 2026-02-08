import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
import os
from dotenv import load_dotenv

# Carrega a senha do banco do arquivo .env
load_dotenv()
DB_URL = os.getenv("DATABASE_URL")

# Caminho da pasta onde estão os CSVs (ajuste se necessário)
DATA_FOLDER = '../db.Olist' 

def upload_data():
    if not DB_URL:
        print("ERRO: Variável DATABASE_URL não encontrada no .env")
        return

    print("Conectando ao Supabase...")
    engine = create_engine(DB_URL)

    # Dicionário mapeando Nome do Arquivo -> Nome da Tabela no Banco
    files_map = {
        'olist_orders_dataset.csv': 'orders',
        'olist_order_items_dataset.csv': 'order_items',
        'olist_products_dataset.csv': 'products',
        'olist_customers_dataset.csv': 'customers',
        'olist_sellers_dataset.csv': 'sellers',
        'olist_order_payments_dataset.csv': 'payments',
        'olist_order_reviews_dataset.csv': 'reviews',
        'olist_geolocation_dataset.csv': 'geolocation',
        'product_category_name_translation.csv': 'category_translation'
    }

    # Colunas que PRECISAM ser convertidas para data (datetime)
    date_columns = [
        'order_purchase_timestamp', 
        'order_approved_at', 
        'order_delivered_carrier_date', 
        'order_delivered_customer_date', 
        'order_estimated_delivery_date',
        'shipping_limit_date',
        'review_creation_date',
        'review_answer_timestamp'
    ]

    for csv_file, table_name in files_map.items():
        file_path = os.path.join(DATA_FOLDER, csv_file)
        
        if os.path.exists(file_path):
            print(f"Lendo {csv_file}...")
            df = pd.read_csv(file_path)

            # Conversão automática de colunas de data
            for col in df.columns:
                if col in date_columns:
                    df[col] = pd.to_datetime(df[col], errors='coerce')
            
            print(f"Enviando {len(df)} linhas para a tabela '{table_name}'...")
            
            # chunksize=1000 envia de mil em mil para não travar a conexão
            df.to_sql(table_name, engine, if_exists='replace', index=False, chunksize=1000)
            print(f"✅ Tabela '{table_name}' carregada com sucesso!")
        else:
            print(f"⚠️ Arquivo {csv_file} não encontrado na pasta {DATA_FOLDER}")

    print("\n--- Processo Finalizado ---")
    print("Todos os dados estão no Supabase prontos para análise SQL.")

if __name__ == "__main__":
    upload_data()
import pandas as pd
import streamlit as st
from urllib.request import urlopen
import json
from .database import get_db_engine, DB_URL
from .utils import normalize_text, ESTADOS_IBGE

@st.cache_data(ttl=3600)
def get_data():
    engine = get_db_engine()
    if not engine: return pd.DataFrame()
    
    query = "SELECT * FROM vw_analise_vendas;"
    try:
        df = pd.read_sql(query, engine)
        df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
        df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
        df['cidade_norm'] = df['cidade_cliente'].apply(normalize_text)
        return df
    except Exception as e:
        st.error(f"Erro ao conectar no banco: {e}")
        return pd.DataFrame()

@st.cache_data(ttl=3600)
def get_payment_data():
    engine = get_db_engine()
    if not engine: return pd.DataFrame()
    
    query = """
    SELECT payment_type, count(order_id) as qtd_pedidos
    FROM payments GROUP BY payment_type ORDER BY qtd_pedidos DESC;
    """
    try:
        return pd.read_sql(query, engine)
    except Exception:
        return pd.DataFrame()

@st.cache_data(ttl=3600)
def get_logistics_data():
    engine = get_db_engine()
    if not engine: return pd.DataFrame()
    
    query = """
    SELECT oi.freight_value, oi.price, p.product_category_name, p.product_weight_g,
           c.customer_state, s.seller_state
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    JOIN orders o ON oi.order_id = o.order_id
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN sellers s ON oi.seller_id = s.seller_id
    WHERE o.order_status = 'delivered' LIMIT 50000;
    """
    try:
        return pd.read_sql(query, engine)
    except Exception:
        return pd.DataFrame()

@st.cache_data(ttl=3600)
def get_geojson_state(uf):
    ibge_code = ESTADOS_IBGE.get(uf)
    if not ibge_code: return None
    
    url = f"https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-{ibge_code}-mun.json"
    try:
        with urlopen(url) as response:
            geojson = json.load(response)
        for feature in geojson['features']:
            feature['properties']['id_norm'] = normalize_text(feature['properties']['name'])
        return geojson
    except Exception:
        return None

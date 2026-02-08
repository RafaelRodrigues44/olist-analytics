import streamlit as st
import pandas as pd
from etl.repository import get_data, get_payment_data, get_logistics_data, get_geojson_state
from etl.utils import format_br, normalize_text
from ui.styles import CSS
from ui.components import kpi_card
from ui.charts import (
    plot_financial_evolution, plot_payment_types, plot_top_states_revenue,
    plot_delivery_status, plot_delay_distribution, plot_delay_rate_evolution,
    plot_delay_ranking_by_state, plot_top_categories_revenue,
    plot_top_categories_volume, plot_freight_weight_relationship,
    plot_freight_efficiency
)
from ui.maps import plot_generic_choropleth

st.set_page_config(page_title="Olist Analytics", layout="wide", page_icon="🇧🇷")
st.markdown(CSS, unsafe_allow_html=True)

df_raw = get_data()

if df_raw.empty:
    st.stop()

st.title("📊 Olist E-Commerce Dashboard")

with st.expander("🎛️ Filtros de Análise", expanded=True):
    col_filtro1, col_filtro2 = st.columns(2)
    
    with col_filtro1:
        min_date = df_raw['order_purchase_timestamp'].min()
        max_date = df_raw['order_purchase_timestamp'].max()
        
        date_range = st.date_input(
            "Período de Análise",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )
        
    with col_filtro2:
        all_states = sorted(df_raw['estado_cliente'].unique())
        selected_states = st.multiselect(
            "Filtrar Estados", 
            all_states
        )

mask = (
    (df_raw['order_purchase_timestamp'].dt.date >= date_range[0]) &
    (df_raw['order_purchase_timestamp'].dt.date <= date_range[1])
)

if selected_states:
    mask = mask & (df_raw['estado_cliente'].isin(selected_states))

df = df_raw.loc[mask]

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(kpi_card("Receita Total", format_br(df['valor_venda'].sum())), unsafe_allow_html=True)

with col2:
    st.markdown(kpi_card("Total Pedidos", df['order_id'].nunique()), unsafe_allow_html=True)

with col3:
    ticket = df['valor_venda'].sum() / df['order_id'].nunique() if df['order_id'].nunique() > 0 else 0
    st.markdown(kpi_card("Ticket Médio", format_br(ticket)), unsafe_allow_html=True)

with col4:
    st.markdown(kpi_card("Frete Médio", format_br(df['valor_frete'].mean())), unsafe_allow_html=True)

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["💰 Visão Financeira", "⏱️ Performance de Prazos", "📦 Produtos", "🚚 Raio-X Logístico"])

with tab1:
    st.subheader("Evolução Financeira: Faturamento vs. Custo de Frete")
    st.plotly_chart(plot_financial_evolution(df), width="stretch")

    st.divider()

    col_pay1, col_pay2 = st.columns(2)
    
    with col_pay1:
        st.subheader("Meios de Pagamento")
        df_pay = get_payment_data()
        fig_pay = plot_payment_types(df_pay)
        if fig_pay:
            st.plotly_chart(fig_pay, width="stretch")
        else:
            st.warning("Dados de pagamento indisponíveis.")

    with col_pay2:
        st.subheader("Top 10 Estados (Receita)")
        st.plotly_chart(plot_top_states_revenue(df), width="stretch")

with tab2:
    col_log1, col_log2 = st.columns(2)
    with col_log1:
        st.subheader("Status de Entrega")
        st.plotly_chart(plot_delivery_status(df), width="stretch")
    
    with col_log2:
        st.subheader("Distribuição de Atrasos")
        st.plotly_chart(plot_delay_distribution(df), width="stretch")
        
    st.divider()
    
    col_prazo1, col_prazo2 = st.columns(2)
    with col_prazo1:
        st.subheader("Evolução da Taxa de Atraso (%)")
        st.plotly_chart(plot_delay_rate_evolution(df), width="stretch")
        
    with col_prazo2:
        st.subheader("Ranking de Atrasos por Estado")
        fig_ranking = plot_delay_ranking_by_state(df)
        if fig_ranking:
            st.plotly_chart(fig_ranking, width="stretch")
        else:
            st.info("Parabéns! Nenhum atraso registrado no período selecionado.")

with tab3:
    st.subheader("Análise de Portfólio de Produtos")
    
    col_rank1, col_rank2 = st.columns(2)
    with col_rank1:
        st.markdown("**Top 10 Categorias por Faturamento**")
        st.plotly_chart(plot_top_categories_revenue(df), width="stretch")
        
    with col_rank2:
        st.markdown("**Top 10 Categorias por Volume de Vendas**")
        st.plotly_chart(plot_top_categories_volume(df), width="stretch")

    st.divider()

    is_single_state = len(selected_states) == 1
    
    if is_single_state:
        st.subheader(f"🏙️ Mapa de Calor: Cidades de {selected_states[0]}")
    else:
        st.subheader("🗺️ Mapa de Calor: Estados do Brasil")

    top_categories = df.groupby('product_category_name')['valor_venda'].sum().sort_values(ascending=False).head(30).index.tolist()
    
    if top_categories:
        cat_selecionada = st.selectbox(
            "Selecione a Categoria:",
            top_categories,
            format_func=lambda x: x.replace('_', ' ').title()
        )
        
        df_cat_map = df[df['product_category_name'] == cat_selecionada]

        if not df_cat_map.empty:
            if is_single_state:
                with st.spinner(f"Carregando mapa de {selected_states[0]}..."):
                    geojson_mun = get_geojson_state(selected_states[0])
                    
                    if geojson_mun:
                        sales_data = df_cat_map.groupby('cidade_norm')['valor_venda'].sum().reset_index()
                        
                        all_cities = pd.DataFrame({'cidade_norm': [f['properties']['id_norm'] for f in geojson_mun['features']]})
                        final_map_data = pd.merge(all_cities, sales_data, on='cidade_norm', how='left')
                        final_map_data['valor_venda'] = final_map_data['valor_venda'].fillna(0)

                        fig_map = plot_generic_choropleth(
                            final_map_data, geojson_mun, 'cidade_norm', 'properties.id_norm', 'valor_venda',
                            f"Vendas em {selected_states[0]}", {'valor_venda': 'Faturamento (R$)', 'cidade_norm': 'Cidade'}
                        )
                        st.plotly_chart(fig_map, width="stretch")
                    else:
                        st.warning("Erro ao carregar GeoJSON.")
            else:
                map_data = df_cat_map.groupby('estado_cliente')['valor_venda'].sum().reset_index()
                geojson_br = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
                
                fig_map = plot_generic_choropleth(
                    map_data, geojson_br, 'estado_cliente', 'properties.sigla', 'valor_venda',
                    f"Distribuição Nacional: {cat_selecionada}", {'valor_venda': 'Faturamento (R$)', 'estado_cliente': 'Estado'}
                )
                st.plotly_chart(fig_map, width="stretch")
        else:
            st.warning("Sem dados para esta categoria.")
    else:
        st.warning("Não há categorias disponíveis.")

with tab4:
    df_log = get_logistics_data()
    
    if not df_log.empty:
        col_row1_a, col_row1_b = st.columns(2)
        
        with col_row1_a:
            st.subheader("Mapa de Calor do Frete")
            frete_estado = df_log.groupby('customer_state')['freight_value'].mean().reset_index()
            geojson_br = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
            
            fig_map_frete = plot_generic_choropleth(
                frete_estado, geojson_br, 'customer_state', 'properties.sigla', 'freight_value',
                "Frete Médio por Estado", {'freight_value': 'Valor (R$)', 'customer_state': 'Estado'}
            )
            st.plotly_chart(fig_map_frete, width="stretch")
            
        with col_row1_b:
            st.subheader("Custo Médio por Faixa de Peso")
            st.plotly_chart(plot_freight_weight_relationship(df_log), width="stretch")
            
        st.divider()
        st.subheader("Eficiência do Frete: Onde ganhamos e onde perdemos?")
        
        col_bad, col_good = st.columns(2)
        with col_bad:
            st.markdown("⚠️ **Categorias com Frete Mais Caro**")
            st.plotly_chart(plot_freight_efficiency(df_log, type='expensive'), width="stretch")
            
        with col_good:
            st.markdown("✅ **Categorias com Frete Mais Barato**")
            st.plotly_chart(plot_freight_efficiency(df_log, type='cheap'), width="stretch")
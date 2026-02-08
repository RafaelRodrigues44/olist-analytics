import plotly.express as px
import pandas as pd

def plot_financial_evolution(df):
    evolucao_tempo = df.set_index('order_purchase_timestamp') \
                        .resample('ME')[['valor_venda', 'valor_frete']] \
                        .sum().reset_index()

    labels_map = {
        'order_purchase_timestamp': 'Mês de Referência',
        'valor_venda': 'Faturamento (R$)',
        'valor_frete': 'Custo de Frete (R$)',
        'value': 'Valor (R$)',
        'variable': 'Indicador'
    }

    fig = px.line(
        evolucao_tempo,
        x='order_purchase_timestamp',
        y=['valor_venda', 'valor_frete'],
        labels=labels_map,
        markers=True,
        line_shape='spline',
        color_discrete_map={
            'valor_venda': '#2980B9',   
            'valor_frete': "#D33030"  
        }
    )

    new_names = {'valor_venda': 'Faturamento', 'valor_frete': 'Frete Total'}
    fig.for_each_trace(lambda t: t.update(
        name=new_names[t.name],
        legendgroup=new_names[t.name],
        hovertemplate=t.hovertemplate.replace(t.name, new_names[t.name])
    ))

    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig

def plot_payment_types(df_pagamentos):
    if df_pagamentos.empty:
        return None

    traducao = {
        "credit_card": "Cartão de Crédito",
        "boleto": "Boleto",
        "voucher": "Voucher",
        "debit_card": "Cartão de Débito",
        "pix": "Pix"
    }

    df_pagamentos['payment_type'] = df_pagamentos['payment_type'].replace(traducao)

    fig = px.pie(
        df_pagamentos,
        values='qtd_pedidos',
        names='payment_type',
        hole=0.55,
        labels={'payment_type': 'Forma de Pagamento', 'qtd_pedidos': 'Pedidos'},
        color_discrete_sequence=['#5DADE2', '#76D7C4', '#F7DC6F', '#F8C471', '#D7BDE2', '#F5B7B1']
    )

    fig.update_traces(
        textinfo='percent',
        textposition='inside',
        insidetextfont=dict(color='black', size=10, family='Arial Black')
    )
    return fig

def plot_top_states_revenue(df):
    vendas_estado = (
        df.groupby('estado_cliente')['valor_venda']
        .sum()
        .reset_index()
        .sort_values('valor_venda', ascending=False)
        .head(10)
    )

    fig = px.bar(
        vendas_estado,
        x='estado_cliente',
        y='valor_venda',
        text_auto='.2s',
        labels={'estado_cliente': 'Estado', 'valor_venda': 'Receita Total'},
        color_discrete_sequence=['#2980B9']
    )

    fig.update_traces(
        textposition='inside',
        insidetextanchor='end',
        textfont=dict(color='black', size=10, family='Arial Black'),
        cliponaxis=False
    )

    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig

def plot_delivery_status(df):
    df_copy = df.copy()
    df_copy['status_entrega'] = df_copy['dias_atraso'].apply(lambda x: 'Atrasado' if x > 0 else 'No Prazo')
    status_counts = df_copy['status_entrega'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Qtd']
    
    fig = px.pie(
        status_counts, 
        values='Qtd', 
        names='Status', 
        hole=0.5,
        color='Status',
        color_discrete_map={'Atrasado':'#E74C3C', 'No Prazo':'#2980B9'},
        labels={'Status': 'Situação', 'Qtd': 'Total de Pedidos'}
    )
    return fig

def plot_delay_distribution(df):
    fig = px.histogram(
        df, 
        x='dias_atraso', 
        nbins=50, 
        labels={'dias_atraso': 'Dias de Atraso (Negativo = Adiantado)'},
        color_discrete_sequence=['#2980B9']
    )
    
    fig.add_vline(x=0, line_dash="dash", line_color="#E74C3C", annotation_text="Prazo Prometido")
    fig.update_layout(showlegend=False, yaxis_title="Quantidade de Pedidos")
    return fig

def plot_delay_rate_evolution(df):
    df_copy = df.copy()
    df_copy['flag_atraso'] = df_copy['dias_atraso'].apply(lambda x: 1 if x > 0 else 0)
    
    evolucao_percentual = df_copy.set_index('order_purchase_timestamp').resample('ME')['flag_atraso'].agg(['mean', 'count']).reset_index()
    evolucao_percentual = evolucao_percentual[evolucao_percentual['count'] > 20]
    evolucao_percentual['mean'] = evolucao_percentual['mean'] * 100
    
    fig = px.line(
        evolucao_percentual, 
        x='order_purchase_timestamp', 
        y='mean',
        markers=True,
        line_shape='spline', 
        labels={'order_purchase_timestamp': 'Mês', 'mean': '% de Pedidos Atrasados'},
        title="Percentual de Pedidos Fora do Prazo (Mensal)"
    )
    fig.update_traces(line_color='#2980B9')
    fig.update_yaxes(ticksuffix="%")
    return fig

def plot_delay_ranking_by_state(df):
    df_atrasados = df[df['dias_atraso'] > 0]
    
    if df_atrasados.empty:
        return None
        
    ranking_atraso = df_atrasados.groupby('estado_cliente')['dias_atraso'].mean().reset_index()
    ranking_atraso = ranking_atraso.sort_values('dias_atraso', ascending=False).head(10)
    
    fig = px.bar(
        ranking_atraso,
        x='dias_atraso',
        y='estado_cliente',
        orientation='h',
        text_auto='.1f',
        labels={'estado_cliente': 'Estado', 'dias_atraso': 'Média de Dias de Atraso'},
        color_discrete_sequence=['#2980B9']
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig

def plot_top_categories_revenue(df):
    prod_stats = df.groupby('product_category_name').agg({
        'valor_venda': 'sum',
        'order_id': 'count'
    }).reset_index()
    
    top_fat = prod_stats.sort_values('valor_venda', ascending=False).head(10).copy()
    
    top_fat['fat_formatado'] = top_fat['valor_venda'].apply(
        lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

    fig = px.bar(
        top_fat,
        x='valor_venda',
        y='product_category_name',
        orientation='h',
        text='fat_formatado',
        color_discrete_sequence=['#2980B9'],
        labels={'product_category_name': 'Categoria', 'valor_venda': 'Faturamento (R$)'}
    )

    fig.update_traces(
        textposition='inside',
        insidetextanchor='end',
        textfont=dict(color='black', size=10, family='Arial Black'),
        cliponaxis=False,
        hovertemplate="<b>%{y}</b><br>Faturamento: %{text}<extra></extra>"
    )

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig

def plot_top_categories_volume(df):
    prod_stats = df.groupby('product_category_name').agg({
        'valor_venda': 'sum',
        'order_id': 'count'
    }).reset_index()

    top_vol = prod_stats.sort_values('order_id', ascending=False).head(10).copy()
    top_vol['vol_formatado'] = top_vol['order_id'].apply(lambda x: f"{int(x):,}".replace(",", "."))

    fig = px.bar(
        top_vol,
        x='order_id',
        y='product_category_name',
        orientation='h',
        text='vol_formatado',
        color_discrete_sequence=['#2980B9'],
        labels={'product_category_name': 'Categoria', 'order_id': 'Quantidade'}
    )

    fig.update_traces(
        textposition='inside',
        insidetextanchor='end',
        textfont=dict(color='black', size=10, family='Arial Black'),
        cliponaxis=False,
        hovertemplate="<b>%{y}</b><br>Vendas: %{text}<extra></extra>"
    )

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig

def plot_freight_weight_relationship(df_log):
    if df_log.empty: return None

    bins = [0, 500, 1000, 2000, 5000, 10000, 30000, 100000]
    labels = ['Até 500g', '500g-1kg', '1kg-2kg', '2kg-5kg', '5kg-10kg', '10kg-30kg', '+30kg']
    
    df_copy = df_log.copy()
    df_copy['faixa_peso'] = pd.cut(df_copy['product_weight_g'], bins=bins, labels=labels)
    
    peso_agg = df_copy.groupby('faixa_peso', observed=True)['freight_value'].mean().reset_index()
    
    fig = px.bar(
        peso_agg, 
        x='faixa_peso', 
        y='freight_value',
        title="Relação Peso x Frete",
        labels={'faixa_peso': 'Faixa de Peso', 'freight_value': 'Frete Médio (R$)'}
    )
    fig.update_traces(marker_color='#2980B9')
    fig.update_yaxes(tickprefix="R$ ", tickformat=".2f")
    return fig

def plot_freight_efficiency(df_log, type='expensive'):
    if df_log.empty: return None

    df_copy = df_log.copy()
    df_copy['frete_relativo'] = (df_copy['freight_value'] / df_copy['price']) * 100
    
    cat_analysis = df_copy.groupby('product_category_name').agg({
        'frete_relativo': 'mean',
        'freight_value': 'mean',
        'price': 'count'
    }).reset_index()
    
    cat_analysis = cat_analysis[cat_analysis['price'] > 50]
    
    labels_barras = {'product_category_name': 'Categoria', 'frete_relativo': '% do Frete sobre Pedido'}

    if type == 'expensive':
        data = cat_analysis.sort_values('frete_relativo', ascending=False).head(10)
        order = 'total ascending'
    else:
        data = cat_analysis.sort_values('frete_relativo', ascending=True).head(10)
        order = 'total descending'

    fig = px.bar(
        data,
        x='frete_relativo',
        y='product_category_name',
        orientation='h',
        text_auto='.1f',
        color_discrete_sequence=['#2980B9'],
        labels=labels_barras
    )
    fig.update_layout(yaxis={'categoryorder': order}, xaxis_title="% do Frete sobre Pedido")
    return fig
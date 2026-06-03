CUSTOM_COLOR_SCALE = [
    [0.0, '#FFFFFF'], [0.05, '#AED6F1'], [0.2, '#2980B9'], [1.0, '#E74C3C']
]

CSS = """
<style>
:root { 
    --tab-list-bg: transparent; 
    /* Cinza claro fosco para o modo light (fora de contexto) */
    --tab-bg: #f0f2f5; 
    --tab-hover: #e4e6eb; 
    --tab-text: #65676b; 
    /* Idêntico ao KPI Card */
    --tab-active-bg: linear-gradient(135deg, #0d3b66, #145da0); 
    --tab-active-text: #ffffff; 
    --tab-shadow: inset 0 0 0 1px rgba(0,0,0,0.05); 
}

@media (prefers-color-scheme: dark) { 
    :root { 
        --tab-list-bg: transparent; 
        /* Cinza escuro/grafite fosco para o modo dark (fora de contexto) */
        --tab-bg: #242526; 
        --tab-hover: #3a3b3c; 
        --tab-text: #b0b3b8; 
        /* Mantém o mesmo gradiente do KPI Card no modo dark */
        --tab-active-bg: linear-gradient(135deg, #0d3b66, #145da0); 
        --tab-active-text: #ffffff; 
        --tab-shadow: none; 
    } 
}

.stTabs [data-baseweb="tab-list"] { gap: 40px; background: var(--tab-list-bg); padding: 10px; border-radius: 18px; margin-left: 400px; }
.stTabs [data-baseweb="tab"] { height: 48px; padding: 0 24px; border-radius: 14px; background: var(--tab-bg); color: var(--tab-text); font-weight: 700; box-shadow: var(--tab-shadow); transition: all .2s ease; }
.stTabs [data-baseweb="tab"]:hover { background: var(--tab-hover); color: var(--tab-text); transform: translateY(-2px); }
.stTabs [aria-selected="true"] { background: var(--tab-active-bg) !important; color: var(--tab-active-text) !important; transform: translateY(-2px); box-shadow: 0 8px 22px rgba(0,0,0,0.25) !important; border: none !important; }
.stTabs [aria-selected="true"] p { color: var(--tab-active-text) !important; }
.stTabs [data-baseweb="tab-panel"] { padding-top: 20px; }
.stTabs [data-baseweb="tab-highlight"] { background-color: transparent !important; }
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* Força os valores internos dos gráficos (barras, fatias, etc.) a ficarem brancos */
.js-plotly-plot .bartext, .js-plotly-plot .slice text { fill: #ffffff !important; color: #ffffff !important; }

.kpi-card { background: linear-gradient(135deg, #0d3b66, #145da0); padding: 28px; border-radius: 18px; text-align: center; box-shadow: 0 6px 18px rgba(0,0,0,0.15); }
.kpi-title { font-size: 14px; color: #cfe8ff; margin-bottom: 8px; letter-spacing: 0.5px; }
.kpi-value { font-size: clamp(1.8rem, 2vw, 2.5rem); font-weight: 800; color: white; white-space: nowrap; }
</style>
"""
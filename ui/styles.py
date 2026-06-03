CUSTOM_COLOR_SCALE = [
    [0.0, '#FFFFFF'], [0.05, '#AED6F1'], [0.2, '#2980B9'], [1.0, '#E74C3C']
]

CSS = """
<style>
:root { --tab-list-bg: transparent; --tab-bg: #f0f2f5; --tab-hover: #e4e6eb; --tab-text: #65676b; --tab-active-bg: linear-gradient(135deg, #0d3b66, #145da0); --tab-active-text: #ffffff; --tab-shadow: inset 0 0 0 1px rgba(0,0,0,0.05); }
@media (prefers-color-scheme: dark) { :root { --tab-list-bg: transparent; --tab-bg: #242526; --tab-hover: #3a3b3c; --tab-text: #b0b3b8; --tab-active-bg: linear-gradient(135deg, #0d3b66, #145da0); --tab-active-text: #ffffff; --tab-shadow: none; } }
.stTabs [data-baseweb="tab-list"] { gap: 40px; background: var(--tab-list-bg); padding: 10px; border-radius: 18px; display: flex; justify-content: center; }
.stTabs [data-baseweb="tab"] { height: 48px; padding: 0 24px; border-radius: 14px; background: var(--tab-bg); color: var(--tab-text); font-weight: 700; box-shadow: var(--tab-shadow); transition: all .2s ease; }
.stTabs [data-baseweb="tab"]:hover { background: var(--tab-hover); color: var(--tab-text); transform: translateY(-2px); }
.stTabs [aria-selected="true"] { background: var(--tab-active-bg) !important; color: var(--tab-active-text) !important; transform: translateY(-2px); box-shadow: 0 8px 22px rgba(0,0,0,0.25) !important; border: none !important; }
.stTabs [aria-selected="true"] p { color: var(--tab-active-text) !important; }
.stTabs [data-baseweb="tab-panel"] { padding-top: 20px; }
.stTabs [data-baseweb="tab-highlight"] { background-color: transparent !important; }
.stTabs [data-baseweb="tab-border"] { display: none !important; }
.js-plotly-plot .bartext, .js-plotly-plot .slice text { fill: #ffffff !important; color: #ffffff !important; }
.kpi-card { background: linear-gradient(135deg, #0d3b66, #145da0); padding: 28px; border-radius: 18px; text-align: center; box-shadow: 0 6px 18px rgba(0,0,0,0.15); }
.kpi-title { font-size: 14px; color: #cfe8ff; margin-bottom: 8px; letter-spacing: 0.5px; }
.kpi-value { font-size: clamp(1.8rem, 2vw, 2.5rem); font-weight: 800; color: white; white-space: nowrap; }
.footer-container { position: relative; margin-top: 1rem; padding: 2.5rem 4rem 1.5rem 6rem; background: transparent; border: 1px solid #4b5563; border-radius: 16px; }
.footer-divider { height: 3px; width: 120px; background: linear-gradient(90deg,#4b5563,#9ca3af); border-radius: 2px; margin-bottom: 2rem; }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 3rem; max-width: 1200px; margin: 0 auto; align-items: start; }
.footer-brand { color: #818181; display: flex; flex-direction: column; justify-content: flex-start; }
.footer-brand h3 { margin: 0 0 1.2rem 0; font-size: 1.25rem; font-weight: 600; letter-spacing: -0.02em; color: #818181; line-height: 1; }
.footer-brand p { color: #818181; font-size: 0.875rem; line-height: 1.8rem; margin: 0; text-align: justify; }
.footer-section { display: flex; flex-direction: column; justify-content: flex-start; }
.footer-section h4 { color: #818181; font-size: 0.875rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin: 0 0 1.2rem 1.5rem; line-height: 1; padding-top: 0.25rem; }
.footer-links { list-style: none; padding: 0; margin: 0; }
.footer-links li { margin-bottom: 0.75rem; line-height: 1.5; }
.footer-links a { color: #818181; text-decoration: none; font-size: 0.875rem; transition: color 0.2s ease; display: inline-flex; align-items: center; gap: 0.4rem; }
.footer-links a:hover { color: #1f2937; }
.footer-bottom { margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid #4b5563; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem; max-width: 1200px; margin-left: auto; margin-right: auto; }
.footer-copyright { color: #818181; font-size: 0.8125rem; }
.footer-badge { display: inline-flex; align-items: center; gap: 0.35rem; background: transparent; color: #4b5563; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 500; border: 1px solid #4b5563; }
.footer-badge.status-live::before { content: ""; width: 6px; height: 6px; background: #22c55e; border-radius: 50%; animation: pulse-dot 2s infinite; }
@keyframes pulse-dot { 0%,100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.5; transform: scale(0.8); } }
@media (max-width: 1024px) { .footer-grid { grid-template-columns: 1.5fr 1fr 1fr; gap: 2rem; } }
@media (max-width: 768px) { .footer-grid { grid-template-columns: 1fr; gap: 2rem; } .footer-bottom { flex-direction: column; text-align: center; } .footer-section h4 { margin-bottom: 0.75rem; } }
[data-theme="dark"] .footer-container { border-color: #ffffff; }
[data-theme="dark"] .footer-brand, [data-theme="dark"] .footer-brand h3, [data-theme="dark"] .footer-section h4 { color: #ffffff !important; }
[data-theme="dark"] .footer-brand p, [data-theme="dark"] .footer-links a, [data-theme="dark"] .footer-copyright { color: #ffffff !important; }
[data-theme="dark"] .footer-links a:hover { color: #ffffff !important; }
[data-theme="dark"] .footer-bottom { border-top: 1px solid #374151; }
[data-theme="dark"] .footer-badge { border-color: #374151; color: #9ca3af; }
</style>
"""
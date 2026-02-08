CUSTOM_COLOR_SCALE = [
    [0.0, '#FFFFFF'], [0.05, '#AED6F1'], [0.2, '#2980B9'], [1.0, '#E74C3C']
]

CSS = """
<style>
:root { --tab-list-bg: #f2f6fb; --tab-bg: #e6eef7; --tab-hover: #cfe2f3; --tab-text: #0d3b66; --tab-active-bg: linear-gradient(135deg, #0d3b66, #145da0); --tab-active-text: #ffffff; --tab-shadow: 0 6px 18px rgba(0,0,0,0.15); }
@media (prefers-color-scheme: dark) { :root { --tab-list-bg: #111418; --tab-bg: #1b1f24; --tab-hover: #252b31; --tab-text: #dbe7ff; --tab-active-bg: linear-gradient(135deg, #1f6feb, #3b82f6); --tab-active-text: #ffffff; --tab-shadow: 0 6px 18px rgba(0,0,0,0.35); } }
.stTabs [data-baseweb="tab-list"] { gap: 10px; background: var(--tab-list-bg); padding: 10px; border-radius: 18px; }
.stTabs [data-baseweb="tab"] { height: 48px; padding: 0 24px; border-radius: 14px; background: var(--tab-bg); color: var(--tab-text); font-weight: 700; box-shadow: var(--tab-shadow); transition: all .2s ease; }
.stTabs [data-baseweb="tab"]:hover { background: var(--tab-hover); transform: translateY(-2px); }
.stTabs [aria-selected="true"] { background: var(--tab-active-bg); color: var(--tab-active-text); transform: translateY(-2px); box-shadow: 0 8px 22px rgba(0,0,0,0.25); }
.stTabs [data-baseweb="tab-panel"] { padding-top: 20px; }
.kpi-card { background: linear-gradient(135deg, #0d3b66, #145da0); padding: 28px; border-radius: 18px; text-align: center; box-shadow: 0 6px 18px rgba(0,0,0,0.15); }
.kpi-title { font-size: 14px; color: #cfe8ff; margin-bottom: 8px; letter-spacing: 0.5px; }
.kpi-value { font-size: 30px; font-weight: 800; color: white; }
</style>
"""
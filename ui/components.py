def kpi_card(title, value):
    return f"""
    <div class="kpi-card">
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{value}</div>
    </div>
    """

def render_footer():
    return f"""
    <div class="footer-container">
        <div class="footer-divider"></div>
        <div class="footer-grid">
            <div class="footer-brand">
                <h3>Olist Analytics</h3>
                <p>Projeto de portfólio para prova de conceito e treinamento em engenharia de dados, visualização e analytics. Construído sobre a base pública da Olist, o dashboard demonstra o pipeline completo: upload dos dados brutos por script Python e criação de views com SQL no Supabase, conexão com o Data Warehouse para obtenção da view, tratamento de dados em Python, modelagem dimensional e visualização interativa de KPIs comerciais, logísticos e de produto, construção de visualização com frontend Streamlit e, por fim, deploy do dashboard com o Streamlit.</p>
            </div>
            <div class="footer-section">
                <h4>Navegação</h4>
                <ul class="footer-links">
                    <li><a href="#top">↑ Topo da página</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Sobre</h4>
                <ul class="footer-links">
                    <li><a href="https://github.com/RafaelRodrigues44/olist-analytics/blob/main/README.md">Documentação</a></li>
                    <li><a href="https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce" target="_blank">Dataset Olist</a></li>
                    <li><a href="https://www.linkedin.com/in/rafael-rodrigues-ab2a981b5/" target="_blank">LinkedIn</a></li>
                    <li><a href="mailto:rafael.rodrigues85@hotmail.com?subject=Bug%20no%20Dashboard%20Olist">Reportar bug</a></li>
                    <li><a href="mailto:rafael.rodrigues85@hotmail.com?subject=Contato%20-%20Olist%20Analytics&body=Olá,%0A%0AGostaria%20de%20entrar%20em%20contato%20sobre...">Contato</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <span class="footer-copyright">© 2026 Rafel Rodrigues - Engenheiro de Software. Todos os direitos reservados.</span>
            <span class="footer-badge">v1.2.0</span>
        </div>
    </div>
    """
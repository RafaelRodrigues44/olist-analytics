import unicodedata

ESTADOS_IBGE = {
    'AC': 12, 'AL': 27, 'AM': 13, 'AP': 16, 'BA': 29, 'CE': 23, 'DF': 53, 'ES': 32,
    'GO': 52, 'MA': 21, 'MG': 31, 'MS': 50, 'MT': 51, 'PA': 15, 'PB': 25, 'PE': 26,
    'PI': 22, 'PR': 41, 'RJ': 33, 'RN': 24, 'RO': 11, 'RR': 14, 'RS': 43, 'SC': 42,
    'SE': 28, 'SP': 35, 'TO': 17
}

def normalize_text(text):
    if not isinstance(text, str): return str(text)
    return ''.join(c for c in unicodedata.normalize('NFD', text) 
                  if unicodedata.category(c) != 'Mn').lower().strip()

def format_br(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
import re

def validarBandeiraCartao(numero_cartao):
    """
    Valida a bandeira de um cartão de crédito com base no número fornecido.

    Args:
        numero_cartao (str): Número do cartão de crédito.

    Returns:
        str: Mensagem formatada com o número do cartão e a bandeira identificada.
    """
    # Remove espaços ou traços do número do cartão
    numero_cartao_limpo = re.sub(r"[ -]", "", numero_cartao)

    # Dicionário com os padrões de bandeiras
    bandeiras = {
        "Visa": r"^4",
        "MasterCard": r"^5[1-5]|^22[2-9][0-9]|^2[3-6][0-9]{2}|^27[0-1][0-9]|^2720",
        "Elo": r"^4011|^4312|^4389|^4514|^4576|^5041|^5066|^5090|^6277|^6362|^6504|^6505|^6507|^6509|^6516|^6550",
        "American Express": r"^3[47]",
        "Discover": r"^6011|^65|^64[4-9]",
        "Hipercard": r"^6062",
        "JCB": r"^35(2[8-9]|[3-8][0-9])",
        "Diners Club": r"^30[0-5]|^36|^38",
        "EnRoute": r"^2014|^2149",
        "Voyage": r"^8699",
        "Aura": r"^50"
    }

    # Verifica o número do cartão contra os padrões
    for bandeira, padrao in bandeiras.items():
        if re.match(padrao, numero_cartao_limpo):
            return f"Cartão número: {numero_cartao} é da bandeira: {bandeira}"

    return f"Cartão número: {numero_cartao} é da bandeira: Bandeira desconhecida"

# Exemplo de uso
numero = "5039 0487 6444 3688"  # Número de exemplo para Visa com espaços
print(validarBandeiraCartao(numero))  # Saída: Cartão número: 4111 1111 1111 1111 é da bandeira: Visa
# Entrada do número máximo de caracteres permitidos
max_length = int(input())

# Entrada do texto do post
user_input = input()

def summarize_text(text, limit):
    """
    Resumo do texto com base no limite de caracteres.
    Adiciona "..." ao final se o texto for cortado.
    """
    if len(text) <= limit:
        return text
    else:
        return text[:limit - 3] + "..."

# Processa o texto com base no limite
output = summarize_text(user_input, max_length)

# Exibe o resultado
print(output)
full_name = input()

def format_name(name):
    # Divide o nome em palavras, capitaliza cada uma e junta novamente
    return ' '.join(word.capitalize() for word in name.split())

formatted = format_name(full_name)
print(formatted)
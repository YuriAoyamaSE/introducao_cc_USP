def remove_repetidos(lista: list) -> list:
    lista_limpa = list(set(lista))
    lista_limpa.sort()
    return lista_limpa

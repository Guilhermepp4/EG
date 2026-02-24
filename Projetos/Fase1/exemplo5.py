#Black formatter
def processar_dados(lista, limite=100):
    return [
        x**2
        for x in lista
        if x > limite or (x % 3 == 0 and x < 1000) or (x % 5 == 0 and x > 500)
    ]

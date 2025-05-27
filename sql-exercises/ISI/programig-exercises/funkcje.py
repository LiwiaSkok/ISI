
def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Nie można obliczyć reszty z dzielenia przez zero!"

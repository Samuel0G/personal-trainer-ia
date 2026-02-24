#Calculo de Calorias
def calorias(objetivo, gasto_total):
    objetivo = objetivo.lower()

    if objetivo == "emagrecer":
        return gasto_total - 500

    elif objetivo == "hipertrofia":
        return gasto_total + 400

    elif objetivo == "manter":
        return gasto_total

    else:
        raise ValueError("Objetivo inválido.")
#Calculo de Calorias
def calorias(objetivo, gasto_total):
    if objetivo.lower() == "emagrecer":
        return gasto_total - 500
    elif objetivo.lower() == "ganhar_massa":
        return gasto_total + 300
    else:
        return gasto_total
#Calculando tmb
def tmb_calculos(peso, altura, idade, sexo):
    if sexo.upper() == "M":
        return (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    else:
        return (10 * peso) + (6.25 * altura) - (5 * idade) - 161

#Calculando gasto com base no nivel de atividade
def tmb_total(tmb, nivel_atividade):
    fatores = {
        "sedentario": 1.2,
        "leve": 1.375,
        "moderado": 1.55,
        "intenso": 1.725
    }
    return tmb * fatores.get(nivel_atividade.lower(), 1.2)
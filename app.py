from calculos import tmb_calculos, tmb_total
from treino import Treino
from dieta import calorias
from memoria import salvar

print("--- AGENTE IA PERSONAL TRAINER ---")

idade = int(input("Idade: "))
peso = float(input("Peso (kg): "))
altura = float(input("Altura (cm): "))
sexo = input("Sexo (M/F): ")
nivel = input("Nivel de atividade (sedentario/leve/moderado/intenso): ")
objetivo = input("Objetivo (emagrecer/hipertrofia/manter): ")

tmb = tmb_calculos(peso, altura, idade, sexo)
gasto_total = tmb_total(tmb, nivel)
Calorias = calorias(objetivo, gasto_total)
treino = Treino(objetivo)

print("\n--- RESULTADOS ---")
print(f"TMB: {tmb:.2f}")
print(f"Gasto Calorico Total: {gasto_total:.2f}")
print(f"Calorias recomendadas: {Calorias:.2f}")
print("\nTreino sugerido:")
print(treino)

salvar({
    "idade": idade,
    "peso": peso,
    "altura": altura,
    "tmb": tmb,
    "gasto_total": gasto_total,
    "calorias": Calorias,
    "objetivo": objetivo,
})
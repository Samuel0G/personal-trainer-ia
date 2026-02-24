from calculos import tmb_calculos, tmb_total, calcular_imc
from treino import Treino
from dieta import calorias
from memoria import salvar

print("--- AGENTE IA PERSONAL TRAINER ---")


# ==============================
# FUNÇÕES DE VALIDAÇÃO
# ==============================

def perguntar_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("⚠️ Digite apenas números inteiros.")

def perguntar_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("⚠️ Digite apenas números.")

def perguntar_opcao(mensagem, opcoes):
    while True:
        valor = input(mensagem).lower().strip()
        if valor in opcoes:
            return valor
        print(f"⚠️ Escolha apenas entre: {', '.join(opcoes)}")


# ==============================
# ENTRADAS DO USUÁRIO
# ==============================

idade = perguntar_int("Idade: ")
peso = perguntar_float("Peso (kg): ")
altura = perguntar_float("Altura (cm): ")

sexo = perguntar_opcao("Sexo (m/f): ", ["m", "f"])

nivel = perguntar_opcao(
    "Nivel (sedentario/leve/moderado/intenso): ",
    ["sedentario", "leve", "moderado", "intenso"]
)

objetivo = perguntar_opcao(
    "Objetivo (emagrecer/hipertrofia/manter): ",
    ["emagrecer", "hipertrofia", "manter"]
)


# ==============================
# PROCESSAMENTO
# ==============================

tmb = tmb_calculos(peso, altura, idade, sexo)
gasto_total = tmb_total(tmb, nivel)
calorias_final = calorias(objetivo, gasto_total)
treino = Treino(objetivo)
imc = calcular_imc(peso, altura)


# ==============================
# RESULTADOS
# ==============================

print("\n--- RESULTADOS ---")
print(f"IMC: {imc:.2f}")
print(f"TMB: {tmb:.2f}")
print(f"Gasto Calórico Total: {gasto_total:.2f}")
print(f"Calorias recomendadas: {calorias_final:.2f}")
print("\nTreino sugerido:")
print(treino)


# ==============================
# SALVAR MEMÓRIA
# ==============================

salvar({
    "idade": idade,
    "peso": peso,
    "altura": altura,
    "tmb": tmb,
    "gasto_total": gasto_total,
    "calorias": calorias_final,
    "objetivo": objetivo,
})

input("\nPressione Enter para sair...")
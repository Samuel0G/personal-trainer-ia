#Geração de treino
def Treino(objetivo):
    if objetivo.lower() == "emagrecer":
        return """
Treino ABC:
A - Peito + Triceps + 20min Cardio
B - Costas + Biceps + 20min Cardio
C - Pernas + 25min Cardio
"""
    elif objetivo.lower() == "hipertrofia":
        return """
Treino ABC:
A - Peito + Triceps (carga progressiva)
B - Costas + Biceps
C - Pernas (foco em agachamento e levantamento)
"""
    else:
        return "Treino funcional 3x por semana."
def interpretar_resultado(prob):
    if prob > 70:
        return "Alto Risco de Diabetes - Ação Recomendada"
    elif prob > 40:
        return "Risco Moderado - Atenção Necessária"
    elif prob > 20:
        return "Baixo Risco - Manutenção Preventiva"
    else:
        return "Risco Muito Baixo - Situação Controlada"
from scipy.stats import variation

# Calcular la variación de coeficiente de un conjunto de datos
data = [10, 12, 23, 23, 16, 23, 21, 16]
coef_variation = variation(data)
print(f"Coeficiente de variación: {coef_variation}")
